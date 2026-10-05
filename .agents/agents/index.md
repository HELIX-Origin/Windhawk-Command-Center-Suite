# Agent Ecosystem Catalog & Architecture

This directory defines the agent team for **Windhawk Command Center Suite**, organized as **primary agents** with **sub-agents** grouped by focus area.

---

## Active Agents Directory

### Primary Agents

| Agent | Focus Area | Core Focus | Specification |
|---|---|---|---|
| **Orchestrator** | Coordination | Task decomposition, roadmap execution, primary coordination, gating | [orchestrator/orchestrator](orchestrator/orchestrator.md) |
| **Style Architect** | Engineering | Design tokens, XAML syntax, Command Center Glass compliance | [engineering/style-architect](engineering/style-architect.md) |
| **Verification Specialist** | Quality | Static validation gate, quality checklists, regression prevention | [quality/verification-specialist](quality/verification-specialist.md) |
| **Docs Specialist** | Documentation | Root tracking files, target evidence records, user guides | [documentation/docs-specialist](documentation/docs-specialist.md) |

### Sub-Agents

| Sub-Agent | Primary | Core Focus | Specification |
|---|---|---|---|
| **Notification Center Specialist** | Style Architect | `src/notification-center-styler.yml`, UWP XAML tree | [engineering/sub-agents/notification-center-specialist](engineering/sub-agents/notification-center-specialist.md) |
| **File Explorer Specialist** | Style Architect | `src/file-explorer.styler.yml`, WinUI 3 XAML tree & Win32 boundary | [engineering/sub-agents/file-explorer-specialist](engineering/sub-agents/file-explorer-specialist.md) |
| **Visual Inspector** | Style Architect | UWPSpy diagnostics, live visual tree discovery | [engineering/sub-agents/visual-inspector](engineering/sub-agents/visual-inspector.md) |
| **Syntax Linter** | Verification Specialist | Automated static validation script enforcement | [quality/sub-agents/syntax-linter](quality/sub-agents/syntax-linter.md) |
| **Catalog Manager** | Docs Specialist | Agent indexes, ecosystem sync, release notes | [documentation/sub-agents/catalog-manager](documentation/sub-agents/catalog-manager.md) |

---

## Surface Ownership Matrix

| Surface / Styler File | Windhawk Mod | Responsible Sub-Agent | Primary Lead |
|---|---|---|---|
| `src/taskbar-customizer.yml` | `windows-11-taskbar-styler` | Shipped Reference | Style Architect |
| `src/start-menu-customizer.yml` | `windows-11-start-menu-styler` | Shipped Reference | Style Architect |
| `src/notification-center-styler.yml` | `windows-11-notification-center-styler` | Notification Center Specialist | Style Architect |
| `src/file-explorer.styler.yml` | `windows-11-file-explorer-styler` | File Explorer Specialist | Style Architect |
