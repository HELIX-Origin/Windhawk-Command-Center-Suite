# 🧩 Extras & Companion Mod Configurations

This directory contains curated companion mod configurations for the **Windhawk Command Center Suite**. While the base styler mods in [`src/`](../) define the foundational "Command Center Glass" surfaces (Taskbar, Start Menu, Notification Center, File Explorer), these companion configs extend the aesthetic into supplemental shell utilities, status indicators, dialogs, flyouts, and system UI behaviors.

## Table of Contents

- [Overview](#overview)
- [Companion Mods Matrix](#companion-mods-matrix)
- [Detailed Configurations](#detailed-configurations)
  - [1. Dynamic Island for Windows](#1-dynamic-island-for-windows-dynamic-island-for-windowsyml)
  - [2. Enhanced Disk Usage](#2-enhanced-disk-usage-enhanced-disk-usageyml)
  - [3. File Operations Styler](#3-file-operations-styler-file-operations-styleryml)
  - [4. Fully Customizable Winver](#4-fully-customizable-winver-fully-customizeable-winveryml)
  - [5. Shell Flyout Positions](#5-shell-flyout-positions-shell-flyout-positionsyml)
  - [6. Start Button Colorizer](#6-start-button-colorizer-start-button-colorizeryml)
  - [7. Taskbar Clock Customization](#7-taskbar-clock-customization-taskbar-clock-customizationyml)
  - [8. Taskbar Tray and Icon Tweaks](#8-taskbar-tray-and-icon-tweaks-taskbar-tray-and-icon-tweaksyml)
- [How to Import Companion Mod Configurations](#how-to-import-companion-mod-configurations)
- [Notes & Compatibility](#notes--compatibility)
- [Related Documentation](#related-documentation)

## Overview

The companion set is intentionally scoped to augment the Command Center theme without altering the core four styler mods. Each YAML is provided as-is for the corresponding official Windhawk mod; behavior depends on mod version and Windows 11 build.

## Companion Mods Matrix

| Companion Mod | Windhawk Mod ID | Configuration File | Target Process | Scope & Function |
|---|---|---|---|---|
| **Dynamic Island for Windows** | [`dynamic-island-for-windows`](https://windhawk.net/mods/dynamic-island-for-windows) | [`dynamic-island-for-windows.yml`](./dynamic-island-for-windows.yml) | Desktop shell overlay | Floating top-center pill (media, volume HUD, hardware stats, weather, privacy indicators) |
| **Enhanced Disk Usage** | [`enhanced-disk-usage`](https://windhawk.net/mods/enhanced-disk-usage) | [`enhanced-disk-usage.yml`](./enhanced-disk-usage.yml) | `explorer.exe` | Rounded glass drive capacity bars with accent-driven gradients in File Explorer |
| **File Operations Styler** | [`file-operations-styler`](https://windhawk.net/mods/file-operations-styler) | [`file-operations-styler.yml`](./file-operations-styler.yml) | `explorer.exe` | Modernized circular progress and typography for copy/move/delete dialogs |
| **Fully Customizable Winver** | [`fully-customizeable-winver`](https://windhawk.net/mods/fully-customizeable-winver) | [`fully-customizeable-winver.yml`](./fully-customizeable-winver.yml) | `winver.exe` | Minimalist slate About Windows card with centered branding and reduced clutter |
| **Shell Flyout Positions** | [`shell-flyout-positions`](https://windhawk.net/mods/shell-flyout-positions) | [`shell-flyout-positions.yml`](./shell-flyout-positions.yml) | `explorer.exe` | Tray-aligned positioning for Notification/Action Center and Start Menu anchoring |
| **Start Button Colorizer** | [`start-button-colorizer`](https://windhawk.net/mods/start-button-colorizer) | [`start-button-colorizer.yml`](./start-button-colorizer.yml) | `explorer.exe` | Tints taskbar Start glyph to match Windows system accent color |
| **Taskbar Clock Customization** | [`taskbar-clock-customization`](https://windhawk.net/mods/taskbar-clock-customization) | [`taskbar-clock-customization.yml`](./taskbar-clock-customization.yml) | `explorer.exe` | Seconds display, custom format, and hover telemetry HUD (time zones, CPU/GPU/RAM/VRAM, network, RSS, weather) |
| **Taskbar Tray and Icon Tweaks** | [`taskbar-tray-and-icon-tweaks`](https://windhawk.net/mods/taskbar-tray-and-icon-tweaks) | [`taskbar-tray-and-icon-tweaks.yml`](./taskbar-tray-and-icon-tweaks.yml) | `explorer.exe` | Tray declutter: hides Recall/Studio Effects/geolocation/mic/language bar; smart bell visibility; compact Show Desktop area |

## Detailed Configurations

### 1. Dynamic Island for Windows (`dynamic-island-for-windows.yml`)

- **Mod Link:** [Dynamic Island for Windows on Windhawk](https://windhawk.net/mods/dynamic-island-for-windows)
- **Design Role:** iOS/macOS-inspired interactive status pill anchored top-center; complements Command Center aesthetic.
- **Key Highlights:**
  - **Theme/Material:** Graphite preset with `PillBgColor: '#08080A'`, 96% opacity, 72% tint intensity, subtle drop shadows, system accent bloom.
  - **Behavior:** Expands on hover, smooth animations, autohides in full-screen apps, hotkey toggle (`Ctrl + Alt + D`).
  - **Modules:** Media playback (auto-expand), volume HUD, battery/Bluetooth, clipboard history, weather (Fahrenheit), hardware metrics (CPU/GPU/RAM/Disk/FPS).
  - **Privacy:** Camera (green) and microphone (amber) access indicators.

### 2. Enhanced Disk Usage (`enhanced-disk-usage.yml`)

- **Mod Link:** [Enhanced Disk Usage on Windhawk](https://windhawk.net/mods/enhanced-disk-usage)
- **Design Role:** Replaces legacy File Explorer "This PC" capacity bars with modern rounded glass meters.
- **Key Highlights:**
  - **Geometry:** `cornerRadius: 5`, `borderThickness: 4`, semi-transparent border (`#80BBBBBB`), translucent track (`#20000000`).
  - **Color Dynamics:** Uses Windows system accent (`useAccentColor: 1`, delta 15) for normal drives; shifts to red alert gradients at critical fullness.

### 3. File Operations Styler (`file-operations-styler.yml`)

- **Mod Link:** [File Operations Styler on Windhawk](https://windhawk.net/mods/file-operations-styler)
- **Design Role:** Modernizes Windows file transfer dialogs (copy/move/delete).
- **Key Highlights:**
  - **Progress:** Enables secondary circular progress bar (`showCurrentFileProgressBar: 1`), custom stroke weights (`circleThickness: 7`, `progressThickness: 8`).
  - **Typography/Palette:** Integrates system accent, tuned sizes (summary 23pt, details 11pt, percentage 26pt).

### 4. Fully Customizable Winver (`fully-customizeable-winver.yml`)

- **Mod Link:** [Fully Customizable Winver on Windhawk](https://windhawk.net/mods/fully-customizeable-winver)
- **Design Role:** Minimalist slate About Windows card replacing legacy text-heavy layout.
- **Key Highlights:**
  - **Declutter:** Hides registration/org/licensing lines and horizontal separators.
  - **Styling:** Centered dark slate theme (`background: 30,30,30`, `textColor: 180,180,180`), dialog centered, Windows logo centered vertically.

### 5. Shell Flyout Positions (`shell-flyout-positions.yml`)

- **Mod Link:** [Shell Flyout Positions on Windhawk](https://windhawk.net/mods/shell-flyout-positions)
- **Design Role:** Anchors shell popups flush with taskbar tray/boundaries.
- **Key Highlights:**
  - **Notification Center:** Horizontal alignment to tray (`horizontalAlignment: tray`).
  - **Action Center:** Consistent tray alignment (`horizontalAlignment: same`).
  - **Start Menu:** Bottom-anchored (`verticalAlignment: bottom`).

### 6. Start Button Colorizer (`start-button-colorizer.yml`)

- **Mod Link:** [Start Button Colorizer on Windhawk](https://windhawk.net/mods/start-button-colorizer)
- **Design Role:** Tints taskbar Start glyph to system accent.
- **Key Highlights:**
  - **Color Source:** `color: accent` at 100% saturation/brightness for seamless harmony with Command Center glass.

### 7. Taskbar Clock Customization (`taskbar-clock-customization.yml`)

- **Mod Link:** [Taskbar Clock Customization on Windhawk](https://windhawk.net/mods/taskbar-clock-customization)
- **Design Role:** Precision clock display + comprehensive hover telemetry HUD.
- **Key Highlights:**
  - **Taskbar Display:** Seconds enabled (`ShowSeconds: 1`), custom emoji-prefixed format (`📅 %date% 🕒 %time%`).
  - **Hover HUD:** Secondary timezone, live CPU/GPU/RAM/VRAM usage, real-time network up/down, RSS headlines, weather conditions.

### 8. Taskbar Tray and Icon Tweaks (`taskbar-tray-and-icon-tweaks.yml`)

- **Mod Link:** [Taskbar Tray and Icon Tweaks on Windhawk](https://windhawk.net/mods/taskbar-tray-and-icon-tweaks)
- **Design Role:** Reduces tray noise and redundant icons.
- **Key Highlights:**
  - **Icon Reductions:** Hides Windows Recall, Studio Effects, geolocation, microphone indicators, language bar.
  - **Smart Bell:** `hideBellIcon: whenInactiveAndNoDnd` (hidden when no unread alerts and not in DND).
  - **Show Desktop:** Compact 8px hit area at taskbar edge.

## How to Import Companion Mod Configurations

1. Open **Windhawk** → **Explore** tab.
2. Search for and install the desired companion mod (e.g., *Taskbar Clock Customization*, *Dynamic Island for Windows*).
3. Open the mod’s **Details → Settings** (Advanced/Textual mode as needed).
4. Copy the entire contents of the matching YAML file from `src/extras/` and paste into the mod’s settings editor.
5. Click **Save settings**. The configuration applies immediately (no Explorer/system restart required).

## Notes & Compatibility

- These are companion configurations for official Windhawk mods; updates to those mods may introduce new settings/fields—re-validate after mod updates.
- Some features depend on Windows 11 build and optional services (e.g., weather/RSS/network metrics).
- Use alongside base suite styles; extras are non-invasive and do not replace the four core styler YAMLs.

## Related Documentation

- **Root overview:** [`../../README.md`](../../README.md)
- **Base styles:** [`../README.md`](../README.md) (canonical tokens, per-mod coverage)
- **Validation:** [`../../tools/Test-WindhawkStyles.ps1`](../../tools/Test-WindhawkStyles.ps1)
- **Tracking:** [`../../CHANGELOG.md`](../../CHANGELOG.md)
