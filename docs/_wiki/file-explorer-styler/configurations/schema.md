---
layout: wiki
title: "Wiki: File Explorer Configurations"
---

# File Explorer Styler Configuration Schema & Options

Complete technical reference for top-level YAML configuration directives, whole-window DWM backdrop effects, and Win32 DirectUI boundaries supported by `windows-11-file-explorer-styler`.

---

## 1. Complete Top-Level Schema Definition

```yaml
theme: ''                              # Built-in preset theme name (empty string for custom suite theme)

styleConstants:                        # Shared token definitions and XAML object brushes
  - TokenName=ScalarValue              # Scalar tokens (e.g., margins, radii, dimensions)
  - TokenName:=<XAML Object>           # Complex XAML object brushes (WindhawkBlur, LinearGradientBrush)

themeResourceVariables:                # Global theme resource brush replacements across host process
  - variableKey: ResourceKeyName
    value: "{ThemeResource ...}"

controlStyles:                         # Target selectors and styling rules applied to WinUI 3 nodes
  - target: SelectorExpression
    styles:
      - Property=ScalarValue
      - Property:=<InlineXAML>
      - Property@VisualState=Value
      - Property:=                     # Empty value clears/resets the property

# Whole-window backdrop material applied via DWM APIs
backgroundTranslucentEffect: acrylic   # acrylic | mica | default | tabbed | ""

# Region to apply the backdrop material to
backgroundTranslucentEffectRegion: ""  # "" (Entire window) | explorerFrame (Title/tab bar only)

# Custom top container height adjustment in pixels
explorerFrameContainerHeight: 0

# Diagnostics attachment behavior
xamlDiagnosticsHandling: alert         # alert | block | allow
```

---

## 2. Whole-Window DWM Backdrops: `backgroundTranslucentEffect`

Because File Explorer's main file view is a native Win32 `DirectUIHWND` control rather than XAML, XAML brushes applied to `controlStyles` cannot directly color the file list. Instead, the File Explorer Styler hooks the Desktop Window Manager (DWM) composition attributes of the top-level Win32 window (`CabinetWClass`).

### Available Modes:
* **`acrylic`**: Injects modern Windows DWM Desktop Acrylic blur across the window frame. Works best when WinUI 3 background controls are set to semi-transparent glass fills.
* **`mica`**: Injects Windows 11 Mica material (wallpaper-tinted blur).
* **`tabbed`**: Injects Windows 11 Mica Alt ("Tabbed") material, commonly used in title bar chrome.
* **`default` / `""`**: Leaves window composition in native system mode.

### Effect Regions:
* **`""` (Empty string)**: Spans the blur effect across the entire File Explorer window canvas, including the Win32 file list.
* **`explorerFrame`**: Confines the DWM effect strictly to the upper title bar and tab strip region.

---

## 3. Win32 DirectUIHWND Boundary & Styling Limitations

> [!WARNING]
> **Understanding the WinUI 3 / Win32 Split**:  
> * **XAML Directives (`controlStyles`)**: Affect *only* the top chrome (tabs, navigation buttons, address bar, search box, command bar, details pane).
> * **Classic Shell Controls**: The folder tree view (`SysTreeView32`), file items list (`DirectUIHWND`), column headers (`SysHeader32`), and classic right-click context menus are pure Win32 controls. They do not parse XAML properties or support `WindhawkBlur`.
> * Translucency for the file list area is achieved strictly through `backgroundTranslucentEffect: acrylic`.

---

## 4. Key Recipes: Applying Translucent Glass to File Explorer

```yaml
backgroundTranslucentEffect: acrylic
backgroundTranslucentEffectRegion: ""
explorerFrameContainerHeight: 0

styleConstants:
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Background=$Frosted
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderThickness=0.3,1,0.3,1

controlStyles:
  # Address bar pill
  - target: Grid#FileExplorerAddressBarGrid
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=6

  # Search box pill
  - target: AutoSuggestBox#FileExplorerSearchBox > Grid#LayoutRoot > TextBox#TextBox
    styles:
      - Background:=$Background
      - BorderBrush:=$BorderBrush
      - BorderThickness=$BorderThickness
      - CornerRadius=6
```
