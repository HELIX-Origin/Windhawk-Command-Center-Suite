# AGENTS

This document is the central entry point and operating manual for all AI agents, coding assistants, and automated agents working on **Windhawk Command Center Suite**.

> **Tracking Files**: `PLAN.md` (current sprint plan), `TODO.md` (task checklist), `BUGS.md` (bug & issue tracker), `ROADMAP.md` (suite milestones), and `CHANGELOG.md` (date/time-grouped history) are repository-tracked planning files that hold active workstream state. All architecture rules, standards, and permanent documentation reside in root Markdown files, `src/extras/README.md`, `AGENTS.md`, and `.agents/`. A `docs/` folder is planned for a future GitHub Pages site but must not be created until the style work is complete.
>
> **Bug & Issue Tracking**: Active bug/problem tracking lives in the `BUGS.md` tracker (only still-open bugs are listed; closed or superseded entries are removed). `AGENTS.md` is the agent ecosystem entry point, not a tracker.

---

## Project

**Windhawk Command Center Suite** is a unified, cohesive dark/light frosted glass styling theme for Windows 11 built for specific Windhawk styler mods.

### Supported Runtime Mods

The suite is approved for exactly **four** official Windhawk styler mods — **three active styler files** exist in `src/`, and File Explorer is deferred:

| Styler File | Windhawk Mod ID | Target Process | Framework | Status |
|---|---|---|---|---|
| `src/windows-11-taskbar-styler.yml` | `windows-11-taskbar-styler` | `explorer.exe` | WinUI 3 / XAML | ✅ Shipped reference |
| `src/windows-11-start-menu-styler.yml` | `windows-11-start-menu-styler` | `StartMenuExperienceHost.exe` | UWP / WinUI 2 | ✅ Shipped reference |
| `src/windows-11-notification-center-styler.yml` | `windows-11-notification-center-styler` | `ShellExperienceHost.exe` / `ShellHost.exe` | UWP `Windows.UI.Xaml` | ✅ Generated & verified (polish active — M.02b / W.04) |
| *— (no styler file)* | `windows-11-file-explorer-styler` | `explorer.exe` | WinUI 3 `Microsoft.UI.Xaml` | ⏸️ Deferred (ROADMAP M.03) — no real benefit yet; existing styles too similar |

### Core Design Philosophy: "Command Center Glass"
- **Unified Frosted Blur**: Consistent `WindhawkBlur` (amount 20, tinting via `{ThemeResource SystemChromeMediumColor}`) providing the base glass surface across all shells.
- **Top-Lit Glass Rim**: Signature vertical gradient border (`LinearGradientBrush #60808080 → #50404040 → #40808080`, thickness `0.3,1,0.3,1`).
- **Harmonized Radii Scale**: XL (`35`) for top-level panels, L (`25`) for search pills, M (`15`) for groups, S (`10`) for tiles/buttons, XS (`6`) for context menus.
- **Intentional Glass Layering**: Foundation frosted glass surfaces host layered glassy cards, pills, and tiles to establish rich depth, contrast, and visual hierarchy; native opaque system fills and hard drop shadows are collapsed.

---

## Agent Ecosystem Architecture & Orchestration

The repository operates on a multi-agent team model where agents collaborate, decompose tasks, enforce evidence-backed selectors, and validate against static and live quality gates.

```mermaid
flowchart TD
    UserGoal(["User Request / Directive"]) --> Orchestrator["Orchestrator Agent (Primary)"]

    Orchestrator --> Engineering["Style Architect (Primary)"]
    Orchestrator --> Quality["Verification Specialist (Primary)"]
    Orchestrator --> Documentation["Docs Specialist (Primary)"]

    Engineering --> NC["Notification Center Specialist (Sub)"]
    Engineering --> FE["File Explorer Specialist (Sub) (Deferred)"]
    Engineering --> Inspect["Visual Inspector (Sub)"]

    Quality --> Linter["Syntax Linter (Sub)"]
    Documentation --> Catalog["Catalog Manager (Sub)"]

    Engineering --> StaticGate{"Static Gate: Test-WindhawkStyles.ps1"}
    Quality --> StaticGate

    StaticGate -->|"Failure"| Rollback["Diagnose & Fix Loop"]
    Rollback --> Engineering

    StaticGate -->|"Pass: 0 errors"| LiveGate["Live Checklist (User Desktop Verification)"]
    LiveGate -->|"Confirmed"| DocsSync["Tracking & Docs Sync"]
    DocsSync --> Complete(["Sprint / Milestone Resolved"])
```

---

## Agent Team Catalog & Capabilities

Agents are organized as **primary agents with sub-agents** grouped by focus area under `.agents/agents/` (see [`.agents/agents/README.md`](.agents/agents/README.md)).

| Agent | Focus Area | Key Responsibilities | Specification File |
|---|---|---|---|
| **Orchestrator** | Coordination (Primary) | Task decomposition, roadmap execution, primary coordination, gating, rollback | [orchestrator](.agents/agents/orchestrator/orchestrator.md) |
| **Style Architect** | Engineering (Primary) | Design token integrity, Rule 03 compliance, XAML grammar, sub-agent ownership | [style-architect](.agents/agents/engineering/style-architect.md) |
| **Notification Center Specialist** | Engineering (Sub) | `src/windows-11-notification-center-styler.yml`, UWP visual tree, Quick Settings, calendar, toasts | [notification-center-specialist](.agents/agents/engineering/sub-agents/notification-center-specialist.md) |
| **File Explorer Specialist** | Engineering (Sub) | ⏸️ Deferred (ROADMAP M.03) — dormant domain reference for a future `src/windows-11-file-explorer-styler.yml` | [file-explorer-specialist](.agents/agents/engineering/sub-agents/file-explorer-specialist.md) |
| **Visual Inspector** | Engineering (Sub) | UWPSpy diagnostics, visual tree discovery, target evidence ledger management | [visual-inspector](.agents/agents/engineering/sub-agents/visual-inspector.md) |
| **Verification Specialist** | Quality (Primary) | Static validation gate, quality checklists, regression prevention | [verification-specialist](.agents/agents/quality/verification-specialist.md) |
| **Syntax Linter** | Quality (Sub) | `tools/Test-WindhawkStyles.ps1` checks, constant ordering, syntax hygiene | [syntax-linter](.agents/agents/quality/sub-agents/syntax-linter.md) |
| **Docs Specialist** | Documentation (Primary) | Root tracking files, target evidence records, surface documentation | [docs-specialist](.agents/agents/documentation/docs-specialist.md) |
| **Catalog Manager** | Documentation (Sub) | Folder README catalogs, tracking file template adherence, milestone summaries | [catalog-manager](.agents/agents/documentation/sub-agents/catalog-manager.md) |

---

## Standard Agent Execution Capabilities

All agents have access to and must leverage the repository's standard execution toolset:
1. **File System Operations**: Read, write, and patch YAML and Markdown files with surgical precision.
2. **Static Gate Execution**: Run the automated syntax and token validation tool:
   ```powershell
   pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
   ```
3. **Live Checklist Preparation**: Generate comprehensive desktop verification checklists using `.agents/templates/live-verification-checklist.md`.
4. **Target Evidence Sourcing**: Source all target selectors from official Windhawk mod source code, settings schemas, and community theme references without manual UWPSpy inspection burden.
5. **Headless Visual Tree Inspection**: Programmatically dump the live UWP / WinUI 3 trees of the seven approved shell processes (read-only by default — no screenshots ever; opening a surface or injecting input only behind explicit per-run user consent, Rule 00; `LockApp.exe` / the lock screen is never automated) using:
   ```powershell
   python tools/inspect_xaml.py --list
   python tools/inspect_xaml.py -p ShellHost.exe -f "NotificationCenter"
   ```
   See [`tools/README.md`](tools/README.md) for options and the enforced read-only contract.

---

## Agent Rules (`.agents/rules/`)

All agent actions are bound by `.agents/rules/`:
- **Rule 00 (`agent-safety-compliance`)**: Safety invariants, zero irreversible damage, no unauthorized Explorer restarts.
- **Rule 01 (`zero-unsolicited-injection`)**: Runtime boundary — four approved styler mods (three active files; File Explorer deferred); no unapproved packages or tools.
- **Rule 02 (`windhawk-styler-syntax`)**: YAML and XAML syntax standards, quoting, constant declaration order.
- **Rule 03 (`design-language-standards`)**: Canonical "Command Center Glass" tokens, materials, and radius scales.
- **Rule 04 (`target-evidence-protocol`)**: Sourced selectors only (official mod themes & source code). No guessing.
- **Rule 05 (`surface-scope-standards`)**: Process targets (`explorer.exe` vs `ShellExperienceHost.exe`), WinUI 3 vs UWP.
- **Rule 06 (`mermaid-standards`)**: GitHub-compatible Mermaid diagrams, quoted special characters, max 12 nodes.
- **Rule 07 (`verification-standards`)**: Mandatory static gate (`tools/Test-WindhawkStyles.ps1`) and user live checklist.
- **Rule 08 (`documentation-standards`)**: Documentation architecture (root Markdown files, `src/extras/README.md`, and `.agents/` ecosystem; folder `README.md` files are the canonical indexes — no `index.md` files; `docs/` is a planned future GitHub Pages site, deferred until style work is complete).
- **Rule 09 (`milestone-standards`)**: Milestone/sprint tracking, per-surface compatibility record, milestone summaries, and the completion gate — the suite uses no versioned releases.
