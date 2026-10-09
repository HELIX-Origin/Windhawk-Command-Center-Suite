---
title: Taskbar Styler
---

# Taskbar Styler (`windows-11-taskbar-styler`)

The **Windows 11 Taskbar Styler** mod restyles the primary Windows 11 taskbar, running applications list, system tray, and secondary taskbar panels.

> [!NOTE]
> **Ongoing Target Mapping**: Target trees and values are being incrementally audited and verified against live Windows builds. Below are the known existing targets and configuration options sourced from the official mod repository (`mods/windows-11-taskbar-styler.wh.cpp`) and the [official Taskbar styling guide](https://github.com/ramensoftware/windows-11-taskbar-styling-guide).

---

## 1. Mod Specifications

- **Mod ID**: `windows-11-taskbar-styler`
- **Target Process**: `explorer.exe`
- **Framework**: WinUI 3 / XAML
- **Version Floor**: `1.10+`

---

## 2. Supported Top-Level Configuration Options

```yaml
styleConstants:
  - ConstantName=Value

themeResourceVariables:
  - variableKey: ResourceKey
    value: "{ThemeResource ...}"

controlStyles:
  - target: Selector#TargetName
    styles:
      - Property=Value
      - Property:=<XAML>

xamlDiagnosticsHandling: alert # alert | block | allow
```

- **`styleConstants`**: Declares reusable constants and brushes.
- **`controlStyles`**: Direct XAML targets and style assignments.
- **`themeResourceVariables`**: Dynamic brush resource reassignments.
- **`xamlDiagnosticsHandling`**: Controls visual tree diagnostic hook behavior (`alert`, `block`, or `allow`).

---

## 3. Known Visual Tree Targets

### Root & Frame Containers
| Target Selector | Element Purpose |
|---|---|
| `Taskbar.TaskbarFrame#TaskbarFrame` | Outer container of the primary taskbar |
| `Border#BackgroundBorder` | Base background fill of the taskbar |
| `Rectangle#BackgroundFill` | Underlying system taskbar fill |
| `Grid#RootGrid` | Main root grid organizing Start, task list, and system tray |

### Task List & App Buttons
| Target Selector | Element Purpose |
|---|---|
| `TaskListUI#TaskList` | Task list control holding running application icons |
| `TaskListButtonPanel` | Item panel containing taskbar app buttons |
| `TaskListButtonPanel@CommonStates > Grid > Border#BackgroundElement` | Running app button pill background |
| `Border#ActiveIndicator` | Active/focused window pill or line indicator |
| `Border#ProgressIndicator` | Taskbar button download/activity progress bar |

### Start Button & Search
| Target Selector | Element Purpose |
|---|---|
| `StartButton#StartButton` | Windows Start logo button |
| `TaskbarSearch#SearchBox` | Embedded taskbar search pill |
| `Border#SearchBoxBackground` | Translucent background plate for the search bar |

### System Tray & Indicators
| Target Selector | Element Purpose |
|---|---|
| `SystemTray#SystemTray` | System tray area holding notifications, clock, and quick icons |
| `ClockControl#Clock` | Taskbar clock and calendar launch trigger |
| `NotificationArea` | Notification icon overflow area |
| `Grid#QuickStatusGrid` | Network, Volume, and Battery status pill cluster |
| `Button#ShowDesktopButton` | Far-right edge "Show Desktop" click area |

---

## 4. Visual State Targeting

Taskbar button hover and active states are targeted using `@CommonStates`:
```yaml
- target: TaskListButtonPanel@CommonStates > Grid > Border#BackgroundElement
  styles:
    - Background@PointerOver:=$OverlayColor2
    - Background@Pressed:=$OverlayColor
    - CornerRadius=$CornerRadius
```
Active running apps receive an emphasized bottom indicator bar:
```yaml
- target: Border#ActiveIndicator
  styles:
    - Background:=$AccentColor
    - CornerRadius=2
    - Height=3
```
