# Tools (`tools/`)

Repository tooling for **Windhawk Themes**.

| Tool | Purpose | Invocation |
|---|---|---|
| [`Test-WindhawkStyles.ps1`](Test-WindhawkStyles.ps1) | **Static validation gate (Rule 07)** — YAML syntax, constant ordering, and token checks for every styler file in `projects/`. | `pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1` |
| [`style-baseline.ini`](style-baseline.ini) | Static gate baseline ledger. | *(consumed automatically)* |
| [`inspect_xaml.py`](inspect_xaml.py) | **Hybrid XAML Inspector & Query CLI** — orchestrates UI automation, invokes the native C++ TAP engine, and parses live visual trees with rich querying. | `python tools/inspect_xaml.py --help` |
| [`native/bin/xaml_dump.exe`](native/bin/xaml_dump.exe) | **Native C++ XAML TAP Engine** — injects `xaml_dump_agent.dll` via `xamlOM.h` to capture live XAML visual trees with zero manual UWPSpy inspection. | `.\tools\native\bin\xaml_dump.exe --help` |

---

## Hybrid XAML Inspection Toolchain

Combines high-performance native C++ TAP injection (`xamlOM.h`) with Python UI automation to guarantee that shell visual trees are actively rendered, populated, and fully captured.

> **Designed for AI "Vibe Coding" Workflows**:  
> This hybrid toolchain is **not intended for manual inspection**. It is engineered specifically for developers who use AI tools and agentic coding assistants to "vibe code" themes. By utilizing UI automation to wake shell processes, open surfaces, dump their complete visual trees into machine-readable JSON, and clean up automatically, AI models can inspect trees, verify hierarchy depths, and discover selectors autonomously without requiring manual clicking in UWPSpy. Human developers wishing to inspect controls interactively should use **UWPSpy**.

### Key Features
1. **Automated Surface Activation**: Automatically sends key chords (Start = Win, Notification Center = Win+N, Quick Settings = Win+A, Search = Win+S) to ensure background UWP shell processes are awake and have populated XAML trees.
2. **Generous Permission Timeout**: Gives the user up to 30 seconds with heartbeat progress if an OS permission or UAC prompt appears, preventing premature timeouts.
3. **Rich Visual Tree Navigation**: Search elements (`--find`), view subtrees (`--tree`), show ancestor breadcrumb paths (`--path`), and list children (`--children`).
4. **Auto-Clean Restoration**: Automatically closes surfaces with Escape after inspection unless `--leave-open` is passed.

### Usage Examples

```powershell
# List active shell processes
python tools/inspect_xaml.py --list

# Inspect Start Menu (automatically opens Start via UI automation, dumps tree, and restores)
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe

# Inspect Notification Center / Calendar
python tools/inspect_xaml.py -p ShellHost.exe --surface notification-center

# Inspect Quick Settings / Action Center
python tools/inspect_xaml.py -p ShellHost.exe --surface action-center

# Inspect Windows Settings
python tools/inspect_xaml.py -p SystemSettings.exe --surface settings

# Search for specific elements in live visual tree
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --find ActionsBar
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --tree PrimaryCardContainer --depth 4
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --path AcrylicOverlay

# Save JSON dump to file
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --format json -o tools/dumps/start_menu.json

# Offline query on saved JSON dump
python tools/inspect_xaml.py -f tools/dumps/start_menu.json --find PinnedList

# Capture a screenshot via ShareX while surface is open
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --screenshot
```

### ShareX Screenshot Integration
The tool automatically parses your ShareX configuration (`HotkeysConfig.json` and `ApplicationConfig.json`) to find your custom screenshot keybinds (e.g. mapping `VK_SLEEP` if your keyboard registers PrintScreen as Sleep) and destination screenshot directories. Pass `--screenshot` (or `-ss`) to trigger a capture while the target shell surface is active.

### Prerequisites & Setup Requirements

The hybrid inspection toolchain utilizes **Visual Studio's XAML Diagnostics API** (`xamlOM.h` / `IVisualTreeServiceCallback2`) to hook into running shell processes without third-party graphical debuggers.

1. **Visual Studio & C++ Requirements**:
   - Visual Studio 2022 / 2026 (Community, Professional, or Build Tools).
   - Workload: **Desktop development with C++**.
   - Components: **MSVC v143/v144 - VS C++ x64/x86 build tools**, **Windows 11 SDK** (10.0.22621.0 or newer), and Visual Studio XAML Diagnostics components.
2. **Python Requirements**:
   - Python 3.10+ (64-bit).
   - Dependencies: Standard libraries (`ctypes`, `subprocess`, `json`, `argparse`, `pathlib`).
   - Install dependencies or optional speedups:
     ```powershell
     pip install -r tools/requirements.txt
     ```

### Rebuilding Native C++ Inspector
```powershell
pwsh -NoProfile -File tools/native/build.ps1
```
