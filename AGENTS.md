# AGENTS

This document is the central entry point and operating manual for all AI agents, coding assistants, and automated agents working on **Windhawk Command Center Suite**.

> **Tracking Files**: `PLAN.md` (current session plan), `TODO.md` (task checklist), `BUGS.md` (bug & issue tracker), and `ROADMAP.md` (suite milestones) are repository-tracked planning files that hold active workstream state. All architecture rules, standards, and permanent documentation reside in `AGENTS.md`, `.agents/`, and `docs/`.
>
> **Bug & Issue Tracking**: Active bug/problem tracking lives in the `BUGS.md` tracker (only still-open bugs are listed; closed or superseded entries are removed). `AGENTS.md` is the agent ecosystem entry point, not a tracker.

---

## Project

**Windhawk Command Center Suite** is a unified, cohesive dark/light frosted glass styling theme for Windows 11 built for specific Windhawk styler mods.

### Supported Runtime Mods

The suite targets exactly **four** official Windhawk styler mods (one YAML configuration file each in `src/`):

| Styler File | Windhawk Mod ID | Target Process | Framework | Status |
|---|---|---|---|---|
| `src/windows-11-taskbar-styler.yml` | `windows-11-taskbar-styler` | `explorer.exe` | WinUI 3 / XAML | ✅ Shipped reference |
| `src/windows-11-start-menu-styler.yml` | `windows-11-start-menu-styler` | `StartMenuExperienceHost.exe` | UWP / WinUI 2 | ✅ Shipped reference |
| `src/windows-11-notification-center-styler.yml` | `windows-11-notification-center-styler` | `ShellExperienceHost.exe` / `ShellHost.exe` | UWP `Windows.UI.Xaml` | 🧪 Generated (Ready for verification) |
| `src/windows-11-file-explorer-styler.yml` | `windows-11-file-explorer-styler` | `explorer.exe` | WinUI 3 `Microsoft.UI.Xaml` | 🧪 Generated (Ready for verification) |

### Core Design Philosophy: "Command Center Glass"
- **Unified Frosted Blur**: Single-layer `WindhawkBlur` (amount 20, tinting via `{ThemeResource SystemChromeMediumColor}`) across all surfaces.
- **Top-Lit Glass Rim**: Signature vertical gradient border (`LinearGradientBrush #60808080 → #50404040 → #40808080`, thickness `0.3,1,0.3,1`).
- **Harmonized Radii Scale**: XL (`35`) for top-level panels, L (`25`) for search pills, M (`15`) for groups, S (`10`) for tiles/buttons, XS (`6`) for context menus.
- **Zero Double-Blur**: Inner wrapper containers reset to transparent to eliminate muddy stacking.

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
    Engineering --> FE["File Explorer Specialist (Sub)"]
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
| **Notification Center Specialist** | Engineering (Sub) | `src/notification-center-styler.yml`, UWP visual tree, Quick Settings, calendar, toasts | [notification-center-specialist](.agents/agents/engineering/sub-agents/notification-center-specialist.md) |
| **File Explorer Specialist** | Engineering (Sub) | `src/file-explorer.styler.yml`, WinUI 3 tabs, nav, command bar, Win32 file list boundary | [file-explorer-specialist](.agents/agents/engineering/sub-agents/file-explorer-specialist.md) |
| **Visual Inspector** | Engineering (Sub) | UWPSpy diagnostics, visual tree discovery, target evidence ledger management | [visual-inspector](.agents/agents/engineering/sub-agents/visual-inspector.md) |
| **Verification Specialist** | Quality (Primary) | Static validation gate, quality checklists, regression prevention | [verification-specialist](.agents/agents/quality/verification-specialist.md) |
| **Syntax Linter** | Quality (Sub) | `tools/Test-WindhawkStyles.ps1` checks, constant ordering, syntax hygiene | [syntax-linter](.agents/agents/quality/sub-agents/syntax-linter.md) |
| **Docs Specialist** | Documentation (Primary) | Root tracking files, target evidence records, surface documentation | [docs-specialist](.agents/agents/documentation/docs-specialist.md) |
| **Catalog Manager** | Documentation (Sub) | Agent indexes, tracking file template adherence, release notes | [catalog-manager](.agents/agents/documentation/sub-agents/catalog-manager.md) |

---

## Standard Agent Execution Capabilities

All agents have access to and must leverage the repository's standard execution toolset:
1. **File System Operations**: Read, write, and patch YAML and Markdown files with surgical precision.
2. **Static Gate Execution**: Run the automated syntax and token validation tool:
   ```powershell
   pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
   ```
3. **Live Checklist Preparation**: Generate comprehensive desktop verification checklists using `.agents/templates/live-verification-checklist.md`.
4. **Target Evidence Logging**: Record visual tree sources and inspection status in `docs/targets/`.

---

## Agent Rules (`.agents/rules/`)

All agent actions are bound by `.agents/rules/`:
- **Rule 00 (`agent-safety-compliance`)**: Safety invariants, zero irreversible damage, no unauthorized Explorer restarts.
- **Rule 01 (`zero-unsolicited-injection`)**: Runtime boundary — exactly four styler mods; no unapproved packages or tools.
- **Rule 02 (`windhawk-styler-syntax`)**: YAML and XAML syntax standards, quoting, constant declaration order.
- **Rule 03 (`design-language-standards`)**: Canonical "Command Center Glass" tokens, materials, and radius scales.
- **Rule 04 (`target-evidence-protocol`)**: Sourced selectors only (UWPSpy / official mod themes). No guessing.
- **Rule 05 (`surface-scope-standards`)**: Process targets (`explorer.exe` vs `ShellExperienceHost.exe`), WinUI 3 vs UWP.
- **Rule 06 (`mermaid-standards`)**: GitHub-compatible Mermaid diagrams, quoted special characters, max 12 nodes.
- **Rule 07 (`verification-standards`)**: Mandatory static gate (`tools/Test-WindhawkStyles.ps1`) and user live checklist.
- **Rule 08 (`documentation-standards`)**: Docs locations, tracking file rules, sync triggers.
- **Rule 09 (`release-standards`)**: Suite-level SemVer, compatibility ledger, and structured release notes.
