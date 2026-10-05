# Windhawk Command Center Suite — Task Checklist & Workstream Tracking

> 📋 **Living Source of Truth**: Active workstream checklist for Windhawk Command Center Suite theming, agent ecosystem governance, and quality verification.

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

## 🔥 Active Workstreams

### 🤖 Workstream W.01: Agent Ecosystem Foundation & Governance Architecture

```mermaid
flowchart TD
    W1_Req["User Directive: Build Agent Ecosystem First"] --> W1_Rules["Mandatory Rules (Rules 00-09)"]
    W1_Rules --> W1_Agents["Focus-Area Agent Specs & Sub-Agents"]
    W1_Agents --> W1_Skills["Domain Skills & Surface Guides"]
    W1_Skills --> W1_Templates["Governance & Blueprint Templates"]
    W1_Templates --> W1_Gate["Static Gate: Test-WindhawkStyles.ps1"]
    W1_Gate -->|"Pass (0 errors)"| W1_Ready["Ecosystem Verified - Ready for Theming"]
```

Build the comprehensive, production-grade AI agent ecosystem modeled after the multi-agent patterns in `D:\Projects`, complete with mandatory rules, focus-area agent specifications, domain skills, governance templates, static validation gates, and tracking infrastructure.

**Locked user directives:**

- "The file-explorer and notification-center styles need to be built. that is our plan for this project. but we need our agents ecosystem first so we don't mess up."
- "This repository's purpose will be for maintaining my Command Center suite for the following Windhawk mods: Windows 11 Notification Center Styler, Windows 11 Start Menu Styler, Windows 11 Taskbar Styler, Windows 11 File Explorer Styler."
- "I also have UWPSpy added to system path. However, I would prefer not having to work with it myself since I have poor eyesight. So if it is needed, it will be used, but if you are able to work without it, I would prefer that."
- "Look at the start-menu-styler.yml and taskbar-styler.yml files to know what the style I am going for is. Note, these are Windhawk styles for specific Windhawk mods. So your first step MUST be to build a detailed and extensive agents ecosystem matching the structure used in my other projects located in D:\Projects. Until that is built and completed, we don't generate the yml code at all."
- "Due to File Explorer limitations, we won't be able to provide the transparent main bg without heavy Windows modification. That is something we want to avoid. So we will have to improvise and find a command center style for File Explorer that doesn't require us to make certain elements invisible or hidden."
- "We also want to avoid using Translucent Windows, since it causes issues with some programs. So all of our styles need to use methods that don't require the TranslucentWindows mod to work."

**Implementation checklist:**

- [x] Survey existing agent ecosystem architectures across `D:\Projects` (`HELIX-Discord-Bot`, `Magick-Studio`, `NH-Reader`, `Universal-Game-Launcher`).
- [x] Research Windhawk mod engines, settings keys, target selectors, and XAML frameworks via official repositories (`ramensoftware/windhawk-mods`).
- [x] Establish Mandatory Agent Rules (`.agents/rules/`):
    - [x] Rule 00: Agent Safety, Instruction Compliance & Damage Prevention (`agent-safety-compliance.md`).
    - [x] Rule 01: Dependency, Mod & Asset Approval (Zero Unsolicited Injection) (`zero-unsolicited-injection.md`).
    - [x] Rule 02: Windhawk Styler YAML & XAML Syntax Standards (`windhawk-styler-syntax.md`).
    - [x] Rule 03: Suite Design Language — "Command Center Glass" (`design-language-standards.md`).
    - [x] Rule 04: Target Evidence Protocol (No Guessed Selectors) & Accessibility Accommodations (`target-evidence-protocol.md`).
    - [x] Rule 05: Surface Scope, Mod Capabilities & Invariants (`surface-scope-standards.md`).
    - [x] Rule 06: GitHub-Flavored Mermaid & Diagram Standards (`mermaid-standards.md`).
    - [x] Rule 07: Verification Standards (Static Gate + Live Checklist) (`verification-standards.md`).
    - [x] Rule 08: Documentation Standards & Ecosystem Synchronization (`documentation-standards.md`).
    - [x] Rule 09: Semantic Versioning & Release Standards (`release-standards.md`).
    - [x] Rules index and catalog (`index.md`, `README.md`).
- [x] Establish Engineering Governance Templates (`.agents/templates/`):
    - [x] Styler Theme Blueprint Template (`styler-theme-template.md`).
    - [x] Target Evidence Ledger Template (`target-evidence-template.md`).
    - [x] Live Desktop Verification Checklist Template (`live-verification-checklist.md`).
    - [x] Commit Message & PR Title Guide (`commit-message-guide.md`).
    - [x] Release Notes Template (`release-notes-template.md`).
    - [x] Root Tracking Templates (`root-plan-file-template.md`, `root-todo-file-template.md`, `root-bugs-file-template.md`, `root-roadmap-file-template.md`).
    - [x] Templates index and catalog (`index.md`, `README.md`).
- [x] Establish Domain Skills Guides (`.agents/skills/`):
    - [x] Windhawk Styler Engineering (`windhawk-styler-engineering.md`).
    - [x] Glass Material & Chrome Recipes (`glass-material-recipes.md`).
    - [x] Notification Center Theming (`notification-center-theming.md`).
    - [x] File Explorer Theming (`file-explorer-theming.md`).
    - [x] Live Visual Inspection (`live-visual-inspection.md`).
    - [x] Skills index and catalog (`index.md`, `README.md`).
- [x] Establish Focus-Area Agent Specifications (`.agents/agents/`):
    - [x] Orchestrator Primary Agent (`orchestrator/orchestrator.md`).
    - [x] Style Architect Primary Agent (`engineering/style-architect.md`).
        - [x] Notification Center Specialist Sub-Agent (`engineering/sub-agents/notification-center-specialist.md`).
        - [x] File Explorer Specialist Sub-Agent (`engineering/sub-agents/file-explorer-specialist.md`).
        - [x] Visual Inspector Sub-Agent (`engineering/sub-agents/visual-inspector.md`).
    - [x] Verification Specialist Primary Agent (`quality/verification-specialist.md`).
        - [x] Syntax Linter Sub-Agent (`quality/sub-agents/syntax-linter.md`).
    - [x] Docs Specialist Primary Agent (`documentation/docs-specialist.md`).
        - [x] Catalog Manager Sub-Agent (`documentation/sub-agents/catalog-manager.md`).
    - [x] Agent team catalog and index (`index.md`, `README.md`).
- [x] Implement Static Validation Tooling (`tools/Test-WindhawkStyles.ps1` & `tools/style-baseline.txt`).
- [x] Compile Sourced Target Evidence Ledgers in `docs/targets/`:
    - [x] Notification Center evidence ledger (`docs/targets/notification-center-styler.md`).
    - [x] File Explorer evidence ledger (`docs/targets/file-explorer.styler.md`).
- [x] Instantiate Central Operating Manual (`AGENTS.md`) and Root Tracking Ledgers (`TODO.md`, `PLAN.md`, `BUGS.md`, `ROADMAP.md`, `README.md`).

---

## 📋 Upcoming Workstreams

### 🔔 Workstream W.02: Windows 11 Notification Center Styler Generation

```mermaid
flowchart TD
    W2_Tokens["Extract Rule 03 Tokens"] --> W2_Panels["NC & Calendar Glass Panels"]
    W2_Panels --> W2_QuickSettings["Quick Settings Toggles & Sliders"]
    W2_QuickSettings --> W2_Toasts["Rounded Toast Cards & Jump Lists"]
    W2_Toasts --> W2_Validate["Test-WindhawkStyles.ps1 Validation"]
    W2_Validate --> W2_Handoff["Desktop Verification Handoff"]
```

Implement the full Command Center Glass theme for `src/windows-11-notification-center-styler.yml` targeting the `windows-11-notification-center-styler` mod.

**Locked user directives:**

- "The file-explorer and notification-center styles need to be built. that is our plan for this project."
- "Look at the start-menu-styler.yml and taskbar-styler.yml files to know what the style I am going for is."
- "Until the agents ecosystem is built and completed, we don't generate the yml code at all."

**Implementation checklist:**

- [x] Complete `src/windows-11-notification-center-styler.yml` with canonical Rule 03 tokens and materials.
- [x] Implement glass styling and rim borders on `Grid#NotificationCenterGrid` and `Grid#CalendarCenterGrid`.
- [x] Collapse native acrylic borders and double-shadows (`Border#CalendarHeaderMinimizedOverlay`, `Shadow:=`).
- [x] Style Quick Actions grid (`Grid#L1Grid > Border`, `PaginatedToggleButton`, `SplitL2Button`).
- [x] Implement styled volume and brightness sliders (`Rectangle#HorizontalTrackRect`, `Rectangle#HorizontalDecreaseRect`).
- [x] Style Media Transport controls (`Grid#MediaTransportControlsRegion`, thumbnail art, transport buttons).
- [x] Style notification popup toasts and taskbar jump lists (`Border#ToastBackgroundBorder`, `Border#JumpListRestyledAcrylic`).
- [x] Validate with `tools/Test-WindhawkStyles.ps1` (0 errors, 0 warnings).
- [x] Complete live desktop verification checklist with user (rebased on Matter selectors, ElementBackground, compact media, hover borders).

---

### 📁 Workstream W.03: Windows 11 File Explorer Styler Generation (Shelved / Deferred)

> ⏸️ **Status: Shelved / Deferred**: User evaluated live visual results and decided to drop File Explorer styling for now. Without intrusive third-party translucency injectors (like TranslucentWindows) which affect the entire OS, File Explorer cannot achieve a cohesive glass appearance that matches the suite.

```mermaid
flowchart TD
    W3_Native["Keep Native Explorer Frame"] --> W3_Eval["Visual Evaluation with User"]
    W3_Eval --> W3_Shelve["Shelved / Deferred per User Directive"]
```

Implement the Command Center Glass theme for `src/windows-11-file-explorer-styler.yml` targeting the `windows-11-file-explorer-styler` mod, adhering strictly to the Safe Glass Chrome principle.

**Locked user directives:**

- "The file-explorer and notification-center styles need to be built. that is our plan for this project."
- "Look at the start-menu-styler.yml and taskbar-styler.yml files to know what the style I am going for is."
- "Due to File Explorer limitations, we won't be able to provide the transparent main bg without heavy Windows modification. That is something we want to avoid. So we will have to improvise and find a command center style for File Explorer that doesn't require us to make certain elements invisible or hidden."
- "We also want to avoid using Translucent Windows, since it causes issues with some programs. So all of our styles need to use methods that don't require the TranslucentWindows mod to work."

**Implementation checklist:**

- [x] Implement canonical Rule 03 tokens in `src/windows-11-file-explorer-styler.yml` (materials, rim gradients, radii scale).
- [x] Preserve the native Explorer window frame and file list (avoid heavy/unstable Windows modifications).
- [x] Ensure **zero** structural UI elements are made invisible or hidden (`Visibility=1` forbidden on functional controls).
- [x] Style tab strip, active tab, inactive tab, and "+" button (`FileExplorerExtensions.FileExplorerTabControl`, `TabViewItem`) as floating glass tabs.
- [x] Style navigation bar and history buttons (`NavigationBarControl`, `AppBarButton#backButton`).
- [x] Style address bar and search pill (`Grid#FileExplorerAddressBarGrid`, `AutoSuggestBox#FileExplorerSearchBox`) with rounded Command Center pill borders (`$CornerRadiusAlt1` / `$CornerRadiusAlt2`).
- [x] Style modern command bar row and action buttons (`Grid#CommandBarControlRootGrid`, `AppBarButton`) with subtle glass hover/press states.
- [x] Style modern context menus and flyouts (`CommandBarOverflowPresenter`, `CommandBarFlyoutCommandBar`) with frosted glass and rim highlight.
- [x] Validate with `tools/Test-WindhawkStyles.ps1` (0 errors, 0 warnings).
- [ ] Complete live desktop verification checklist with user.

---

## ✅ Completed Workstreams

### ✅ Workstream W.01: Agent Ecosystem Foundation & Governance Architecture
- Complete AI agent ecosystem ([`.agents/`](.agents/)) with Rules 00–09, Domain Skills, Agent Roles, and Templates.
- Sourced target evidence records ([`docs/targets/`](docs/targets/)).
- Automated static validation gate ([`tools/Test-WindhawkStyles.ps1`](tools/Test-WindhawkStyles.ps1)) and baseline tracking.
- Central Operating Manual ([`AGENTS.md`](AGENTS.md)) and root tracking ledgers ([`TODO.md`](TODO.md), [`PLAN.md`](PLAN.md), [`BUGS.md`](BUGS.md), [`ROADMAP.md`](ROADMAP.md), [`README.md`](README.md)).
- Remote GitHub repository initialized and synchronized at `https://github.com/HELIX-Origin/Windhawk-Command-Center-Suite`.

---

## 🛠️ Verification Commands

```powershell
# Run the complete static validation gate
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1

# Run validation on a specific styler file
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1 -Path src/windows-11-notification-center-styler.yml
```

---

## 🔖 Metadata

- **Project**: Windhawk Command Center Suite · **version** 1.0.0-preview
- **Agent Ecosystem:** [`AGENTS.md`](./AGENTS.md) and [`.agents/`](.agents/) are tracked directly in repository git tracking.
