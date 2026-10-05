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
- 🟠 **High**: *Bugs that significantly impact aesthetics or cause double-blur.*
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

### 2026-10-05 — NC Styler: Inner Card Selectors Not Matching (Notification + Calendar Panels)

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
3. Update selectors in `src/windows-11-notification-center-styler.yml` and `docs/targets/notification-center-styler.md`.

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

### 2026-10-05 — Duplicate Target Selectors in Shipped Reference Files

- **Severity**: 🟢 Low (Baseline Warning W101)
- **Status**: ⚠️ open (Baseline Ledger)
- **Reported Issue**: `windows-11-start-menu-styler.yml` and `windows-11-taskbar-styler.yml` contain duplicate target selectors (recorded in `tools/style-baseline.txt`).

#### Root Cause
1. **Historical Style Merging**: Previous iterative edits to the start menu and taskbar configurations added duplicate blocks for elements like `Border#AppBorder` and `SnapBarBorder`.
    - **Impact**: Later blocks silently override earlier ones without breaking functionality.
    - **Proposed Fix**: Surgical deduplication scheduled during future refactoring turns (preserving shipped visual parity per Rule 00).

---

## 🛠️ Verification Commands

```powershell
# Run the complete static validation gate
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
```

---

## 🔖 Metadata

- **Project**: Windhawk Command Center Suite · **version** 1.0.0-preview
- **Agent Ecosystem:** [`AGENTS.md`](./AGENTS.md) and [`.agents/`](.agents/) are tracked directly in repository git tracking.
