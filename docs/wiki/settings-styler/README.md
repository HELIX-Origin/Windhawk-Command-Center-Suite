---
layout: documentation
title: "Wiki: Settings Styler"
---

# Wiki: Settings Styler Targets & Configuration

Comprehensive reference for the **Windows 11 Settings Styler** mod (`windows-11-settings-styler`), navigation split views, setting cards, expander groups, and hero banners.

---

## 1. Mod Overview & Process Host

| Property | Value | Notes |
|---|---|---|
| **Mod ID** | `windows-11-settings-styler` | Official Windhawk mod |
| **Target Process** | `SystemSettings.exe` | UWP / WinUI host for the Windows 11 Settings app |
| **Framework** | `Windows.UI.Xaml` | UWP / WinUI XAML |
| **Version Floor** | `1.0+` | Direct composition and token support |

---

## 2. Configuration Options & Top-Level Keys

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

### Directives:
* **`styleConstants`**: Declares shared color brushes, margins, and border radii.
* **`controlStyles`**: Direct element targeting.
* **`themeResourceVariables`**: Dynamic resource brush replacements.
* **`WindhawkBlur`**: Fully supported on Settings page backgrounds and cards.

---

## 3. Verified Visual Tree Targets

### Root Window & SplitView Navigation
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Page#RootPage` | `Page` | Top-level host page for the entire Settings app. |
| `SplitView#RootSplitView` | `SplitView` | Main split view separating sidebar navigation from page content. |
| `SplitViewPane` | `SplitViewPane` | Left sidebar container hosting navigation items. |
| `NavigationViewItem` | `NavigationViewItem` | Individual navigation category items (System, Bluetooth, Network, Personalization, etc.). |
| `NavigationViewItem@CommonStates > Grid > Border` | `Border` | Background card of navigation items with pointer-over and selected states. |
| `AutoSuggestBox#SearchBox` | `AutoSuggestBox` | Global search box located at top of the navigation sidebar. |

### Header & Breadcrumb Navigation
| Selector | Type | Purpose & Notes |
|---|---|---|
| `TextBlock#PageTitle` | `TextBlock` | Primary category title at top of the page. |
| `BreadcrumbBar#PageBreadcrumbs` | `BreadcrumbBar` | Navigation breadcrumb trail on sub-setting pages. |
| `BreadcrumbBarItem` | `BreadcrumbBarItem` | Individual breadcrumb node link. |

### Setting Cards & Group Containers
| Selector | Type | Purpose & Notes |
|---|---|---|
| `SettingCard` | `SettingCard` | Standard expandable or action setting card. |
| `SettingCard@CommonStates > Grid > Border#CardBackground` | `Border` | Primary background fill and border rim of setting cards. |
| `SettingExpander` | `SettingExpander` | Multi-item expandable setting group. |
| `SettingExpander@CommonStates > Grid > Border#HeaderBackground` | `Border` | Top header card of an expandable setting group. |
| `TextBlock#CardTitle` | `TextBlock` | Setting label headline. |
| `TextBlock#CardDescription` | `TextBlock` | Sub-label description beneath the title. |

### System Hero Banner
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Grid#SystemHeroBanner` | `Grid` | Hero card at the top of the System page (computer name, rename button). |
| `Border#DeviceCardBackground` | `Border` | Device representation card border. |
| `TextBlock#DeviceName` | `TextBlock` | PC name label. |

### Controls & Toggles
| Selector | Type | Purpose & Notes |
|---|---|---|
| `ToggleSwitch#SettingToggle` | `ToggleSwitch` | On/off feature toggle switch. |
| `Button#ActionButton` | `Button` | Action button inside setting cards. |
| `ComboBox#OptionDropdown` | `ComboBox` | Multi-choice dropdown selector within setting cards. |
