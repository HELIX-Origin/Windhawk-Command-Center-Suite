# 🎨 Styler Theme Blueprint Template

Use this blueprint when creating or refactoring a styler YAML file for a Windhawk styler mod. It includes the mandatory Rule 03 material headers, edge brushes, standard radii scale, and the canonical target blocks.

---

```yaml
styleConstants:
  # Mandatory Rule 03 Materials Header (Do not modify order)
  - Translucent=<WindhawkBlur BlurAmount="15" TintColor="#10808080"/>
  - Glass=<WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Acrylic=<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8" />

  # Canonical Surface, Edge & Accent Tokens
  - Background=$Frosted
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderThickness=0.3,1,0.3,1
  - AccentColor=<AcrylicBrush TintColor="{ThemeResource SystemAccentColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - OverlayColor=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.8" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - OverlayColor2=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - ActiveColor=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="1" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />

  # Canonical Radius Scale
  - CornerRadius=35      # XL: Main panels, cards
  - CornerRadiusAlt1=25  # L: Search pills, large buttons
  - CornerRadiusAlt4=15  # M: Group containers
  - CornerRadiusAlt2=10  # S: Tiles, items, buttons
  - CornerRadiusAlt3=6   # XS: Menus, flyouts, compact items

controlStyles:
  # 1. Main Surface Root (Glass Panel Recipe)
  - target: Selector#RootGrid
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadius

  # 2. Redundant System Wrapper Reset (Clear intermediate system wrappers)
  - target: Selector#InnerWrapper
    styles:
      - Background:=Transparent
      - BorderBrush:=Transparent
      - BorderThickness=0
      - Shadow:=

  # 3. Layered Glass Elements / Cards (Depth & Hierarchy)
  - target: Selector#ChildCard
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CornerRadiusAlt1

  # 4. Native Chrome Collapse
  - target: Border#AcrylicBorder
    styles:
      - Visibility=1

  # 5. Interactive Item States
  - target: Selector#Item@CommonStates > Border#BackgroundBorder
    styles:
      - BorderThickness=$BorderThickness
      - BorderBrush@PointerOver:=$BorderBrush
      - BorderBrush@Pressed:=$BorderBrush
      - CornerRadius=$CornerRadiusAlt2
      - BackgroundSizing=InnerBorderEdge

  # 6. Flyouts & Context Menus
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
