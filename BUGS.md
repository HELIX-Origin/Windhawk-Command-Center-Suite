# Windhawk Command Center Suite — Bug & Issue Tracker

> 🐛 **Living Source of Truth**: Active tracking ledger for open bugs, quirks, external limitations, and resolution history across all styler mods.

> [!IMPORTANT]
> AI agents strictly required to update this page and all related pages **before** working on any new bug fixes or features and push it to the remote first, without exception. Failure to do so may result in working with outdated information and potentially introducing conflicts or redundant work. 

---

## 📜 Tracking Rules

- **No Typo Duplication**: When recording user reports, clean and fix all typos to preserve professional quality.
- **Consistent Formatting**: Maintain consistent formatting and style throughout all documentation to ensure readability and professionalism.
- **Clear Sectioning**: Use clear and descriptive headers for each section to improve navigation and readability.
- **Active Items First**: The currently active milestone, sprint, task, or workstream must always be placed at the top of the content sections.
- **Regular Updates**: Ensure that the roadmap is regularly updated to reflect the latest developments and changes in the project.
- **Improve User Directives**: Continuously refine and clarify user directives to ensure they are easily understood and actionable.
- **Accessibility Invariant**: Accommodate the user's poor eyesight by exhausting official mod sources and community themes first to avoid manual visual tree inspection.
- **Always Track Everything**: Every new feature request, enhancement, or bug report must be logged in [`BUGS.md`](./BUGS.md), [`TODO.md`](./TODO.md), and [`ROADMAP.md`](./ROADMAP.md) before execution.

---

## 📖 Legend

### 🚦 Status

- ⚠️ **open** — reproducible, needs fixing *(Detailed lists with possible fixes encouraged).*
- 🚧 **investigating** — repro/root-cause in progress *(List of issues currently being worked on).*
- 🚫 **wontfix** — accepted limitations *(features that can't be fixed without significant platform trade-offs).*
- ✅ **resolved** — verified and fixed *(moved to closed with corresponding version or commit).*

### 🚨 Severity

- 🔴 **Critical**: *Bugs that cause shell crashes or visual unreadability.*
- 🟠 **High**: *Bugs that significantly impact aesthetics or cause layering glitches.*
- 🟡 **Medium**: *Bugs that affect minor visual alignments or state transitions.*
- 🟢 **Low**: *Minor warnings, duplicate selectors, or non-visual syntax quirks.*

---

## 🚫 Known Quirks & External Limitations (wontfix bucket)

- 🪟 **Classic Win32 File List & Avoidance of Heavy Windows Modifications**:
    - The classic file/folder view and navigation tree in File Explorer are Win32 DirectUI controls. Providing transparent main backgrounds on these controls requires heavy, unstable Windows modifications and invasive system hooks that the suite explicitly avoids.
    - Furthermore, hiding controls or making elements invisible degrades File Explorer usability.
    - **Resolution**: Improvise using the **Safe Glass Chrome** design pattern: the native Explorer window frame and file list remain stable, while the WinUI 3 interactive chrome (tabs, navigation bar, address bar, search box, command bar buttons, and context menus) is styled with floating Command Center Glass materials without hiding any controls.
- ⏱️ **One-Time Evaluation of Target Selectors**:
    - Windhawk stylers match target selectors when an element enters the visual tree or inflates its template. If attached properties or child indices change dynamically without a visual state transition, Windhawk does not re-evaluate the target.
    - **Resolution**: Use static visual state triggers (`@CommonStates`) rather than dynamic property filters wherever possible.
- 📦 **Windows 11 24H2 ShellHost Process Migration**:
    - On Windows 11 24H2, the Action Center / Quick Settings flyout runs in `ShellHost.exe` rather than `ShellExperienceHost.exe`.
    - **Resolution**: Windhawk Notification Center Styler v1.1.3+ targets both processes automatically.

---

## 💡 Explicitly Not Bugs

- 🎨 **Different Radii on Taskbar vs Start Menu**: The taskbar uses compact radii (`R1=6`, `R2=20`) due to its 38px height, while Start Menu and Notification Center use large panel radii (`R0=35`). This is an intentional design scale hierarchy.
- 📁 **Win32 Scrollbars in File Explorer**: Under Windows 11 default theming, Win32 DirectUI scrollbars follow system mode rather than custom XAML styles.

---

## ⚠️ Active & Open Bugs

---

### 2026-10-07 — Notification / Action Center Quick Settings Split Button Color Mismatch

- **Severity**: 🟠 High (visual dissonance / state mismatch)
- **Status**: 🚧 fix applied (pending live desktop verification)
- **Affected File**: `src/windows-11-notification-center-styler.yml`
- **Reported Issue**: Section buttons in the Action Center Quick Settings panel do not receive correct colors due to split-button template layering. In particular, split buttons (such as Wi-Fi and Bluetooth) show a color mismatch where the left toggle half displays an accent color and the right chevron half displays bright high-contrast blue (`media_1791431699608_c575da8b.png`). Unselected buttons also show inconsistent backgrounds.

#### Root Cause
Quick Settings split buttons in UWP (`SplitL2Button`, `PaginatedToggleButton`) have multi-part internal visual trees where the primary toggle button and the flyout chevron button inherit distinct visual state brushes (`CommonStates` vs `CheckedStates`). Current styling only partially overrides the container border, leaving the child chevron button template falling back to native high-contrast brushes.

#### Resolution Applied
1. Reset outer button backgrounds and borders to `Background:=Transparent`, `BorderThickness=0` on `ControlCenter.PaginatedToggleButton#ToggleButton`, `QuickActions.AccessibleToggleButton#ToggleButton`, `ControlCenter.PaginatedToggleButton#SplitL2Button`, and `Button#SplitL2Button`.
2. Routed all state styling through `ContentPresenter#ContentPresenter@CommonStates` across both `#ToggleButton` and `#SplitL2Button`.
3. Applied canonical Command Center tokens:
   - `Normal` / `Disabled`: `$ElementBackground` with `$BorderBrush`
   - `PointerOver`: `$OverlayColor2` with `$BorderBrush`
   - `Pressed`: `$OverlayColor` with `$BorderBrush`
   - `Checked` / `CheckedPointerOver`: `$AccentColor` with `$BorderBrush`
   - `CheckedPressed`: `$OverlayColor` with `$BorderBrush`
4. Maintained `Margin=4,0,-4,0` on `#SplitL2Button` to preserve clean pill separation.

---

### 2026-10-07 — Taskbar Snap Layout Internal Elements Theming

- **Severity**: 🟡 Medium (incomplete theme coverage)
- **Status**: ⚠️ open
- **Affected File**: `src/windows-11-taskbar-styler.yml`
- **Reported Issue**: Snap containers internal elements still lack full Command Center glass theming. While the individual layout cards receive backgrounds, internal buttons and container elements need refinement to match suite styling without disrupting layout coordinate calculations.

#### Root Cause
Snap layout elements inside `snaplayout.dll` rely on precise internal margins and hit-testing bounds. Target selectors must style visual properties (`Background`, `BorderBrush`, `BorderThickness`, `CornerRadius`) on `LayoutBorder` and button states without modifying internal layout padding or sizing dimensions.

### 2026-10-07 — Taskbar System Tray Overflow Flyout Missing Glass Background

- **Severity**: 🟡 Medium (visual regression / missing surface)
- **Status**: 🚧 fix applied (pending live desktop verification)
- **Affected File**: `src/windows-11-taskbar-styler.yml`
- **Reported Issue**: The system tray overflow grid (the chevron popup holding overflow notification icons) lost its background styling (`media_1791432063085_e18460b5.png`, `media_1791491404487_b1aea40b.png`).

#### Root Cause
In `src/windows-11-taskbar-styler.yml`, `Grid#OverflowRootGrid > Border` was explicitly set to `Background:=Transparent`, `BorderBrush:=Transparent`, `BorderThickness=0`, which stripped both the frosted glass backdrop and border from the overflow flyout.

#### Resolution Applied
Restored `Background:=$Background`, `BorderBrush:=$BorderBrush`, `BorderThickness=$BorderThickness`, `CornerRadius=$CornerRadius`, and collapsed hard system shadows (`Shadow:=`) on `Grid#OverflowRootGrid > Border`.

---

### 2026-10-07 — Start Menu Search & Companion Geometry and Panel Width Alignment

- **Severity**: 🟡 Medium (spatial alignment & width refinement)
- **Status**: 🚧 fix applied (pending live desktop verification)
- **Affected File**: `src/windows-11-start-menu-styler.yml`
- **Reported Issue**:
    1. Start Menu redesign felt too wide (`Width=910`, 5 pin columns, 3 category columns per `media_1791492109151_4e5f4a21.png`).
    2. User requested reverting to the compact preferred width (`media_1791492134279_cf79372d.png`): 750px total panel width, 470px MainMenu, 360px PinnedList (3 pin columns, 2 category columns), crisp vertical divider between MainMenu and Phone Link companion, and cohesive Command Center Glass styling.

#### Root Cause
Stretched layout used `StartDocked.StartSizingFrame Width=910`, `Grid#MainMenu MaxWidth=650`, and `StartMenu.PinnedList MaxWidth=550`, which inflated the pin grid to 5 columns and category cards to 3 columns, while collapsing the vertical divider border.

#### Resolution Applied
1. Restored compact panel width: `StartDocked.StartSizingFrame Width=750, Height=700`.
2. Set `Grid#MainMenu Width=470, Height=700`.
3. Set `StartMenu.PinnedList#StartMenuPinnedList Width=360` and `ScrollViewer Width=360` (yielding 3 pin columns and 2 category columns).
4. Restored native vertical divider border (`Border#MainMenuHighContrastBorder`) separating the Main Menu from the Right Companion.
5. Preserved unified frosted glass backdrop (`Border#DropShadowDismissTarget`) and styled Phone Link cards (`$ElementBackground`, `$BorderBrush`, `$BorderThickness`, `$CardRadius`).

---

### 2026-10-07 — Start Menu: Phone Link Companion Merged with Unified Glass Surface

- **Severity**: 🟡 Medium (feature refinement / surface integration)
- **Status**: ✅ resolved — commit `(pending)`
- **Affected File**: `src/windows-11-start-menu-styler.yml`
- **Reported Issue**: Phone Link panel appeared as a disconnected separate tile with its background clipping at 470px. User requested merging it into the Start Menu with a wider unified background and 3 distinct glass cards for its sub-sections (Device Status, Quick Actions, Recent Notifications).

#### Root Cause
Targeting `Grid#MainMenu > Border#AcrylicBorder` constrained the glass background to the 470px width of `Grid#MainMenu`. Per the `WindowGlass` architecture, the root outer glass surface must be anchored on `Border#DropShadowDismissTarget` inside `StartDocked.StartSizingFrame` at 750px width.

#### Resolution
- Moved `$Background` and top-lit rim gradient border to `Border#DropShadowDismissTarget` (width 750px, height 700px).
- Set `Border#AcrylicBorder` (both in `Grid#MainMenu` and `CompanionRoot`) to `Transparent` / 0 thickness to remove the divider.
- Structured Phone Link sub-sections into 3 Command Center Glass cards: Device Status (`PrimaryCardContainer`, `AdaptiveCardContent`), Quick Actions (`ActionsBar`), and Recent Notifications (`WholeItemsPanel > Border`).


- **Severity**: 🟡 Medium (duplicate nested border rendering)
- **Status**: ✅ resolved — commit `(pending)`
- **Affected File**: `src/windows-11-start-menu-styler.yml`
- **Reported Issue**: Folder popup modals (`StartMenu.FolderModal#StartFolderModal`) rendered with a double border: an outer rim on `Grid#Root` and an inner rim on `Grid#Root > Border`.

#### Root Cause
Both the outer container `StartMenu.FolderModal#StartFolderModal > Grid#Root` (with `Padding=12`) and its inner card element `Grid#Root > Border` were assigned `$BorderBrush` and `$BorderThickness`, creating concentric borders around the modal.

#### Resolution
- Removed border, background, and padding from `StartMenu.FolderModal#StartFolderModal > Grid#Root`, keeping only responsive bounds.
- Maintained the single Command Center Glass background and top-lit rim gradient border exclusively on the inner card element `Grid#Root > Border`.

---

### 2026-10-07 — Start Menu: Collapsing Recent / Recommended Section

- **Severity**: 🟡 Medium (layout decluttering)
- **Status**: ✅ resolved — commit `(pending)`
- **Affected File**: `src/windows-11-start-menu-styler.yml`
- **Reported Issue**: Experimental sizing attempts on the Recommended section caused visual inconsistencies; user requested full collapse.

#### Resolution
- Replaced experimental recommendations rules with complete collapse (`Visibility=Collapsed`) on `Grid#TopLevelSuggestionsRoot`, `Grid#TopLevelSuggestionsContainerParent`, `Grid#TopLevelSuggestionsContainer`, and `Grid#TopLevelSuggestionsListHeader`.
- Restored All Apps category and grid layout to upstream defaults without restrictive column-squishing constraints.


- **Severity**: 🟠 High (glass material not applied to notification/calendar panels)
- **Status**: ⚠️ open
- **Affected File**: `src/windows-11-notification-center-styler.yml`
- **Reported Issue**: `Border#NotificationCenterBorder` and `Border#CalendarCenterBorder` targets do not match any elements in the live visual tree. As a result, the Notification panel and Calendar panel receive no `$Background` glass material — they render with the system default dark surface. No wallpaper is visible between the two panels; they appear as a continuous unstyled block instead of two separate floating glass cards.

#### Root Cause Hypothesis
The selector names `Border#NotificationCenterBorder` and `Border#CalendarCenterBorder` were inferred from naming convention rather than confirmed via visual tree inspection. The real inner-card container names in `ShellExperienceHost.exe` / `ShellHost.exe` are unknown without UWPSpy or a confirmed community theme reference.

#### Evidence
- Screenshot at commit `f841203`: Notification + calendar panels show no frosted blur, no `$BorderBrush` rim, no wallpaper gap between them — system default dark surface only.
- Outer container transparency (`Grid#NotificationCenterGrid`, `Grid#CalendarCenterGrid` → `Transparent`) result unclear without further inspection.

#### Proposed Fix
1. Use UWPSpy (on PATH) to inspect the live visual tree of `ShellHost.exe` while Notification Center is open.
2. Identify the actual `Border` or `Grid` elements serving as the notification list card and calendar card surfaces.
3. Update selectors in `src/windows-11-notification-center-styler.yml` and verify against the static gate.

---

### 2026-10-05 — NC Styler: Quick Settings Card Background Not Applying (Grid#L1Grid Miss)

- **Severity**: 🟠 High (glass material not applied to Quick Settings toggle panel)
- **Status**: ✅ resolved — commit `(pending)`
- **Affected File**: `src/windows-11-notification-center-styler.yml`
- **Reported Issue**: `Grid#L1Grid` was targeted as the Quick Settings card surface but the glass material was not applying.

#### Root Cause (Confirmed via UWPSpy — ShellHost.exe, Win11 24H2)
`Grid#L1Grid` is a **layout container**, not the card background surface. The actual card background element is `Border#RootGridBorder`, a sibling of `Grid#L1Grid` under `ControlCenter.ControlCenterView > Grid#RootGrid`.

**Note**: UWPSpy can only attach to `ShellHost.exe` on Win11 24H2. `ShellExperienceHost.exe` returns an error. The NC mod targets both processes but visual tree inspection must use `ShellHost.exe`.

#### Resolution
- Replaced `Grid#L1Grid → $Background` with approach: outer `Grid#ControlCenterRegion → $Background`, inner `Border#RootGridBorder → Transparent` (double-blur prevention).
- `Grid#L1Grid` kept as `Background:=Transparent` layout reset.

---

### 2026-10-07 — Taskbar Styler Snap Layout Clipping, Floating Background & Deduplication

- **Severity**: 🟠 High (visual clipping / layout distortion)
- **Status**: ✅ resolved — commit `(pending)`
- **Affected File**: `src/windows-11-taskbar-styler.yml`
- **Reported Issue**: Snap Layout flyout was clipping through the top border with distorted tile proportions; duplicate selectors existed for `SnapBarBorder`, `HorizontalTrackRect`, and `HorizontalDecreaseRect`; taskbar lacked floating background.

#### Root Cause
1. **Over-Broad Selector**: Global `Windows.UI.Xaml.Controls.ContentPresenter#ContentPresenter` injected `Padding=6`, `Margin=2`, and borders into every internal tile of the Snap Layout popup.
2. **Inner Snap Layout Override**: Intrusive styling on `SnapLayoutPickerControl`, `SnapLayoutControl`, and `LayoutBorder` disrupted `SnapLayout.dll` coordinate calculations.
3. **Selector Duplication**: `SnapBarBorder`, `HorizontalTrackRect`, and `HorizontalDecreaseRect` were defined multiple times.

#### Resolution
- Introduced floating taskbar background on `Taskbar.TaskbarBackground > Grid` with `Margin=8,4,8,4`, `$Background`, `$BorderBrush`, and `$CornerRadiusAlt1`.
- Sized taskbar elements (`BaseHeight=32`, `BaseWidth=34`, centered margins) to fit inside the floating background with ample clearance.
- Completely removed the overbroad `ContentPresenter#ContentPresenter` block.
- Removed intrusive inner SnapLayout rules and padding from `Border#SnapPickerBorder`, letting native layout sizing govern tiles smoothly while retaining frosted glass background and rim.
- Deduplicated all target selectors; `tools/Test-WindhawkStyles.ps1 -Path src/windows-11-taskbar-styler.yml` now passes with 0 errors and 0 warnings.

---

### 2026-10-05 — Duplicate Target Selectors in Shipped Reference Files

- **Severity**: 🟢 Low (Baseline Warning W101)
- **Status**: ⚠️ partially resolved (`windows-11-taskbar-styler.yml` cleaned; `windows-11-start-menu-styler.yml` open)
- **Reported Issue**: `windows-11-start-menu-styler.yml` and `windows-11-taskbar-styler.yml` contained duplicate target selectors.

#### Resolution
- `src/windows-11-taskbar-styler.yml` completely deduplicated (0 warnings).
- `src/windows-11-start-menu-styler.yml` scheduled for future refactor.

---

## 🛠️ Verification Commands

```powershell
# Run the complete static validation gate
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
```

---

## 🔖 Metadata

- **Project**: Windhawk Command Center Suite · tracked via milestones/sprints (no versioned releases)
- **Agent Ecosystem:** [`AGENTS.md`](./AGENTS.md) and [`.agents/`](.agents/) are tracked directly in repository git tracking.
