# !/usr/bin/env python3
"""Unified Hybrid XAML Visual Tree Inspector & Query CLI with ShareX Integration.

Universal tooling for Windhawk Themes and AI-assisted development.
Designed specifically for developers who use AI tools to "vibe code" themes:
- Uses programmatic UI automation (virtual chords) to wake background shell processes,
  activate target surfaces, and populate their live XAML trees.
- Injects a native C++ TAP agent via xamlOM.h to extract complete, accurate element hierarchies.
- Dumps structured JSON representations so AI models can discover selectors, inspect bounds,
  and query parent-child chains autonomously without requiring manual clicking in UWPSpy.
- Automatically cleans up and restores desktop state by dismissing opened surfaces.

Supported Surfaces for UI Automation:
  - start               (Win)   -> StartMenuExperienceHost.exe
  - action-center       (Win+A) -> ShellExperienceHost.exe / ShellHost.exe (Quick Settings)
  - notification-center (Win+N) -> ShellHost.exe (Notification Center / Calendar)
  - search              (Win+S) -> SearchHost.exe
  - settings            (Win+I) -> SystemSettings.exe

Usage Examples:
    # List active shell processes
    python tools/inspect_xaml.py --list

    # Inspect Start Menu with automated surface activation & tree dump
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --surface start

    # Inspect Start Menu and capture a screenshot using ShareX
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --screenshot

    # Inspect Notification Center / Calendar
    python tools/inspect_xaml.py -p ShellHost.exe --surface notification-center

    # Search for specific elements in live visual tree
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --find ActionsBar
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --tree PrimaryCardContainer --depth 4
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --path AcrylicOverlay

    # Save complete JSON visual tree to file
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --format json -o tools/dumps/start_menu_tree.json

    # Query previously saved JSON dump offline
    python tools/inspect_xaml.py -f tools/dumps/start_menu_tree.json --find PinnedList
"""

import argparse
import ctypes
import json
import os
import pathlib
import subprocess
import sys
import time
from ctypes import wintypes
from typing import Any, Dict, List, Optional, Tuple

SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
NATIVE_EXE = SCRIPT_DIR / "native" / "bin" / "xaml_dump.exe"

# --- Virtual Key Codes ---
VK_LWIN = 0x5B
VK_A = 0x41
VK_N = 0x4E
VK_S = 0x53
VK_ESCAPE = 0x1B
VK_SLEEP = 0x5F
VK_CONTROL = 0x11
VK_MENU = 0x12  # Alt
VK_SHIFT = 0x10
VK_SNAPSHOT = 0x2C  # PrintScreen

KEY_NAME_MAP = {
    "sleep": VK_SLEEP,
    "control": VK_CONTROL,
    "ctrl": VK_CONTROL,
    "alt": VK_MENU,
    "menu": VK_MENU,
    "shift": VK_SHIFT,
    "printscreen": VK_SNAPSHOT,
    "snapshot": VK_SNAPSHOT,
    "win": VK_LWIN,
}

SURFACE_MAP = {
    "start": {
        "label": "Start Menu",
        "keys": [VK_LWIN],
        "default_process": "StartMenuExperienceHost.exe",
    },
    "action-center": {
        "label": "Action Center / Quick Settings",
        "keys": [VK_LWIN, VK_A],
        "default_process": "ShellHost.exe",
    },
    "quick-settings": {
        "label": "Quick Settings",
        "keys": [VK_LWIN, VK_A],
        "default_process": "ShellHost.exe",
    },
    "notification-center": {
        "label": "Notification Center / Calendar",
        "keys": [VK_LWIN, VK_N],
        "default_process": "ShellHost.exe",
    },
    "calendar": {
        "label": "Notification Center / Calendar",
        "keys": [VK_LWIN, VK_N],
        "default_process": "ShellHost.exe",
    },
    "search": {
        "label": "Windows Search",
        "keys": [VK_LWIN, VK_S],
        "default_process": "SearchHost.exe",
    },
    "settings": {
        "label": "Windows Settings",
        "keys": [VK_LWIN, 0x49],  # VK_I
        "default_process": "SystemSettings.exe",
    },
}

PROCESS_DEFAULT_SURFACES = {
    "startmenuexperiencehost.exe": "start",
    "searchhost.exe": "search",
    "systemsettings.exe": "settings",
}


def send_key_chord(keys: List[int]) -> None:
    """Sends a key press sequence and releases in reverse order via SendInput."""
    user32 = ctypes.windll.user32

    class KEYBDINPUT(ctypes.Structure):
        _fields_ = [
            ("wVk", wintypes.WORD),
            ("wScan", wintypes.WORD),
            ("dwFlags", wintypes.DWORD),
            ("time", wintypes.DWORD),
            ("dwExtraInfo", ctypes.c_size_t),
        ]

    class INPUT(ctypes.Structure):
        class _U(ctypes.Union):
            _fields_ = [("ki", KEYBDINPUT)]

        _anonymous_ = ("u",)
        _fields_ = [("type", wintypes.DWORD), ("u", _U)]

    KEYEVENTF_KEYUP = 0x0002
    INPUT_KEYBOARD = 1

    inputs = []
    for k in keys:
        inp = INPUT(type=INPUT_KEYBOARD)
        inp.ki = KEYBDINPUT(wVk=k, wScan=0, dwFlags=0, time=0, dwExtraInfo=0)
        inputs.append(inp)

    for k in reversed(keys):
        inp = INPUT(type=INPUT_KEYBOARD)
        inp.ki = KEYBDINPUT(wVk=k, wScan=0, dwFlags=KEYEVENTF_KEYUP, time=0, dwExtraInfo=0)
        inputs.append(inp)

    arr = (INPUT * len(inputs))(*inputs)
    user32.SendInput(len(inputs), arr, ctypes.sizeof(INPUT))


def open_surface(surface_name: str) -> None:
    """Activates the specified shell surface via UI automation."""
    sinfo = SURFACE_MAP.get(surface_name.lower())
    if not sinfo:
        return
    print(f"\n[UI-AUTOMATION] Activating {sinfo['label']} on your screen...")
    print("[UI-AUTOMATION] Please DO NOT touch keyboard or mouse while the tree is being captured!")
    send_key_chord(sinfo["keys"])
    time.sleep(1.2)  # Settle time for window creation and XAML tree population


def close_surface() -> None:
    """Closes any active surface with Escape."""
    send_key_chord([VK_ESCAPE])
    time.sleep(0.3)


# --- ShareX Screenshot Integration ---
def get_sharex_config_paths() -> Tuple[Optional[pathlib.Path], Optional[pathlib.Path]]:
    """Locates ShareX HotkeysConfig.json and ApplicationConfig.json."""
    candidates = [
        pathlib.Path.home() / "Documents" / "ShareX",
        pathlib.Path(os.environ.get("APPDATA", "")) / "ShareX",
        pathlib.Path(os.environ.get("LOCALAPPDATA", "")) / "ShareX",
    ]
    for d in candidates:
        hk = d / "HotkeysConfig.json"
        app = d / "ApplicationConfig.json"
        if hk.is_file():
            return hk, app if app.is_file() else None
    return None, None


def get_sharex_screenshot_folder() -> pathlib.Path:
    """Determines where ShareX saves screenshots."""
    _, app_cfg = get_sharex_config_paths()
    if app_cfg and app_cfg.is_file():
        try:
            data = json.loads(app_cfg.read_text(encoding="utf-8"))
            if data.get("UseCustomScreenshotsPath") and data.get("CustomScreenshotsPath"):
                custom = pathlib.Path(data["CustomScreenshotsPath"])
                if custom.exists():
                    return custom
        except Exception:
            pass
    # Fallback default ShareX screenshots location
    docs = pathlib.Path.home() / "Documents" / "ShareX" / "Screenshots"
    if docs.exists():
        return docs
    onedrive = pathlib.Path.home() / "OneDrive" / "Pictures" / "Screenshots"
    if onedrive.exists():
        return onedrive
    return pathlib.Path.home() / "Pictures" / "Screenshots"


def parse_sharex_hotkey(job_name: str = "ActiveWindow") -> Optional[List[int]]:
    """Extracts the exact key codes for a given ShareX job from HotkeysConfig.json."""
    hk_cfg, _ = get_sharex_config_paths()
    if not hk_cfg or not hk_cfg.is_file():
        return None

    try:
        data = json.loads(hk_cfg.read_text(encoding="utf-8"))
        hotkeys = data.get("Hotkeys", [])

        target_hk = None
        for hk in hotkeys:
            job = hk.get("TaskSettings", {}).get("Job", "")
            if job.lower() == job_name.lower():
                target_hk = hk
                break

        # Fallback to PrintScreen job if ActiveWindow is not found
        if not target_hk:
            for hk in hotkeys:
                job = hk.get("TaskSettings", {}).get("Job", "")
                if job.lower() == "printscreen":
                    target_hk = hk
                    break

        if not target_hk:
            return None

        hinfo = target_hk.get("HotkeyInfo", {})
        hotkey_str = hinfo.get("Hotkey", "")
        is_win = hinfo.get("Win", False)

        keys: List[int] = []
        if is_win:
            keys.append(VK_LWIN)

        for part in hotkey_str.split(","):
            token = part.strip().lower()
            if token in KEY_NAME_MAP:
                keys.append(KEY_NAME_MAP[token])

        return keys if keys else None
    except Exception as exc:
        print(f"[WARNING] Error reading ShareX hotkeys: {exc}", file=sys.stderr)
        return None


def capture_sharex_screenshot(job: str = "ActiveWindow") -> Optional[pathlib.Path]:
    """Triggers ShareX screenshot using user's configured hotkey and locates resulting file."""
    keys = parse_sharex_hotkey(job)
    if not keys:
        print("[WARNING] Could not parse ShareX hotkey. Trying default fallback (Sleep)...", file=sys.stderr)
        keys = [VK_SLEEP]

    screenshot_dir = get_sharex_screenshot_folder()
    existing_files = set()
    if screenshot_dir.exists():
        existing_files = set(screenshot_dir.rglob("*.*"))

    key_names = [k for k, v in KEY_NAME_MAP.items() if v in keys]
    print(f"[SCREENSHOT] Triggering ShareX capture via keybind: {keys} ({', '.join(key_names)})...")
    send_key_chord(keys)
    time.sleep(1.5)  # Wait for ShareX capture & save

    # Find newly created image file
    if screenshot_dir.exists():
        new_files = [f for f in screenshot_dir.rglob("*.*") if f not in existing_files and f.suffix.lower() in [".png", ".jpg", ".jpeg"]]
        if new_files:
            latest = max(new_files, key=lambda f: f.stat().st_mtime)
            print(f"[SCREENSHOT] Captured successfully: {latest}")
            return latest

    print(f"[SCREENSHOT] Screenshot triggered in {screenshot_dir}")
    return None


class XamlTree:
    """In-memory representation of visual tree with hierarchy navigation."""

    def __init__(self, data: Dict[str, Any]):
        self.pid: int = data.get("pid", 0)
        self.elements: List[Dict[str, Any]] = data.get("elements", [])
        self.by_handle: Dict[str, Dict[str, Any]] = {el["handle"]: el for el in self.elements}
        self.children_map: Dict[str, List[str]] = {}
        for el in self.elements:
            parent_handle = el.get("parent", "0x0")
            self.children_map.setdefault(parent_handle, []).append(el["handle"])

    @classmethod
    def from_json_str(cls, text: str) -> "XamlTree":
        return cls(json.loads(text))

    @classmethod
    def from_file(cls, path: pathlib.Path) -> "XamlTree":
        with open(path, "r", encoding="utf-8") as f:
            return cls(json.load(f))

    def find_elements(self, query: str) -> List[Dict[str, Any]]:
        clean_q = query.lstrip("#").lower()
        matches = []
        for el in self.elements:
            handle = (el.get("handle") or "").lower()
            name = (el.get("name") or "").lower()
            el_type = (el.get("type") or "").lower()
            if clean_q == handle or clean_q == name or clean_q in name or clean_q in el_type:
                matches.append(el)
        return matches

    def get_ancestors(self, handle: str) -> List[Dict[str, Any]]:
        chain = []
        curr = handle
        while curr and curr != "0x0" and curr in self.by_handle:
            chain.append(self.by_handle[curr])
            curr = self.by_handle[curr].get("parent", "0x0")
        chain.reverse()
        return chain

    def print_subtree(self, handle: str, depth: int = 0, max_depth: int = 6) -> None:
        if depth > max_depth or handle not in self.by_handle:
            return
        el = self.by_handle[handle]
        name_str = f" [#{el['name']}]" if el.get("name") else ""
        num_children = len(self.children_map.get(handle, []))
        child_badge = f" ({num_children} children)" if num_children > 0 else ""
        print("  " * depth + f"{el.get('type')}{name_str}{child_badge}")
        for ch in self.children_map.get(handle, []):
            self.print_subtree(ch, depth + 1, max_depth)


def run_native_dump(process_name: str, surface: Optional[str] = None, leave_open: bool = False) -> Optional[str]:
    """Runs native C++ xaml_dump.exe to capture the JSON visual tree."""
    if not NATIVE_EXE.is_file():
        print(f"[ERROR] Native inspector executable not found at: {NATIVE_EXE}", file=sys.stderr)
        print("Building native inspector now...", file=sys.stderr)
        build_script = SCRIPT_DIR / "native" / "build.ps1"
        res = subprocess.run(["pwsh", "-NoProfile", "-File", str(build_script)])
        if res.returncode != 0 or not NATIVE_EXE.is_file():
            print("[ERROR] Build failed. Please run: pwsh -File tools/native/build.ps1", file=sys.stderr)
            return None

    cmd = [str(NATIVE_EXE), "-p", process_name, "--format", "json"]
    if surface:
        cmd.extend(["-s", surface])
    if leave_open:
        cmd.append("--leave-open")

    print(f"[INFO] Launching native inspection for {process_name}...")
    proc = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")

    if proc.returncode != 0:
        print(f"[ERROR] Native inspection failed:\n{proc.stderr}", file=sys.stderr)
        return None

    stdout_lines = proc.stdout.splitlines()
    json_lines = []
    recording = False
    for line in stdout_lines:
        if line.strip().startswith("{"):
            recording = True
        if recording:
            json_lines.append(line)

    payload = "\n".join(json_lines).strip()
    if not payload:
        print(f"[ERROR] No valid JSON payload received from inspector:\n{proc.stdout}", file=sys.stderr)
        return None

    return payload


def handle_queries(tree: XamlTree, args: argparse.Namespace) -> int:
    print(f"\n[INFO] Visual Tree captured: PID {tree.pid}, Elements: {len(tree.elements)}")

    if args.find:
        matches = tree.find_elements(args.find)
        print(f"\nFound {len(matches)} matching element(s) for '{args.find}':")
        for m in matches:
            name_str = f" [#{m['name']}]" if m.get("name") else ""
            print(f"  - {m['type']}{name_str} (handle: {m['handle']}, parent: {m.get('parent')})")

    if args.tree:
        matches = tree.find_elements(args.tree)
        if not matches:
            print(f"[WARNING] No elements found matching '{args.tree}'")
        for m in matches:
            name_str = f" [#{m['name']}]" if m.get("name") else ""
            print(f"\n=== Subtree for {m['type']}{name_str} ({m['handle']}) ===")
            tree.print_subtree(m["handle"], 0, args.depth)

    if args.path:
        matches = tree.find_elements(args.path)
        if not matches:
            print(f"[WARNING] No elements found matching '{args.path}'")
        for m in matches:
            name_str = f" [#{m['name']}]" if m.get("name") else ""
            print(f"\n=== Path to {m['type']}{name_str} ({m['handle']}) ===")
            ancestors = tree.get_ancestors(m["handle"])
            for idx, a in enumerate(ancestors):
                a_name = f" [#{a['name']}]" if a.get("name") else ""
                print("  " * idx + f"-> {a['type']}{a_name}")

    if args.children:
        matches = tree.find_elements(args.children)
        if not matches:
            print(f"[WARNING] No elements found matching '{args.children}'")
        for m in matches:
            name_str = f" [#{m['name']}]" if m.get("name") else ""
            ch_handles = tree.children_map.get(m["handle"], [])
            print(f"\n=== Immediate children of {m['type']}{name_str} ({len(ch_handles)} children) ===")
            for ch in ch_handles:
                el = tree.by_handle[ch]
                ch_name = f" [#{el['name']}]" if el.get("name") else ""
                print(f"  - {el['type']}{ch_name} (handle: {el['handle']})")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Unified Hybrid XAML Visual Tree Inspector with UI Automation & ShareX Integration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    group = parser.add_mutually_exclusive_group()
    group.add_argument("-p", "--process", default="StartMenuExperienceHost.exe", help="Target shell process (default: StartMenuExperienceHost.exe)")
    group.add_argument("-f", "--file", type=pathlib.Path, help="Load and query saved JSON dump file offline")
    group.add_argument("-l", "--list", action="store_true", help="List active approved shell processes")

    parser.add_argument("-s", "--surface", choices=list(SURFACE_MAP.keys()), help="Shell surface to auto-open via UI automation")
    parser.add_argument("--screenshot", "-ss", action="store_true", help="Capture a screenshot via ShareX while surface is active")
    parser.add_argument("--leave-open", action="store_true", help="Do not close surface with Escape after capture")
    parser.add_argument("--find", help="Find elements by handle, name, or type")
    parser.add_argument("--tree", help="Print subtree starting at target element")
    parser.add_argument("--path", help="Print ancestor breadcrumb path down to target element")
    parser.add_argument("--children", help="List immediate children of target element")
    parser.add_argument("-d", "--depth", type=int, default=6, help="Maximum subtree depth (default: 6)")
    parser.add_argument("--format", choices=["text", "json", "markdown", "md"], default="text", help="Output format (default: text)")
    parser.add_argument("-o", "--output", type=pathlib.Path, help="Save output (JSON or tree) to specified file")

    args = parser.parse_args()

    if args.list:
        if not NATIVE_EXE.is_file():
            subprocess.run(["pwsh", "-NoProfile", "-File", str(SCRIPT_DIR / "native" / "build.ps1")])
        subprocess.run([str(NATIVE_EXE), "--list"])
        return 0

    if args.file:
        if not args.file.is_file():
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            return 1
        tree = XamlTree.from_file(args.file)
        return handle_queries(tree, args)

    surface = args.surface
    if not surface:
        surface = PROCESS_DEFAULT_SURFACES.get(args.process.lower())

    # If screenshot requested, ensure surface stays open until screenshot is taken
    effective_leave_open = args.leave_open or args.screenshot

    json_payload = run_native_dump(args.process, surface=surface, leave_open=effective_leave_open)
    if not json_payload:
        return 1

    # Take screenshot if requested
    if args.screenshot:
        capture_sharex_screenshot("ActiveWindow")
        if not args.leave_open:
            close_surface()

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as out:
            out.write(json_payload)
        print(f"[INFO] Saved JSON visual tree dump to {args.output}")

    tree = XamlTree.from_json_str(json_payload)

    has_queries = any([args.find, args.tree, args.path, args.children])
    if has_queries:
        return handle_queries(tree, args)

    if args.format == "json":
        if not args.output:
            print(json_payload)
        return 0

    print(f"\n=== Visual Tree Overview: {args.process} (Elements: {len(tree.elements)}) ===")
    root_handles = tree.children_map.get("0x0", [])
    if not root_handles and tree.elements:
        root_handles = [tree.elements[0]["handle"]]
    for r in root_handles:
        tree.print_subtree(r, 0, args.depth)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
