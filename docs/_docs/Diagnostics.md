---
layout: docs
parent: Documentation Directory
title: Visual Tree Diagnostics
---

# Visual Tree Diagnostics & Inspection

Understanding the live visual tree of Windows 11 shell components is essential for authoring robust target selectors that survive Windows updates.

> [!NOTE]
> **Built for AI Vibe Coding & Automated Workflows**:  
> The diagnostic tools here (`tools/inspect_xaml.py` and `xaml_dump.exe`) are designed specifically for developers using AI tools to "vibe code" Windhawk themes. Instead of requiring human visual inspection, the toolchain uses **UI automation** to programmatically trigger shell surfaces (Start, Notification Center, Quick Settings, Search), wait for the trees to populate, dump the complete hierarchy into structured JSON, and dismiss the surface. AI coding assistants can then parse and query this JSON directly to verify selector syntax and hierarchy depth without human intervention.
>
> For human developers who prefer manual, point-and-click inspection, see [UWPSpy Manual Inspection Guide](UWPSpy.md).

---

## 1. Approved Target Processes

The toolchain operates strictly within an approved set of shell processes:

| Process | UI Surface | Framework |
|---|---|---|
| `StartMenuExperienceHost.exe` | Windows Start Menu | UWP / WinUI 2 |
| `SearchHost.exe` / `SearchApp.exe` | Windows Search & Web Search | UWP / WinUI 2 |
| `ShellExperienceHost.exe` | Action Center / Notifications (Win11 21H2–23H2) | UWP `Windows.UI.Xaml` |
| `ShellHost.exe` | Action Center / Quick Settings (Win11 24H2) | UWP `Windows.UI.Xaml` |
| `SystemSettings.exe` | Windows 11 Settings App | UWP / WinUI 2/3 |
| `explorer.exe` | Windows Taskbar & File Explorer chrome | WinUI 3 `Microsoft.UI.Xaml` |
| `LockApp.exe` | Windows Lock Screen *(read-only; automation barred)* | UWP `Windows.UI.Xaml` |

---

## 2. Inspecting Live Surfaces

### Listing Running Processes
```powershell
python tools/inspect_xaml.py --list
```
Displays all currently running candidate processes with their PIDs, architectures, and AppContainer statuses.

### Capturing a Surface Tree
```powershell
# Capture Notification Center
python tools/inspect_xaml.py -p ShellHost.exe --surface notification-center -o scratch/json/nc_tree.json
```

### Searching Elements Offline
Once a tree is captured to JSON, query elements without re-injecting into the process:
```powershell
# Search for quick action toggles
python tools/inspect_xaml.py --query scratch/json/nc_tree.json --find QuickActionTile

# Search for specific automation names or IDs
python tools/inspect_xaml.py --query scratch/json/nc_tree.json --find BrightnessSlider
```

---

## 3. Interpreting Element Output

The inspector produces structured JSON representing each XAML element:

```json
{
  "type": "ControlCenter.QuickActionTile",
  "name": "QuickActionTile_WiFi",
  "bounds": { "x": 24, "y": 80, "width": 140, "height": 60 },
  "visualStateGroups": ["CommonStates", "ToggleStates"],
  "children": [
    {
      "type": "Border",
      "name": "TileRoot",
      "children": [...]
    }
  ]
}
```

- **`type`**: The XAML class type (e.g. `ControlCenter.QuickActionTile`).
- **`name`**: The `x:Name` or automation identifier (prefixed with `#` in styler selectors: `#TileRoot`).
- **`visualStateGroups`**: Available visual state groups for state-specific styles (e.g. `@CommonStates`).
- **`children`**: Direct visual tree descendants for child combinator chains (`>`).
