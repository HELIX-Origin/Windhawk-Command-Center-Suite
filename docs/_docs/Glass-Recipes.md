---
title: Glass Material Recipes
---

# Glass Material Recipes & Chrome Collapsing

Achieving a clean, high-performance translucent glass aesthetic in Windows 11 requires careful material selection and intentional chrome collapsing.

---

## 1. `WindhawkBlur` vs `AcrylicBrush`

| Feature | `WindhawkBlur` | `AcrylicBrush` |
|---|---|---|
| **Engine** | Windhawk DirectComposition / DWM shader | Native XAML compositor brush |
| **Blur Radius** | Direct pixel control (`BlurAmount="20"`) | Fixed system default |
| **Theme Resource** | Supported (`TintColor="{ThemeResource ...}"`) | Supported |
| **Flicker / Lag** | Smooth, fast, artifact-free | Can flicker during rapid redraws |
| **Best Used For** | **Primary panel surfaces** (main flyout panes) | **Interactive cards and hover fills** |

---

## 2. Recipe 1: Foundational Frosted Glass Panel

The base surface material for primary shell windows:

```yaml
styleConstants:
  - Background:=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8"/>
  - BorderBrush:=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0"/><GradientStop Color="#50404040" Offset="0.5"/><GradientStop Color="#40808080" Offset="1.0"/></LinearGradientBrush>
  - BorderThickness=0.3,1,0.3,1
  - CornerRadius=35

controlStyles:
  - target: Grid#RootPanel
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius
```

---

## 3. Recipe 2: Specular Rim Lighting

A vertical linear gradient border simulates natural ambient light catching the polished rim of a glass pane:

```xml
<LinearGradientBrush StartPoint="0,0" EndPoint="0,1">
  <GradientStop Color="#60808080" Offset="0.0"/>
  <GradientStop Color="#50404040" Offset="0.5"/>
  <GradientStop Color="#40808080" Offset="1.0"/>
</LinearGradientBrush>
```

Paired with asymmetric thickness (`0.3,1,0.3,1`), the top and bottom borders appear highlighted while the side edges remain subtle.

---

## 4. Recipe 3: Collapsing Native Chrome & Shadows

To allow custom frosted glass to show through without muddy halos or black boxes:

```yaml
controlStyles:
  # Collapse native drop shadows
  - target: Selector#MasterFrame
    styles:
      - Shadow:=
      - BorderThickness=0

  # Collapse native opaque system background
  - target: Border#NativeBackground
    styles:
      - Background:=Transparent
```

---

## 5. Recipe 4: Interactive Glass Cards (Layered Depth)

Layered elements (quick settings tiles, calendar cells, flyout pills) sit above the base panel:

```yaml
styleConstants:
  - ElementBackground:=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="0.4" FallbackColor="#202020"/>
  - OverlayColor:=<SolidColorBrush Color="#20ffffff"/>
  - OverlayColor2:=<SolidColorBrush Color="#40ffffff"/>

controlStyles:
  - target: Border#CardRoot
    styles:
      - Background:=$ElementBackground
      - Background@PointerOver:=$OverlayColor2
      - Background@Pressed:=$OverlayColor
      - CornerRadius=10
```
