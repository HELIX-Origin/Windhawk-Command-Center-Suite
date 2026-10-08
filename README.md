# 🎛️ Windhawk Command Center Suite

![Windhawk Command Center Suite Desktop Overview](/assets/command-center-header.png)

A cohesive, modern frosted glass customization suite for Windows 11 built for official [Windhawk](https://windhawk.net/) mods.

The suite delivers a unified, dark/light-adaptive **"Command Center Glass"** visual theme across all primary Windows shell surfaces—top-lit gradient rim highlights, pixel-accurate `WindhawkBlur`, adaptive theme resource colors, and consistent corner-radius scaling.

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Primary Styler Mods](#primary-styler-mods)
- [Companion & Supplemental Mods](#companion--supplemental-mods-src-extras)
- [Design System: "Command Center Glass"](#design-system-command-center-glass)
- [AI Agent Ecosystem](#ai-agent-ecosystem)
- [Quality Gates & Validation](#quality-gates--validation)
- [Documentation](#documentation)
- [Contributing](#contributing)
- [License](#license)

## Overview

Windhawk Command Center Suite is a unified styling layer for four official Windhawk Styler mods plus a curated set of companion configurations. All base styles share canonical materials, radii, and the top-lit glass rim to preserve visual consistency across Taskbar, Start Menu, Notification Center/Quick Settings, and File Explorer.

For implementation details (style constants, per-mod coverage, selector intent), see [`src/README.md`](src/README.md).

## Quick Start

1. **Install Windhawk** from [windhawk.net](https://windhawk.net/).
2. **Install the target mod(s)** via Windhawk → Explore (e.g., *Windows 11 Taskbar Styler*, *Windows 11 Start Menu Styler*, *Windows 11 Notification Center Styler*, *Windows 11 File Explorer Styler*).
3. **Apply base YAML**: Open each mod’s **Settings → Advanced/Textual** editor and paste the corresponding file from [`src/`](src/):
   - Taskbar: [`src/windows-11-taskbar-styler.yml`](src/windows-11-taskbar-styler.yml)
   - Start Menu: [`src/windows-11-start-menu-styler.yml`](src/windows-11-start-menu-styler.yml)
   - Notification Center: [`src/windows-11-notification-center-styler.yml`](src/windows-11-notification-center-styler.yml)
   - File Explorer: [`src/windows-11-file-explorer-styler.yml`](src/windows-11-file-explorer-styler.yml)
4. **Save** — changes apply immediately to the target shell process (no full restart required).
5. **(Optional) Apply extras**: See [Extras Guide](src/extras/README.md) to import companion mod configurations.

## Primary Styler Mods

The suite targets exactly **four** official Windhawk Styler mods (one YAML each in [`src/`](src/)).

| Surface | Windhawk Mod ID | Configuration File | Target Process | Framework | Status |
|---|---|---|---|---|---|
| **Taskbar** | [`windows-11-taskbar-styler`](https://windhawk.net/mods/windows-11-taskbar-styler) | [`src/windows-11-taskbar-styler.yml`](src/windows-11-taskbar-styler.yml) | `explorer.exe` | WinUI 3 / XAML | ✅ Shipped |
| **Start Menu** | [`windows-11-start-menu-styler`](https://windhawk.net/mods/windows-11-start-menu-styler) | [`src/windows-11-start-menu-styler.yml`](src/windows-11-start-menu-styler.yml) | `StartMenuExperienceHost.exe` (LockApp surfaces included) | UWP / WinUI 2 | ✅ Shipped |
| **Notification Center** | [`windows-11-notification-center-styler`](https://windhawk.net/mods/windows-11-notification-center-styler) | [`src/windows-11-notification-center-styler.yml`](src/windows-11-notification-center-styler.yml) | `ShellExperienceHost.exe` / `ShellHost.exe` | UWP `Windows.UI.Xaml` | 🧪 Generated (Ready for verification) |
| **File Explorer** | [`windows-11-file-explorer-styler`](https://windhawk.net/mods/windows-11-file-explorer-styler) | [`src/windows-11-file-explorer-styler.yml`](src/windows-11-file-explorer-styler.yml) | `explorer.exe` | WinUI 3 `Microsoft.UI.Xaml` | 🧪 Generated (Ready for verification) |

> See [`src/README.md`](src/README.md) for canonical tokens, style constants, per-mod coverage, and notes on Win32/file list boundaries.

## Companion & Supplemental Mods (`src/extras/`)

The suite includes curated configurations for **8 companion Windhawk mods** extending the Command Center aesthetic into desktop utilities, status indicators, dialogs, and flyout behaviors. Full details in the [**Extras Guide**](src/extras/README.md).

| Companion Mod | Target Area | Configuration File |
|---|---|---|
| **Dynamic Island for Windows** | Top-center status, media, & hardware pill | [`src/extras/dynamic-island-for-windows.yml`](src/extras/dynamic-island-for-windows.yml) |
| **Enhanced Disk Usage** | File Explorer drive capacity meter bars | [`src/extras/enhanced-disk-usage.yml`](src/extras/enhanced-disk-usage.yml) |
| **File Operations Styler** | Copy/move/delete progress dialogs | [`src/extras/file-operations-styler.yml`](src/extras/file-operations-styler.yml) |
| **Fully Customizable Winver** | Minimalist slate About Windows card | [`src/extras/fully-customizeable-winver.yml`](src/extras/fully-customizeable-winver.yml) |
| **Shell Flyout Positions** | Flyout tray and boundary alignment | [`src/extras/shell-flyout-positions.yml`](src/extras/shell-flyout-positions.yml) |
| **Start Button Colorizer** | Accent-tinted taskbar Start glyph | [`src/extras/start-button-colorizer.yml`](src/extras/start-button-colorizer.yml) |
| **Taskbar Clock Customization** | Seconds format & hardware telemetry HUD | [`src/extras/taskbar-clock-customization.yml`](src/extras/taskbar-clock-customization.yml) |
| **Taskbar Tray and Icon Tweaks** | System tray decluttering & icon filtering | [`src/extras/taskbar-tray-and-icon-tweaks.yml`](src/extras/taskbar-tray-and-icon-tweaks.yml) |

## Design System: "Command Center Glass"

- **Surface Material**: Foundation `WindhawkBlur` (BlurAmount 20, tint `{ThemeResource SystemChromeMediumColor}`, TintOpacity 0.7) — adapts to Windows Dark/Light modes.
- **Top-Lit Rim Border**: Vertical linear gradient (`#60808080 → #50404040 → #40808080`, thickness `0.3,1,0.3,1`) simulating overhead glass rim lighting.
- **Accent Integration**: `SystemAccentColor` reserved for active state indicators, volume/brightness fills, and clock highlights.
- **Harmonized Radius Scale**:
  - `35px` — Top-level panels/flyout cards (Start Menu, Notification Center/Calendar)
  - `25px` — Search pills/large inputs
  - `15px` — Grouped regions/secondary cards
  - `10px` — Buttons/tiles/list items/tabs
  - `6px` — Context menus/flyouts/taskbar buttons
- **Intentional Glass Layering**: Frosted foundation hosts layered glassy cards, pills, and tiles for depth/hierarchy; native opaque fills and hard drop shadows are collapsed where conflicting.
- **Theme-Aware**: Leverages system theme resources with AcrylicBrush fallbacks for readability.

## AI Agent Ecosystem

This repository is governed by a multi-agent ecosystem (rules, agents, skills, templates):

- [**`AGENTS.md`**](./AGENTS.md) — Central operating manual and multi-agent coordination model.
- [**`.agents/rules/`**](./.agents/rules/) — Mandatory architectural, safety, syntax, design, evidence, scope, verification, documentation, and release rules (Rules 00–09).
- [**`.agents/skills/`**](./.agents/skills/) — Subsystem technical guides and glass styling recipes.
- [**`.agents/agents/`**](./.agents/agents/) — Primary and sub-agent team catalog (roles, responsibilities, specs).
- [**`.agents/templates/`**](./.agents/templates/) — Governance blueprints and live verification checklists.

## Quality Gates & Validation

All styles must pass repository quality gates before a change is considered complete:

- **Static validation (mandatory):**

  ```powershell
  pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
  ```

  Target: `0 errors`. Warnings should be reviewed and addressed per rules.

- **Live desktop verification (mandatory):** Generate/use the template checklist at [`.agents/templates/live-verification-checklist.md`](./.agents/templates/live-verification-checklist.md) covering Taskbar, Start Menu/Lock, Notification Center/Quick Settings, File Explorer, states (normal/hover/active), theme switching, and regression checks.

- **Target evidence (Rule 04):** Selectors must be sourced from official Windhawk mod source code, settings schemas, or community theme references. Avoid guessing.

## Documentation

- **Base styles:** [`src/README.md`](src/README.md) — design tokens, constants, per-mod details, validation/conventions.
- **Extras:** [`src/extras/README.md`](src/extras/README.md) — companion mod catalog, configuration notes, import instructions.
- **Changelog:** [`CHANGELOG.md`](CHANGELOG.md) — chronological log of completed work (no formal releases; tracked via milestones/sprints in planning files)
- **Planning/tracking:** [`PLAN.md`](PLAN.md), [`TODO.md`](TODO.md), [`BUGS.md`](BUGS.md), [`ROADMAP.md`](ROADMAP.md)
- **Architecture/agents:** [`AGENTS.md`](AGENTS.md) and [`.agents/`](.agents/)
- **Validation tool:** [`tools/Test-WindhawkStyles.ps1`](tools/Test-WindhawkStyles.ps1)

## Contributing

Changes must remain consistent with surrounding code patterns, respect the four-mod scope (Rule 01), follow Windhawk Styler syntax (Rule 02), use canonical design tokens (Rule 03), provide evidence-backed targets (Rule 04), and pass static + live gates (Rule 07). Permanent docs live in root Markdown files + `src/extras/README.md` + `.agents/` (no `docs/` folder) per Rule 08.

## License

See [LICENSE](LICENSE) if present in the repository.
