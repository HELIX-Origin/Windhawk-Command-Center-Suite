---
layout: docs
parent: Documentation Directory
title: Windows 11 File Explorer Styler
---

# Windows 11 File Explorer Styler (`windows-11-file-explorer-styler`)

The **Windows 11 File Explorer Styler** mod allows extensive customization of the modern WinUI 3 XAML controls in Windows 11 File Explorer (`explorer.exe`), including tabs, navigation bar, address bar, search box, command bar, and whole-window backdrop effects.

> [!NOTE]
> **Ongoing Target Mapping**: Target trees and values are being incrementally audited and verified against live Windows builds. Below are the known existing targets and configuration options sourced from the official mod repository (`mods/windows-11-file-explorer-styler.wh.cpp`) and the [official File Explorer styling guide](https://github.com/ramensoftware/windows-11-file-explorer-styling-guide).

---

## 1. Mod Specifications

- **Mod ID**: `windows-11-file-explorer-styler`
- **Target Process**: `explorer.exe`
- **Framework**: WinUI 3 `Microsoft.UI.Xaml`
- **Version Floor**: `1.7+` (`WindhawkBlur` supported since v1.2+)

---

## 2. Supported Top-Level Configuration Options

The File Explorer Styler mod supports a rich set of top-level configuration keys:

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

### Key Configuration Directives:
- **`backgroundTranslucentEffect`**: Applies system-level window backdrop effects (`acrylic`, `mica`, `tabbed`, or `default`). Setting to `""` disables whole-window DWM hooks and uses native rendering.
- **`backgroundTranslucentEffectRegion`**: Determines whether the translucency effect is applied to the entire Explorer window or exclusively to the top `explorerFrame` chrome container.
- **`explorerFrameContainerHeight`**: Adjusts the top container height (in pixels) to accommodate custom tab bar sizing, taller address bars, or compact chrome.
- **`xamlDiagnosticsHandling`**: Governs XAML diagnostics attachment behavior (`alert`, `block`, or `allow`) when hooking into `explorer.exe`.

---

## 3. Known Visual Tree Targets

Sourced from the official File Explorer styling guide and popular community themes:

### 3.1 Tab Bar & TabView Controls
| Target Selector | Element Purpose |
|---|---|
| `FileExplorerExtensions.FileExplorerTabControl` | Master WinUI 3 TabView control |
| `TabViewItem` | Individual browser-style file tab item |
| `Grid#TabContainerGrid` | Container organizing tabs and add tab button |
| `Button#AddTabButton` | New tab (`+`) button |
| `Border#TabBorder` | Tab item background plate and border |
| `TextBlock#TabTitle` | Title text displayed on each tab |
| `Button#CloseButton` | Tab close (`x`) button |

### 3.2 Navigation Bar & Breadcrumb Controls
| Target Selector | Element Purpose |
|---|---|
| `FileExplorerExtensions.NavigationBarControl#NavigationBarControl` | Header bar hosting Back, Forward, Up, and Address bar |
| `Grid#NavigationBarControlGrid` | Layout container for navigation controls |
| `Button#BackButton` / `Button#ForwardButton` | History navigation buttons |
| `Button#UpButton` | Parent directory navigation button |
| `FileExplorerExtensions.AddressBarControl` | Main address and breadcrumb container |
| `Grid#FileExplorerAddressBarGrid` | Interactive address bar search and path pill |
| `AutoSuggestBox#FileExplorerSearchBox` | Upper-right file search input pill |
| `Border#SearchBoxBorder` | Translucent background plate for the search bar |

### 3.3 Command Bar & Action Buttons
| Target Selector | Element Purpose |
|---|---|
| `CommandBar#FileExplorerCommandBar` | Ribbon replacement command bar (New, Cut, Copy, Paste, Sort, View) |
| `Grid#CommandBarControlRootGrid` | Background and layout frame of the command bar |
| `AppBarButton` | Standard command bar action buttons |
| `AppBarSeparator` | Vertical separator line between button groups |
| `CommandBarOverflowPresenter` | Command bar "..." more options flyout |
| `CommandBarFlyoutCommandBar` | Contextual flyout command bar |

### 3.4 Details Pane & Home / Gallery Root
| Target Selector | Element Purpose |
|---|---|
| `Grid#DetailsViewControlRootGrid` | Right-side details and file preview pane |
| `Grid#HomeViewRootGrid` | Home page and Gallery grid root layout |
| `SplitView#RootSplitView` | Main split view dividing folder navigation tree and file area |

---

## 4. Understanding the Win32 DirectUI Boundary

> [!IMPORTANT]
> The classic file listing (the folder view displaying file items, details, and icons) and the left tree view are **Win32 DirectUI controls**, not XAML elements.
>
> - DirectUI controls cannot be styled using XAML `controlStyles` rules.
> - Translucency for the file list and navigation tree is managed through the mod's whole-window `backgroundTranslucentEffect` setting.
> - The recommended theming pattern (**Safe Glass Chrome**) styles the modern WinUI 3 chrome controls (tabs, navigation bar, search box, command bar buttons, and menus) as floating frosted glass controls while leaving the core file list stable and readable.
