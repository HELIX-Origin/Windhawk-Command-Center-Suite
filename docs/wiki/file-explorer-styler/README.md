---
layout: documentation
title: "Wiki: File Explorer Styler"
---

# Wiki: File Explorer Styler Targets & Configuration

Comprehensive reference for the **Windows 11 File Explorer Styler** mod (`windows-11-file-explorer-styler`), WinUI 3 tab controls, address bar, command bar, and whole-window DWM backdrops.

---

## 1. Mod Overview & Process Host

| Property | Value | Notes |
|---|---|---|
| **Mod ID** | `windows-11-file-explorer-styler` | Official Windhawk mod |
| **Target Process** | `explorer.exe` | Main Windows shell process hosting File Explorer windows |
| **Framework** | WinUI 3 `Microsoft.UI.Xaml` | Modern WinUI 3 top chrome |
| **Version Floor** | `1.7+` | Direct composition and DWM background hooks |

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

# Whole-window backdrop material (DWM effects)
backgroundTranslucentEffect: acrylic # acrylic | mica | default | tabbed | ""

# Region to apply the backdrop material to
backgroundTranslucentEffectRegion: "" # "" (Entire window) | explorerFrame

# Custom top container height adjustment
explorerFrameContainerHeight: 0

# Conflict & diagnostic handling
xamlDiagnosticsHandling: alert # alert | block | allow
```

### Directives:
* **`backgroundTranslucentEffect`**: Instructs the mod to apply DWM blur composition attributes across the Win32 window (`acrylic`, `mica`, `tabbed`, or `default`).
* **`backgroundTranslucentEffectRegion`**: Confines the DWM effect to the top title/tab bar (`explorerFrame`) or applies it to the entire window canvas (`""`).
* **`explorerFrameContainerHeight`**: Adjusts top container height in pixels.
* **`xamlDiagnosticsHandling`**: Diagnostics attachment behavior (`alert`, `block`, or `allow`).

---

## 3. Verified Visual Tree Targets

### Tab Controls & Title Bar
| Selector | Type | Purpose & Notes |
|---|---|---|
| `FileExplorerExtensions.FileExplorerTabControl` | `FileExplorerTabControl` | Root tab control hosting open folder tabs. |
| `Grid#TabContainerGrid` | `Grid` | Container grid holding the tab strip and "+" button. |
| `TabViewItem` | `TabViewItem` | Individual tab control. |
| `TabViewItem > Grid#LayoutRoot@CommonStates` | `Grid` | Tab layout root with hover/pressed states. |
| `TabViewItem > Grid#LayoutRoot > Canvas > Path#SelectedBackgroundPath` | `Path` | Active selected tab card shape. |
| `Grid#TabContainerGrid > Border > Button#AddButton` | `Button` | New tab "+" button. |

### Navigation & Address Bar
| Selector | Type | Purpose & Notes |
|---|---|---|
| `FileExplorerExtensions.NavigationBarControl#NavigationBarControl > Grid#NavigationBarControlGrid` | `Grid` | History arrows and address bar row. |
| `AppBarButton#backButton` | `AppBarButton` | Back navigation arrow. |
| `AppBarButton#forwardButton` | `AppBarButton` | Forward navigation arrow. |
| `AppBarButton#upButton` | `AppBarButton` | Up to parent folder arrow. |
| `Grid#FileExplorerAddressBarGrid` | `Grid` | Address bar outer pill container. |
| `FileExplorerExtensions.AddressBarControl` | `AddressBarControl` | Breadcrumb trail navigation control. |
| `AutoSuggestBox#PART_AutoSuggestBox > Grid#LayoutRoot > TextBox#TextBox` | `TextBox` | Editable address text field. |

### Search Box
| Selector | Type | Purpose & Notes |
|---|---|---|
| `AutoSuggestBox#FileExplorerSearchBox` | `AutoSuggestBox` | File Explorer search bar container. |
| `AutoSuggestBox#FileExplorerSearchBox > Grid#LayoutRoot > TextBox#TextBox` | `TextBox` | Search input text box. |

### Command Bar (Ribbon Replacement)
| Selector | Type | Purpose & Notes |
|---|---|---|
| `CommandBar#FileExplorerCommandBar` | `CommandBar` | Modern command bar control (New, Cut, Copy, Paste, Share). |
| `Grid#CommandBarControlRootGrid` | `Grid` | Command bar root layout grid on newer Windows builds. |
| `AppBarButton[ToolTipService.ToolTip = Cut]` | `AppBarButton` | Cut action button targeted by tooltip string. |
| `AppBarButton[ToolTipService.ToolTip = Copy]` | `AppBarButton` | Copy action button. |
| `AppBarButton[ToolTipService.ToolTip = Paste]` | `AppBarButton` | Paste action button. |
| `Button#MoreButton` | `Button` | "..." overflow menu button. |

### Panes & Context Menus
| Selector | Type | Purpose & Notes |
|---|---|---|
| `Grid#DetailsViewControlRootGrid` | `Grid` | Right-side details and metadata pane. |
| `Grid#HomeViewRootGrid` | `Grid` | File Explorer Home landing page root grid. |
| `FileExplorerExtensions.GalleryViewControl#GalleryViewControl` | `GalleryViewControl` | Windows Photos/Gallery view container. |
| `MenuFlyoutPresenter > Border` | `Border` | Modern context menu popup border card. |
| `ToolTip > ContentPresenter#LayoutRoot` | `ContentPresenter` | Hover tooltip background pill. |

---

## 4. Win32 DirectUI Boundary Invariant

> [!WARNING]
> **XAML Scope vs Win32 Shell**:  
> The File Explorer Styler operates exclusively on the **WinUI 3 XAML island** (tabs, navigation bar, command bar, details pane). The classic folder file list (`DirectUIHWND`), navigation tree, and classic context menus are native Win32 controls that cannot be targeted with XAML properties. Translucency for the classic file list is managed via the top-level `backgroundTranslucentEffect` setting.

---

## 5. Integrated Companion Settings: Translucent Windows & Drive Gauges

When styling File Explorer alongside companion mods:
* **Enhanced Disk Usage (`enhanced-disk-usage`)**: Adjusts drive space meter percentage thresholds, warning colors, and bar heights within "This PC".
* **Resource Redirect (`resource-redirect`)**: Intercepts `imageres.dll` and `shell32.dll` to serve custom drive, folder, and library icons.
