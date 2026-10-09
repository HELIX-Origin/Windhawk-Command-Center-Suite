---
layout: documentation
title: "Wiki: Start Menu Element Targets"
---

# Start Menu Visual Tree Element Targets

Living catalog of verified XAML visual tree element names, types, and hierarchical relationships in `StartMenuExperienceHost.exe`.

---

## Root & Master Framing

| Element Selector | Class Type | Verified Windows Builds | Description & Interaction Notes |
|---|---|---|---|
| `Border#DropShadowDismissTarget` | `Windows.UI.Xaml.Controls.Border` | Win11 21H2 – 24H2 | Root drop shadow dismiss host. Setting `Shadow:=` and `BorderThickness=0` eliminates the native system halo. |
| `Border#AcrylicBorder` | `Windows.UI.Xaml.Controls.Border` | Win11 21H2 – 24H2 | Outer frosted glass panel container hosting header and content areas. |
| `Border#AcrylicOverlay` | `Windows.UI.Xaml.Controls.Border` | Win11 21H2 – 24H2 | Split overlay panel separating bottom navigation from content. Set to transparent for uniform glass panels. |
| `Grid#NavPanePlaceholder` | `Windows.UI.Xaml.Controls.Grid` | Win11 21H2 – 24H2 | Bottom navigation row container hosting user profile and power buttons. |
| `Grid#RootGrid` | `Windows.UI.Xaml.Controls.Grid` | Win11 21H2 – 24H2 | Visual tree layout root inside the Start flyout. |

---

## Embedded Search Bar

| Element Selector | Class Type | Verified Windows Builds | Description & Interaction Notes |
|---|---|---|---|
| `AutoSuggestBox#SearchBox` | `Windows.UI.Xaml.Controls.AutoSuggestBox` | Win11 21H2 – 24H2 | Embedded search input bar at the top of the Start Menu. |
| `Border#SearchBoxBorder` | `Windows.UI.Xaml.Controls.Border` | Win11 21H2 – 24H2 | Pill background plate for the search bar. |
| `TextBox#SearchTextBox` | `Windows.UI.Xaml.Controls.TextBox` | Win11 21H2 – 24H2 | Editable text box input area. |
| `TextBlock#SearchBoxPlaceholderText` | `Windows.UI.Xaml.Controls.TextBlock` | Win11 21H2 – 24H2 | Placeholder hint label ("Type here to search"). |

---

## Pinned Applications & Items Grid

| Element Selector | Class Type | Verified Windows Builds | Description & Interaction Notes |
|---|---|---|---|
| `GridView#PinnedList` | `Windows.UI.Xaml.Controls.GridView` | Win11 21H2 – 24H2 | Grid control hosting pinned application icons. |
| `GridViewItem` | `Windows.UI.Xaml.Controls.GridViewItem` | Win11 21H2 – 24H2 | Individual pinned application tile wrapper. |
| `Border#ItemRootBorder` | `Windows.UI.Xaml.Controls.Border` | Win11 21H2 – 24H2 | Tile card background fill and border rim. |
| `TextBlock#ItemTitle` | `Windows.UI.Xaml.Controls.TextBlock` | Win11 21H2 – 24H2 | Application title label beneath or beside the icon. |

---

## Recommendations & Recent Files

| Element Selector | Class Type | Verified Windows Builds | Description & Interaction Notes |
|---|---|---|---|
| `ListView#RecommendedList` | `Windows.UI.Xaml.Controls.ListView` | Win11 21H2 – 24H2 | List view holding recommended files and recent items. |
| `ListViewItem` | `Windows.UI.Xaml.Controls.ListViewItem` | Win11 21H2 – 24H2 | Individual recommended file list item wrapper. |
| `Button#MoreRecommendedButton` | `Windows.UI.Xaml.Controls.Button` | Win11 21H2 – 24H2 | "More" button to expand full recommended items list. |

---

## All Apps List

| Element Selector | Class Type | Verified Windows Builds | Description & Interaction Notes |
|---|---|---|---|
| `Button#AllAppsButton` | `Windows.UI.Xaml.Controls.Button` | Win11 21H2 – 24H2 | "All apps" chevron button in header. |
| `ListView#AllAppsList` | `Windows.UI.Xaml.Controls.ListView` | Win11 21H2 – 24H2 | Alphabetical installed application list. |
| `SemanticZoom#AllAppsSemanticZoom` | `Windows.UI.Xaml.Controls.SemanticZoom` | Win11 21H2 – 24H2 | Alphabet letter jump zoom control. |
| `TextBlock#HeaderLetter` | `Windows.UI.Xaml.Controls.TextBlock` | Win11 21H2 – 24H2 | Group header letter (A, B, C...) in All Apps list. |

---

## Power & User Profile Controls

| Element Selector | Class Type | Verified Windows Builds | Description & Interaction Notes |
|---|---|---|---|
| `Button#PowerButton` | `Windows.UI.Xaml.Controls.Button` | Win11 21H2 – 24H2 | Power options button (Shutdown, Restart, Sleep). |
| `Button#UserProfileButton` | `Windows.UI.Xaml.Controls.Button` | Win11 21H2 – 24H2 | User avatar button and lock trigger. |
| `FontIcon#PowerIcon` | `Windows.UI.Xaml.Controls.FontIcon` | Win11 21H2 – 24H2 | Power icon glyph. |
