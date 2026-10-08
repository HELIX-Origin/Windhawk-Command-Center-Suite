# Rule 02: Windhawk Styler YAML & XAML Syntax Standards

## Purpose

Windhawk styler files are YAML documents whose leaf values are interpreted by each mod's internal parser into Windows XAML property assignments, XAML snippet inflations, and visual-state animations. This rule defines the **exact grammar, naming rules, quoting conventions, and formatting** required for all styler files in this repository.

Throughout this rule, **NC** and **FE** abbreviate the Windhawk mods `windows-11-notification-center-styler` and `windows-11-file-explorer-styler`, and version floors such as NC v1.5+ / FE v1.7+ describe **external mod capabilities only**. The suite has **no File Explorer styler file** (deferred — [Rule 05](surface-scope-standards.md) §2.2); nothing in this rule authorizes creating one.

---

## 1. Top-Level YAML Structure

Every styler file in `src/` must contain only the top-level keys supported by its specific mod (see [Rule 05](surface-scope-standards.md)).

```yaml
# Strict key ordering:
styleConstants:
  - ConstantName=Value
controlStyles:
  - target: Selector#Name
    styles:
      - Property=Value
```

### 1.1 YAML Hygiene
- **Two spaces** for indentation. Never use tabs (enforced by static check `E001`).
- **CRLF** line endings across all files (enforced by static check `E002`).
- No flow-style JSON mappings (`{ target: ... }`); always block style.
- Comments start with `#` and must be on their own line or follow a space. Windhawk line comments (`//`) inside target/style lists are tolerated by the mod parser, but native YAML `#` comments are preferred at the top level.

---

## 2. Style Constants (`styleConstants`)

Constants are declared as a YAML list of strings in the format `Name=Value`.

```yaml
styleConstants:
  - Translucent=<WindhawkBlur BlurAmount="15" TintColor="#10808080"/>
  - Glass=<WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Acrylic=<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8" />
  - Background=$Frosted
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderThickness=0.3,1,0.3,1
  - CornerRadius=35
```

### 2.1 Constant Declaration Rules
1. **Never prefix the name with `$` in the declaration** (e.g. `- $BB1=...` is malformed and causes parser ambiguity; use `- BB1=...`). Enforced by static check `E004`.
2. **Declaration order matters**: a constant may reference another constant (e.g. `Background=$Frosted`), **but only if the referenced constant was declared earlier in the file**. The Windhawk parser applies replacements sequentially as constants are loaded. Forward references fail to resolve.
3. **Usage syntax**: reference a declared constant anywhere in `controlStyles` or `themeResourceVariables` using `$Name` (e.g. `Background:=$Background`, `CornerRadius=$CornerRadius`).
4. **Case sensitivity**: constant names are case-sensitive. Match declarations exactly.
5. **No duplicate declarations**: declaring the same constant name twice in one file is an error (`E008`).

---

## 3. Target Selector Grammar

A selector identifies one or more elements in the XAML visual tree.

```
Selector      := TargetChain ( "," TargetChain )*
TargetChain   := [ ":root" ">" ] Step ( ( ">" | "> * >" ) Step )*
Step          := ClassName [ "#" ElementName ] [ "[" ChildIndex "]" ] [ PropertyFilter ]* [ "@" VisualStateGroup ]
PropertyFilter:= "[" PropertyName "=" PropertyValue "]"
ChildIndex    := Integer (1-based, e.g. [1], [2])
```

### 3.1 Selector Elements
- **`ClassName`**: XAML control type name. Can be unqualified (`Grid`, `Border`, `TabViewItem`, `Button`) or fully qualified (`Windows.UI.Xaml.Controls.Grid` in NC, `Microsoft.UI.Xaml.Controls.Grid` in FE). Unqualified names are preferred for readability unless disambiguation is required.
- **`#ElementName`**: Matches `x:Name` or `FrameworkElement.Name` (e.g. `Grid#NotificationCenterGrid`, `Border#BackgroundBorder`).
- **`[N]`**: 1-based child index among its parent's direct children (e.g. `GridViewItem[1]`, `Border[2]`). Note: there is **no** CSS `:nth-child` syntax.
- **`[Property=Value]`**: Matches dependency properties, especially attached accessibility properties:
  - `Button[AutomationProperties.AutomationId=Microsoft.QuickAction.Volume]`
  - `Grid[AutomationProperties.LocalizedLandmarkType=Footer]`
  - `AppBarButton[ToolTipService.ToolTip = Cut]`
- **`>`**: Direct child combinator.
- **`> * >`**: Ancestor/descendant wildcard combinator (matches zero or more intermediate controls; supported in NC v1.5+ and FE v1.5+). Cannot be leftmost or rightmost.
- **`:root >`**: Anchors the selector to a root control that has no parent.
- **`@VisualStateGroup`**: Attaches a visual state group scope to the step (e.g. `Grid@CommonStates`, `Grid#IconPanel@RunningIndicatorStates`). Must appear at most once per target chain.
- **`,`**: Comma-separated targets share the same styles block (supported in NC v1.7+ and FE v1.6+). Commas inside `[...]` do not split targets.

---

## 4. Property Assignment & XAML Snippet Syntax

Styles inside a `styles:` list take one of four assignment forms:

| Form | Syntax | Example | Purpose |
|---|---|---|---|
| **Literal** | `Prop=Value` | `CornerRadius=$CornerRadius`<br>`Visibility=1`<br>`VerticalAlignment=2` | Simple property values, numbers, enum ordinals, string constants |
| **XAML Object** | `Prop:=<XAML/>` | `Background:=$Background`<br>`BorderBrush:=$BorderBrush`<br>`RenderTransform:=<TranslateTransform X="0" Y="10"/>` | Inflatables: brushes, transforms, transitions, collections |
| **Clear Property** | `Prop:=` | `Shadow:=` | Clears/nullifies a property value |
| **Visual State** | `Prop@State=Val`<br>`Prop@State:=<XAML/>` | `Background@PointerOver:=$OverlayColor`<br>`Fill@ActiveRunningIndicator:=$AccentColor` | Conditional styling applied only when the target's `@VisualStateGroup` is in `@State` |

### 4.1 Quoting Rules in YAML
1. Any style line containing characters that trigger YAML parsing issues (such as leading colons, braces, quotes, or trailing colons) **must be quoted**:
   ```yaml
   styles:
     - 'transition: background-color 0.083s ease-in-out !important' # web content style
     - Shadow:=                                                     # safe unquoted
     - Foreground:=$BG1                                             # safe unquoted
     - Margin=4,0,4,0                                               # safe unquoted
   ```
2. When quotes are used, double quotes `"` are preferred unless the value contains double quotes (in which case wrap in single quotes `'`).
3. Never leave an empty or whitespace-only style line like `- ''` in production code. Clean up all scaffold placeholders before verification (warning `W105`).

---

## 5. XAML Snippet Invariants

1. **Self-closing tags**: XML snippets with no children must be self-closing (e.g. `<TranslateTransform X="0" />`, `<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />`).
2. **Attribute casing**: Match Windows XAML SDK casing (`BlurAmount`, `TintColor`, `TintOpacity`, `TintLuminosityOpacity`, `StartPoint`, `EndPoint`, `Offset`, `ScaleX`, `ScaleY`, `Duration`, `Color`).
3. **No outer namespace declarations**: Windhawk automatically provides standard XAML namespaces in snippet evaluation. Do not declare `xmlns=...` inside snippets.
4. **Theme resources**: Use `{ThemeResource ResourceKey}` for dynamic light/dark/accent binding.

---

## 6. Style Variables (`Prop=>VarName` and `{{VarName}}`)

Supported in NC v1.5+ and FE v1.5+:
- **Capture**: `Width=>tabWidth`
- **Use**: `MinWidth={{tabWidth + 12}}`
- Supported arithmetic: `+`, `-`, `*`, `/`, `?:`, `min()`, `max()`.
- Scope: closest ancestor capture wins.
- **Caveat**: `skip()` expression is supported **only in File Explorer Styler v1.7+**, not in Notification Center Styler.
