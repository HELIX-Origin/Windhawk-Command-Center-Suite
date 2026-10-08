# 🧩 Extras & Companion Mod Configurations

This directory contains curated companion mod configurations for the **Windhawk Command Center Suite**. While the primary styler mods in `src/` govern the foundational frosted glass surfaces and controls of the shell, these companion mods extend the aesthetic into supplemental shell utilities, status indicators, dialogs, and flyout behaviors.

---

## 📋 Companion Mods Overview

| Companion Mod | Windhawk Mod ID | Configuration File | Target Process | Scope & Function |
|---|---|---|---|---|
| **Dynamic Island for Windows** | [`dynamic-island-for-windows`](https://windhawk.net/mods/dynamic-island-for-windows) | [`dynamic-island-for-windows.yml`](./dynamic-island-for-windows.yml) | Desktop shell overlay | Floating top pill with media, volume HUD, hardware stats, and weather |
| **Enhanced Disk Usage** | [`enhanced-disk-usage`](https://windhawk.net/mods/enhanced-disk-usage) | [`enhanced-disk-usage.yml`](./enhanced-disk-usage.yml) | `explorer.exe` | Rounded glass drive capacity bars with accent gradients in File Explorer |
| **File Operations Styler** | [`file-operations-styler`](https://windhawk.net/mods/file-operations-styler) | [`file-operations-styler.yml`](./file-operations-styler.yml) | `explorer.exe` | Modernized circular progress indicators and typography for file transfers |
| **Fully Customizable Winver** | [`fully-customizeable-winver`](https://windhawk.net/mods/fully-customizeable-winver) | [`fully-customizeable-winver.yml`](./fully-customizeable-winver.yml) | `winver.exe` | Minimalist dark slate About Windows dialog with centered system branding |
| **Shell Flyout Positions** | [`shell-flyout-positions`](https://windhawk.net/mods/shell-flyout-positions) | [`shell-flyout-positions.yml`](./shell-flyout-positions.yml) | `explorer.exe` | Tray alignment and bottom-edge anchoring for shell popups and flyouts |
| **Start Button Colorizer** | [`start-button-colorizer`](https://windhawk.net/mods/start-button-colorizer) | [`start-button-colorizer.yml`](./start-button-colorizer.yml) | `explorer.exe` | Tint taskbar Start button glyph to match Windows system accent color |
| **Taskbar Clock Customization** | [`taskbar-clock-customization`](https://windhawk.net/mods/taskbar-clock-customization) | [`taskbar-clock-customization.yml`](./taskbar-clock-customization.yml) | `explorer.exe` | Seconds display, custom format strings, and hardware/weather tooltip HUD |
| **Taskbar Tray and Icon Tweaks** | [`taskbar-tray-and-icon-tweaks`](https://windhawk.net/mods/taskbar-tray-and-icon-tweaks) | [`taskbar-tray-and-icon-tweaks.yml`](./taskbar-tray-and-icon-tweaks.yml) | `explorer.exe` | Declutters background noise: hides Recall, Studio Effects, and inactive bell |

---

## 🔍 Detailed Mod Configurations

### 1. Dynamic Island for Windows (`dynamic-island-for-windows.yml`)
* **Mod Link**: [Dynamic Island for Windows on Windhawk](https://windhawk.net/mods/dynamic-island-for-windows)
* **Design Role**: Provides an iOS/macOS-inspired interactive status pill anchored at the top-center of the primary monitor that complements the Command Center aesthetic.
* **Key Configuration Highlights**:
  * **Theme & Material**: Uses the `graphite` preset with `PillBgColor: '#08080A'`, 96% opacity, 72% tint intensity, subtle drop shadows, and system accent bloom.
  * **Behavior**: Expands on hover with smooth animations, autohides in full-screen applications, and features a manual toggle hotkey (`Ctrl + Alt + D`).
  * **Active Modules**: Media playback controls with auto-expand, volume HUD overlay, battery and Bluetooth status, clipboard history, weather reporting in Fahrenheit, and hardware monitoring metrics (CPU, GPU, RAM, Disk, FPS).
  * **Privacy Indicators**: Displays camera (green) and microphone (amber) access dots matching native mobile OS conventions.

### 2. Enhanced Disk Usage (`enhanced-disk-usage.yml`)
* **Mod Link**: [Enhanced Disk Usage on Windhawk](https://windhawk.net/mods/enhanced-disk-usage)
* **Design Role**: Replaces the dated Windows 10/11 progress bars in File Explorer "This PC" with modern, rounded capacity meters.
* **Key Configuration Highlights**:
  * **Geometry**: `cornerRadius: 5` and `borderThickness: 4` with a semi-transparent border (`#80BBBBBB`) and a translucent background track (`#20000000`).
  * **Color Dynamics**: Automatically derives its gradient from the Windows system accent color (`useAccentColor: 1`, delta 15) for healthy drives, shifting to red alert gradients when storage is critically full.

### 3. File Operations Styler (`file-operations-styler.yml`)
* **Mod Link**: [File Operations Styler on Windhawk](https://windhawk.net/mods/file-operations-styler)
* **Design Role**: Enhances the Windows file transfer progress dialog (copy, move, delete) to match clean modern UI standards.
* **Key Configuration Highlights**:
  * **Visual Presentation**: Enables the secondary circular progress bar (`showCurrentFileProgressBar: 1`) with custom stroke weighting (`circleThickness: 7`, `progressThickness: 8`).
  * **Palette & Layout**: Integrates system accent colors and sets clear typographic sizing across summary text (23pt), body details (11pt), and percentage indicators (26pt).

### 4. Fully Customizable Winver (`fully-customizeable-winver.yml`)
* **Mod Link**: [Fully Customizable Winver on Windhawk](https://windhawk.net/mods/fully-customizeable-winver)
* **Design Role**: Strips the legacy Windows 95-era text blocks from `winver.exe`, transforming it into a clean, minimalist system card.
* **Key Configuration Highlights**:
  * **Decluttering**: Completely hides the user registration lines, organizational info, licensing paragraph, and horizontal separators.
  * **Styling**: Applies a centered, dark slate theme (`background: 30,30,30`, `textColor: 180,180,180`), centers the dialog on screen, and showcases the Windows system logo centered vertically.

### 5. Shell Flyout Positions (`shell-flyout-positions.yml`)
* **Mod Link**: [Shell Flyout Positions on Windhawk](https://windhawk.net/mods/shell-flyout-positions)
* **Design Role**: Fine-tunes popup window positioning so shell panels anchor flush with the taskbar tray and display boundaries.
* **Key Configuration Highlights**:
  * **Notification Center**: Horizontally aligned to the tray area (`horizontalAlignment: tray`).
  * **Action Center**: Aligned consistently with the tray layout (`horizontalAlignment: same`).
  * **Start Menu**: Anchored to the bottom taskbar boundary (`verticalAlignment: bottom`).

### 6. Start Button Colorizer (`start-button-colorizer.yml`)
* **Mod Link**: [Start Button Colorizer on Windhawk](https://windhawk.net/mods/start-button-colorizer)
* **Design Role**: Replaces the default white/gray Windows icon on the taskbar with an accent-tinted glyph.
* **Key Configuration Highlights**:
  * **Color Source**: Targets `color: accent` at 100% saturation and brightness, ensuring the Start button reflects the user's active theme accent color and harmonizes with the Command Center glass surface.

### 7. Taskbar Clock Customization (`taskbar-clock-customization.yml`)
* **Mod Link**: [Taskbar Clock Customization on Windhawk](https://windhawk.net/mods/taskbar-clock-customization)
* **Design Role**: Upgrades the taskbar system clock with multi-line precision formatting and an extensive telemetry tooltip.
* **Key Configuration Highlights**:
  * **Taskbar Display**: Shows seconds (`ShowSeconds: 1`) and custom emoji-prefixed formatting (`📅 %date% 🕒 %time%`).
  * **Hover Telemetry HUD**: Generates a detailed system tooltip on hover displaying secondary timezone, live CPU / GPU / RAM / VRAM usage, real-time network upload & download speeds, RSS news headlines, and weather conditions.

### 8. Taskbar Tray and Icon Tweaks (`taskbar-tray-and-icon-tweaks.yml`)
* **Mod Link**: [Taskbar Tray and Icon Tweaks on Windhawk](https://windhawk.net/mods/taskbar-tray-and-icon-tweaks)
* **Design Role**: Eliminates visual clutter and redundant icons from the Windows 11 system tray.
* **Key Configuration Highlights**:
  * **Icon Reductions**: Hides Windows Recall, Studio Effects, geolocation, microphone indicators, and the language bar.
  * **Smart Bell**: Collapses the notification bell icon when there are no active unread alerts or Do Not Disturb states (`hideBellIcon: whenInactiveAndNoDnd`).
  * **Show Desktop**: Sets a compact 8px Show Desktop hit area at the edge of the taskbar.

---

## 🛠️ How to Import Companion Mod Configurations

1. Open **Windhawk** and navigate to the **Explore** tab.
2. Search for the desired companion mod (e.g. *Taskbar Clock Customization* or *Dynamic Island for Windows*) and click **Details → Install**.
3. Once installed, navigate to the mod's **Settings** tab.
4. Click the options menu (or switch to **Textual mode**).
5. Copy the contents of the matching YAML file in `src/extras/` and paste it into the mod's settings box.
6. Click **Save settings**. Windhawk applies the configuration immediately without requiring an Explorer restart.