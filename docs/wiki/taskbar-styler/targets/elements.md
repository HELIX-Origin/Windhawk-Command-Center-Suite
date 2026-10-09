---
layout: documentation
title: "Wiki: Taskbar Element Targets"
---

# Taskbar Visual Tree Element Targets

Living catalog of verified WinUI 3 XAML elements in `explorer.exe` (Windows 11 Taskbar).

---

## Root Dock & Canvas

| Element Selector | Class Type | Verified Builds | Description & Interaction Notes |
|---|---|---|---|
| `Taskbar.TaskbarFrame#TaskbarFrame` | `TaskbarFrame` | Win11 21H2 – 24H2 | Root taskbar container frame. Setting `Height`, `Margin`, and `CornerRadius` creates floating dock appearances. |
| `Border#BackgroundBorder` | `Border` | Win11 21H2 – 24H2 | Taskbar background card surface. |
| `Rectangle#BackgroundFill` | `Rectangle` | Win11 21H2 – 24H2 | System solid taskbar fill. Set `Visibility=Collapsed` or `Fill:=Transparent` to allow custom glass styling. |
| `Grid#RootGrid` | `Grid` | Win11 21H2 – 24H2 | Main layout organizing Start, apps list, and system tray. |

---

## Running Apps & Task List Buttons

| Element Selector | Class Type | Verified Builds | Description & Interaction Notes |
|---|---|---|---|
| `TaskListUI#TaskList` | `TaskList` | Win11 21H2 – 24H2 | Items control hosting running application icons. |
| `Taskbar.TaskListButtonPanel` | `TaskListButtonPanel` | Win11 21H2 – 24H2 | Panel holding taskbar app buttons. |
| `TaskListButtonPanel@CommonStates > Grid > Border#BackgroundElement` | `Border` | Win11 21H2 – 24H2 | Running app button pill card with hover and pressed states. |
| `Border#ActiveIndicator` | `Border` | Win11 21H2 – 24H2 | Active window bottom indicator pill. |
| `Border#ProgressIndicator` | `Border` | Win11 21H2 – 24H2 | File transfer / download progress indicator inside app buttons. |

---

## Start Button & Search Box

| Element Selector | Class Type | Verified Builds | Description & Interaction Notes |
|---|---|---|---|
| `StartButton#StartButton` | `StartButton` | Win11 21H2 – 24H2 | Windows Start logo button. |
| `FontIcon#StartButtonIcon` | `FontIcon` | Win11 21H2 – 24H2 | Start logo icon glyph. |
| `TaskbarSearch#SearchBox` | `SearchBox` | Win11 21H2 – 24H2 | Embedded taskbar search box pill. |
| `Border#SearchBoxBackground` | `Border` | Win11 21H2 – 24H2 | Search pill background surface plate. |

---

## System Tray & Notification Area

| Element Selector | Class Type | Verified Builds | Description & Interaction Notes |
|---|---|---|---|
| `SystemTray#SystemTray` | `SystemTray` | Win11 21H2 – 24H2 | Container for notification icons, clock, and quick status. |
| `Grid#QuickStatusGrid` | `Grid` | Win11 21H2 – 24H2 | Pill cluster containing network, volume, and battery icons. |
| `ClockControl#Clock` | `ClockControl` | Win11 21H2 – 24H2 | Clock and calendar flyout trigger. |
| `ContentPresenter#DateTimePresenter` | `ContentPresenter` | Win11 21H2 – 24H2 | Clock text block presenter. |
| `NotificationArea` | `NotificationArea` | Win11 21H2 – 24H2 | Notification icon overflow area. |
| `Button#ShowDesktopButton` | `Button` | Win11 21H2 – 24H2 | Extreme right-hand edge "Show Desktop" line. Set `Visibility=Collapsed` to hide. |
