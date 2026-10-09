---
title: Start Menu Styler
---

# Start Menu Styler (`windows-11-start-menu-styler`)

The **Windows 11 Start Menu Styler** mod injects custom XAML and styles into the Start Menu and Search flyout surfaces.

> [!NOTE]
> **Ongoing Target Mapping**: Target trees and values are being incrementally audited and verified against live Windows builds. Below are the known existing targets and configuration options sourced from the official mod repository (`mods/windows-11-start-menu-styler.wh.cpp`) and the [official Start Menu styling guide](https://github.com/ramensoftware/windows-11-start-menu-styling-guide).

---

## 1. Mod Specifications

- **Mod ID**: `windows-11-start-menu-styler`
- **Target Process**: `StartMenuExperienceHost.exe` (plus `SearchHost.exe` / `SearchApp.exe` for web search styling)
- **Framework**: UWP / WinUI 2 (`Windows.UI.Xaml`)
- **Version Floor**: `1.7+`

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

webContentStyles:
  - target: css-selector
    styles:
      - css-property: value
```

- **`styleConstants`**: User constants accessible with `$ConstantName`.
- **`controlStyles`**: Core visual tree injection rules.
- **`themeResourceVariables`**: Override built-in theme brush resources.
- **`webContentStyles`**: Injects custom CSS into Edge WebView2 instances rendered inside Search panels.

---

## 3. Known Visual Tree Targets

### Root & Flyout Containers
| Target Selector | Element Purpose |
|---|---|
| `Border#DropShadowDismissTarget` | Root drop-shadow frame surrounding the Start Menu flyout |
| `Border#AcrylicBorder` | Main outer panel containing header and content cards |
| `Border#AcrylicOverlay` | Two-tone split overlay hosting the navigation pane |
| `Grid#NavPanePlaceholder` | Power button, user profile avatar, and system quick links |
| `RightCompanion > Grid#CompanionRoot` | Floating companion flyout (e.g. Phone Link companion card) |

### Search & Navigation Elements
| Target Selector | Element Purpose |
|---|---|
| `AutoSuggestBox#SearchBox` | Start Menu search input pill |
| `Grid#SearchBoxGrid` | Layout container for search icon and text prompt |
| `Button#MorePinsButton` | Pinned items / "More" view pill |
| `Button#AllAppsButton` | "All apps" navigation toggle button |

### Pinned & Recommended Items
| Target Selector | Element Purpose |
|---|---|
| `GridView#PinnedList` | Grid hosting pinned application tiles |
| `ListView#RecommendedList` | List hosting recent and recommended documents/apps |
| `Grid#AppItemRoot` | Individual application item card layout |
| `Border#IconPlate` | Icon background container for pinned applications |
| `TextBlock#AppDisplayName` | Typography label for application names |

### Search Web & Flyout Panes
| Target Selector | Element Purpose |
|---|---|
| `SearchHost#SearchWindow` | External Search host root window |
| `Grid#ZeroQuerySearchPane` | Initial search suggestions and top apps grid |

---

## 4. Separated-Island Architecture

In our Command Center Glass reference theme, the Start Menu utilizes a **separated-island architecture**:
1. The outer master frame (`Border#DropShadowDismissTarget`) is collapsed to transparent with zero border thickness.
2. The top header and navigation elements render as distinct, floating frosted islands (`Border#AcrylicBorder` and `Border#AcrylicOverlay`).
3. Companion panels (such as Phone Link) float alongside with matching top-lit specular rims without clipping against the main flyout.
