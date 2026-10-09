# Skill: Live Visual Inspection & Diagnostic Tooling

## Purpose

Standard operating procedure for inspecting the live XAML visual trees of Windows 11 shell surfaces to discover, verify, or debug target selectors without guessing (Rule 04).

---

## 1. Preferred Tool: Unified Hybrid XAML Inspector (`tools/inspect_xaml.py`)

The repository's unified inspection toolchain combines an in-process native C++ TAP injection engine (`tools/native/bin/xaml_dump.exe` + `xaml_dump_agent.dll` via `xamlOM.h`) with a Python CLI orchestration layer (`tools/inspect_xaml.py`).

### Key Capabilities
- **Automated Surface Activation**: Automatically sends key chords (`start` = Win, `action-center` = Win+A, `notification-center` = Win+N, `search` = Win+S) to ensure background UWP shell processes render active, populated XAML trees.
- **Auto-Restoration**: Surfaces opened during inspection are automatically closed with Escape upon completion (unless `--leave-open` is passed).
- **Generous Permission Timeout**: Features a 30-second heartbeat wait loop for target connection, allowing operators ample time to click "Allow" if prompted by OS elevation or security prompts.
- **ShareX Screenshot Integration**: Automatically captures screenshots via `--screenshot` (`-ss`), parsing the operator's custom ShareX keybinds (`HotkeysConfig.json`, including `VK_SLEEP` mappings) and saving to their designated screenshot directory.
- **Rich Tree Querying**: Fast search by handle, name, or type (`--find`), subtree visualization (`--tree`), ancestor breadcrumb navigation (`--path`), and immediate children listing (`--children`).

### Usage Invocations

```powershell
# List running approved shell processes
python tools/inspect_xaml.py --list

# Inspect Start Menu (auto-activates Start via Win, dumps tree, closes with Escape)
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe

# Inspect Start Menu and capture a screenshot via ShareX
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --screenshot

# Inspect Notification Center / Calendar
python tools/inspect_xaml.py -p ShellHost.exe --surface notification-center

# Inspect Quick Settings / Action Center
python tools/inspect_xaml.py -p ShellHost.exe --surface action-center

# Query specific controls in the live visual tree
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --find ActionsBar
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --tree PrimaryCardContainer --depth 4
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --path AcrylicOverlay

# Save JSON dump to disk
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --format json -o tools/dumps/start_menu.json

# Offline query against saved JSON dump
python tools/inspect_xaml.py -f tools/dumps/start_menu.json --find PinnedList
```

Approved targets only: `StartMenuExperienceHost.exe`, `SearchHost.exe`, `SearchApp.exe`, `LockApp.exe`, `ShellExperienceHost.exe`, `ShellHost.exe`, `explorer.exe` (Rule 01).
**Never automate `LockApp.exe` / the lock screen** — it locks the system and cannot be inspected as a result.

---

## 2. Fallback Tool: UWPSpy

UWPSpy remains available for manual deep XAML property inspection if COM diagnostics or TAP injection cannot run. Launch it only when needed; the user should never have to drive it.

### 2.1 Process & Framework Selection

| Surface | Process to Select | Target Framework |
|---|---|---|
| **Notification Center / Action Center** | `ShellExperienceHost.exe` (or `ShellHost.exe` on Win11 24H2) | **UWP (`Windows.UI.Xaml`)** |
| **Start Menu** | `StartMenuExperienceHost.exe` | **UWP / WinUI 2** |
| **Taskbar** | `explorer.exe` | **WinUI 3 / XAML Island** |
| **File Explorer** *(deferred — reference only, ROADMAP M.03)* | `explorer.exe` | **WinUI 3 (`Microsoft.UI.Xaml`)** |

---

## 3. Selector Quality Checklist

- [ ] Does the selector uniquely identify the intended control without bleeding into unrelated controls?
- [ ] Is it anchored with a `#Name` or property filter rather than a bare common type?
- [ ] Is the selector documented in the surface's target evidence table (`.agents/targets/`)?
