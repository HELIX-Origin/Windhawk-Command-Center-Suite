---
layout: documentation
title: "Wiki: Start Menu Styler"
---

# Wiki: Start Menu Styler Targets & Configuration

Comprehensive reference for the **Windows 11 Start Menu Styler** mod (`windows-11-start-menu-styler`), covering verified XAML visual tree elements, top-level configuration options, and companion positioning settings.

---

## 1. Mod Overview & Process Host

| Property | Value | Notes |
|---|---|---|
| **Mod ID** | `windows-11-start-menu-styler` | Official Windhawk mod |
| **Target Process** | `StartMenuExperienceHost.exe` | UWP / WinUI 2 host for the Start Menu |
| **Secondary Process** | `SearchHost.exe` / `SearchApp.exe` | Search suggestion panels & WebView2 components |
| **XAML Framework** | `Windows.UI.Xaml` | Standard UWP XAML |
| **Version Floor** | `1.7+` | `WindhawkBlur` supported since v1.2+ |

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

webContentStyles:
  - target: css-selector
    styles:
      - css-property: value
```

### Directives:
* **`styleConstants`**: Declares named variables (colors, brushes, margins, radii). Values are resolved using `$ConstantName`. Constants cannot reference other constants directly.
* **`themeResourceVariables`**: Replaces internal XAML theme brush resources across the host process.
* **`controlStyles`**: Core styling directives applied to visual tree nodes.
* **`webContentStyles`**: Injects custom CSS rules into WebView2 instances running within search panes.

---

## 3. Verified Visual Tree Targets

### Root Flyout & Master Framing
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Border#DropShadowDismissTarget` | `Border` | Outermost root drop-shadow container. Setting `Shadow:=` and `BorderThickness=0` collapses the native dark halo. |
| `Border#AcrylicBorder` | `Border` | Primary glass container holding the header and pinned items. |
| `Border#AcrylicOverlay` | `Border` | Two-tone navigation split overlay. Can be styled or made transparent for a unified glass panel. |
| `Grid#NavPanePlaceholder` | `Grid` | Container for the bottom navigation row (power button, user profile). |
| `Grid#RootGrid` | `Grid` | Main visual tree root grid inside the Start flyout. |

### Search Box & Header
| Selector | Type | Purpose & Notes |
|---|---|---|
| `AutoSuggestBox#SearchBox` | `AutoSuggestBox` | Start Menu embedded search input bar. |
| `Border#SearchBoxBorder` | `Border` | Background border of the search pill. |
| `TextBox#SearchTextBox` | `TextBox` | Search input field text box. |
| `TextBlock#SearchBoxPlaceholderText` | `TextBlock` | "Type here to search" placeholder label. |

### Pinned Apps & Recommendations
| Selector | Type | Purpose & Notes |
|---|---|---|
| `GridView#PinnedList` | `GridView` | Grid view containing pinned application icons. |
| `ListView#RecommendedList` | `ListView` | List view containing recent files and recommended items. |
| `GridViewItem` | `GridViewItem` | Individual pinned app tile wrapper. |
| `ListViewItem` | `ListViewItem` | Individual recommended file list item. |
| `Border#ItemRootBorder` | `Border` | Visual card background for individual grid items. |
| `TextBlock#ItemTitle` | `TextBlock` | Label text for pinned application tiles. |

### Navigation & Power Controls
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Button#PowerButton` | `Button` | Power options button (Shutdown, Restart, Sleep). |
| `Button#UserProfileButton` | `Button` | User profile avatar button and lock trigger. |
| `FontIcon#PowerIcon` | `FontIcon` | Glyphs rendered inside the power flyout button. |
| `MenuFlyout#PowerMenu` | `MenuFlyout` | Flyout menu containing power options. |

### All Apps List
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Button#AllAppsButton` | `Button` | "All apps" chevron button in header. |
| `ListView#AllAppsList` | `ListView` | Alphabetical list of all installed programs. |
| `SemanticZoom#AllAppsSemanticZoom` | `SemanticZoom` | Alphabet jump navigation control. |
| `TextBlock#HeaderLetter` | `TextBlock` | Group header letter (A, B, C, etc.) in All Apps list. |

### Companion Cards (Phone Link)
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Border#CompanionCardRoot` | `Border` | Phone Link companion flyout attached to Start. |
| `Grid#CompanionHeader` | `Grid` | Phone Link device header and battery telemetry. |

---

## 4. Integrated Companion Settings: Shell Flyout Positions

When pairing Start Menu styling with the **Shell Flyout Positions** (`shell-flyout-positions`) companion mod:

| Setting Key | Supported Values | Description |
|---|---|---|
| `startMenu.alignment` | `top`, `bottom`, `center`, `left`, `right` | Anchor position of the Start Menu on screen. |
| `startMenu.offsetX` | Integer (e.g. `0`, `12`, `-12`) | Horizontal offset in pixels from the anchor border. |
| `startMenu.offsetY` | Integer (e.g. `16`) | Vertical offset in pixels (e.g. gap above taskbar dock). |
| `startMenu.dockMonitor` | `primary`, `cursor`, `secondary` | Monitor target for Start Menu placement. |
