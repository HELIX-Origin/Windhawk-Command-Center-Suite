---
parent: Taskbar Styler
grand_parent: Target & Configuration Wiki
layout: wiki
title: Taskbar Companions
---

# Taskbar Companion Mods: Technical Settings Reference

Complete technical settings schema and options for companion mods that operate alongside the Windows 11 Taskbar Styler.

---

## 1. Taskbar Clock Customization (`taskbar-clock-customization`)

The **Taskbar Clock Customization** mod enhances the Windows taskbar clock with custom formatting strings, precise seconds display, and a telemetry HUD flyout shown on hover.

* **Mod ID**: `taskbar-clock-customization`
* **Target Process**: `explorer.exe`

### Configuration Directives & Schema

| Setting Key | Type | Default Value | Description & Supported Options |
|---|---|---|---|
| `ShowSeconds` | Integer (0/1) | `0` | Displays real-time ticking seconds on the taskbar clock. |
| `TimeFormat` | String | `hh':'mm tt` | Time format string using Windows date/time format specifiers. Semicolons separate single-line from multiline formats. |
| `DateFormat` | String | `ddd, MMM dd` | Date format string for long date display. |
| `DateLocale` | String | `""` | Optional locale override string (e.g. `en-US`, `ja-JP`). |
| `TopLine` | String | `""` | Primary display line on the taskbar. Supports tokens like `%date%`, `%time%`, and unicode glyphs. |
| `BottomLine` | String | `""` | Secondary display line rendered beneath the top line. |
| `TooltipLine` | String | `""` | Custom tooltip string shown when hovering over the clock. Supports tokens: `%cpu%`, `%gpu%`, `%ram%`, `%vram%`, `%upload_speed%`, `%download_speed%`, `%date2%`, `%time2%`, and `%n%` (newline). |
| `TooltipLineMode` | String | `append` | Governs tooltip behavior: `append` adds to native tooltip, `replace` overwrites it completely. |
| `Width` | Integer | `0` | Fixed width in pixels for the taskbar clock area (0 = automatic width). |
| `Height` | Integer | `0` | Fixed height in pixels for the clock area (0 = automatic height). |
| `MaxWidth` | Integer | `0` | Maximum width constraint in pixels (0 = unconstrained). |
| `TextSpacing` | Integer | `0` | Spacing adjustment between text characters. |
| `DataCollection.UpdateInterval` | Integer | `1` | Polling frequency in seconds for live telemetry counters. |
| `DataCollection.NetworkMetricsFormat` | String | `bytesDynamic` | Unit format for network transfer rates: `bytesDynamic`, `mbitsDynamic`, `kbitsDynamic`. |
| `DateStyle.Hidden` | Integer (0/1) | `0` | Hides the date text block inside the clock control. |
| `TimeStyle.TextAlignment` | String | `Left` | Text alignment within the time display block: `Left`, `Center`, `Right`. |

---

## 2. Taskbar Tray and Icon Tweaks (`taskbar-tray-and-icon-tweaks`)

The **Taskbar Tray and Icon Tweaks** mod selectively manages system status indicators, notification bell visibility, and the Show Desktop edge button.

* **Mod ID**: `taskbar-tray-and-icon-tweaks`
* **Target Process**: `explorer.exe`

### Configuration Directives & Schema

| Setting Key | Type | Default Value | Description & Supported Options |
|---|---|---|---|
| `hideVolumeIcon` | Integer (0/1) | `0` | Toggles visibility of the audio volume speaker tray icon. |
| `hideNetworkIcon` | Integer (0/1) | `0` | Toggles visibility of the network (Wi-Fi / Ethernet) tray icon. |
| `hideBatteryIcon` | Integer (0/1) | `0` | Toggles visibility of the battery indicator icon on portable devices. |
| `grayscaleBatteryIcon` | Integer (0/1) | `0` | Renders the battery status icon in grayscale. |
| `hideMicrophoneIcon` | Integer (0/1) | `0` | Toggles visibility of the microphone in-use privacy indicator. |
| `hideGeolocationIcon` | Integer (0/1) | `0` | Toggles visibility of the location tracking compass pin icon. |
| `hideStudioEffectsIcon` | Integer (0/1) | `0` | Toggles visibility of the Windows Studio Effects camera/audio indicator. |
| `hideRecallIcon` | Integer (0/1) | `0` | Toggles visibility of the Windows Recall AI snapshot tray icon on Copilot+ PCs. |
| `hideLanguageBar` | Integer (0/1) | `0` | Toggles visibility of the input method / keyboard layout switcher indicator. |
| `hideBellIcon` | String | `never` | Notification bell badge visibility: `never`, `always`, `whenInactive`, `whenInactiveAndNoDnd`. |
| `showDesktopButtonWidth` | Integer | `0` | Width in pixels of the Show Desktop strip at the extreme taskbar edge (0 = system default). |

---

## 3. Dynamic Island for Windows (`dynamic-island-for-windows`)

The **Dynamic Island for Windows** mod provides a floating status pill that handles media playback HUDs, volume sliders, and hardware alerts.

* **Mod ID**: `dynamic-island-for-windows`
* **Target Process**: Desktop shell overlay window

### Configuration Directives & Schema

| Setting Key | Type | Default Value | Description & Supported Options |
|---|---|---|---|
| `Appearance.Position` | String | `top-center` | Anchor placement on screen: `top-center`, `top-left`, `top-right`, `bottom-center`. |
| `Appearance.TargetMonitor` | String | `primary` | Target display: `primary`, `cursor`, `all`. |
| `Appearance.OffsetX` / `OffsetY` | Integer | `0` | Positional offset in pixels from the anchor edge. |
| `Appearance.ShapeStyle` | String | `default` | Island geometry: `default`, `w11`, `ios`. |
| `Appearance.SizeScale` | String | `'1.0'` | Global geometry scaling multiplier. |
| `Behavior.AlwaysOnTop` | Integer (0/1) | `0` | Keeps overlay above all top-level windows. |
| `Behavior.ExpandOnHover` | Integer (0/1) | `1` | Automatically expands modules into detailed view cards on hover. |
| `Behavior.AutoHideFullscreen` | Integer (0/1) | `1` | Hides overlay during full-screen games or video playback. |
| `Themes.ThemePreset` | String | `glass` | Visual preset: `dark`, `light`, `glass`, `graphite`. |
| `Themes.PillBgColor` | String (Hex) | `#000000` | Base background color fill for the island container. |
| `Themes.PillOpacity` | Integer | `90` | Base surface opacity percentage (0–100). |
| `Themes.TintIntensity` | Integer | `50` | Blur tint intensity percentage (0–100). |
| `Indicators.PrivacyDots` | Integer (0/1) | `1` | Enables camera and microphone access indicator dots. |
| `Modules.Media` | Integer (0/1) | `1` | Enables media playback controls module. |
| `Modules.Volume` | Integer (0/1) | `1` | Enables interactive volume HUD slider module. |

---

## 4. Start Button Colorizer (`start-button-colorizer`)

* **Mod ID**: `start-button-colorizer`
* **Target Process**: `explorer.exe`

### Configuration Directives & Schema

| Setting Key | Type | Default Value | Description & Supported Options |
|---|---|---|---|
| `color` | String | `custom` | Color source: `accent` (matches system accent), `custom`, `random`. |
| `effects.saturation` | Integer | `100` | Color saturation percentage (0–100). |
| `effects.brightness` | Integer | `100` | Color brightness percentage (0–100). |
| `effects.opacity` | Integer | `100` | Icon opacity percentage (0–100). |
| `size` | Integer | `100` | Icon glyph scaling percentage. |
