---
layout: docs
parent: Documentation Directory
title: Settings Styler
---

# Settings Styler (`windows-11-settings-styler`)

The **Windows 11 Settings Styler** mod customizes the modern Windows 11 Settings application (`SystemSettings.exe`).

> [!NOTE]
> **Ongoing Target Mapping**: Target trees and values are being incrementally audited and verified against live Windows builds. Below are the known existing targets and configuration options sourced from the official mod repository (`mods/windows-11-settings-styler.wh.cpp`).

---

## 1. Mod Specifications

- **Mod ID**: `windows-11-settings-styler`
- **Target Process**: `SystemSettings.exe`
- **Framework**: UWP / WinUI `Windows.UI.Xaml`
- **Version Floor**: `1.0+`

---

## 2. Supported Top-Level Configuration Options

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
```

- **`styleConstants`**: Declares shared tokens, brushes, and radii.
- **`controlStyles`**: Direct XAML targets and styling definitions.
- **`themeResourceVariables`**: Resource brush replacements.
- **`WindhawkBlur`**: Supported for panel background glass effects.

---

## 3. Known Visual Tree Targets

### Root Window & Navigation Pane
| Target Selector | Element Purpose |
|---|---|
| `Page#RootPage` | Settings app top-level window page |
| `SplitView#RootSplitView` | SplitView hosting navigation sidebar and content pane |
| `SplitViewPane` | Left navigation pane container |
| `NavigationViewItem` | Sidebar navigation categories (System, Bluetooth, Network, Personalization, etc.) |
| `AutoSuggestBox#SearchBox` | Global settings search input box |

### Page Layout & Headers
| Target Selector | Element Purpose |
|---|---|
| `Grid#ContentRoot` | Main settings page scrollable content area |
| `BreadcrumbBar` | Navigation breadcrumb path header |
| `TextBlock#PageTitle` | Large page section header title |
| `StackPanel#HeroBanner` | Top status banner (device name, Windows build, profile avatar) |

### Settings Cards & Expanders
| Target Selector | Element Purpose |
|---|---|
| `SettingsCard` | Standard settings option row card |
| `SettingsExpander` | Expandable multi-option settings card |
| `ToggleSwitch#SettingToggle` | On/Off toggle switches |
| `ComboBox#SettingDropdown` | Option selection dropdowns |
| `Button#ActionButton` | Secondary action buttons (e.g. "Check for updates", "Rename PC") |

---

## 4. Theming Approach

1. **Collapsing Opaque Fills**: Replacing hard system backgrounds on `Page#RootPage` with transparent brushes allows `WindhawkBlur` to shine through.
2. **Card Elevation**: Setting `$ElementBackground` and `$BorderBrush` on `SettingsCard` and `SettingsExpander` transforms the flat interface into a layered, floating glass workspace.
3. **Harmonized Radii**: Navigation search box uses `$SearchRadius` (25px), cards use `$CardRadius` (10px), and buttons use `$ButtonRadius` (6px).
