# {{ project.name }} — Bug & Issue Tracker

> 🐛 **Living Source of Truth**: {{ page.description }}

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
- 🟠 **High**: *Bugs that significantly impact aesthetics or cause layering glitches.*
- 🟡 **Medium**: *Bugs that affect minor visual alignments or state transitions.*
- 🟢 **Low**: *Minor warnings, duplicate selectors, or non-visual syntax quirks.*

---

## 🚫 Known Quirks & External Limitations (wontfix bucket)

- {{ emoji }} **{{ list.item.title }}**: {{ list.item.description }}
    - **Resolution**: {{ sublist.item.description }}
- {{ emoji }} **{{ list.item.title }}**: {{ list.item.description }}
    - **Resolution**: {{ sublist.item.description }}

---

## 💡 Explicitly Not Bugs

- {{ emoji }} **{{ list.item.title }}**: {{ list.item.description }}
- {{ emoji }} **{{ list.item.title }}**: {{ list.item.description }}

---

## ⚠️ Active & Open Bugs

<!--
    ... Active open bugs currently being investigated or queued for resolution ...
    ... Must always be placed at the top above resolved issues and wontfix items ...
-->

### {{ issue.date }} — {{ issue.title }}

- **Severity**: {{ emoji }} {{ severity }} ({{ category }})
- **Status**: {{ emoji }} {{ status }}
- **Affected File**: `src/{{ styler.file }}`
- **Reported Issue**: {{ short.summary }}

#### Root Cause

<!--
    ... Root cause analysis for the issue ...
    ... Resolved entries add a #### Resolution subsection with the applied fix ...
    ... Unresolved entries add #### Evidence and/or #### Proposed Fix subsections as needed ...
-->

{{ root.cause }}

#### Resolution

- {{ list.item }}
- {{ list.item }}

<!-- Variant subsections (use as applicable):
#### Evidence
- {{ evidence.item }}

#### Proposed Fix
1. {{ fix.step }}
-->

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
