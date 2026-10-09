---
layout: documentation
title: "Wiki: Taskbar Styler"
---

# Wiki: Taskbar Styler Targets & Configuration

Comprehensive reference for the **Windows 11 Taskbar Styler** mod (`windows-11-taskbar-styler`) and integrated companion utilities.

---

## 1. Mod Overview & Process Host

| Property | Value | Notes |
|---|---|---|
| **Mod ID** | `windows-11-taskbar-styler` | Official Windhawk mod |
| **Target Process** | `explorer.exe` | WinUI 3 XAML island running within Windows shell |
| **Framework** | `Microsoft.UI.Xaml` | Modern WinUI 3 runtime |
| **Version Floor** | `1.10+` | Full direct composition and token support |

---

## 2. Configuration Options & Top-Level Keys

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

### Directives:
* **`styleConstants`**: Declares named design tokens and brush snippets.
* **`controlStyles`**: Target selectors and property rules.
* **`xamlDiagnosticsHandling`**: Governs diagnostics hook compatibility (`alert`, `block`, or `allow`).

---

## 3. Verified Visual Tree Targets

### Root Taskbar Frame & Canvas
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Taskbar.TaskbarFrame#TaskbarFrame` | `TaskbarFrame` | Outer container of the primary taskbar. Setting `Height`, `Margin`, and `CornerRadius` controls the floating dock appearance. |
| `Border#BackgroundBorder` | `Border` | Primary background border card for the taskbar dock. |
| `Rectangle#BackgroundFill` | `Rectangle` | Native system taskbar fill rectangle. Collapse to `Transparent` or `Visibility=Collapsed` to prevent solid backgrounds. |
| `Grid#RootGrid` | `Grid` | Master layout grid organizing Start, running apps, and the notification tray. |

### Task List & App Buttons
| Selector | Type | Purpose & Notes |
|---|---|---|
| `TaskListUI#TaskList` | `TaskList` | Main items control holding all application icons. |
| `Taskbar.TaskListButtonPanel` | `TaskListButtonPanel` | Panel container for running application buttons. |
| `TaskListButtonPanel@CommonStates > Grid > Border#BackgroundElement` | `Border` | Hover/active card background pill for taskbar icons. |
| `Border#ActiveIndicator` | `Border` | Active window bottom pill or line indicator. |
| `Border#ProgressIndicator` | `Border` | Real-time download/activity progress bar rendered across button cards. |
| `TextBlock#TaskbarButtonLabel` | `TextBlock` | Text label for uncombined taskbar buttons. |

### Start Button & Embedded Search
| Selector | Type | Purpose & Notes |
|---|---|---|
| `StartButton#StartButton` | `StartButton` | Windows Start orb button. |
| `FontIcon#StartButtonIcon` | `FontIcon` | Windows Start logo icon glyph. |
| `TaskbarSearch#SearchBox` | `SearchBox` | Embedded taskbar search box pill. |
| `Border#SearchBoxBackground` | `Border` | Search pill background surface. |
| `TextBlock#SearchPlaceholderText` | `TextBlock` | "Search" placeholder text block. |

### System Tray & Corner Area
| Selector | Type | Purpose & Notes |
|---|---|---|
| `SystemTray#SystemTray` | `SystemTray` | Outer container for notification area, clock, and quick status. |
| `Grid#QuickStatusGrid` | `Grid` | Pill cluster containing network, volume, and battery icons. |
| `ClockControl#Clock` | `ClockControl` | Taskbar clock and calendar trigger area. |
| `ContentPresenter#DateTimePresenter` | `ContentPresenter` | Text block presenter displaying the clock string. |
| `NotificationArea` | `NotificationArea` | System tray notification icon overflow area. |
| `Button#ShowDesktopButton` | `Button` | Extreme right-hand edge "Show Desktop" line. Set `Visibility=Collapsed` to remove. |
| `Button#ChevronButton` | `Button` | Overflow arrow button for hidden tray icons. |

### Secondary Taskbars (Multi-Monitor)
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Taskbar.SecondaryTaskbarFrame#SecondaryTaskbarFrame` | `TaskbarFrame` | Taskbar container rendered on secondary displays. |
| `SecondaryTaskListUI#SecondaryTaskList` | `TaskList` | Running applications list on secondary monitors. |

---

## 4. Integrated Companion Mod Settings

### A. Taskbar Clock Customization (`taskbar-clock-customization`)
* **`clockFormat`** (String): Format string for time/date (e.g. `HH:mm:ss`, `HH:mm\nMM/dd`).
* **`fontFamily`** (String): Custom font family (e.g. `Segoe UI Variable Display`).
* **`fontSize`** (Integer): Font size in points.
* **`showMilliseconds`** (Boolean): Enable high-precision millisecond counters.

### B. Taskbar Tray and Icon Tweaks (`taskbar-tray-and-icon-tweaks`)
* **`hideShowDesktop`** (Boolean): Removes the 1px desktop strip at far right.
* **`hideNotificationCenter`** (Boolean): Hides the notification bell badge.
* **`iconPadding`** (Integer): Custom horizontal padding between tray icons in pixels.

### C. Taskbar Tray Icon Spacing and Grid (`taskbar-tray-icon-spacing-and-grid`)
* **`gridRows`** (Integer): Number of vertical rows for tray icons (e.g. `2` or `3`).
* **`horizontalSpacing`** / **`verticalSpacing`** (Integer): Custom grid spacing in pixels.

### D. Taskbar Height and Icon Size (`taskbar-height-and-icon-size`)
* **`taskbarHeight`** (Integer): Overall taskbar height in pixels (e.g. `36`, `48`, `60`).
* **`iconSize`** (Integer): Application icon dimension scaling in pixels (e.g. `20`, `24`, `32`).
