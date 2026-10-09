---
layout: wiki
title: "Wiki: Taskbar Configurations"
---

# Taskbar Styler Configuration Schema & Options

Complete technical reference for top-level YAML configuration directives, token mechanics, diagnostics handling, and click-through parameters supported by `windows-11-taskbar-styler`.

---

## 1. Complete Top-Level Schema Definition

The mod expects a structured YAML configuration root parsing the following directives:

```yaml
theme: ''                              # Built-in preset theme name (empty string for custom suite theme)

styleConstants:                        # Shared token definitions and XAML object brushes
  - TokenName=ScalarValue              # Scalar tokens (e.g., margins, radii, dimensions)
  - TokenName:=<XAML Object>           # Complex XAML object brushes (WindhawkBlur, LinearGradientBrush)

themeResourceVariables:                # Global theme resource brush replacements across host process
  - variableKey: ResourceKeyName
    value: "{ThemeResource ...}"

controlStyles:                         # Target selectors and styling rules applied to visual tree nodes
  - target: SelectorExpression
    styles:
      - Property=ScalarValue
      - Property:=<InlineXAML>
      - Property@VisualState=Value
      - Property:=                     # Empty value clears/resets the property

clickThroughTaskbar: 0                 # 0 | 1 - Allows mouse clicks to pass through transparent taskbar margins
xamlDiagnosticsHandling: ''            # alert | block | allow - Governs behavior when XAML diagnostics hooks attach
```

---

## 2. Deep Dive: `styleConstants` Token Mechanics

The `styleConstants` list defines design tokens referenced throughout `controlStyles` via the `$TokenName` prefix.

### Declaration Invariants
1. **List of Strings**: Each constant entry must be formatted as `TokenName=Value` or `TokenName:=<XAML>`.
2. **No Leading `$` in Declarations**: Writing `-$Background=...` is invalid; write `- Background=...`.
3. **No Direct Nested Constant Declarations**: A constant cannot define another constant inside its value assignment in declaration blocks.
4. **Ordering Convention**: Organized hierarchically:
   * **Blur & Glass Foundations**: Base `WindhawkBlur` brushes.
   * **Gradient Borders**: Top-lit rim lighting brushes (`LinearGradientBrush`).
   * **Card & Tile Fills**: Translucent fills and overlays (`AcrylicBrush`, `SolidColorBrush`).
   * **Geometric Scale**: Border thicknesses and radius scale (`CornerRadius`, `CornerRadiusAlt1`, `BaseHeight`, `BaseWidth`).

### Concrete XAML Material Examples in `styleConstants`

```yaml
styleConstants:
  - Translucent=<WindhawkBlur BlurAmount="15" TintColor="#10808080"/>
  - Glass=<WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Acrylic=<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8" />
  - Background=$Frosted
  - OverlayColor=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.8" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - OverlayColorAlt=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - AccentColor=<AcrylicBrush TintColor="{ThemeResource SystemAccentColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderThickness=0.3,1,0.3,1
  - CornerRadius=6
  - CornerRadiusAlt1=20
  - BaseHeight=32
  - BaseWidth=34
```

---

## 3. Deep Dive: `controlStyles` Syntax & Property Rules

The `controlStyles` block applies styling directives to WinUI 3 XAML visual tree nodes discovered in `explorer.exe`.

### Target Selector Expressions
* **Type Selector**: `Taskbar.TaskbarFrame`, `Border`, `Grid` matches nodes of that type.
* **Name Selector**: `#BackgroundControl` matches an element by its `x:Name`.
* **Qualified Selector**: `Taskbar.TaskbarBackground#BackgroundControl` matches both type and name.
* **Child Combinator (`>`)**: Direct parent-to-child relationship (e.g., `Taskbar.TaskbarFrame > Grid#RootGrid`).
* **Multi-Target Lists (comma-separated)**: Applies identical styles across multiple nodes:
  ```yaml
  - target: Taskbar.TaskbarBackground#HoverFlyoutBackgroundControl, Taskbar.TaskbarBackground#HoverFlyoutBackgroundControl > Grid
    styles:
      - Background:=Transparent
      - BorderBrush:=Transparent
      - BorderThickness=0
  ```
* **Property Filtering**: `[AutomationProperties.AutomationId = StartButton]` matches attached dependency properties.
* **Visual State Overrides**: `@CommonStates` allows overriding properties based on interactive control states:
  * `@ActiveNormal` / `@ActivePointerOver` / `@ActivePressed`
  * `@InactiveNormal` / `@InactivePointerOver` / `@InactivePressed`
  * `@MultiWindowNormal` / `@MultiWindowPointerOver` / `@MultiWindowPressed`

---

## 4. Diagnostics & Click-Through Handling

* **`clickThroughTaskbar`**: When set to `1`, mouse clicks on transparent regions (such as margins creating the floating dock effect) pass through directly to windows underneath or the desktop wallpaper.
* **`xamlDiagnosticsHandling`**: Governs behavior when developer tools attach to the XAML tree (`alert`, `block`, or `allow`).
