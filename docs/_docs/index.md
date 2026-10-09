---
layout: docs
title: Documentation Directory
permalink: /docs/
---

# Developer Documentation Directory

Welcome to the **Windhawk Themes Documentation Guides**. These comprehensive technical guides cover the architecture, surface guides, companion tools, and quality gates for engineering cohesive Windows 11 themes.

---

## 🧭 Topic Guides

### 🌟 Overview & Architecture
* **[Getting Started Guide](Getting-Started.md)** — Scaffolding workspaces, installing dependencies, and initializing themes.
* **[Architecture & Design Philosophy](Architecture.md)** — Multi-mod design system, glass materials, and spatial token hierarchy.

### 🪟 Styler Surface Guides
* **[Start Menu Styler Guide](Start-Menu.md)** — Start menu flyouts, pinned app grids, and companion cards.
* **[Taskbar Styler Guide](Taskbar.md)** — Floating taskbar frame, grouped task list button pills, system tray styling.
* **[Notification Center Styler Guide](Notification-Center.md)** — Quick settings tiles, sliders, calendar flyout, toasts.
* **[Settings Styler Guide](Settings.md)** — Modern Settings app styling, cards, search box.
* **[File Explorer Styler Guide](File-Explorer.md)** — WinUI 3 tab controls, address bar, breadcrumbs, search pills.

### 🧩 Companion & Utility Mods
* **[Companion Mods Overview](Companion-Mods.md)** — Companion mod integration guidelines and ecosystem map.
* **[Taskbar Utility Mods](Companion-Taskbar.md)** — Taskbar styling companions and system tray utilities.
* **[Shell Flyouts & Positions](Companion-Shell.md)** — Shell flyout positioning, margins, and anchor tweaks.
* **[System & Translucency Mods](Companion-System.md)** — DWM blur and system translucency companion guidelines.

### 🔍 Toolchain & Diagnostics
* **[Hybrid XAML Inspector](Toolchain.md)** — Native C++ TAP engine and Python CLI tools.
* **[Visual Tree Diagnostics](Diagnostics.md)** — Querying elements, automated surface activation.
* **[UWPSpy Manual Inspection](UWPSpy.md)** — Interactive GUI visual tree inspection guide.

### 📐 Standards & Quality Gates
* **[Style Syntax & Tokens](Syntax-Standards.md)** — YAML syntax rules, strict constant ordering.
* **[Glass Material Recipes](Glass-Recipes.md)** — `WindhawkBlur` shaders, `AcrylicBrush` usage, rim gradients.
* **[Target Evidence Protocol](Evidence-Protocol.md)** — Sourced selectors only from verified evidence.
* **[Verification & Quality Gates](Verification.md)** — Automated static test runner (`Test-WindhawkStyles.ps1`).
