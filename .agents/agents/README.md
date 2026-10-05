# 👥 Agent Ecosystem Specifications (`.agents/agents/`)

This directory defines the agent team specifications for **Windhawk Command Center Suite**, organized as **primary agents** with **sub-agents** grouped by focus area.

---

## 🏗️ Structure

```
.agents/agents/
├── orchestrator/                    # Coordination (Primary)
├── engineering/                     # Style architecture & XAML mods (Primary + Sub-Agents)
│   └── sub-agents/
├── quality/                         # Static gate & live verification (Primary + Sub-Agents)
│   └── sub-agents/
└── documentation/                   # Tracking files, evidence ledgers, docs (Primary + Sub-Agents)
    └── sub-agents/
```

---

## 🔄 Focus-Area Team Structure

```mermaid
flowchart TD
    UserGoal(["User Goal / Issue"]) --> Orchestrator["Orchestrator (Primary)"]

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
    StaticGate -->|"Pass (0 errors)"| LiveCheck["Live Checklist (Desktop Verification)"]
    LiveCheck --> Done(["Milestone Resolved & Committed"])
```

---

## 📋 Agent Catalog

### Primary Agents

| Agent | Focus Area | Key Responsibilities | Specification |
|---|---|---|---|
| **Orchestrator** | Coordination | Task decomposition, roadmap execution, gate enforcement, rollback | [orchestrator/orchestrator](orchestrator/orchestrator.md) |
| **Style Architect** | Engineering | Design token integrity, Rule 03 compliance, XAML grammar, sub-agent ownership | [engineering/style-architect](engineering/style-architect.md) |
| **Verification Specialist** | Quality | Static validation gate, quality checklists, regression prevention | [quality/verification-specialist](quality/verification-specialist.md) |
| **Docs Specialist** | Documentation | Root tracking files, target evidence records, surface documentation | [documentation/docs-specialist](documentation/docs-specialist.md) |

### Sub-Agents

| Sub-Agent | Primary | Key Responsibilities | Specification |
|---|---|---|---|
| **Notification Center Specialist** | Style Architect | `src/notification-center-styler.yml`, UWP XAML visual tree | [engineering/sub-agents/notification-center-specialist](engineering/sub-agents/notification-center-specialist.md) |
| **File Explorer Specialist** | Style Architect | `src/file-explorer.styler.yml`, WinUI 3 XAML tabs, nav, command bar | [engineering/sub-agents/file-explorer-specialist](engineering/sub-agents/file-explorer-specialist.md) |
| **Visual Inspector** | Style Architect | UWPSpy diagnostics, live visual tree discovery, target verification | [engineering/sub-agents/visual-inspector](engineering/sub-agents/visual-inspector.md) |
| **Syntax Linter** | Verification Specialist | `tools/Test-WindhawkStyles.ps1` checks, constant ordering, syntax | [quality/sub-agents/syntax-linter](quality/sub-agents/syntax-linter.md) |
| **Catalog Manager** | Docs Specialist | Agent indexes, tracking file template adherence, release notes | [documentation/sub-agents/catalog-manager](documentation/sub-agents/catalog-manager.md) |
