---
parent: File Explorer Styler
grand_parent: Target & Configuration Wiki
layout: wiki
title: File Explorer Companions
---

# File Explorer Companion Mods: Technical Settings Reference

Complete technical settings schema and options for companion mods that operate alongside the Windows 11 File Explorer Styler.

---

## 1. Enhanced Disk Usage (`enhanced-disk-usage`)

The **Enhanced Disk Usage** mod customizes the drive capacity bars displayed in File Explorer "This PC" with rounded meters, translucent track backgrounds, and accent color gradients.

* **Mod ID**: `enhanced-disk-usage`
* **Target Process**: `explorer.exe`

### Configuration Directives & Schema

| Setting Key | Type | Default Value | Description & Supported Options |
|---|---|---|---|
| `enableBarCustomization` | Integer (0/1) | `1` | Master toggle enabling custom bar graphics. |
| `useAccentColor` | Integer (0/1) | `0` | Tints the drive capacity fill dynamically using the active Windows system accent color. |
| `accentColorGradientDelta` | Integer | `0` | Luminance offset creating a gradient across the accent fill. |
| `barNormalStart` | String (Hex) | `#FF2ECC71` | Gradient start color when accent color is disabled. |
| `barNormalEnd` | String (Hex) | `#FF27AE60` | Gradient end color when accent color is disabled. |
| `barFullStart` | String (Hex) | `#FFE74C3C` | Warning gradient start color when drive space is critical. |
| `barFullEnd` | String (Hex) | `#FFC0392B` | Warning gradient end color when drive space is critical. |
| `gradientDirection` | Integer | `90` | Gradient angle in degrees (e.g. 90 = vertical, 0 = horizontal). |
| `cornerRadius` | Integer | `0` | Corner border radius in pixels for the capacity meter bar. |
| `borderThickness` | Integer | `0` | Outer border stroke width in pixels. |
| `borderColor` | String (Hex) | `#00000000` | Color and opacity for the meter border rim. |
| `trackColor` | String (Hex) | `#40000000` | Background track color representing unallocated space. |
| `enableTextCustomization` | Integer (0/1) | `0` | Enables custom drive capacity label formatting. |
| `formatString` | String | `"%f free of %t total\n%p used"` | Custom text template supporting `%f` (free), `%t` (total), `%p` (percent). |
| `enableWordEllipsis` | Integer (0/1) | `1` | Truncates long drive labels with ellipses when space is constrained. |

---

## 2. File Operations Styler (`file-operations-styler`)

The **File Operations Styler** mod modernizes Windows file transfer dialogs (copying, moving, deleting) with circular progress rings and tuned typography.

* **Mod ID**: `file-operations-styler`
* **Target Process**: `explorer.exe`

### Configuration Directives & Schema

| Setting Key | Type | Default Value | Description & Supported Options |
|---|---|---|---|
| `showCurrentFileProgressBar` | Integer (0/1) | `0` | Displays a secondary circular progress ring tracking the currently transferring file. |
| `customization.enabled` | Integer (0/1) | `1` | Master toggle for dialog styling. |
| `customization.preset` | String | `default` | Color palette preset: `default`, `system` (matches Windows accent), `custom`. |
| `customization.style.circleThickness` | Integer | `5` | Stroke width in pixels for the circular progress ring. |
| `customization.style.progressThickness` | Integer | `6` | Stroke width in pixels for the horizontal overall progress bar. |
| `customization.text.fontPreset` | String | `default` | Typography preset for dialog labels. |
| `customization.text.summarySize` | Integer | `18` | Font point size for the primary file transfer headline. |
| `customization.text.bodySize` | Integer | `10` | Font point size for transfer speed and item count details. |
| `customization.text.percentSize` | Integer | `20` | Font point size for the numerical completion percentage. |

---

## 3. Fully Customizable Winver (`fully-customizeable-winver`)

* **Mod ID**: `fully-customizeable-winver`
* **Target Process**: `winver.exe`

### Configuration Directives & Schema

| Setting Key | Type | Default Value | Description & Supported Options |
|---|---|---|---|
| `logo.enabled` | Integer (0/1) | `1` | Displays the OS branding emblem. |
| `logo.center` | Integer (0/1) | `0` | Horizontally and vertically centers the OS logo. |
| `windowColors.background` | RGB String | `255,255,255` | Background fill color for the About Windows dialog. |
| `windowColors.textColor` | RGB String | `0,0,0` | Primary text color for version and build strings. |
| `modifyWindows[Separator].hidden` | Integer (0/1) | `0` | Toggles visibility of the horizontal separator line. |
| `modifyWindows[LicenseInfo].hidden` | Integer (0/1) | `0` | Toggles visibility of EULA and copyright text lines. |
