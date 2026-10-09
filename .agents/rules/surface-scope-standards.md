# Rule 05: Surface Scope, Mod Capabilities & Invariants

## Purpose

Each of the **five base** styler mods targets a distinct Windows shell process, hooks a specific XAML framework, and exposes a specific set of top-level settings and capabilities. Applying settings or selectors across mod boundaries produces silent failures or crashes. This rule defines the strict capabilities, constraints, and process targets for every supported surface: Taskbar, Start Menu, Notification Center, Settings, and File Explorer (files organized under `projects/<project>/`).

---

## 1. Surface Capability Matrix

| Attribute | Taskbar Styler | Start Menu Styler | Notification Center Styler | File Explorer Styler | Settings Styler |
|---|---|---|---|---|---|
| **Mod ID** | `windows-11-taskbar-styler` | `windows-11-start-menu-styler` | `windows-11-notification-center-styler` | `windows-11-file-explorer-styler` | `windows-11-settings-styler` |
| **Style File** | `projects/<project>/windows-11-taskbar-styler.yml` | `projects/<project>/windows-11-start-menu-styler.yml` | `projects/<project>/windows-11-notification-center-styler.yml` | *— (no file; deferred)* | *— (base intended scope)* |
| **Target Process(es)** | `explorer.exe` | `StartMenuExperienceHost.exe`<br>`SearchHost.exe`<br>`SearchApp.exe` | `ShellExperienceHost.exe`<br>`ShellHost.exe` (Win11 24H2) | `explorer.exe` | `SystemSettings.exe` |
| **XAML Framework** | WinUI / XAML | WinUI / XAML | **UWP `Windows.UI.Xaml`** | **WinUI 3 `Microsoft.UI.Xaml`** | **UWP / WinUI 2/3 `Windows.UI.Xaml`** |
| **Current Mod Version** | 1.10+ | 1.7+ | 1.7+ | 1.7+ | 1.0+ |
| **`styleConstants`** | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported |
| **`controlStyles`** | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported |
| **`themeResourceVariables`** | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported |
| **`WindhawkBlur`** | ✅ Supported | ✅ Supported | ✅ Supported (v1.3+) | ✅ Supported (v1.2+) | ✅ Supported |
| **`backgroundTranslucentEffect`** | ❌ None | ❌ None | ❌ None | ✅ **Supported** (`acrylic`, `mica`, `default`, etc.) | ❌ None |
| **`backgroundTranslucentEffectRegion`** | ❌ None | ❌ None | ❌ None | ✅ **Supported** (`""` = Entire window, `explorerFrame`) | ❌ None |
| **`explorerFrameContainerHeight`** | ❌ None | ❌ None | ❌ None | ✅ **Supported** (integer, default 0) | ❌ None |
| **`xamlDiagnosticsHandling`** | ✅ Supported | ❌ None | ❌ None | ✅ **Supported** (`alert`, `block`, `allow`) | ❌ None |
| **`webContentStyles`** | ❌ None | ✅ Supported (Search) | ❌ None | ❌ None | ❌ None |
| **Status in Universal Scope** | ✅ Shipped reference | ✅ Shipped reference | ✅ Generated & Verified | ⏸️ Deferred (ROADMAP M.03) | 🌐 Base Intended Scope (Supported) |

---

## 2. Invariant Rules per Surface

Surface IDs match `.agents/skills/README.md`: **S1** = Notification Center, **S2** = File Explorer (deferred), **S3** = Taskbar, **S4** = Start Menu.

### 2.1 Surface S1 — Notification Center Styler (`projects/<project>/windows-11-notification-center-styler.yml`)
1. **Target Processes**: Runs inside `ShellExperienceHost.exe` (all Windows 11 builds) and `ShellHost.exe` (Windows 11 24H2 Action Center).
2. **Framework Scope**: Uses UWP `Windows.UI.Xaml`.
3. **Covered Regions**:
   - Notification Center main panel (`Grid#NotificationCenterGrid`)
   - Calendar center panel (`Grid#CalendarCenterGrid`)
   - Control Center / Quick Settings (`Grid#ControlCenterRegion`, `ControlCenter.ControlCenterPage`, `Grid#L1Grid`)
   - Media transport controls (`Grid#MediaTransportControlsRegion`, `Grid#ThumbnailImage`)
   - Toast popups (`Border#ToastBackgroundBorder`, `ActionCenter.FlexibleToastView#FlexibleNormalToastView`)
   - Taskbar Jump Lists (`Border#JumpListRestyledAcrylic`, `JumpViewUI.JumpListControl#JumpList`)
   - Focus Assist / DND (`ActionCenter.FocusSessionControl#FocusSessionControl > Grid#FocusGrid`)
4. **Unsupported Keys**: Never declare `webContentStyles`, `backgroundTranslucentEffect`, or `explorerFrameContainerHeight` in this file.
5. **No `skip()` Expression**: The `skip()` variable expression is not supported in the Notification Center Styler.

### 2.2 Surface S2 — File Explorer Styler (Deferred Reference — No File)

> **Deferred (ROADMAP M.03, TODO W.03).** The File Explorer styler mod remains approved under Rule 01's five-mod boundary, but **no styler file exists** — `projects/<project>/windows-11-file-explorer-styler.yml` was generated and then discontinued (git 1cc49e9) and must not be scaffolded, regenerated, or created without a new explicit user directive.
> **Locked user directive (2026-10-07)**: *"deferred due to lack of plausible customizations. there are other already existing styles that are too similar and as such there is no real benefit to having our own file explorer style just yet."*
> Everything below is recorded **for reference only** and stays dormant until the user revives the surface.

1. **Target Process**: Runs inside `explorer.exe`.
2. **Framework Scope**: WinUI 3 `Microsoft.UI.Xaml`.
3. **Covered XAML Chrome Regions**:
   - Tab control & tab items (`FileExplorerExtensions.FileExplorerTabControl`, `TabViewItem`, `Grid#TabContainerGrid`)
   - Navigation bar (`FileExplorerExtensions.NavigationBarControl#NavigationBarControl > Grid#NavigationBarControlGrid`)
   - Address bar / breadcrumb (`Grid#FileExplorerAddressBarGrid`, `FileExplorerExtensions.AddressBarControl`)
   - Search box (`AutoSuggestBox#FileExplorerSearchBox`)
   - Command bar (`CommandBar#FileExplorerCommandBar`, `FileExplorerExtensions.CommandBarControl_Wave1`, `Grid#CommandBarControlRootGrid`)
   - Details & preview pane (`Grid#DetailsViewControlRootGrid`)
   - Home & Gallery view root (`Grid#HomeViewRootGrid`, `FileExplorerExtensions.GalleryViewControl#GalleryViewControl`)
   - Context menus & flyouts (`CommandBarOverflowPresenter`, `CommandBarFlyoutCommandBar`)
4. **The Safe Glass Chrome Principle (Locked User Directive — future-dormant while File Explorer is deferred)**:
   > [!IMPORTANT]
   > Due to File Explorer platform limitations, providing a transparent main background requires heavy, unstable Windows modifications and invasive hacks, which we explicitly avoid.
   > Furthermore, theme styling for File Explorer **must NOT make elements invisible or hidden**.
   >
   > Instead, File Explorer is themed using **Floating Glass Chrome**:
   > - The native Explorer window frame and file list remain visible, stable, and unmolested.
   > - The WinUI 3 interactive chrome (Tabs, Address Bar, Search Box, Command Bar buttons, and Context Menus) is styled with floating glass materials (`WindhawkBlur`), top-lit rim borders, and rounded corners.
   > - No structural UI controls are collapsed or hidden (`Visibility=1` is forbidden on functional controls).
5. **Conflict & Diagnostics Handling**: Handled via `xamlDiagnosticsHandling: alert`. Avoid invasive third-party injection tools.

### 2.3 Surface S3 — Taskbar Styler (Reference)
1. `projects/<project>/windows-11-taskbar-styler.yml` provides the reference styles for the taskbar.
2. It serves as a visual and structural baseline.
3. No breaking architectural modifications may be made to it without explicit user consent.

### 2.4 Surface S4 — Start Menu Styler (Reference & Flyout Architecture)
1. `projects/<project>/windows-11-start-menu-styler.yml` provides the visual and structural contract for the Start Menu.
2. **Flyout Separated-Island Architecture**:
   - Master outer frame collapsed (`Border#DropShadowDismissTarget`: `Background:=Transparent`, `BorderThickness=0`).
   - Header island (`Border#AcrylicBorder`: `Height=114`, `$CardRadius`, `$Background`, `$BorderBrush`, `$BorderThickness`).
   - Two-Tone Split: Layered overlay (`Border#AcrylicOverlay`: `Height=48`, `$ElementBackground`, `CornerRadius=0,0,$CardRadius,$CardRadius`) hosts the hoisted navigation pane (`Grid#NavPanePlaceholder`).
   - Floating companion cards: `RightCompanion > Grid#CompanionRoot` floats independently with dedicated glass tokens.
   - Pinned view pills (`★ v` / `⊞ v`), compact 2-column categories, 3-column pinned list, and Phone Link companion cards are strictly preserved.
   - Unused external targets (clock, widgets, media transport targets) are purged to avoid phantom styling on default-hidden elements.
3. No breaking architectural modifications or loss of custom layouts may occur without explicit user consent.

### 2.5 Surface S5 — Settings Styler (`windows-11-settings-styler`)
1. **Target Process**: Runs inside `SystemSettings.exe`.
2. **Framework Scope**: UWP / WinUI 2/3 `Windows.UI.Xaml`.
3. **Covered Regions**:
   - Navigation pane and navigation view items (`NavigationViewItem`, `SplitViewPane`)
   - Settings page root and layout containers (`Page`, `ScrollViewer`, `Grid#ContentRoot`)
   - Setting group cards and expandable cards (`SettingsCard`, `SettingsExpander`, `StackPanel`)
   - Header area, breadcrumbs, search box, and account user badge
4. **Mod Capabilities**: Supports `styleConstants`, `controlStyles`, `themeResourceVariables`, and `WindhawkBlur`.

---

## 3. Forbidden Cross-Pollination
- Never copy selectors from File Explorer into Notification Center or vice versa. The visual trees belong to different processes and different frameworks (WinUI 3 vs UWP).
- Never place Start Menu `webContentStyles` in Notification Center or File Explorer.
