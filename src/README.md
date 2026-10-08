# Windhawk Command Center Suite – Base Styles (`src/`)

This directory contains the core Windhawk Styler mod configurations that implement the **"Command Center Glass"** unified dark/light frosted-glass design language for Windows 11.

> **Note:** The File Explorer styler (`windows-11-file-explorer-styler.yml`) is referenced in `AGENTS.md` as generated/ready for verification and may be present in the working tree as part of the suite. See the [File Explorer](#4-windows-11-file-explorer-styler) section for target details.

## Table of Contents

- [Overview](#overview)
- [Design Philosophy: "Command Center Glass"](#design-philosophy-command-center-glass)
- [Canonical Design Tokens](#canonical-design-tokens)
  - [Blur Materials](#blur-materials)
  - [Brushes & Colors](#brushes--colors)
  - [Radii Scale](#radii-scale)
  - [Layout & Sizing](#layout--sizing)
- [Base Mods](#base-mods)
  - [1. windows-11-taskbar-styler.yml](#1-windows-11-taskbar-styler-yml)
  - [2. windows-11-start-menu-styler.yml](#2-windows-11-start-menu-styler-yml)
  - [3. windows-11-notification-center-styler.yml](#3-windows-11-notification-center-styler-yml)
  - [4. windows-11-file-explorer-styler.yml](#4-windows-11-file-explorer-styler-yml)
- [Style Constants Reference](#style-constants-reference)
- [Installation & Usage](#installation--usage)
- [Validation & Quality Gates](#validation--quality-gates)
- [Conventions & Compliance](#conventions--compliance)
- [Related Documentation](#related-documentation)

## Overview

The suite targets exactly **four** official Windhawk Styler mods (one YAML per mod). Each file uses Windhawk's Styler syntax (`styleConstants` + `controlStyles` with target selectors and per-state styles) to restyle the targeted shell surface with a consistent frosted-glass treatment.

| Styler File | Windhawk Mod ID | Target Process | Framework | Status |
|---|---|---|---|---|
| `windows-11-taskbar-styler.yml` | `windows-11-taskbar-styler` | `explorer.exe` | WinUI 3 / XAML | ✅ Shipped reference |
| `windows-11-start-menu-styler.yml` | `windows-11-start-menu-styler` | `StartMenuExperienceHost.exe` (LockApp surfaces also targeted) | UWP / WinUI 2 | ✅ Shipped reference |
| `windows-11-notification-center-styler.yml` | `windows-11-notification-center-styler` | `ShellExperienceHost.exe` / `ShellHost.exe` | UWP `Windows.UI.Xaml` | 🧪 Generated (Ready for verification) |
| `windows-11-file-explorer-styler.yml` | `windows-11-file-explorer-styler` | `explorer.exe` | WinUI 3 `Microsoft.UI.Xaml` | 🧪 Generated (Ready for verification) |

All surfaces share the same canonical tokens and materials to preserve a unified "Command Center" look across taskbar, Start menu/lock widgets, Notification Center/Quick Settings, and File Explorer chrome.

## Design Philosophy: "Command Center Glass"

- **Unified Frosted Blur**: Consistent `WindhawkBlur` (base `BlurAmount="20"`, tinted via `{ThemeResource SystemChromeMediumColor}` with `TintOpacity="0.7"`) forms the foundation glass surface across shells.
- **Top-Lit Glass Rim**: Signature vertical gradient border `LinearGradientBrush` from `#60808080` (top) → `#50404040` (mid) → `#40808080` (bottom) with `BorderThickness="0.3,1,0.3,1"`.
- **Harmonized Radii Scale**: XL (35) for top-level panels, L (25) for search pills/large surfaces, M (15–13) for groups/cards, S (10) for tiles/buttons, XS (6) for chips/context menus.
- **Intentional Glass Layering**: Frosted foundation surfaces host layered glassy cards, pills, tiles and subtle element backgrounds (`ElementBackground` with low opacity) to create depth/contrast and visual hierarchy.
- **Minimal Native Chrome**: Native opaque fills, hard drop shadows, and heavy acrylic overlays are collapsed/hidden where they conflict with the glass treatment (e.g. drop shadows on Start/NC panels, some acrylic borders/overlays hidden).
- **Theme-Aware**: Uses system theme resources (`SystemChromeMediumColor`, `SystemAltLowColor`, `SystemAccentColor`, `CardStrokeColorDefaultSolid`) with AcrylicBrush fallbacks to remain readable in light/dark.

## Canonical Design Tokens

### Blur Materials

| Token | Definition | Usage |
|---|---|---|
| `Translucent` | `WindhawkBlur BlurAmount="15" TintColor="#10808080"` | Subtle/translucent fills where lighter blur is desired |
| `Glass` | `WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7"` | Very light glass accents |
| `Frosted` | `WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7"` | **Base background** (`Background = $Frosted`) |
| `Acrylic` | `WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8"` | Stronger blur for heavier surfaces/accents |

### Brushes & Colors

| Token | Definition | Notes |
|---|---|---|
| `Background` | `$Frosted` | Canonical panel background material |
| `BorderBrush` | Vertical `LinearGradientBrush` (0,0)-(0,1): `#60808080` @0.0 → `#50404040` @0.25 → `#40808080` @1.0 | Top-lit glass rim |
| `BorderBrush2` (Start/NC) | `WindhawkBlur BlurAmount="10" TintColor="#909090" TintOpacity="0.3"` | Alternate soft border treatment used on select surfaces |
| `OverlayColor` | `AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.8" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}"` | Pointer-over/active state fill |
| `OverlayColorAlt`/`OverlayColor2` | Lower luminosity variants (`0.5`) | Inactive/multi-window or alternate hover states |
| `AccentColor` | `AcrylicBrush TintColor="{ThemeResource SystemAccentColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}"` | Accent-driven highlights (e.g. active running indicator) |
| `ElementBackground` | `SolidColorBrush Color="{ThemeResource SystemAltLowColor}" Opacity="0.25"` | Layered inner cards/panels (calendar, control center pages, etc.) |
| `ClockBG` (Start Menu) | `SolidColorBrush Color="{ThemeResource SystemAccentColor}" Opacity="1"` | Lock screen clock/date accent color |
| `BorderThickness` | `0.3,1,0.3,1` | Thin top/bottom, slightly thicker sides (rim) |

### Radii Scale

| Token | Value | Applied To |
|---|---|---|
| `CornerRadius` (Taskbar base) | `6` | XS – buttons/chips and general small elements |
| `CornerRadiusAlt1` (Taskbar) | `20` | L – taskbar background frame |
| `CornerRadius` (Start Menu) | `35` | XL – top-level Start/Menu frames |
| `PanelRadius` (Start/NC) | `15` (Start), `13` (NC) | M/L – main panels/frames |
| `CardRadius` | `10` | S – cards/groups, inner panels |
| `ChipRadius` | `6` | XS – chips, flyouts, jump lists |
| `SearchBoxRadius` (Start) | `10` | S – search pill |

### Layout & Sizing

| Token | Value | Notes |
|---|---|---|
| `BaseHeight`/`BaseWidth` (Taskbar) | `32` / `34` | Standardized icon/search button footprint |
| `thumbnailImageSize` (NC) | `70` | Toast/thumbnail sizing |

## Base Mods

### 1. `windows-11-taskbar-styler.yml`

- **Windhawk Mod ID:** `windows-11-taskbar-styler`
- **Target Process:** `explorer.exe`
- **Framework:** WinUI 3 / XAML
- **Goal:** Glass-rounded taskbar with consistent button states, centered/aligned icon treatments, and styled Start/search elements.

**Key styled surfaces:**

- **Taskbar background frame** (`Taskbar.TaskbarFrame > ... TaskbarBackground > Grid`): `Margin=8,4,8,4`, `Background=$Frosted`, rim border, `CornerRadius=20`.
- **Background fill/stroke visibility**: Ensures background fill and stroke elements remain visible with glass treatment.
- **Hover/flyout background control**: Collapses/neutralizes hover flyout background to avoid double-layering (`Background/Border Transparent`, thickness 0).
- **Task list buttons (labeled/icon states, multi-window/active/inactive)**: Per-state backgrounds (`ActiveNormal/PointerOver/Pressed`, `Inactive*`, `MultiWindow*`) using `$Background`/`$OverlayColor`/`$OverlayColorAlt`; rounded `6` with padding/margins for pill-like hit areas.
- **Search icon button (`SearchUx.SearchUI.SearchIconButton` root grid)**: Glass background+rim, fixed `32x34` footprint, radius 6.
- **Icon panels & labeled button panels**: Standardized `32x34`, radius 6, same state mapping as task list buttons.
- **Start button (`ExperienceToggleButton#LaunchListButton[AutomationProperties.AutomationId=StartButton]`)**: Centered alignment, standardized size/padding/corner radius, Start icon scaled to 0.8x with centered transform origin.
- **Running indicator**: Thin rounded bar (`RadiusX/Y=1.5`, height 2.5), width 10 → 18 when `ActiveRunningIndicator`, filled with `$OverlayColor`/`$AccentColor`.

**Notes:** Heavy use of `@CommonStates` and `@RunningIndicatorStates` with per-state `Background`/`Fill`/`Width` to preserve native state semantics while applying glass materials.

### 2. `windows-11-start-menu-styler.yml`

- **Windhawk Mod ID:** `windows-11-start-menu-styler`
- **Target Process:** `StartMenuExperienceHost.exe` (also targets LockApp surfaces: `StackPanel#TimeAndDatePanel`, `TimePanel#Time`, `Date`, `WidgetFrameGrid`, `MediaTransportControls/Container`)
- **Framework:** UWP / WinUI 2
- **Goal:** Command Center glass treatment for Start Menu frame, top search pill, and Lock Screen clock/date/widgets/media controls with intentional layout tweaks.

**Key styled surfaces:**

- **Lock Screen clock/date**: Large centered time with transform group (translate/scale) and `Morganite SemiBold`; date positioned below with `vivo Sans EN VF`, both using `ClockBG` accent brush.
- **Lock Screen widgets frame** (`Grid#WidgetFrameGrid`): Glass background+rim, `CornerRadius=35`.
- **Widget canvas**: Centered with vertical translate for positioning.
- **Lock Screen media transport/controls** (`Grid#MediaTransportControls`, `Grid#MediaControlsContainer`): Glass treatment, radius 35; container visibility adjusted and positioned (`RenderTransform` translate, margin 0).
- **Start Menu foundation**: `StartDocked.StartSizingFrame` sized to `750x700`, `Grid#MainMenu` to `470x700`.
- **Main menu panel chrome**: `Border#DropShadowDismissTarget` becomes the glass panel (`Background=$Frosted`, rim, `PanelRadius=15`, margin/padding 0). `AcrylicBorder`, `AcrylicOverlay`, drop shadows (`RootGridDropShadow`, `StartDropShadow`, `RightCompanionDropShadow`, `dropshadow`), and accent layer borders are collapsed (`Visibility=Collapsed`).
- **Top search pill** (`StartMenu.SearchBoxToggleButton#SearchBoxToggleButton`): Centered `340x40`, glass background+rim, `SearchBoxRadius=10`. Placeholder text updated to `"Search This Precision"`.
- **Taskbar search box (StartDocked)**: `Cortana.UI.Views.CortanaRichSearchBox#SearchTextBox` height 32 (max 32, centered), glass border+background, `ChipRadius=6`.

**Notes:** Mixes layout transforms/positioning (translate/scale) for Lock Screen visual composition and collapses multiple native shadows/overlays to favor the unified glass layer.

### 3. `windows-11-notification-center-styler.yml`

- **Windhawk Mod ID:** `windows-11-notification-center-styler`
- **Target Process:** `ShellExperienceHost.exe` / `ShellHost.exe`
- **Framework:** UWP `Windows.UI.Xaml`
- **Goal:** Frosted glass treatment for Notification Center grid, Calendar center, Control Center region, Quick Settings/pages, toast views, and flyouts/jump lists with layered inner cards.

**Key styled surfaces:**

- **Notification Center & Calendar** (`Grid#NotificationCenterGrid`, `Grid#CalendarCenterGrid`): Glass background+rim, `PanelRadius=13`, shadows removed (`Shadow=`), calendar has margin and min height.
- **Calendar inner surfaces** (`ScrollViewer#CalendarControlScrollViewer`, `Border#CalendarHeaderMinimizedOverlay`): `ElementBackground` with `CardRadius=10`, negative margins to align layering, height on header overlay.
- **Focus Session** (`ActionCenter.FocusSessionControl#FocusSessionControl > Grid#FocusGrid`): Layered card with `ElementBackground`, `CardRadius=10`, margins.
- **Flyouts & Jump Lists** (`MenuFlyoutPresenter`, `Border#JumpListRestyledAcrylic`): Glass treatment with `ChipRadius=6`, tight padding/margins, shadows removed.
- **Control Center region** (`Grid#ControlCenterRegion`): Main glass panel, `PanelRadius=13`, bottom margin adjusted.
- **Quick Settings pages** (`ContentPresenter#PageContent`, `ContentPresenter#PageContent > Grid > Border`): Page content made transparent, inner borders/cards get `ElementBackground` with `CardRadius=10` and margins.
- **Full-screen page window** (`QuickActions.ControlCenter.AccessibleWindow#PageWindow > ContentPresenter > Grid#FullScreenPageRoot`): Transparent background, shadows removed.
- **Page header** (`FullScreenPageRoot > ContentPresenter#PageHeader`): Layered `ElementBackground` card, `CardRadius=10`, margins.
- **List content** (`ScrollViewer#ListContent`): `ElementBackground` card, `CardRadius=10`, horizontal margins.
- **Toasts** (`ActionCenter.FlexibleToastView#FlexibleNormalToastView`, `...#FlexibleActionsToastView`): Background set to transparent (glass is handled by container/parent layers).
- **Toast elements**: App icon, progress bar, buttons, and selection elements receive glass/overlay treatments (e.g. `Border#ProgressBarTrack` → `ElementBackground` radius 6, `Button#SnoozeButton` → glass border+background radius 6, selection check border radius 4).

**Notes:** Emphasizes inner `ElementBackground` cards to create frosted layering inside the main glass panels; removes shadows and neutralizes some page backgrounds to let the unified glass show through.

### 4. `windows-11-file-explorer-styler.yml`

- **Windhawk Mod ID:** `windows-11-file-explorer-styler`
- **Target Process:** `explorer.exe`
- **Framework:** WinUI 3 `Microsoft.UI.Xaml`
- **Status:** 🧪 Generated (Ready for verification) — per `AGENTS.md`
- **Goal:** Command Center Glass treatment for File Explorer chrome (navigation, tabs, command bar, address bar, file list chrome, panes, flyouts) while keeping the Win32 file list area behavior respectful and avoiding over-styling native list content.

**Intended coverage (from suite architecture):** WinUI 3 tabs, navigation, command bar, Win32 file list boundary. (Specific selector set to be finalized/verified against current Explorer builds; treat as generated baseline until live verification.)

**Notes:** Generated baseline to be validated with Visual Inspector + live checklist. Keep Win32 file list boundary in mind to avoid visual breakage.

## Style Constants Reference

All four files define the same core constants (with small additive tokens where needed). Use `$Token` references in `styles` for consistency.

| Constant | Type | Purpose |
|---|---|---|
| `Translucent` | `WindhawkBlur` | Light blur accent |
| `Glass` | `WindhawkBlur` | Ultra-light glass |
| `Frosted` | `WindhawkBlur` | Base panel material |
| `Acrylic` | `WindhawkBlur` | Strong blur |
| `Background` | alias `$Frosted` | Canonical background |
| `BorderBrush` | `LinearGradientBrush` (vertical rim) | Top-lit glass rim |
| `BorderBrush2` | `WindhawkBlur` (alt) | Soft alternate border (Start/NC) |
| `OverlayColor` | `AcrylicBrush` | Active/pointer-over fill |
| `OverlayColorAlt`/`OverlayColor2` | `AcrylicBrush` | Inactive/multi-window/alt hover |
| `AccentColor` | `AcrylicBrush` (system accent) | Accent highlights |
| `ElementBackground` | `SolidColorBrush` (low opacity) | Layered inner cards |
| `ClockBG` | `SolidColorBrush` (accent, solid) | Lock screen clock/date (Start) |
| `BorderThickness` | thickness | Rim thickness |
| `CornerRadius*`/`PanelRadius`/`CardRadius`/`ChipRadius`/`SearchBoxRadius` | radii | Harmonized scale |
| `BaseHeight`/`BaseWidth` | size | Taskbar button footprint |
| `thumbnailImageSize` | size | NC thumbnail |

## Installation & Usage

1. **Install Windhawk**: [windhawk.net](https://windhawk.net/)
2. **Install the official Windhawk Styler mod(s)** for each surface you want styled:
   - Taskbar: `windows-11-taskbar-styler`
   - Start Menu: `windows-11-start-menu-styler`
   - Notification Center: `windows-11-notification-center-styler`
   - File Explorer: `windows-11-file-explorer-styler`
3. **Apply the YAML**: In each mod's settings, import/copy the corresponding YAML from `src/`. Each YAML is self-contained with `styleConstants` and `controlStyles`.
4. **Theme awareness**: Styles read Windows theme resources and should adapt to light/dark automatically.

> **Process targets:** Taskbar+File Explorer → `explorer.exe`. Start Menu → `StartMenuExperienceHost.exe`. Notification Center → `ShellExperienceHost.exe`/`ShellHost.exe`.

## Validation & Quality Gates

This repo enforces static validation and live verification.

- **Static gate (mandatory):** Run syntax/token validation with the PowerShell linter:

  ```powershell
  pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
  ```

  The suite must pass with `0 errors` before considering changes complete.

- **Live verification:** Use the template checklist to validate on desktop:
  - Template: `.agents/templates/live-verification-checklist.md`
  - Covers each surface (Taskbar, Start Menu/Lock, Notification Center/Quick Settings, File Explorer), states (normal/hover/active), theme switching, and regression spots.

- **Target evidence (Rule 04):** Selectors must be sourced from official Windhawk mod source code, settings schemas, or community theme references. Avoid guessing; prefer evidence-backed targets.

## Conventions & Compliance

All changes must comply with `.agents/rules/` and repo standards:

- **Rule 01 – Zero unsolicited injection:** Exactly four styler mods; no unapproved packages/tools.
- **Rule 02 – Windhawk Styler syntax:** YAML/XAML syntax, quoting, constant declaration order, no inline syntax errors.
- **Rule 03 – Design language standards:** Use canonical "Command Center Glass" tokens/materials and radius scales above.
- **Rule 04 – Target evidence protocol:** Sourced selectors only; document evidence when adding/changing targets.
- **Rule 05 – Surface scope standards:** Respect process targets and WinUI 3 vs UWP boundaries.
- **Rule 07 – Verification standards:** Mandatory static gate + user live checklist.
- **Rule 08 – Documentation standards:** Root Markdown files + `src/extras/README.md` + `.agents/`; no `docs/` folder.
- **Rule 09 – Tracking standards:** Work is tracked via milestones/sprints in the planning files (`ROADMAP.md`, `PLAN.md`, `TODO.md`, `BUGS.md`) — the project does not use formal versioned releases.

## Related Documentation

- **Repository root:** [`README.md`](../README.md), [`AGENTS.md`](../AGENTS.md), [`PLAN.md`](../PLAN.md), [`TODO.md`](../TODO.md), [`BUGS.md`](../BUGS.md), [`ROADMAP.md`](../ROADMAP.md)
- **Extras & assets:** [`src/extras/README.md`](extras/README.md)
- **Agent ecosystem:** [`.agents/agents/README.md`](../.agents/agents/README.md), [`.agents/rules/`](../.agents/rules/)
- **Validation tool:** [`tools/Test-WindhawkStyles.ps1`](../tools/Test-WindhawkStyles.ps1)
- **Live checklist template:** [`.agents/templates/live-verification-checklist.md`](../.agents/templates/live-verification-checklist.md)
- **Changelog:** [`CHANGELOG.md`](../CHANGELOG.md) — chronological log of completed work (tracked via milestones/sprints, not versioned releases)