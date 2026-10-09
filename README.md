# 🎛️ Windhawk Themes

![Windhawk Themes Desktop Overview](https://github.com/HELIX-Origin.png?size=200)

A universal Windows 11 theme engineering framework, cohesive styling suites, and visual tree inspection toolchain built for official [Windhawk](https://windhawk.net/) styler mods.

The framework delivers unified, dark/light-adaptive frosted glass and modern acrylic visual themes across Windows shell surfaces—top-lit specular gradient rims, hardware-accelerated `WindhawkBlur`, adaptive theme resource colors, proportional corner radii scaling, and a hybrid C++/Python visual tree inspection engine.

---

## 📖 Table of Contents

- [Overview](#overview)
- [Online Documentation](#online-documentation)
- [Base Intended Styler Mods](#base-intended-styler-mods)
- [Quick Start](#quick-start)
- [Theme Suites & Projects](#theme-suites--projects)
- [Companion & Supplemental Mods](#companion--supplemental-mods)
- [Design Architecture & Materials](#design-architecture--materials)
- [Hybrid Inspection Toolchain](#hybrid-inspection-toolchain)
- [AI Agent Ecosystem](#ai-agent-ecosystem)
- [Quality Gates & Validation](#quality-gates--validation)
- [Milestones & Releases](#milestones--releases)
- [License](#license)

---

## Overview

**Windhawk Themes** provides a structured, automated, and evidence-backed workflow for engineering, inspecting, and maintaining cohesive themes across Windows 11 shell surfaces.

All theme suites share canonical materials, proportional radii scales, and specular glass rim lighting to preserve visual harmony across the Taskbar, Start Menu, Notification Center, Quick Settings, and Settings apps.

---

## 🌐 Online Documentation

The full documentation site is hosted on GitHub Pages:
- **[Windhawk Themes Documentation Site](https://helix-origin.github.io/Windhawk-Themes/)**
- Local documentation source: [`docs/`](docs/)

---

## Base Intended Styler Mods

The framework defines **five primary official Windhawk styler mods** as its canonical base scope:

| Surface | Windhawk Mod ID | Configuration File | Target Process | Framework | Status |
|---|---|---|---|---|---|
| **Start Menu** | [`windows-11-start-menu-styler`](https://windhawk.net/mods/windows-11-start-menu-styler) | [`projects/command-center/windows-11-start-menu-styler.yml`](projects/command-center/windows-11-start-menu-styler.yml) | `StartMenuExperienceHost.exe` | UWP / WinUI 2 | ✅ Supported reference |
| **Taskbar** | [`windows-11-taskbar-styler`](https://windhawk.net/mods/windows-11-taskbar-styler) | [`projects/command-center/windows-11-taskbar-styler.yml`](projects/command-center/windows-11-taskbar-styler.yml) | `explorer.exe` | WinUI 3 / XAML | ✅ Supported reference |
| **Notification Center** | [`windows-11-notification-center-styler`](https://windhawk.net/mods/windows-11-notification-center-styler) | [`projects/command-center/windows-11-notification-center-styler.yml`](projects/command-center/windows-11-notification-center-styler.yml) | `ShellExperienceHost.exe` / `ShellHost.exe` | UWP `Windows.UI.Xaml` | ✅ Generated & verified |
| **Settings** | [`windows-11-settings-styler`](https://windhawk.net/mods/windows-11-settings-styler) | *— (styler file optional)* | `SystemSettings.exe` | UWP / WinUI `Windows.UI.Xaml` | 🌐 In base scope (Tooling supported) |
| **File Explorer** | [`windows-11-file-explorer-styler`](https://windhawk.net/mods/windows-11-file-explorer-styler) | *— (styler file optional)* | `explorer.exe` | WinUI 3 `Microsoft.UI.Xaml` | ⏸️ Deferred (ROADMAP M.03) |

---

## Quick Start

1. **Install Windhawk** from [windhawk.net](https://windhawk.net/).
2. **Install the target mod(s)** via Windhawk → Explore (e.g. *Windows 11 Taskbar Styler*, *Windows 11 Start Menu Styler*, *Windows 11 Notification Center Styler*).
3. **Apply base YAML**: Open each mod’s **Settings → Advanced/Textual** editor and paste the corresponding file from `projects/command-center/`:
   - Taskbar: [`projects/command-center/windows-11-taskbar-styler.yml`](projects/command-center/windows-11-taskbar-styler.yml)
   - Start Menu: [`projects/command-center/windows-11-start-menu-styler.yml`](projects/command-center/windows-11-start-menu-styler.yml)
   - Notification Center: [`projects/command-center/windows-11-notification-center-styler.yml`](projects/command-center/windows-11-notification-center-styler.yml)
4. **Save** — changes apply immediately in real time to the running shell process.
5. **(Optional) Apply extras**: See [Extras Guide](projects/command-center/extras/README.md) to import companion mod configurations.

---

## Theme Suites & Projects

Theme configurations are organized modularly in `projects/<project-name>/`:
- **`projects/command-center/`**: The reference **Command Center Glass** suite featuring separated-island flyouts, compact 2-column categories, floating taskbar pills, and translucent Quick Settings.

Each theme project maintains its own styler YAML files, companion extras, and README documentation.

---

## Companion & Supplemental Mods

Curated configurations for companion Windhawk mods are maintained in `projects/<project>/extras/`. See the [Extras Guide](projects/command-center/extras/README.md) for details:
- **Dynamic Island for Windows**: Top-center status, media, and telemetry pill.
- **Enhanced Disk Usage**: Drive capacity meter bars in File Explorer.
- **File Operations Styler**: Translucent copy/move progress dialogs.
- **Fully Customizable Winver**: Modern minimalist About Windows card.
- **Shell Flyout Positions**: Tray alignment and flyout boundary offset adjustments.
- **Start Button Colorizer**: Accent-tinted taskbar Start glyph.
- **Taskbar Clock Customization**: Seconds format and hardware telemetry HUD.
- **Taskbar Tray and Icon Tweaks**: Tray decluttering and icon padding.

---

## Design Architecture & Materials

- **Surface Material**: Foundation `WindhawkBlur` (BlurAmount 20, tint `{ThemeResource SystemChromeMediumColor}`) adapting to Windows Dark/Light modes.
- **Top-Lit Rim Border**: Specular vertical linear gradient (`#60808080 → #50404040 → #40808080`, thickness `0.3,1,0.3,1`).
- **Accent Integration**: `SystemAccentColor` reserved for active state indicators, volume/brightness fills, and clock highlights.
- **Harmonized Radius Scale**:
  - `35px` (XL) — Top-level panels and flyout cards (Start Menu, Notification Center, Calendar)
  - `25px` (L) — Search pills and large input boxes
  - `15px` (M) — Grouped regions and secondary cards
  - `10px` (S) — Interactive buttons, tiles, cards, and list items
  - `6px` (XS) — Context menus, flyouts, and badges
- **Intentional Layering**: Native opaque chrome fills and hard drop shadows are collapsed to allow translucent materials to float with clean depth.

---

## Hybrid Inspection Toolchain

The repository includes a native C++ and Python visual tree inspection toolchain:
- **`tools/inspect_xaml.py`**: Unified CLI with automated shell surface activation (`start`, `action-center`, `notification-center`, `search`, `settings`), offline tree queries, and ShareX screenshot capture.
- **`tools/native/bin/xaml_dump.exe`**: Native MSVC injector and `ExplorerTAP` XAML diagnostics client.
- **`tools/Test-WindhawkStyles.ps1`**: Automated static validation gate.

---

## AI Agent Ecosystem

This repository is governed by an automated multi-agent team:
- [**`AGENTS.md`**](AGENTS.md) — Central operating manual and multi-agent coordination model.
- [**`.agents/rules/`**](.agents/rules/) — Mandatory architectural, safety, syntax, design, evidence, scope, verification, documentation, and milestone rules (Rules 00–09).
- [**`.agents/skills/`**](.agents/skills/) — Subsystem technical skills and material recipes.
- [**`.agents/agents/`**](.agents/agents/) — Agent catalog and specification files.
- [**`.agents/templates/`**](.agents/templates/) — Governance blueprints and verification checklists.

---

## Quality Gates & Validation

All style files must pass repository quality gates before deployment:

```powershell
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
```

Target: `0 errors, 0 warnings`.

---

## Milestones & Releases

Progress is tracked via **Milestones** (`M.01`, `M.02`, `M.02b`, `M.03`) with sprint tracking for active steps:
- **Milestone-Based Releases**: Releases use milestone tags as release identifiers rather than standard semantic versioning.
- **Zero Asset Attachments**: Releases carry no attached binary or zip assets; the release is strictly the verified git tag checkpoint.
- Active planning and progress ledgers: [`ROADMAP.md`](ROADMAP.md), [`PLAN.md`](PLAN.md), [`TODO.md`](TODO.md), [`BUGS.md`](BUGS.md), and [`CHANGELOG.md`](CHANGELOG.md).

---

## License

MIT License. See [LICENSE](LICENSE).
