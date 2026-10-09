# Settings Specialist Agent (Sub-Agent)

**Parent Primary**: [Style Architect](../style-architect.md)  
**Focus**: Engineering

The **Settings Specialist Agent** is the domain engineer for Windows 11 Settings styling targeting the `windows-11-settings-styler` mod.

> **Status**: Part of the canonical **universal five-mod base scope**. Tooling and inspection supported (`SystemSettings.exe` / surface `settings`).

---

## Domain Responsibilities

1. **Target Environment**:
   - Host Process: `SystemSettings.exe`
   - Framework: UWP / WinUI 2/3 `Windows.UI.Xaml`
2. **Surface Coverage**:
   - Navigation pane (`SplitViewPane`, `NavigationViewItem`, account profile hero banner)
   - Content area (`Page`, `ScrollViewer`, `Grid#ContentRoot`)
   - Settings cards and grouped items (`SettingsCard`, `SettingsExpander`, action buttons)
   - Search box (`AutoSuggestBox#SearchBox`) and navigation breadcrumb bar
3. **Design System Integration**:
   - Apply canonical theme glass recipes (`WindhawkBlur`, top-lit rim gradient borders).
   - Collapse opaque native backgrounds and drop shadows to establish clean glass cards.
   - Maintain full light and dark mode contrast and theme-aware resource tokens.
4. **Tooling & Inspection**:
   - Leverage `python tools/inspect_xaml.py -p SystemSettings.exe` with automated surface activation (`Win+I`).
