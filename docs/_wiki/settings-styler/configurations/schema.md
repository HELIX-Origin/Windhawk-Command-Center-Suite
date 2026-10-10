---
parent: Settings Styler
grand_parent: Target & Configuration Wiki
layout: wiki
title: Settings Configurations
---

# Settings Styler Configuration Schema & Options

Complete technical reference for top-level YAML configuration directives, token mechanics, and WindhawkBlur applications supported by `windows-11-settings-styler`.

---

## 1. Complete Top-Level Schema Definition

```yaml
theme: ''                              # Built-in preset theme name (empty string for custom suite theme)

styleConstants:                        # Shared token definitions and XAML object brushes
  - TokenName=ScalarValue              # Scalar tokens (e.g., margins, radii, dimensions)
  - TokenName:=<XAML Object>           # Complex XAML object brushes (WindhawkBlur, LinearGradientBrush)

themeResourceVariables:                # Global theme resource brush replacements across SystemSettings.exe
  - variableKey: ResourceKeyName
    value: "{ThemeResource ...}"

controlStyles:                         # Target selectors and styling rules applied to visual tree nodes
  - target: SelectorExpression
    styles:
      - Property=ScalarValue
      - Property:=<InlineXAML>
      - Property@VisualState=Value
      - Property:=                     # Empty value clears/resets the property
```

---

## 2. Deep Dive: `styleConstants` Token Mechanics

```yaml
styleConstants:
  # Blur & Glass Foundations
  - Translucent=<WindhawkBlur BlurAmount="15" TintColor="#10808080"/>
  - Glass=<WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Acrylic=<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8" />
  - Background=$Frosted
  
  # Border Lighting & Accents
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - OverlayColor=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.8" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - AccentColor=<AcrylicBrush TintColor="{ThemeResource SystemAccentColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - ElementBackground=<SolidColorBrush Color="{ThemeResource SystemAltLowColor}" Opacity="0.25" />
  
  # Geometric Scale
  - BorderThickness=0.3,1,0.3,1
  - CardRadius=10        # M: SettingCard and SettingExpander cards
  - ChipRadius=6         # S: Action buttons, dropdowns, navigation pills
```

---

## 3. Key Recipes: Applying Frosted Glass to Settings

```yaml
styleConstants:
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Background=$Frosted
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderThickness=0.3,1,0.3,1
  - CardRadius=10
  - ChipRadius=6

controlStyles:
  # Whole-app window background
  - target: Page#RootPage
    styles:
      - Background:=$Background

  # Transparent sidebar pane
  - target: SplitViewPane
    styles:
      - Background:=Transparent

  # Glass setting cards
  - target: SettingCard@CommonStates > Grid > Border#CardBackground
    styles:
      - Background:=$ElementBackground
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CardRadius

  # Glass setting expanders
  - target: SettingExpander@CommonStates > Grid > Border#HeaderBackground
    styles:
      - Background:=$ElementBackground
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=$CardRadius
```
