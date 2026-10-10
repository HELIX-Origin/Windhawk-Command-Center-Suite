---
title: Documentation Home
---

# Windhawk Themes Documentation

Welcome to the **Windhawk Themes** engineering documentation. This site covers the developer framework, hybrid inspection toolchain, and universal target references for creating and maintaining your own custom Windows 11 theme suites using official Windhawk styler mods.

---

## 🧭 Navigation & Topic Guides

### 🌟 Overview
- **[Getting Started](_docs/Getting-Started.md)** — Setting up the framework, using the inspection tools, and scaffolding a new theme suite.
- **[Architecture & Design](_docs/Architecture.md)** — Universal shell architecture, visual hierarchy, specular rim dynamics, and framework boundaries.

### 🪟 Shell Surfaces
- **[Start Menu Styler](_docs/Start-Menu.md)** — Separated-island flyout layout, category groupings, view pills, and Phone Link companion cards.
- **[Taskbar Styler](_docs/Taskbar.md)** — Floating taskbar frame, grouped task list button pills, system tray styling, and hardware telemetry HUDs.
- **[Notification Center & Quick Settings](_docs/Notification-Center.md)** — Quick action tiles, sliders, calendar flyout, toast popups, and jump lists.
- **[Settings Styler](_docs/Settings.md)** — Windows 11 modern Settings app (`SystemSettings.exe`), navigation cards, and search box styling.
- **[File Explorer Styler](_docs/File-Explorer.md)** — WinUI 3 tab controls, address bar, breadcrumbs, search pills, and classic Win32 boundaries.

### 🛠️ Toolchain & Inspection
- **[Hybrid XAML Inspector](_docs/Toolchain.md)** — The native C++ TAP injection engine (`xaml_dump.exe`) and unified Python CLI (`inspect_xaml.py`).
- **[Visual Tree Diagnostics](_docs/Diagnostics.md)** — Querying elements, automated surface activation, and ShareX screenshot capture.
- **[UWPSpy Manual Inspection](_docs/UWPSpy.md)** — Interactive GUI visual tree inspection guide for live UWP and WinUI 3 trees.

### 📐 Engineering Standards
- **[Style Syntax & Tokens](_docs/Syntax-Standards.md)** — YAML syntax rules, strict constant ordering, and token declarations.
- **[Glass Material Recipes](_docs/Glass-Recipes.md)** — `WindhawkBlur` shaders, `AcrylicBrush` usage, gradient rims, and chrome collapsing.
- **[Target Evidence Protocol](_docs/Evidence-Protocol.md)** — Selector verification tiers (T1–T5), avoiding guessed targets, and accessibility protocols.
- **[Verification & Quality Gates](_docs/Verification.md)** — Automated static test runner (`Test-WindhawkStyles.ps1`) and desktop live checklists.

### 📚 Community Wiki
- **[Wiki Home](_wiki/README.md)** — Community-driven living knowledge base of verified targets and options.
- **[Start Menu Styler Wiki](_wiki/start-menu-styler/README.md)** — Detailed selector ledgers and positioning settings.
- **[Taskbar Styler Wiki](_wiki/taskbar-styler/README.md)** — Taskbar frames, items, trays, and companion tweak metrics.
- **[Notification Center Styler Wiki](_wiki/notification-center-styler/README.md)** — Quick settings, sliders, calendar cells, and toasts.
- **[File Explorer Styler Wiki](_wiki/file-explorer-styler/README.md)** — Tabs, breadcrumbs, command bar, and backdrop effects.
- **[Settings Styler Wiki](_wiki/settings-styler/README.md)** — Split views, setting cards, and navigation items.

---

## 📦 Supported Windhawk Mods

| Mod | Mod ID | Process | Framework | Status |
|---|---|---|---|---|
| **Start Menu Styler** | `windows-11-start-menu-styler` | `StartMenuExperienceHost.exe` | UWP / WinUI 2 | ✅ Reference supported |
| **Taskbar Styler** | `windows-11-taskbar-styler` | `explorer.exe` | WinUI 3 / XAML | ✅ Reference supported |
| **Notification Center Styler** | `windows-11-notification-center-styler` | `ShellExperienceHost.exe` / `ShellHost.exe` | UWP `Windows.UI.Xaml` | ✅ Reference supported |
| **Settings Styler** | `windows-11-settings-styler` | `SystemSettings.exe` | UWP / WinUI `Windows.UI.Xaml` | 🌐 In base scope |
| **File Explorer Styler** | `windows-11-file-explorer-styler` | `explorer.exe` | WinUI 3 `Microsoft.UI.Xaml` | ⏸️ Deferred (Milestone M.03) |

---

## 🚀 Quick Verification Gate

Validate any styler file or the entire repository against static syntax and token standards:

```powershell
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
```
