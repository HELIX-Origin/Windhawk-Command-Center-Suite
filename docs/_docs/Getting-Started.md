---
layout: docs
parent: Documentation Directory
title: Getting Started
---

# Getting Started with the Theme Engineering Framework

The **Windhawk Themes** repository provides the scaffolding, engineering standards, and hybrid inspection toolset for creating, testing, and maintaining your own custom Windows 11 theme suites.

---

## 1. What This Repository Provides

When engineering theme suites for Windhawk, this repository equips you with:
1. **Hybrid C++/Python Visual Tree Inspector**: Uses UI automation to wake shell processes and dump XAML trees to structured JSON for AI vibe coding without manual inspection burden.
2. **Design Language & Evidence Standards**: Canonical "Command Center Glass" tokens, proportional radius scales, and an evidence protocol requiring selectors sourced from official reference material.
3. **Automated Static Quality Gate**: `tools/Test-WindhawkStyles.ps1` verifies YAML syntax, constant ordering, and token references across all projects.
4. **Universal Surface Target Reference**: Empirical selector documentation across the 5 base Windhawk stylers and companion mods.

---

## 2. Setting Up Your Development Environment

### Prerequisites:
1. **Windows 11** (21H2 through 24H2 build 26100+).
2. **[Windhawk](https://windhawk.net/)** installed on your system.
3. Official Windhawk Styler mods installed from the in-app mod browser:
   - **Windows 11 Taskbar Styler** (`windows-11-taskbar-styler`)
   - **Windows 11 Start Menu Styler** (`windows-11-start-menu-styler`)
   - **Windows 11 Notification Center Styler** (`windows-11-notification-center-styler`)
   - **Windows 11 Settings Styler** (`windows-11-settings-styler`)
   - **Windows 11 File Explorer Styler** (`windows-11-file-explorer-styler`)
4. **Visual Studio 2022 / 2026** (C++ Desktop development workload for XAML Diagnostics headers) and **Python 3.10+**.

---

## 3. Engineering a New Theme Suite

To build a new theme suite using this framework:

1. **Scaffold a Project Folder**:
   Create a dedicated subfolder under `projects/<your-theme-name>/`.
2. **Define Styler YAML Files**:
   Create styler configuration files matching the Windhawk mod IDs you wish to theme:
   - `projects/<your-theme-name>/windows-11-taskbar-styler.yml`
   - `projects/<your-theme-name>/windows-11-start-menu-styler.yml`
   - `projects/<your-theme-name>/windows-11-notification-center-styler.yml`
3. **Inspect Shell Trees Using the Toolchain**:
   Run the hybrid inspector or query saved dumps to discover selectors:
   ```powershell
   # Inspect live Start Menu via automated activation
   python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --find ActionsBar

   # Inspect live Notification Center / Calendar on Win11 24H2
   python tools/inspect_xaml.py -p ShellHost.exe --surface notification-center
   ```
4. **Run the Static Validation Gate**:
   Ensure your theme styles adhere to syntax and token rules:
   ```powershell
   pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
   ```
5. **Import into Windhawk & Verify**:
   Copy your YAML configuration into the **Advanced (Textual)** editor of the target mod in Windhawk and verify live desktop rendering.
