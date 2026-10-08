#!/usr/bin/env python3
"""Unified Hybrid XAML Visual Tree Inspector & Query CLI.

Part of the Windhawk Command Center Suite toolchain.
Architecture:
- Native C++ TAP Engine: tools/native/bin/xaml_dump.exe (fast in-process injection & Named Pipe IPC)
- Python CLI Wrapper:    tools/inspect_xaml.py (orchestration, rich querying, tree navigation)

Usage examples:
    # Basic inspection & listing (delegates to C++ native tool)
    python tools/inspect_xaml.py --list
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe -d 3
    python tools/inspect_xaml.py -p SearchHost.exe -f SearchBox
    python tools/inspect_xaml.py -p ShellHost.exe --format json -o out.json

    # Rich hierarchy queries (hybrid C++ dump + Python query engine)
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --find ActionsBar
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --tree PrimaryCardContainer --depth 4
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --path ActionsBar
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --children MainContent

    # Offline querying of previously saved JSON dumps
    python tools/inspect_xaml.py -f dump.json --find AcrylicOverlay
    python tools/inspect_xaml.py -f dump.json --tree CompanionRoot --depth 5
"""

import argparse
import json
import os
import pathlib
import subprocess
import sys
from typing import Any, Dict, List, Optional


SCRIPT_DIR = pathlib.Path(__file__).resolve().parent
NATIVE_EXE = SCRIPT_DIR / "native" / "bin" / "xaml_dump.exe"


class XamlTree:
    """Represents a flat-element XAML visual tree with reconstructed hierarchy."""

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
        """Finds elements matching query by handle (0x...), exact name, name substring, or type."""
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
        """Returns the ancestor chain from root down to this element."""
        chain = []
        curr = handle
        while curr and curr != "0x0" and curr in self.by_handle:
            chain.append(self.by_handle[curr])
            curr = self.by_handle[curr].get("parent", "0x0")
        chain.reverse()
        return chain

    def print_subtree(self, handle: str, depth: int = 0, max_depth: int = 6) -> None:
        """Recursively prints a subtree starting at handle."""
        if depth > max_depth or handle not in self.by_handle:
            return
        el = self.by_handle[handle]
        name_str = f" [#{el['name']}]" if el.get("name") else ""
        num_children = len(self.children_map.get(handle, []))
        child_badge = f" ({num_children} children)" if num_children > 0 else ""
        print("  " * depth + f"{el.get('type')}{name_str}{child_badge}")
        for ch in self.children_map.get(handle, []):
            self.print_subtree(ch, depth + 1, max_depth)


def run_native_direct(args: List[str]) -> int:
    """Directly executes the native C++ binary with passed arguments."""
    if not NATIVE_EXE.is_file():
        print(f"[ERROR] Native binary not found at: {NATIVE_EXE}", file=sys.stderr)
        print("Please build it first with: pwsh -File tools/native/build.ps1", file=sys.stderr)
        return 1
    result = subprocess.run([str(NATIVE_EXE)] + args)
    return result.returncode


def dump_process_to_json(process_name: str) -> Optional[str]:
    """Uses the native C++ binary to dump the process tree to JSON string in memory."""
    if not NATIVE_EXE.is_file():
        print(f"[ERROR] Native binary not found at: {NATIVE_EXE}", file=sys.stderr)
        return None
    cmd = [str(NATIVE_EXE), "-p", process_name, "--format", "json"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"[ERROR] Native inspection failed for {process_name}:\n{result.stderr}", file=sys.stderr)
        return None
    return result.stdout


def handle_queries(tree: XamlTree, args: argparse.Namespace) -> int:
    """Processes search, tree navigation, and path queries against the XamlTree."""
    print(f"[INFO] Visual Tree: PID {tree.pid}, Total Elements: {len(tree.elements)}")

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
    query_flags = {"--find", "--tree", "--path", "--children", "-f", "--file"}
    has_query = any(arg in query_flags for arg in sys.argv[1:])

    # If pure native operation without Python query flags, delegate directly to C++
    if not has_query:
        return run_native_direct(sys.argv[1:])

    # Parse query arguments
    parser = argparse.ArgumentParser(description="Hybrid XAML Visual Tree Inspector & Query CLI")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--process", help="Target process name or PID")
    group.add_argument("-f", "--file", type=pathlib.Path, help="Path to dumped JSON file")

    parser.add_argument("--find", help="Find elements by handle, name, or type")
    parser.add_argument("--tree", help="Print subtree starting at target element")
    parser.add_argument("--path", help="Print ancestor breadcrumb path down to target element")
    parser.add_argument("--children", help="List immediate children of target element")
    parser.add_argument("-d", "--depth", type=int, default=6, help="Maximum subtree depth (default: 6)")
    parser.add_argument("-o", "--output", type=pathlib.Path, help="Optionally save dumped JSON to file")

    args = parser.parse_args()

    if args.file:
        if not args.file.is_file():
            print(f"[ERROR] File not found: {args.file}", file=sys.stderr)
            return 1
        tree = XamlTree.from_file(args.file)
    else:
        json_payload = dump_process_to_json(args.process)
        if not json_payload:
            return 1
        if args.output:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            with open(args.output, "w", encoding="utf-8") as out:
                out.write(json_payload)
            print(f"[INFO] Saved dump to {args.output}")
        tree = XamlTree.from_json_str(json_payload)

    return handle_queries(tree, args)


if __name__ == "__main__":
    raise SystemExit(main())
