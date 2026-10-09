---
layout: documentation
title: "Wiki: Notification Center Styler"
---

# Wiki: Notification Center Styler Targets & Configuration

Comprehensive reference for the **Windows 11 Notification Center Styler** mod (`windows-11-notification-center-styler`), Quick Settings, Calendar flyout, and system toasts.

---

## 1. Mod Overview & Process Host

| Property | Value | Notes |
|---|---|---|
| **Mod ID** | `windows-11-notification-center-styler` | Official Windhawk mod |
| **Target Process (Win11 21H2–23H2)** | `ShellExperienceHost.exe` | UWP host on older Windows 11 builds |
| **Target Process (Win11 24H2 build 26100+)** | `ShellHost.exe` | **Crucial**: Quick Settings / Action Center migrated to `ShellHost.exe` in 24H2 |
| **XAML Framework** | `Windows.UI.Xaml` | Standard UWP XAML |
| **Version Floor** | `1.7+` | Direct `WindhawkBlur` supported since v1.3+ |

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
```

### Directives:
* **`styleConstants`**: Declares shared brushes, blur objects, and radii tokens.
* **`controlStyles`**: Direct visual tree target rules.
* **`themeResourceVariables`**: Resource brush remappings.
* **Unsupported Keys**: `webContentStyles`, `backgroundTranslucentEffect`, and `explorerFrameContainerHeight` are not supported.

---

## 3. Verified Visual Tree Targets

### Root Flyout Panels
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Grid#NotificationCenterGrid` | `Grid` | Main Notification Center window frame. |
| `Grid#CalendarCenterGrid` | `Grid` | Calendar flyout container frame. |
| `Grid#ControlCenterRegion` | `Grid` | Quick Settings (Win+A) outer flyout container. Primary surface for glass panel styling. |
| `ControlCenter.ControlCenterView > Grid#RootGrid > Border#RootGridBorder` | `Border` | System-painted inner background card. Clear to `Transparent` to prevent double-blur. |
| `Grid#L1Grid` | `Grid` | Primary layout grid inside Quick Settings. Sibling of `RootGridBorder`. |

### Quick Settings Toggles & Buttons
| Selector | Type | Purpose & Notes |
|---|---|---|
| `ControlCenter.PaginatedToggleButton#ToggleButton` | `ToggleButton` | Primary quick action toggle button (Wi-Fi, Bluetooth, Airplane mode, etc.). |
| `ControlCenter.PaginatedToggleButton#SplitL2Button` | `Button` | Right-hand chevron chevron button on split quick action tiles. |
| `QuickActions.AccessibleToggleButton#ToggleButton` | `ToggleButton` | Legacy quick action toggle button target for Windows 11 21H2–23H2. |
| `ControlCenter.FrameWithContentChanged#L2Frame` | `Frame` | Secondary expanded panel frame (e.g. Wi-Fi network selection or Bluetooth device list). |
| `Border#L2ContentBorder` | `Border` | Background card of the L2 expanded panel. |

### Sliders (Volume & Brightness)
| Selector | Type | Purpose & Notes |
|---|---|---|
| `ControlCenter.AsyncSlider` | `AsyncSlider` | Custom UWP wrapper around volume and display brightness sliders. |
| `Grid#SliderContainer` | `Grid` | Slider track and thumb container within `AsyncSlider`. |
| `Rectangle#HorizontalTrackRect` | `Rectangle` | Inactive slider track background rectangle. |
| `Rectangle#HorizontalDecreaseRect` | `Rectangle` | Active highlighted portion of the slider track. |
| `Primitives.Thumb#HorizontalThumb` | `Thumb` | Draggable slider thumb pill/circle. |
| `FontIcon#SliderIcon` | `FontIcon` | Speaker or Sun glyph icon beside the slider. |

### Media Controls
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Grid#MediaTransportControlsRegion` | `Grid` | Floating media playback card embedded inside Action Center. |
| `Grid#ThumbnailImage` | `Grid` | Album artwork thumbnail image container. |
| `Button#PlayPauseButton` | `Button` | Media play / pause toggle button. |
| `RepeatButton#PreviousButton` | `RepeatButton` | Skip previous track button. |
| `RepeatButton#NextButton` | `RepeatButton` | Skip next track button. |
| `TextBlock#MediaTitleText` | `TextBlock` | Song / media title string. |
| `TextBlock#MediaArtistText` | `TextBlock` | Artist / publisher string. |

### Calendar Flyout
| Selector | Type | Purpose & Notes |
|---|---|---|
| `ScrollViewer#CalendarControlScrollViewer` | `ScrollViewer` | Calendar main scrollable container. |
| `StackPanel#CalendarHeader` | `StackPanel` | Month / year header and navigation arrows. |
| `Border#CalendarHeaderMinimizedOverlay` | `Border` | Compact minimized calendar header overlay card. |
| `CalendarViewDayItem > Border` | `Border` | Individual day number cell border in month grid. |
| `Button#ExpandCollapseButton` | `Button` | Chevron button toggling full vs compact calendar height. |

### Toast Notifications & Jump Lists
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Border#ToastBackgroundBorder` | `Border` | Primary system popup notification toast card. |
| `Border#ToastBackgroundBorder2` | `Border` | Secondary toast popup notification card variant. |
| `ActionCenter.FlexibleToastView#FlexibleNormalToastView` | `FlexibleToastView` | Toast interactive view hierarchy. |
| `Button#DismissButton` | `Button` | "X" dismiss button on notification cards. |
| `Button#ClearAll` | `Button` | "Clear all" notifications header button. |
| `Border#JumpListRestyledAcrylic` | `Border` | Taskbar right-click jump list acrylic frame. |
| `JumpViewUI.JumpListListViewItem > Grid#LayoutRoot > Border#BackgroundBorder` | `Border` | Individual jump list menu item card. |

### Footer Row
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Grid#FooterGrid` | `Grid` | Bottom utility row holding battery percentage and Settings shortcut. |
| `Button#FooterButton` | `Button` | Settings gear icon button in the Quick Settings footer. |
| `TextBlock#BatteryPercentage` | `TextBlock` | Battery level readout label. |

---

## 4. Integrated Companion Settings: Shell Flyout Positions

When pairing Notification Center styling with `shell-flyout-positions`:
* **`actionCenter.alignment`**: `top`, `bottom`, `right`, `left`, `center`
* **`actionCenter.offsetY`**: Pixel offset from display edge or taskbar.
* **`notificationCenter.alignment`**: Placement for calendar / notification flyout.
