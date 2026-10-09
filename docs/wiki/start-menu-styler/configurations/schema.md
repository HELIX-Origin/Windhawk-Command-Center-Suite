---
layout: documentation
title: "Wiki: Start Menu Configurations"
---

# Start Menu Styler Configuration Schema & Options

Exhaustive technical reference for top-level YAML configuration directives, token mechanics, WebContent injection, and companion positioning supported by `windows-11-start-menu-styler`.

---

## 1. Complete Top-Level Schema Definition

The mod expects a structured YAML configuration root parsing the following directives:

```yaml
theme: ''                              # Built-in preset theme name (empty string for custom suite theme)
disableNewStartMenuLayout: ''          # Optional toggle to disable 24H2 grouped category grid layout

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

webContentStyles:                      # Custom CSS rules injected into WebView2 search flyouts
  - target: 'css-selector'
    styles:
      - 'css-property: value !important'

webContentCustomJs: ''                 # Optional custom JavaScript injected into WebView2 contexts
```

---

## 2. Deep Dive: `styleConstants` Token Mechanics

The `styleConstants` list defines design tokens referenced throughout `controlStyles` via the `$TokenName` prefix.

### Declaration Invariants
1. **List of Strings**: Each constant entry must be formatted as `TokenName=Value` or `TokenName:=<XAML>`.
2. **No Leading `$` in Declarations**: Writing `-$Background=...` is invalid; write `- Background=...`.
3. **No Direct Nested Constant Declarations**: A constant cannot define another constant inside its value assignment (e.g. `BorderThickness=$OtherThickness` is unsupported in declaration blocks).
4. **Ordering Convention**: Per repository engineering standards, constants must be organized in clean hierarchical blocks:
   * **Blur & Glass Foundations**: Base `WindhawkBlur` brushes.
   * **Gradient Borders**: Top-lit rim lighting brushes (`LinearGradientBrush`).
   * **Card & Tile Fills**: Translucent fills and overlays (`AcrylicBrush`, `SolidColorBrush`).
   * **Geometric Scale**: Border thicknesses and radius scale (`PanelRadius`, `CardRadius`, `ChipRadius`).

### Concrete XAML Material Examples in `styleConstants`

#### A. Unified Frosted Glass (`WindhawkBlur`)
```yaml
styleConstants:
  - Translucent=<WindhawkBlur BlurAmount="15" TintColor="#10808080"/>
  - Glass=<WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Acrylic=<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8" />
  - Background=$Frosted
```

#### B. Top-Lit Rim Lighting Gradient
```yaml
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderThickness=0.3,1,0.3,1
```

#### C. Proportional Radius Scale
```yaml
  - PanelRadius=35       # XL: Outermost flyout frame
  - CardRadius=15        # M: Group cards, pinned background plates
  - ChipRadius=10        # S: Action buttons, power pill, user tile
  - SearchBoxRadius=25   # L: Top search pill
```

---

## 3. Deep Dive: `controlStyles` Syntax & Property Rules

The `controlStyles` block applies styling directives to XAML visual tree nodes discovered in `StartMenuExperienceHost.exe`.

### Target Selector Expressions
* **Type Selector**: `Border`, `Grid`, `Button` matches all nodes of that type.
* **Name Selector**: `#DropShadowDismissTarget` matches an element by its `x:Name`.
* **Qualified Selector**: `Border#DropShadowDismissTarget` matches an element with specific type and name.
* **Child Combinator (`>`)**: Direct parent-to-child relationship (e.g., `Grid#MainMenu > Border#AcrylicBorder`).
* **Descendant Combinator (space)**: Matches nested descendants at any depth (e.g., `StartMenu.SearchBoxToggleButton Grid FontIcon`).
* **Multi-Target Lists (comma-separated)**: Applies identical styles across multiple nodes:
  ```yaml
  - target: Border#StartDropShadow, Border#RightCompanionDropShadow, Border#RootGridDropShadow
    styles:
      - Visibility=Collapsed
  ```
* **Property Filtering**: `[AutomationProperties.Name = Show all]` matches by attached dependency properties.
* **Windhawk Dynamic State Binding**: `ActualHeight=>pinnedListHeight` captures dynamic control height into a variable, which can then be referenced in relative layout math like `RenderTransform:=<TranslateTransform Y="{{-224 - pinnedListHeight}}" />`.

### Property Assignment Operators
| Operator | Syntax Example | Behavior |
|---|---|---|
| `=` | `Height=32` | Assigns scalar value, enum, or string. |
| `: =` | `Background:=$Background` | Inflates complex XAML objects (brushes, transforms, transitions). |
| `:=` *(empty)* | `Shadow:=` | Resets or clears the target property to null/unspecified. |
| `@VisualState` | `Background@PointerOver:=$OverlayColor` | Overrides property during specific visual states without full template re-authoring. |

---

## 4. Deep Dive: `webContentStyles` (WebView2 CSS Injection)

Windows Search and certain Start Menu suggestion flyouts embed Microsoft Edge WebView2 web instances to render cloud-connected search suggestions and MSN feeds. The Start Menu Styler provides the unique `webContentStyles` key to style these web components.

### Syntax & Mechanics
```yaml
webContentStyles:
  - target: '*'
    styles:
      - 'transition: background-color 0.083s ease-in-out !important'
  - target: 'body'
    styles:
      - 'background-color: transparent !important'
      - 'color: #ffffff !important'
  - target: '.suggestion-item'
    styles:
      - 'border-radius: 8px !important'
      - 'background-color: rgba(255, 255, 255, 0.05) !important'
```

* **Target**: Any standard CSS selector (`*`, `body`, `.class-name`, `div[role="button"]`).
* **Styles**: Standard CSS key-value strings. The use of `!important` is strongly recommended to override internal Microsoft web styles.

---

## 5. Companion Mod: Shell Flyout Positions Schema

When pairing Start Menu styling with the **Shell Flyout Positions** (`shell-flyout-positions`) companion mod:

```yaml
startMenu:
  verticalAlignment: bottom     # bottom | top | center (default: windowsDefault)
  horizontalAlignment: center   # center | left | right | tray (default: windowsDefault)
  horizontalShift: 0            # Horizontal shift in pixels (default: 0)
  verticalShift: 0              # Vertical offset in pixels (default: 0)
```

* **`verticalAlignment`**: Controls whether the Start Menu anchors to the top, bottom, or system default location.
* **`verticalShift` / `horizontalShift`**: Adjusts pixel offsets relative to the anchor edge or taskbar.
