---
layout: documentation
title: "Wiki: Start Menu Configurations"
---

# Start Menu Styler Configuration Schema & Options

Complete reference for top-level YAML configuration directives supported by `windows-11-start-menu-styler`.

---

## 1. Top-Level Configuration Keys

```yaml
styleConstants:
  - ConstantName=Value

themeResourceVariables:
  - variableKey: ResourceKey
    value: "{ThemeResource ...}"

controlStyles:
  - target: Selector#TargetName
    styles:
      - Property=Value
      - Property:=<XAML>

webContentStyles:
  - target: css-selector
    styles:
      - css-property: value
```

---

## 2. Directives Reference

### `styleConstants`
Declares constants accessible via `$ConstantName`. Constants:
* Must be a list of `Name=Value` strings.
* Cannot have a leading `$` in the declaration.
* Cannot reference other constants in the declaration block.

### `themeResourceVariables`
Replaces system theme resources across `StartMenuExperienceHost.exe`. Useful for overriding default solid background brushes or text colors without targeting individual controls.

### `controlStyles`
List of target selectors and XAML property assignments. Supported operators:
* `=` (scalar property assignment)
* `:=` (inline XAML object inflation)
* `:=` *(empty)* (clears property)
* `@VisualState` (overrides property in specific visual states)

### `webContentStyles`
Unique to the Start Menu Styler. Allows injecting CSS rules into WebView2 instances rendered inside Windows Search panes:
```yaml
webContentStyles:
  - target: "body"
    styles:
      - background-color: "transparent !important"
      - color: "#ffffff !important"
```
