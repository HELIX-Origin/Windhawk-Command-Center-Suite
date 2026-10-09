---
title: Notification Center & Quick Settings
---

# Notification Center & Quick Settings (`windows-11-notification-center-styler`)

The **Windows 11 Notification Center Styler** mod targets the Action Center, Calendar flyout, Quick Settings control grid, media playback controls, and system toast notifications.

> [!NOTE]
> **Ongoing Target Mapping**: Target trees and values are being incrementally audited and verified against live Windows builds. Below are the known existing targets and configuration options sourced from the official mod repository (`mods/windows-11-notification-center-styler.wh.cpp`) and the [official Notification Center styling guide](https://github.com/ramensoftware/windows-11-notification-center-styling-guide).

---

## 1. Mod Specifications

- **Mod ID**: `windows-11-notification-center-styler`
- **Target Processes**: `ShellExperienceHost.exe` (Win11 21H2–23H2) and `ShellHost.exe` (Win11 24H2 build 26100+)
- **Framework**: UWP `Windows.UI.Xaml`
- **Version Floor**: `1.7+` (v1.3+ introduced `WindhawkBlur` support)

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
```

- **`styleConstants`**: Declares shared tokens, brushes, and radii.
- **`controlStyles`**: Direct XAML targets and styling definitions.
- **`themeResourceVariables`**: Resource brush replacements.
- **Unsupported Keys**: `webContentStyles`, `backgroundTranslucentEffect`, and `explorerFrameContainerHeight` are not supported by this mod and must never be declared.

---

## 3. Known Visual Tree Targets

### Root Flyout Panels
| Target Selector | Element Purpose |
|---|---|
| `Grid#NotificationCenterGrid` | Main Notification Center panel |
| `Grid#CalendarCenterGrid` | Calendar flyout container |
| `Grid#ControlCenterRegion` | Quick Settings (Win+A) main flyout frame |
| `Grid#L1Grid` | Primary layout grid inside Quick Settings |
| `Border#BackgroundBorder` | Base panel background container |

### Quick Settings Controls
| Target Selector | Element Purpose |
|---|---|
| `ControlCenter.ControlCenterPage` | Quick Settings root page |
| `ControlCenter.QuickActionTile` | Wi-Fi, Bluetooth, Airplane Mode toggle tiles |
| `ControlCenter.QuickActionTile > Border#TileRoot` | Card boundary of each quick action tile |
| `SplitButton#QuickActionSplitButton` | Two-part tiles with flyout chevrons (e.g. Wi-Fi network picker) |
| `Slider#BrightnessSlider` | Screen brightness slider bar |
| `Slider#VolumeSlider` | System audio volume slider bar |
| `Button#AllSettingsButton` | Footer cog button navigating to Windows Settings |

### Calendar Flyout
| Target Selector | Element Purpose |
|---|---|
| `CalendarView#CalendarView` | Calendar date picker control |
| `CalendarViewDayItem` | Individual day cells in the calendar grid |
| `Button#HeaderButton` | Month and year navigation header button |
| `Button#PreviousButton` / `Button#NextButton` | Previous/Next month pagination buttons |

### Media Controls
| Target Selector | Element Purpose |
|---|---|
| `Grid#MediaTransportControlsRegion` | Now Playing media card layout |
| `Grid#ThumbnailImage` | Album artwork thumbnail container |
| `Button#PlayPauseButton` | Media play/pause control button |
| `TextBlock#MediaTitle` | Track title text element |
| `TextBlock#MediaArtist` | Artist name text element |

### Toasts & Jump Lists
| Target Selector | Element Purpose |
|---|---|
| `Border#ToastBackgroundBorder` | System notification banner card |
| `ActionCenter.FlexibleToastView#FlexibleNormalToastView` | Toast notification interactive layout |
| `Border#JumpListRestyledAcrylic` | Taskbar right-click jump list background card |

---

## 4. Layered Glass Architecture

In universal layered glass themes:
1. Outer panels (`NotificationCenterGrid`, `CalendarCenterGrid`, `ControlCenterRegion`) use `WindhawkBlur` with `$Background` and specular `$BorderBrush` rims.
2. Native opaque drop shadows are collapsed (`Shadow:=`) and system backgrounds cleared.
3. Internal cards (quick action tiles, sliders, and calendar day cells) layer `$ElementBackground` and `$CornerRadiusAlt1` (10px) to establish visual depth.
