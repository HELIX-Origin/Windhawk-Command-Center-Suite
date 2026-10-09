# Project Configuration: Command Center Suite

This directory contains project-specific definitions, custom tokens, and notes for the **Command Center Suite** theme implementation. This folder is gitignored to keep the core `.agents/` ecosystem fully universal and portable.

---

## Command Center Glass Design Language

- **Unified Frosted Blur**: Consistent `WindhawkBlur` (amount 20, tinting via `{ThemeResource SystemChromeMediumColor}`) providing the base glass surface across all shells.
- **Top-Lit Glass Rim**: Signature vertical gradient border (`LinearGradientBrush #60808080 → #50404040 → #40808080`, thickness `0.3,1,0.3,1`).
- **Harmonized Radii Scale**:
  - Top-level panels: XL (`35`)
  - Search pills: L (`25`)
  - Groups / category cards: M (`15`)
  - Tiles / buttons: S (`10`)
  - Context menus & flyouts: XS (`6`)
- **Intentional Glass Layering**: Foundation frosted glass surfaces host layered glassy cards, pills, and tiles to establish rich depth, contrast, and visual hierarchy; native opaque system fills and hard drop shadows are collapsed.
- **Start Menu Architecture**: Separated-island flyout with transparent outer frame, top header island with layered two-tone split (`Border#AcrylicOverlay` with `$ElementBackground`) hosting the hoisted navigation pane (`Grid#NavPanePlaceholder`), custom view pills (`★ v` / `⊞ v`), compact 2-column categories, 3-column pinned list, and floating Phone Link companion card.
