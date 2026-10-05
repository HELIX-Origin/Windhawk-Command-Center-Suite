# 🔬 Target Evidence Record: Notification Center Styler

Evidence ledger for `src/windows-11-notification-center-styler.yml` targeting `windows-11-notification-center-styler` mod per **Rule 04 (Target Evidence Protocol)**.

> [!NOTE]
> **Accessibility Accommodation**: The user has poor eyesight and prefers zero manual UWPSpy inspection. All selectors below are sourced from official Windhawk mod source code (`mods/windows-11-notification-center-styler.wh.cpp`), official community themes (TranslucentShell, FrostyGlass, OS26 Tahoe Glass), and the user's initial scaffold. Manual UWPSpy inspection is avoided.

---

## 📋 Surface Overview

- **Style File**: `src/windows-11-notification-center-styler.yml`
- **Windhawk Mod**: Windows 11 Notification Center Styler (`windows-11-notification-center-styler` v1.7)
- **Target Process**: `ShellExperienceHost.exe` (Win11 21H2–23H2) and `ShellHost.exe` (Win11 24H2)
- **XAML Framework**: UWP `Windows.UI.Xaml`

---

## 🎯 Target Evidence Ledger

| Selector | Surface Region | Tier | Source / Citation | Status | Notes |
|---|---|---|---|---|---|
| `Grid#NotificationCenterGrid` | Main Notifications Panel | T4 | `mods/windows-11-notification-center-styler.wh.cpp` L432 | 🟢 Sourced | Main root container for notifications |
| `Grid#CalendarCenterGrid` | Calendar Panel | T4 | Mod source (TranslucentShell, FrostyGlass) | 🟢 Sourced | Lower panel containing the calendar |
| `Grid#ControlCenterRegion` | Quick Settings Panel | T4 | Mod source + UWPSpy (ShellHost.exe, 24H2) | 🟢 Confirmed | Quick settings flyout container — glass card surface |
| `ControlCenter.ControlCenterView > Grid#RootGrid > Border#RootGridBorder` | Quick Settings (inner bg) | T4 | **UWPSpy live inspection** (ShellHost.exe, 24H2) | 🟢 Confirmed | System-painted card background inside ControlCenterView — must be cleared Transparent to prevent double-blur |
| `Grid#L1Grid` | Quick Settings (layout) | T4 | **UWPSpy live inspection** (ShellHost.exe, 24H2) | 🟢 Confirmed | Layout container sibling of RootGridBorder — NOT the card surface; keep Transparent |
| `Grid#NotificationCenterTopBanner` | Banner | T3 / T4 | User scaffold & Mod source | 🔴 Unconfirmed | Selector not verified in live tree — may not match |
| `Border#ToastBackgroundBorder` | Toasts | T4 | Mod source (TranslucentShell, FrostyGlass) | 🟢 Sourced | Popup toast notification card |
| `Border#ToastBackgroundBorder2` | Toasts | T4 | Mod source (TranslucentShell, FrostyGlass) | 🟢 Sourced | Secondary popup toast card variant |
| `ActionCenter.FlexibleToastView#FlexibleNormalToastView` | Toasts | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Toast view inner container |
| `ActionCenter.NotificationListViewItem` | Notifications | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Individual notification item in list |
| `Button#DismissButton` | Notifications | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Dismiss notification button |
| `Button#ClearAll` | Notifications | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | "Clear all" button |
| `ScrollViewer#CalendarControlScrollViewer` | Calendar | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Calendar scroll viewer |
| `Border#CalendarHeaderMinimizedOverlay` | Calendar | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Minimized calendar overlay border |
| `StackPanel#CalendarHeader` | Calendar | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Calendar navigation header |
| `CalendarViewDayItem > Border` | Calendar | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Day number border in month view |
| `Button#ExpandCollapseButton` | Calendar | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Chevron toggling calendar view |
| `ControlCenter.PaginatedToggleButton#ToggleButton` | Quick Settings | T4 | **UWPSpy live inspection** (ShellHost.exe, 24H2) | 🟢 Confirmed | Quick settings toggle button (Wi-Fi, BT, etc.) |
| `ControlCenter.PaginatedToggleButton#SplitL2Button` | Quick Settings | T4 | **UWPSpy live inspection** (ShellHost.exe, 24H2) | 🟢 Confirmed | L2 chevron split button — sibling of ToggleButton per GridViewItem |
| `QuickActions.AccessibleToggleButton#ToggleButton` | Quick Settings (Legacy) | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Backward-compatibility toggle target (21H2–23H2) |
| `ControlCenter.AsyncSlider` | Sliders | T4 | **UWPSpy live inspection** (ShellHost.exe, 24H2) | 🟢 Confirmed | Volume/Brightness slider wrapper |
| `Grid#SliderContainer` | Sliders | T3 / T4 | **UWPSpy live inspection** (ShellHost.exe, 24H2) | 🟢 Confirmed | Slider track container inside AsyncSlider |
| `Rectangle#HorizontalTrackRect` | Sliders | T3 / T4 | UWPSpy + Mod source | 🟢 Confirmed | Inactive track background |
| `Rectangle#HorizontalDecreaseRect` | Sliders | T3 / T4 | UWPSpy + Mod source | 🟢 Confirmed | Active track fill |
| `Primitives.Thumb#HorizontalThumb` | Sliders | T3 / T4 | UWPSpy + Mod source | 🟢 Confirmed | Draggable slider thumb |
| `Grid#MediaTransportControlsRegion` | Media Controls | T3 / T4 | UWPSpy + Mod source | 🟢 Confirmed | Media transport container (under RootContent) |
| `Grid#ThumbnailImage` | Media Controls | T3 / T4 | UWPSpy + Mod source | 🟢 Confirmed | Media album art container |
| `Button#PlayPauseButton` | Media Controls | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Play/pause button |
| `RepeatButton#PreviousButton` | Media Controls | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Previous track button |
| `RepeatButton#NextButton` | Media Controls | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Next track button |
| `Grid#FooterGrid` | Quick Settings Footer | T4 | **UWPSpy live inspection** (ShellHost.exe, 24H2) | 🟢 Confirmed | Footer row containing LeftFooter + RightFooter |
| `Button#FooterButton` | Quick Settings Footer | T3 / T4 | UWPSpy + Mod source | 🟢 Confirmed | Settings gear / footer action button |
| `ControlCenter.FrameWithContentChanged#L2Frame` | Quick Settings L2 | T4 | **UWPSpy live inspection** (ShellHost.exe, 24H2) | 🟢 Confirmed | L2 expanded panel frame at bottom of ControlCenterView |
| `Border#JumpListRestyledAcrylic` | Jump Lists | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Taskbar right-click jump list border |
| `JumpViewUI.JumpListListViewItem > Grid#LayoutRoot > Border#BackgroundBorder` | Jump Lists | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Individual jump list menu item |
| `MenuFlyoutPresenter > Border` | Menus | T4 | Mod source (FrostyGlass) | 🟢 Sourced | Context menu flyout border |
| `ActionCenter.FocusSessionControl#FocusSessionControl > Grid#FocusGrid` | Focus Assist | T3 / T4 | User scaffold & Mod source | 🟢 Sourced | Focus session / DND control |

> [!NOTE]
> **UWPSpy Process Note (Win11 24H2)**: UWPSpy can only attach to `ShellHost.exe`. Attaching to `ShellExperienceHost.exe` returns an error on 24H2. The Windhawk NC mod targets both processes, but all visual tree evidence must be gathered from `ShellHost.exe`.
