# Skill: Glass Material & Chrome Recipes

## Purpose

Technical guide for mastering `WindhawkBlur`, `AcrylicBrush`, gradient rim borders, and chrome collapsing within Windows 11 shell surfaces to achieve the canonical Command Center Glass aesthetic.

---

## 1. WindhawkBlur vs AcrylicBrush

| Feature | `WindhawkBlur` | `AcrylicBrush` |
|---|---|---|
| **Underlying API** | Windhawk DirectComposition / DWM blur shader | Windows.UI.Xaml / Microsoft.UI.Xaml native brush |
| **Blur Radius Control** | Pixel-accurate `BlurAmount` (e.g. 5, 15, 20, 30) | Fixed system blur radius |
| **Theme Resource Support** | Supported: `TintColor="{ThemeResource SystemChromeMediumColor}"` | Supported: `TintColor="{ThemeResource SystemAltLowColor}"` |
| **Luminosity / Opacity** | Supports `TintOpacity`, `TintLuminosityOpacity`, `TintSaturation` | Supports `TintOpacity`, `TintLuminosityOpacity`, `FallbackColor` |
| **Bugs / Artifacts** | Clean, minimal artifacts, fast | Can flicker or fail to refresh during rapid window redraws |
| **Recommendation** | **Primary surface material** (panels, backgrounds) | **Interaction state fills** (hover, pressed, track fills) |

---

## 2. Recipe R1: The Frosted Glass Panel

The foundational material for panel surfaces:
```yaml
styleConstants:
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderThickness=0.3,1,0.3,1
  - CornerRadius=35

controlStyles:
  - target: Selector#PanelRoot
    styles:
      - Background:=$Frosted
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
```

---

## 3. Recipe R2: Inner Layer Reset (Preventing "Double-Blur")

Windows 11 surfaces often wrap controls in multiple nested `Border` and `Grid` elements, each carrying default background brushes or drop shadows. If left intact, applying a glass blur to the root causes a muddy, opaque "double-blur".

Always identify inner containers and reset them:
```yaml
  - target: Selector#InnerContainer
    styles:
      - Background:=Transparent
      - BorderBrush:=Transparent
      - BorderThickness=0
      - Shadow:=
```

---

## 4. Recipe R3: Native Chrome & Shadow Collapsing

To remove hard system frames or opaque acrylic overlays:
```yaml
  - target: Border#AcrylicBorder, Border#dropshadow, Border#RootGridDropShadow
    styles:
      - Visibility=1 # Collapsed
```
*(Remember: `Visibility=0` is `Visible`, `Visibility=1` is `Collapsed`).*

---

## 5. Recipe R4: Interactive Hover/Pressed States

For buttons, cards, and list items:
```yaml
styleConstants:
  - OverlayColor=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.8" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - OverlayColor2=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />

controlStyles:
  - target: Button#Item@CommonStates > Border#BackgroundBorder
    styles:
      - Background@PointerOver:=$OverlayColor2
      - Background@Pressed:=$OverlayColor
      - BorderBrush@PointerOver:=$BorderBrush
      - BorderBrush@Pressed:=$BorderBrush
      - CornerRadius=10
```
