# 🎛️ Windhawk Command Center Suite

A cohesive, modern frosted glass customization suite for Windows 11 built for official [Windhawk](https://windhawk.net/) mods.

The suite delivers a unified, dark/light-adaptive "Command Center Glass" visual theme across all primary Windows shell surfaces: top-lit gradient rim highlights, pixel-accurate `WindhawkBlur`, adaptive theme resource colors, and consistent corner radius scaling.

---

## 🎨 Supported Surfaces & Windhawk Mods

| Surface | Windhawk Mod ID | Configuration File | Status |
|---|---|---|---|
| **Taskbar** | [`windows-11-taskbar-styler`](https://windhawk.net/mods/windows-11-taskbar-styler) | `src/windows-11-taskbar-styler.yml` | ✅ Shipped |
| **Start Menu** | [`windows-11-start-menu-styler`](https://windhawk.net/mods/windows-11-start-menu-styler) | `src/windows-11-start-menu-styler.yml` | ✅ Shipped |
| **Notification Center** | [`windows-11-notification-center-styler`](https://windhawk.net/mods/windows-11-notification-center-styler) | `src/windows-11-notification-center-styler.yml` | 🚧 In-Progress |

*Companion mod configurations are stored in `src/extras/`.*

---

## 💎 Design System: "Command Center Glass"

- **Surface Material**: Single-layer `WindhawkBlur` (amount 20, tint `{ThemeResource SystemChromeMediumColor}`, opacity 0.7) that automatically adapts to Windows Dark and Light modes.
- **Top-Lit Rim Border**: Signature vertical linear gradient (`#60808080 → #50404040 → #40808080`, thickness `0.3,1,0.3,1`) simulating overhead light catching a glass pane.
- **Accent Integration**: Windows `SystemAccentColor` is reserved for active state indicators, volume/brightness slider fill bars, and clock highlights.
- **Harmonized Radius Scale**:
  - `35px` — Top-level panels and flyout cards (Start Menu, Notification Center, Calendar).
  - `25px` — Search pills and rounded input boxes.
  - `15px` — Grouped control regions and secondary cards.
  - `10px` — Buttons, tiles, list items, and tabs.
  - `6px` — Context menus, flyout presenters, and taskbar buttons.
- **Zero Double-Blur**: Native chrome layers, hard backgrounds, and drop shadows are collapsed or reset to transparent to prevent muddy overlapping blur.

---

## 🤖 AI Agent Ecosystem

This repository is governed by an extensive multi-agent ecosystem documented in:
- [**`AGENTS.md`**](./AGENTS.md) — Central operating manual and multi-agent coordination.
- [**`.agents/rules/`**](./.agents/rules/) — Mandatory architectural, safety, syntax, and verification rules (Rules 00–09).
- [**`.agents/skills/`**](./.agents/skills/) — Subsystem technical guides and glass styling recipes.
- [**`.agents/agents/`**](./.agents/agents/) — Primary and sub-agent team catalog.
- [**`.agents/templates/`**](./.agents/templates/) — Governance blueprints and verification checklists.

### Quality & Static Validation Gate

All styles are verified using the repository's native validation script:
```powershell
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
```

---

## 📥 How to Apply Styles

1. Install and launch [Windhawk](https://windhawk.net/).
2. In the Windhawk **Explore** tab, search for and install the desired mod (e.g. *Windows 11 Notification Center Styler*).
3. Open the mod details, navigate to the **Advanced** tab, and locate the **Settings** editor.
4. Copy the entire contents of the matching YAML file from `src/` into the editor.
5. Click **Save**. Windhawk applies the style immediately to the target shell process without requiring a system restart.