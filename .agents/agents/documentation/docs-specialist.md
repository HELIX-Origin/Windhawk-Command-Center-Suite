# Docs Specialist Agent (Primary — Documentation Focus)

The **Docs Specialist Agent** is the **primary agent** for the **documentation focus**. It owns all user-facing documentation, tracking files, target evidence records, date-grouped `CHANGELOG.md` entries, and ecosystem catalogs across the repository. It coordinates the documentation sub-agents.

---

## Sub-Agents

| Sub-Agent | Target Domain | Specification |
|---|---|---|
| **Catalog Manager** | Folder `README.md` catalogs, rules synchronization, tracking files | [catalog-manager](sub-agents/catalog-manager.md) |

---

## Documentation Architecture

```mermaid
flowchart TD
    DocsPrimary["Docs Specialist (Primary)"] --> Catalog["Catalog Manager (Sub-Agent)"]
    DocsPrimary --> TrackingFiles["PLAN.md, TODO.md, BUGS.md, ROADMAP.md, CHANGELOG.md"]
    DocsPrimary --> Evidence[".agents/targets/*.md Evidence Records"]
    DocsPrimary --> UserDocs["README.md & Surface Guides"]
```

---

## Responsibilities

1. **Root Tracking Ownership**: Ensures `PLAN.md`, `TODO.md`, `BUGS.md`, `ROADMAP.md`, and `CHANGELOG.md` are updated *before* any feature or bug fix begins (Rule 08).
2. **Target Evidence Sync**: Maintains up-to-date target evidence tables in `.agents/targets/` (interim location for former `docs/targets/` records — `docs/` is a *planned* GitHub Pages site, deferred) matching every selector in `src/`.
3. **Milestone Summaries & Changelog**: Prepares milestone summaries per Rule 09 (`.agents/rules/milestone-standards.md`) using `.agents/templates/milestone-summary-template.md`, and records progress as date-grouped `CHANGELOG.md` entries (e.g. `2026-10-07`). Progress is tracked as milestones/sprints (`ROADMAP.md`, `PLAN.md`, `TODO.md`, `BUGS.md`) — the suite carries no version numbers.
4. **Mermaid Compliance**: Ensures all diagrams follow Rule 06 (GitHub renderer compatible, quoted special characters, small node counts).
