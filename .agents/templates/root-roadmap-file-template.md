# {{ project.name }} — Suite Roadmap & Milestones

> 🗺️ **Living Source of Truth**: {{ page.description }} The project tracks progress via milestones and sprints — it does not use versioned releases.

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

## 🗺️ Repository Milestone Overview

<!--
    ... High-level summary of the entire repository history, active development, and upcoming initiatives ...
    ... Keep this table updated as milestones progress from Planned to Active to Completed ...
    ... Status states: ✅ Complete | 🚀 Active | ⏳ Planned | ⏸️ Shelved/Deferred ...
-->

| Milestone | Category | Status | Primary Focus |
| :--- | :--- | :--- | :--- |
| **M.{{N}}** | {{ category }} | {{ emoji }} {{ status.text }} | {{ primary.focus }} |
| **M.{{N}}** | {{ category }} | {{ emoji }} {{ status.text }} | {{ primary.focus }} |
| **M.{{N}}** | {{ category }} | {{ emoji }} {{ status.text }} | {{ primary.focus }} |

---

## 🚀 Active Milestones

<!--
    ... Currently active architectural milestones in flight ...
    ... Must always be placed at the top above planned and completed milestones ...
-->

### Milestone M.{{N}}: {{ milestone.title }}

```mermaid
flowchart TD
    M{{N}}_A["{{ phase.a }}"] --> M{{N}}_B["{{ phase.b }}"]
    M{{N}}_B --> M{{N}}_Gate["Static Gate: Test-WindhawkStyles.ps1"]
```

Refine and deliver the following focus areas for this milestone:
1. **{{ list.item.header }}**: {{ list.item.description }}
2. **{{ list.item.header }}**: {{ list.item.description }}
3. **{{ list.item.header }}**: {{ list.item.description }}

---

## 📋 Milestones Status

<!--
    ... Combined section for completed, shelved/deferred, and planned milestones ...
    ... Use flat bullet bodies (no nested phase breakdowns) ...
    ... Status emoji prefixes: ✅ Completed | ⏸️ Shelved / Deferred | ⏳ Planned ...
-->

### ✅ Milestone M.{{N}}: {{ milestone.title }} (Completed)

- {{ list.item }}
- {{ list.item }}

### ⏸️ Milestone M.{{N}}: {{ milestone.title }} (Shelved / Deferred)

- {{ list.item }}
- Shelved per user directive: {{ milestone.deferred.reason }}
- {{ milestone.title }} work is deferred; no styler file is maintained while deferred.

### ⏳ Milestone M.{{N}}: {{ milestone.title }}

- {{ list.item }}
- {{ list.item }}

---

## 🛠️ Verification Commands

```powershell
# Run the complete static validation gate
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
```

---

## 🔖 Metadata

- **Project**: {{ project.name }} · tracked via milestones/sprints (no versioned releases)
- **Agent Ecosystem:** [`AGENTS.md`](./AGENTS.md) and [`.agents/`](.agents/) are tracked directly in repository git tracking.
