# Docs Specialist Agent (Primary — Documentation Focus)

The **Docs Specialist Agent** is the **primary agent** for the **documentation focus**. It owns all user-facing documentation, tracking files, target evidence records, changelogs, and ecosystem catalogs across the repository. It coordinates the documentation sub-agents.

---

## Sub-Agents

| Sub-Agent | Target Domain | Specification |
|---|---|---|
| **Catalog Manager** | Agent indexes, rules synchronization, tracking files | [catalog-manager](sub-agents/catalog-manager.md) |

---

## Documentation Architecture

```mermaid
flowchart TD
    DocsPrimary["Docs Specialist (Primary)"] --> Catalog["Catalog Manager (Sub-Agent)"]
    DocsPrimary --> TrackingFiles["PLAN.md, TODO.md, BUGS.md, ROADMAP.md"]
    DocsPrimary --> Evidence["docs/targets/*.md Evidence Records"]
    DocsPrimary --> UserDocs["README.md & Surface Guides"]
```

---

## Responsibilities

1. **Root Tracking Ownership**: Ensures `PLAN.md`, `TODO.md`, `BUGS.md`, and `ROADMAP.md` are updated *before* any feature or bug fix begins (Rule 08).
2. **Target Evidence Sync**: Maintains up-to-date target evidence tables in `docs/targets/` matching every selector in `src/`.
3. **Release Management**: Prepares structured release notes adhering to SemVer rules (Rule 09) and the release notes template.
4. **Mermaid Compliance**: Ensures all diagrams follow Rule 06 (GitHub renderer compatible, quoted special characters, small node counts).
