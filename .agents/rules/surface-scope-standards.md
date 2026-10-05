# Rule 05: Surface Scope, Mod Capabilities & Invariants

## Purpose

Each of the four styler mods targets a distinct Windows shell process, hooks a specific XAML framework, and exposes a specific set of top-level settings and capabilities. Applying settings or selectors across mod boundaries produces silent failures or crashes. This rule defines the strict capabilities, constraints, and process targets for each of the four surfaces in the suite.

---

## 1. Surface Capability Matrix

| Attribute | Taskbar Styler | Start Menu Styler | Notification Center Styler | File Explorer Styler |
|---|---|---|---|---|
| **Mod ID** | `windows-11-taskbar-styler` | `windows-11-start-menu-styler` | `windows-11-notification-center-styler` | `windows-11-file-explorer-styler` |
| **Style File** | `src/taskbar-customizer.yml` | `src/start-menu-customizer.yml` | `src/notification-center-styler.yml` | `src/file-explorer.styler.yml` |
| **Target Process(es)** | `explorer.exe` | `StartMenuExperienceHost.exe`<br>`SearchHost.exe`<br>`SearchApp.exe` | `ShellExperienceHost.exe`<br>`ShellHost.exe` (Win11 24H2) | `explorer.exe` |
| **XAML Framework** | WinUI / XAML | WinUI / XAML | **UWP `Windows.UI.Xaml`** | **WinUI 3 `Microsoft.UI.Xaml`** |
| **Current Mod Version** | 1.10+ | 1.7+ | 1.7 | 1.7 |
| **`styleConstants`** | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported |
| **`controlStyles`** | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported |
| **`themeResourceVariables`** | ✅ Supported | ✅ Supported | ✅ Supported | ✅ Supported |
| **`WindhawkBlur`** | ✅ Supported | ✅ Supported | ✅ Supported (v1.3+) | ✅ Supported (v1.2+) |
| **`backgroundTranslucentEffect`** | ❌ None | ❌ None | ❌ None | ✅ **Supported** (`acrylic`, `mica`, `default`, etc.) |
| **`backgroundTranslucentEffectRegion`** | ❌ None | ❌ None | ❌ None | ✅ **Supported** (`""` = Entire window, `explorerFrame`) |
| **`explorerFrameContainerHeight`** | ❌ None | ❌ None | ❌ None | ✅ **Supported** (integer, default 0) |
| **`xamlDiagnosticsHandling`** | ✅ Supported | ❌ None | ❌ None | ✅ **Supported** (`alert`, `block`, `allow`) |
| **`webContentStyles`** | ❌ None | ✅ Supported (Search) | ❌ None | ❌ None |
| **Status in Suite** | ✅ Shipped reference | ✅ Shipped reference | 🚧 Scaffold in progress | 🚧 Empty in progress |

---

## 2. Invariant Rules per Surface

### 2.1 Surface S1 — Notification Center Styler (`src/notification-center-styler.yml`)
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

### 2.2 Surface S2 — File Explorer Styler (`src/file-explorer.styler.yml`)
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
4. **The Safe Glass Chrome Principle (Locked User Directive)**:
   > [!IMPORTANT]
   > Due to File Explorer platform limitations, providing a transparent main background requires heavy, unstable Windows modifications and invasive hacks, which we explicitly avoid.
   > Furthermore, the Command Center style for File Explorer **must NOT make elements invisible or hidden**.
   >
   > Instead, File Explorer is themed using **Command Center Glass Chrome**:
   > - The native Explorer window frame and file list remain visible, stable, and unmolested.
   > - The WinUI 3 interactive chrome (Tabs, Address Bar, Search Box, Command Bar buttons, and Context Menus) is styled with floating Command Center Glass materials (`WindhawkBlur`), top-lit rim borders, and rounded corners.
   > - No structural UI controls are collapsed or hidden (`Visibility=1` is forbidden on functional controls).
5. **Conflict & Diagnostics Handling**: Handled via `xamlDiagnosticsHandling: alert`. Avoid invasive third-party injection tools.

### 2.3 Surface S3 & S4 — Taskbar & Start Menu (Shipped References)
1. Both files in `src/` are shipped and verified reference implementations.
2. They serve as the visual and structural contract for the suite.
3. No breaking architectural modifications may be made to them without explicit user consent.

---

## 3. Forbidden Cross-Pollination
- Never copy selectors from File Explorer into Notification Center or vice versa. The visual trees belong to different processes and different frameworks (WinUI 3 vs UWP).
- Never place Start Menu `webContentStyles` in Notification Center or File Explorer.
