---
layout: catalogue-item
title: Command Center Suite
summary: Unified frosted glass design language with top-lit specular rim borders and harmonized radii tiers across Windows 11 shell surfaces.
category: Frosted Glass
badge: Featured Suite
version: M.02b
author: HELIX Origin
tags:
  - Frosted Glass
  - WindhawkBlur
  - Taskbar
  - Start Menu
  - Notification Center
  - Dark Theme
docs_url: /docs/
github_url: https://github.com/HELIX-Origin/Windhawk-Themes/tree/main/projects/command-center
---

## 🧭 Overview

The **Command Center Suite** is our premier unified theme suite implementing the signature **"Command Center Glass"** design language for Windows 11. Engineered with precision mathematical tokens, it eliminates visual dissonance across disconnected shell surfaces and replaces flat, opaque Windows 11 chrome with high-performance translucent glass materials.

<img width="80%" align="center" src="{{ 'assets/images/command-center-header.png' | relative_url }}" alt="Command Center Suite Header">

---

## ✨ Design Pillars

- **Unified Frosted Blur**: Consistent `WindhawkBlur` (base `BlurAmount="20"`, tinted dynamically via `{ThemeResource SystemChromeMediumColor}`) establishes a solid frosted glass base across all shell panes.
- **Top-Lit Specular Rim**: Signature multi-stop vertical gradient border (`#60808080` → `#50404040` → `#40808080`) with physical glass edge lighting (`BorderThickness="0.3,1,0.3,1"`).
- **Proportional Radii Hierarchy**: Strict radius tiers matching Windows 11 Fluent guidelines:
  - **XL (35px)**: Top-level flyout root containers (Start Menu, Notification Center flyouts).
  - **L (25px)**: Prominent input pills and search bars.
  - **M (15px)**: Grouping containers and secondary cards.
  - **S (10px)**: Action tiles, buttons, calendar cells.
  - **XS (6px)**: Context menus and tooltips.
- **Intentional Layering**: Collapses distracting native drop shadows and heavy opaque overlays to let translucent glass cards float cleanly.

---

## 🔍 Supported Surface Mods

| Styler Mod | Mod ID | Targeted Surface | Status |
|---|---|---|---|
| **Windows 11 Taskbar Styler** | `windows-11-taskbar-styler` | Taskbar panel, system tray, running app buttons | ✅ Shipped Reference |
| **Windows 11 Start Menu Styler** | `windows-11-start-menu-styler` | Start menu frame, pinned grid, all apps, search pill | ✅ Shipped Reference |
| **Windows 11 Notification Center Styler** | `windows-11-notification-center-styler` | Action center, quick settings flyout, calendar grid | ✅ Shipped Reference |
| **Windows 11 Settings Styler** | `windows-11-settings-styler` | Navigation sidebar, card views, settings search | 🌐 In Base Scope |
| **Windows 11 File Explorer Styler** | `windows-11-file-explorer-styler` | Tabs, address bar, navigation tree | ⏸️ Deferred (M.03) |

---

## 🛠️ Installation & Setup

1. Install **[Windhawk](https://windhawk.net/)** on Windows 11 (22H2, 23H2, or 24H2).
2. Install the three core styler mods from the Windhawk Mod Manager:
   - *Windows 11 Taskbar Styler*
   - *Windows 11 Start Menu Styler*
   - *Windows 11 Notification Center Styler*
3. Copy the YAML styler configurations from the suite directory in the repository:
   - [`windows-11-taskbar-styler.yml`](https://github.com/HELIX-Origin/Windhawk-Themes/blob/main/projects/command-center/windows-11-taskbar-styler.yml)
   - [`windows-11-start-menu-styler.yml`](https://github.com/HELIX-Origin/Windhawk-Themes/blob/main/projects/command-center/windows-11-start-menu-styler.yml)
   - [`windows-11-notification-center-styler.yml`](https://github.com/HELIX-Origin/Windhawk-Themes/blob/main/projects/command-center/windows-11-notification-center-styler.yml)
4. Paste into the respective mod's **Advanced** tab in Windhawk settings and click **Save**.

---

## 🧪 Verification & Gate Status

- **Static Validation Gate**: `pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1` verified with **0 errors**.
- **Windows 11 Compatibility**: Verified across Windows 11 builds `22631.x` (23H2) and `26100.x` (24H2).
