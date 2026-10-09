---
title: Style Syntax & Tokens
---

# Style Syntax & Design Token Standards

Windhawk styler files are YAML documents whose key-value pairs are translated at runtime into Windows XAML property assignments, XAML snippet inflations, and visual-state animations.

---

## 1. Top-Level YAML Structure

Every styler file adheres to strict top-level key ordering:

```yaml
styleConstants:
  - ConstantName=Value

themeResourceVariables:
  - variableKey: ResourceKey
    value: "{ThemeResource ...}"

controlStyles:
  - target: Selector#Name
    styles:
      - Property=Value
```

### Formatting Rules:
- **Indentation**: Exactly 2 spaces per indentation level. Tabs (`\t`) are strictly forbidden.
- **Line Endings**: Windows standard CRLF (`\r\n`) across all styler files.
- **No Duplicate Keys**: Keys must never appear twice in the same scope.

---

## 2. Style Constants (`styleConstants`)

Constants are declared as a list of `Name=Value` strings and referenced using `$Name`:

```yaml
styleConstants:
  - Background:=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8"/>
  - BorderBrush:=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0"/><GradientStop Color="#50404040" Offset="0.5"/><GradientStop Color="#40808080" Offset="1.0"/></LinearGradientBrush>
  - CornerRadius=10
  - BorderThickness=0.3,1,0.3,1
```

### Constant Rules:
- **No Leading `$` in Declarations**: Correct: `- CornerRadius=10`. Wrong: `- $CornerRadius=10`.
- **References**: Always use `$ConstantName` when consuming a constant in a style value.
- **No Unused Tokens**: Every declared token should be utilized in `controlStyles` or explicitly reserved in the header.

---

## 3. Style Assignment Operators

| Operator | Usage | Example |
|---|---|---|
| `=` | Simple scalar / string property assignment | `CornerRadius=10`, `Visibility=Collapsed` |
| `:=` | XAML snippet inflation | `Background:=<SolidColorBrush Color="#101010"/>` |
| `@VisualState` | State-specific property override | `Background@PointerOver:=$OverlayColor` |
| `:=` (empty) | Clears property to null / default | `Shadow:=`, `Background:=` |

---

## 4. Target Selector Syntax

Selectors match controls within the live visual tree:

| Pattern | Description | Example |
|---|---|---|
| `TypeName` | Match by XAML class name | `Grid`, `Button` |
| `#Name` | Match by element `x:Name` | `#NotificationCenterGrid` |
| `Type#Name` | Typed name selector | `Border#BackgroundBorder` |
| `[Prop=Val]` | Match by dependency property | `[AutomationProperties.AutomationId=WiFi]` |
| `Parent > Child` | Direct child combinator | `Grid#L1Grid > Border#TileRoot` |
| `@StateGroup` | Scope to a visual state group | `TaskListButtonPanel@CommonStates` |
