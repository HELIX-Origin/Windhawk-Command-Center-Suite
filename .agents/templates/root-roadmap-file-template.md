# {{ project.name }} — {{ page.title }}

> 🗺️ **Living Source of Truth**: {{ page.description }}

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
- **Universal Direct Store Links**: Every game alert, giveaway, or deal **MUST** resolve to the actual storefront page of the game.
- **Always Track Everything**: Every new feature request, enhancement, or bug report must be logged in [`BUGS.md`](./BUGS.md), [`TODO.md`](./TODO.md), and [`ROADMAP.md`](./ROADMAP.md) before execution.

---

## 🗺️ Repository Milestone Overview

<!--
    ... High-level summary of the entire repository history, active development, and upcoming initiatives ...
    ... Keep this table updated as milestones progress from Planned to Active to Completed ...
-->

| Milestone | Target Version | Category | Status | Primary Focus |
| :--- | :--- | :--- | :--- | :--- |
| **M.{{N}}** | `v{{X.Y.Z}}` | {{ category }} | {{ emoji }} {{ status.text }} | {{ primary.focus }} |
| **M.{{N}}** | `v{{X.Y.Z}}` | {{ category }} | {{ emoji }} {{ status.text }} | {{ primary.focus }} |
| **M.{{N}}** | `v{{X.Y.Z}}` | {{ category }} | {{ emoji }} {{ status.text }} | {{ primary.focus }} |

---

## 🚀 Active Milestones

<!--
    ... Currently active architectural milestones in flight ...
    ... Must always be placed at the top above planned and completed milestones ...
    ... Detailed phase breakdowns, architecture diagrams, and interface definitions ...
-->

### Milestone M.{{N}}: {{ milestone.title }}

```mermaid
{{ milestone.diagram }}
```

{{ milestone.description }}

#### 🧭 Architecture & Implementation Phases

{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}

---

## 🔮 Planned & Future Milestones

<!--
    ... Future roadmap milestones and planned initiatives ...
    ... Outlines prerequisites, structural design, and target goals ...
-->

### Milestone M.{{N}}: {{ milestone.title }}

```mermaid
{{ milestone.diagram }}
```

{{ milestone.description }}

#### 🎯 Strategic Objectives & Deliverables

{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}

---

## ✅ Completed Milestones (Historical Evolution)

<!--
    ... Historical milestones documenting major evolutionary phases of the repository ...
    ... Each milestone should include its version tag, key architectural milestones achieved, and summary ...
-->

### Milestone M.{{N}}: {{ milestone.title }} (`{{ milestone.version }}`)

```mermaid
{{ milestone.diagram }}
```

{{ milestone.description }}

#### 🏛️ Architectural Accomplishments

{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}
{{ list.item.number }}. **{{ list.item.header }}**:
    - {{ list.item.title }}: {{ list.item.description }}
        - {{ sublist.item.title }}: {{ sublist.item.description }}

---

## 🔖 Metadata

- **Project**: {{ project.name }} · **version** {{ project.version }}
- **Agent Ecosystem:** [`AGENTS`](./AGENTS) and [`.agents/`](.agents/) are tracked directly in repository git tracking.
- **Last Updated:** {{ MMM, dd yyyy }} - {{ hh:mm tt }}