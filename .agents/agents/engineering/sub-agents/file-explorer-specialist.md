# File Explorer Specialist Agent (Sub-Agent — Dormant)

> ⏸️ **DEFERRED (ROADMAP M.03)** — The File Explorer surface is shelved and **no styler file exists**. Official rationale (user, 2026-10-07): deferred due to a lack of plausible customizations, existing third-party styles being too similar, and no real benefit yet. A styler file was generated, then discontinued (git `1cc49e9`); should the surface be resumed (TODO W.03), the file would be `projects/<project>/windows-11-file-explorer-styler.yml`. This specification is retained as reference for possible future resumption.

**Parent Primary**: [Style Architect](../style-architect.md)  
**Focus**: Engineering

Should the surface be resumed, the **File Explorer Specialist Agent** would serve as the domain engineer for `projects/<project>/windows-11-file-explorer-styler.yml` targeting the `windows-11-file-explorer-styler` mod.

---

## Domain Reference (Dormant)

Everything below is **conditional**: these duties apply only if the File Explorer surface is resumed. Until then, the material is kept as reference knowledge.

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
3. **Invariants** (reference for resumption):
   - **Win32 DirectUI Boundary**: The classic file list is not XAML. Translucency for the list is handled strictly through the mod's whole-window setting:
     ```yaml
     backgroundTranslucentEffect: acrylic
     backgroundTranslucentEffectRegion: ""
     ```
   - Never attempt to apply XAML `controlStyles` to Win32 elements.
   - Respect dense layout constraints (`R1=6` / `CornerRadiusAlt3=6` for context menus, `CornerRadiusAlt2=10` for tabs).
