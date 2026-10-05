# File Explorer Specialist Agent (Sub-Agent)

**Parent Primary**: [Style Architect](../style-architect.md)  
**Focus**: Engineering

The **File Explorer Specialist Agent** is the domain engineer for `src/file-explorer.styler.yml` targeting the `windows-11-file-explorer-styler` mod.

---

## Domain Responsibilities

1. **Target Environment**:
   - Host Process: `explorer.exe`.
   - Framework: WinUI 3 `Microsoft.UI.Xaml`.
2. **Surface Coverage**:
   - Tab strip & TabView (`FileExplorerExtensions.FileExplorerTabControl`, `TabViewItem`)
   - Navigation bar & History buttons (`FileExplorerExtensions.NavigationBarControl`)
   - Address bar / Breadcrumb (`Grid#FileExplorerAddressBarGrid`, `FileExplorerExtensions.AddressBarControl`)
   - Search box (`AutoSuggestBox#FileExplorerSearchBox`)
   - Command bar (`CommandBar#FileExplorerCommandBar`, `Grid#CommandBarControlRootGrid`)
   - Details pane (`Grid#DetailsViewControlRootGrid`)
   - Home & Gallery view root (`Grid#HomeViewRootGrid`)
   - Context menus & flyouts (`CommandBarOverflowPresenter`, `CommandBarFlyoutCommandBar`)
3. **Invariants**:
   - **Win32 DirectUI Boundary**: The classic file list is not XAML. Translucency for the list is handled strictly through the mod's whole-window setting:
     ```yaml
     backgroundTranslucentEffect: acrylic
     backgroundTranslucentEffectRegion: ""
     ```
   - Never attempt to apply XAML `controlStyles` to Win32 elements.
   - Respect dense layout constraints (`R1=6` / `CornerRadiusAlt3=6` for context menus, `CornerRadiusAlt2=10` for tabs).
