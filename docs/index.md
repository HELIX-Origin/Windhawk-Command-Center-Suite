---
layout: default
title: Home
---

# Universal Windows 11 Theme Engineering Framework

Windhawk Themes is a complete developer framework, autonomous multi-agent ecosystem, and hybrid C++/Python inspection toolchain designed for engineering, validating, and maintaining your own cohesive theme suites across Windows 11 shell surfaces.

> [!NOTE]
> **Framework & Ecosystem**: Built for developers and AI vibe coders creating custom theme suites. Provides full coverage for the 5 base Windhawk styler mods, companion mods, empirical visual tree inspection, and static syntax gates.

---

## 1. Why Windhawk Themes?

Building custom Windows 11 theme suites across multiple Windhawk mods often leads to fragile selectors, clashing styles, and broken layouts following Windows updates. The **Windhawk Themes** repository solves this by providing the tools, standards, and automation needed to build your own theme suites:

* **Multi-Agent Ecosystem**: Specialized AI agents for style architecture, visual inspection, syntax linting, and surface engineering working under strict safety rules.
* **Hybrid Inspection Toolchain**: Native C++ TAP engine and Python CLI utilizing UI automation to wake shell surfaces and dump live visual trees into JSON for AI vibe coding.
* **Empirical Selector Evidence**: Strict target evidence protocol requiring verified element types and names from official source code and live visual tree dumps.
* **Automated Quality Gates**: Built-in static validation gate verifying YAML syntax, constant ordering, and token references across all theme suite projects.

---

## 2. Supported Styler Surfaces

The framework targets five base official Windhawk styler mods covering primary Windows 11 shell experiences:

| Surface | Windhawk Mod ID | Target Process | Framework | Surface Guide |
|---|---|---|---|---|
| **Start Menu** | `windows-11-start-menu-styler` | `StartMenuExperienceHost.exe` | UWP / WinUI 2 | [Start Menu Guide](_docs/Start-Menu.md) |
| **Taskbar** | `windows-11-taskbar-styler` | `explorer.exe` | WinUI 3 / XAML | [Taskbar Guide](_docs/Taskbar.md) |
| **Notification Center** | `windows-11-notification-center-styler` | `ShellExperienceHost.exe` / `ShellHost.exe` | UWP `Windows.UI.Xaml` | [Notification Center Guide](_docs/Notification-Center.md) |
| **Settings** | `windows-11-settings-styler` | `SystemSettings.exe` | UWP / WinUI `Windows.UI.Xaml` | [Settings Guide](_docs/Settings.md) |
| **File Explorer** | `windows-11-file-explorer-styler` | `explorer.exe` | WinUI 3 `Microsoft.UI.Xaml` | [File Explorer Guide](_docs/File-Explorer.md) |

---

## 3. Hybrid C++/Python Toolchain

Reliable theming requires empirical visual tree inspection without manual burden. Our high-speed native inspection suite combines direct C++ TAP hooks with a flexible Python CLI:

* **Automated Surface Activation**: Programmatically opens and closes shell surfaces (Start, Action Center, Notification Center, Search, Settings) via UI automation to ensure UWP visual trees are fully populated.
* **Heartbeat Resiliency**: Built-in 30-second heartbeat loops accommodate OS elevation and UAC security prompts without premature timeouts.
* **ShareX Screenshot Integration**: Auto-detects user keybindings (including `VK_SLEEP` PrintScreen mappings) to capture desktop verification evidence automatically.
* **Automated Static Gate**: `tools/Test-WindhawkStyles.ps1` verifies YAML syntax, constant ordering, token definitions, and safety rules before any style is published.

---

## 4. Exploration & Reference

* **[Getting Started Guide](_docs/Getting-Started.md)** — Setting up the environment, CLI tools, and project workspaces.
* **[Architecture & Design Philosophy](_docs/Architecture.md)** — Core design principles, radii scales, and visual hierarchies.
* **[Community Development Wiki](_wiki/README.md)** — Extensive reference of verified XAML selectors and mod configuration schemas.
