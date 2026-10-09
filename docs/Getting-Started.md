---
title: Getting Started
---

# Getting Started with Windhawk Themes

This guide walks you through setting up Windhawk and applying theme styles to your Windows 11 system.

---

## 1. Prerequisites

1. **Windows 11** (21H2, 22H2, 23H2, or 24H2 build 26100+).
2. **[Windhawk](https://windhawk.net/)** installed on your system.
3. Official Windhawk Styler mods installed from the Windhawk in-app mod browser:
   - **Windows 11 Taskbar Styler** (`windows-11-taskbar-styler`)
   - **Windows 11 Start Menu Styler** (`windows-11-start-menu-styler`)
   - **Windows 11 Notification Center Styler** (`windows-11-notification-center-styler`)
   - *(Optional)* **Windows 11 Settings Styler** (`windows-11-settings-styler`)

---

## 2. Applying Theme Styles

All theme configurations are distributed as clean, self-contained YAML files organized by theme project (e.g., `projects/command-center/`).

### Step-by-Step Import:

1. Open the **Windhawk** client application.
2. Locate the installed mod you wish to style (e.g. *Windows 11 Taskbar Styler*).
3. Click on the mod card and navigate to the **Settings** tab.
4. In the upper-right corner of the settings pane, click **Advanced** (or switch to the **Textual** editor mode).
5. Open the corresponding `.yml` file from this repository:
   - Taskbar: `projects/command-center/windows-11-taskbar-styler.yml`
   - Start Menu: `projects/command-center/windows-11-start-menu-styler.yml`
   - Notification Center: `projects/command-center/windows-11-notification-center-styler.yml`
6. Copy the entire contents of the YAML file and paste it into the Windhawk editor.
7. Click **Save** (and accept the elevation prompt if prompted).
8. The styles will apply immediately in real time!

---

## 3. Light & Dark Mode Compatibility

All themes in this suite are built using dynamic Windows XAML `{ThemeResource ...}` references:
- Tints dynamically derive from `{ThemeResource SystemChromeMediumColor}` and `{ThemeResource SystemAltLowColor}`.
- Text brushes map to `{ThemeResource TextFillColorPrimaryBrush}`.
- Accent colors derive from `{ThemeResource SystemAccentColor}`.

When you switch between Windows Light and Dark modes in Windows Settings, all shell surfaces automatically update without requiring mod restarts or file edits.

---

## 4. Companion Mod Enhancements

For users seeking additional desktop polish, curated companion mod configurations are provided under `projects/<project>/extras/`:
- **Dynamic Island for Windows**: Media and hardware status pill.
- **Enhanced Disk Usage**: Drive capacity meters in File Explorer.
- **File Operations Styler**: Translucent copy/move progress dialogs.
- **Start Button Colorizer**: Accent-tinted taskbar Start glyph.
- **Taskbar Clock Customization**: Telemetry HUD and custom seconds formatting.
