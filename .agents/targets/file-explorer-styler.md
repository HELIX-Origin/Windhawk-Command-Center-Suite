# 🔬 Target Evidence Record: File Explorer Styler

> [!WARNING]
> **⏸️ DEFERRED (ROADMAP M.03)** — No styler file exists (`projects/<project>/windows-11-file-explorer-styler.yml` was generated, then discontinued — git `1cc49e9`). Official rationale (2026-10-07): deferred due to a lack of plausible customizations; existing styles too similar, no real benefit yet. This ledger is retained as dormant reference material for a possible resumption.

Evidence ledger for the (currently nonexistent) `projects/<project>/windows-11-file-explorer-styler.yml` targeting `windows-11-file-explorer-styler` mod per **Rule 04 (Target Evidence Protocol)**.

> [!NOTE]
> **Accessibility Accommodation**: The user has poor eyesight and prefers zero manual UWPSpy inspection. All selectors below are sourced from official Windhawk mod source code (`mods/windows-11-file-explorer-styler.wh.cpp`), official community themes (Translucent Explorer11, WindowGlass, LiquidGlass, TintedGlass), and official mod documentation. Manual UWPSpy inspection is avoided.

---

## 📋 Surface Overview

- **Style File**: `projects/<project>/windows-11-file-explorer-styler.yml`
- **Windhawk Mod**: Windows 11 File Explorer Styler (`windows-11-file-explorer-styler` v1.7)
- **Target Process**: `explorer.exe`
- **XAML Framework**: WinUI 3 `Microsoft.UI.Xaml`

---

## 🎯 Target Evidence Ledger

| Selector | Surface Region | Tier | Source / Citation | Status | Notes |
|---|---|---|---|---|---|
| `FileExplorerExtensions.FileExplorerTabControl` | Tabs | T4 | `mods/windows-11-file-explorer-styler.wh.cpp` L474 | 🟢 Sourced | Root tab control |
| `Grid#TabContainerGrid` | Tabs | T4 | Mod source (Translucent Explorer11) | 🟢 Sourced | Tab strip container grid |
| `TabViewItem` | Tabs | T4 | Mod source (WindowGlass) | 🟢 Sourced | Individual tab control |
| `TabViewItem > Grid#LayoutRoot@CommonStates` | Tabs | T4 | Mod source (WindowGlass, LiquidGlass) | 🟢 Sourced | Tab layout root with visual states |
| `TabViewItem > Grid#LayoutRoot > Canvas > Path#SelectedBackgroundPath` | Tabs | T4 | Mod source (Translucent Explorer11) | 🟢 Sourced | Selected active tab background path |
| `Grid#TabContainerGrid > Border > Button#AddButton` | Tabs | T4 | Mod source | 🟢 Sourced | New tab "+" button |
| `FileExplorerExtensions.NavigationBarControl#NavigationBarControl > Grid#NavigationBarControlGrid` | Nav Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | History & address bar row |
| `AppBarButton#backButton` | Nav Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Back navigation button |
| `AppBarButton#forwardButton` | Nav Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Forward navigation button |
| `AppBarButton#upButton` | Nav Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Up folder navigation button |
| `Grid#FileExplorerAddressBarGrid` | Address Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Address bar outer container |
| `FileExplorerExtensions.AddressBarControl` | Address Bar | T4 | Mod source (Translucent Explorer11) | 🟢 Sourced | Breadcrumb navigation control |
| `AutoSuggestBox#PART_AutoSuggestBox > Grid#LayoutRoot > TextBox#TextBox` | Address Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Editable address input field |
| `AutoSuggestBox#FileExplorerSearchBox` | Search Box | T4 | Mod source (WindowGlass) | 🟢 Sourced | Search box container |
| `AutoSuggestBox#FileExplorerSearchBox > Grid#LayoutRoot > TextBox#TextBox` | Search Box | T4 | Mod source (WindowGlass) | 🟢 Sourced | Search text box |
| `CommandBar#FileExplorerCommandBar` | Command Bar | T4 | Mod source (Translucent Explorer11) | 🟢 Sourced | Main command bar control |
| `Grid#CommandBarControlRootGrid` | Command Bar | T4 | Mod source v1.6/v1.7 | 🟢 Sourced | Command bar root grid (modern builds) |
| `FileExplorerExtensions.CommandBarControl_Wave1 > Grid` | Command Bar | T4 | Mod source (Translucent Explorer11) | 🟢 Sourced | Command bar row (Wave 1 builds) |
| `AppBarButton[ToolTipService.ToolTip = Cut]` | Command Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Cut button by tooltip |
| `AppBarButton[ToolTipService.ToolTip = Copy]` | Command Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Copy button by tooltip |
| `AppBarButton[ToolTipService.ToolTip = Paste]` | Command Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Paste button by tooltip |
| `Button#MoreButton` | Command Bar | T4 | Mod source (WindowGlass) | 🟢 Sourced | Overflow "..." menu button |
| `CommandBarOverflowPresenter#SecondaryItemsControl > Grid#LayoutRoot` | Context Menu | T4 | Mod source (WindowGlass) | 🟢 Sourced | Command bar overflow menu border |
| `Microsoft.UI.Xaml.Controls.Primitives.CommandBarFlyoutCommandBar` | Context Menu | T4 | Mod source (WindowGlass) | 🟢 Sourced | Modern context menu top row |
| `Grid#DetailsViewControlRootGrid` | Details Pane | T4 | Mod source (Translucent Explorer11) | 🟢 Sourced | Details pane container |
| `Grid#HomeViewRootGrid` | Home | T4 | Mod source (WindowGlass) | 🟢 Sourced | Home page container |
| `FileExplorerExtensions.GalleryViewControl#GalleryViewControl` | Gallery | T4 | Mod source (WindowGlass) | 🟢 Sourced | Gallery view container |
| `MenuFlyoutPresenter > Border` | Menus | T4 | Mod source (WindowGlass) | 🟢 Sourced | Context menu flyout border |
| `ToolTip > ContentPresenter#LayoutRoot` | Tooltips | T4 | Mod source (Translucent Explorer11) | 🟢 Sourced | Tooltip popup container |

---

## ⚠️ Win32 DirectUI Boundary Note

The classic file list and left tree view are **Win32 DirectUI**, not XAML. Translucency for the entire window is controlled via:
```yaml
backgroundTranslucentEffect: acrylic
backgroundTranslucentEffectRegion: "" # Entire window
```
Do not attempt to target file list items via XAML `controlStyles`.
