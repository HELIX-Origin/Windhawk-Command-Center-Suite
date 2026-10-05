# Rule 03: Suite Design Language — "Command Center Glass"

## Purpose

Every surface in the suite must look like it was cut from the same sheet of glass. This rule is the **canonical, extracted specification** of the visual language already shipped in `src/start-menu-customizer.yml` and `src/taskbar-customizer.yml`. New styles (Notification Center, File Explorer) **must** be built from these tokens and recipes. Inventing new values is a violation unless the user approves it and this rule is updated first.

> [!IMPORTANT]
> The shipped files are the reference implementation. If this rule and a shipped file disagree, the shipped file wins and this rule is the bug — fix the rule (and record the change in `BUGS.md`), never "correct" the shipped file to match a stale rule.

---

## 1. Design Principles

1. **One glass layer per surface.** Native chrome (acrylic borders, drop shadows, layer borders, background fills) is collapsed so the suite's `WindhawkBlur` is the *only* material. Nested containers are reset to transparent so glass never stacks into muddy double-blur.
2. **Top-lit edge.** Every panel carries the same thin vertical-gradient border, thicker on top/bottom than on the sides, which reads as light catching the rim of a glass pane.
3. **Theme-aware tint.** Tints come from `{ThemeResource SystemChromeMediumColor}` / `SystemAltLowColor` so the suite follows light/dark mode automatically. The **accent color** (`SystemAccentColor`) is reserved for *state and emphasis*: active indicators, slider fill, the clock, focus.
4. **Rounded hierarchy.** Big containers are very round, interactive items are moderately round, menus/tooltips are slightly round. Radius communicates hierarchy.
5. **Quick, subtle motion.** 83 ms brush transitions, 0.8× press-scale on icons, short horizontal slide-in on menus. Nothing bouncy or slow.

---

## 2. Design Tokens (`styleConstants`)

### 2.1 Materials

| Token | Value | Use |
|---|---|---|
| `Translucent` | `<WindhawkBlur BlurAmount="15" TintColor="#10808080"/>` | Nearly clear glass; reserved, rarely used |
| `Glass` | `<WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />` | Light blur; small overlays |
| `Frosted` | `<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />` | **Default surface material** |
| `Acrylic` | `<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8" />` | Heaviest blur; large text-heavy panes needing legibility |

The four material constants are **always declared verbatim, in this order, as the first four lines** of every styler file — even if some are unused — so all files share one header and swapping the default material is a one-line change.

### 2.2 Surface, Edge & Accent

| Role | Canonical Value | Start Menu name | Taskbar name | Notification Center name |
|---|---|---|---|---|
| Surface | `$Frosted` | `BG0` | `Background` | `Background` |
| Edge brush | `<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>` | `BB0` | `BorderBrush` | `BorderBrush` |
| Edge thickness | `0.3,1,0.3,1` | `BT0` | `BorderThickness` | `BorderThickness` |
| Alt edge (blurred) | `<WindhawkBlur BlurAmount="10" TintColor="#909090" TintOpacity="0.3"/>` | `$BB1` *(malformed — see BUGS)* | — | `BorderBrushAlt` |
| Accent fill | `<SolidColorBrush Color="{ThemeResource SystemAccentColor}" Opacity="1"/>` | `BG1` | — | `BackgroundAlt` |

### 2.3 Interaction-State Brushes (Taskbar reference)

| Token | Value | Use |
|---|---|---|
| `OverlayColor` | `<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.8" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />` | Pressed / active-hover; slider track |
| `OverlayColor2` | same, `TintLuminosityOpacity="0.5"` | Inactive hover |
| `AccentColor` | `<AcrylicBrush TintColor="{ThemeResource SystemAccentColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />` | Accent fills that should still feel glassy (indicators, slider fill, hover on snap layouts) |
| `ActiveColor` | same as `OverlayColor`, `TintLuminosityOpacity="1"` | Active/selected item |

### 2.4 Corner Radius Scale

| Tier | Value | Start Menu | Notification Center | Applies To |
|---|---|---|---|---|
| XL — Panel | `35` | `R0` | `CornerRadius` | Top-level flyout/panel roots, media card, large cards |
| L — Pill | `25` | `R1` | `CornerRadiusAlt1` | Search boxes, pill inputs |
| M — Group | `15` | `R4` | `CornerRadiusAlt4` | Secondary cards / grouped regions inside a panel |
| S — Item | `10` | `R2` | `CornerRadiusAlt2` | Buttons, list items, tiles, tooltips |
| XS — Menu | `6` | `R3` | `CornerRadiusAlt3` | Context menus, menu items, flyout presenters |

The taskbar deliberately uses a compact scale (`R1=6` buttons/flyouts, `R2=20` pills/badges) because it is 38 px tall. File Explorer chrome is similarly dense — see §5.

### 2.5 Typography

| Use | Font | Source |
|---|---|---|
| Display / hero numerals | `Morganite SemiBold` | Start menu clock |
| Secondary display | `vivo Sans EN VF` | Start menu date |
| Everything else | System default (`Segoe UI Variable`) — do not override | — |

Display fonts are **only** for hero numerals/headings (clocks, dates, large counters). Never set them on body text, list items, or buttons.

---

## 3. Canonical Recipes

Use these blocks verbatim (with the file's own token names).

### 3.1 Glass Panel

```yaml
  - target: <panel root>
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
```

### 3.2 Transparent Reset (inner containers under a glass panel)

```yaml
  - target: <nested container>
    styles:
      - Background:=Transparent
      - BorderBrush:=Transparent
      - BorderThickness=0
      - Shadow:=
```

### 3.3 Native Chrome Collapse

```yaml
  - target: Border#AcrylicBorder
    styles:
      - Visibility=1
```

`Visibility=1` is `Collapsed`; `Visibility=0` is `Visible` (XAML enum ordinal). Use it on native acrylic/shadow/fill layers only — never on content.

### 3.4 Interactive Item (hover/press edge)

```yaml
  - target: <item> > Grid@CommonStates > Border#BackgroundBorder
    styles:
      - BorderThickness=$BorderThickness
      - BorderBrush@PointerOver:=$BorderBrush
      - BorderBrush@Pressed:=$BorderBrush
      - CornerRadius=$CornerRadiusAlt2
      - BackgroundSizing=InnerBorderEdge
```

### 3.5 Menu / Flyout

```yaml
  - target: MenuFlyoutPresenter > Border
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadiusAlt3
  - target: MenuFlyoutItem
    styles:
      - CornerRadius=$CornerRadiusAlt3
      - Margin=4,0,4,0
```

### 3.6 Slider

Track `Fill:=$OverlayColor` (or `$Background`), decrease/fill rect `Fill:=$AccentColor`, track `Height=8`.

### 3.7 Motion

| Effect | Style |
|---|---|
| Brush transition | `BackgroundTransition:=<BrushTransition Duration="0:0:0.083" />` |
| Icon press | `RenderTransform@Pressed:=<ScaleTransform ScaleX="0.8" ScaleY="0.8" />` + `RenderTransformOrigin=0.5,0.5` |
| Menu entrance | `ChildrenTransitions:=<TransitionCollection><EntranceThemeTransition IsStaggeringEnabled="False" FromHorizontalOffset="-25" FromVerticalOffset="0" /></TransitionCollection>` |

---

## 4. Token Naming for New Files

1. New styler files use the **descriptive** names already scaffolded in `src/notification-center-styler.yml` (`Background`, `BorderBrush`, `BorderBrushAlt`, `BackgroundAlt`, `BorderThickness`, `CornerRadius`, `CornerRadiusAlt1…4`), plus the taskbar's state brushes (`OverlayColor`, `OverlayColor2`, `AccentColor`, `ActiveColor`) when interaction states are needed.
2. Existing shipped files are **not** renamed as a side effect of other work (Rule 00 §1.1). A token-name unification is its own workstream and needs user approval.
3. Every declared token must be used, or commented in the file header as intentionally reserved (the four materials are always reserved-allowed).

---

## 5. Per-Surface Application Guidance

| Surface | Panel radius | Item radius | Menu radius | Notes |
|---|---|---|---|---|
| Start Menu (reference) | 35 | 10 | 6 | Shipped |
| Taskbar (reference) | 6 | 6 | 6 | Compact; 20 for pills |
| Notification Center | 35 (`NotificationCenterGrid`, `CalendarCenterGrid`, `ControlCenterRegion`) | 10 (toasts, quick-action tiles, list items) | 6 | Pairs visually with Start; the toggle-tile accent = `$AccentColor` |
| File Explorer | 10 (tabs, address bar, search pill) | 6 (action buttons) | 6 (context menus) | **Safe Glass Chrome**: The native window background remains unmolested. No elements hidden. Tabs, address bar, search box, command bar buttons, and menus styled as floating Command Center Glass controls. |

---

## 6. Conformity Checklist

- [ ] Header declares the four materials verbatim and in order
- [ ] Surface/edge/thickness tokens use canonical values (§2.2)
- [ ] Radii come only from the scale (§2.4)
- [ ] Native chrome collapsed; nested containers reset transparent (no double-blur)
- [ ] Accent used only for state/emphasis
- [ ] Display fonts only on hero numerals
- [ ] Motion values match §3.7
- [ ] Every declared token used or explicitly reserved
