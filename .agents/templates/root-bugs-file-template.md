# {{ project.name }} — {{ page.name }}

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
- **Universal Direct Store Links**: Every game alert, giveaway, or deal **MUST** resolve to the actual storefront page of the game.
- **Always Track Everything**: Every new feature request, enhancement, or bug report must be logged in [`BUGS.md`](./BUGS.md), [`TODO.md`](./TODO.md), and [`ROADMAP.md`](./ROADMAP.md) before execution.

---

## 📖 Legend

### 🚦 Status

- ⚠️ **open** — reproducible, needs fixing *(Detailed lists with possible fixes encouraged. Attempt to include steps to reproduce, expected behavior, and actual behavior. An estimate of how long it might take to fix is also helpful.)*
- 🚧 **investigating** — repro/root-cause in progress *(List of issues currently being worked on. Used for tracking active work. must reference an existing bug from the open section.)*
- 🚫 **wontfix** — accepted limitations *(features that can't be fixed at this time without significant changes or trade-offs)*
- ✅ **resolved** — verified and fixed *(moved to closed with the corresponding release version or commit)*

### 🚨 Severity

- 🔴 **Critical**: *Bugs that cause crashes or major functionality loss.*
- 🟠 **High**: *Bugs that significantly impact usability but do not crash the app.*
- 🟡 **Medium**: *Bugs that affect certain features or have minor usability issues.*
- 🟢 **Low**: *Minor bugs or visual glitches that do not significantly impact the user experience.*

---

## 🚫 Known Quirks & External Limitations (wontfix bucket)

- {{ emoji }} **{{ list.item .title}}**: {{ list.item.description }}
    - **{{ sublist.item.title }}**: {{ sublist.item.description }}
- {{ emoji }} **{{ list.item .title}}**: {{ list.item.description }}
    - **{{ sublist.item.title }}**: {{ sublist.item.description }}
- {{ emoji }} **{{ list.item .title}}**: {{ list.item.description }}
    - **{{ sublist.item.title }}**: {{ sublist.item.description }}

## 💡 Explicitly Not Bugs

- {{ emoji }} **{{ list.item .title}}**: {{ list.item.description }}
    - **{{ sublist.item.title }}**: {{ sublist.item.description }}
- {{ emoji }} **{{ list.item .title}}**: {{ list.item.description }}
    - **{{ sublist.item.title }}**: {{ sublist.item.description }}
- {{ emoji }} **{{ list.item .title}}**: {{ list.item.description }}
    - **{{ sublist.item.title }}**: {{ sublist.item.description }}

## ⚠️ Active & Open Bugs

<!--
    ... Active open bugs currently being investigated or queued for resolution ...
    ... Must always be placed at the top above resolved issues and wontfix items ...
-->

### {{ issue.date }} — {{ issue.title }}

- **Status**: {{ emoji }} {{ status }}  // e.g., Open, In Progress, Resolved 
- **Severity**: {{ emoji }} {{ severity }} ({{ category }}) // e.g., Critical, High, Medium, Low
- **Reported Issue**: "{{ short.summary }}" // e.g., Brief description of the issue

#### Expected Behavior

<!-- 
    ... Describe the expected behavior of the application when the issue is resolved ...
    ... Include any relevant screenshots or visual references if applicable ...
    ... Mention any specific conditions or configurations required for the expected behavior ...
    ... Provide any relevant links to related issues or documentation ...
-->

{{ expected.behavior }} // e.g., What the user expects to happen

#### Actual Behavior

<!--
    ... Describe the actual behavior observed when the issue occurs ...
    ... Include any relevant error messages or stack traces ...
    ... Provide screenshots if applicable ...
    ... Mention any deviations from the expected behavior ...
-->

{{ actual.behavior }} // e.g., What actually happens when the issue occurs

#### Additional Information

<!--
    ... Any additional context, logs, screenshots, or relevant information that can help in understanding the issue ...
    ... Include any relevant links to related issues or documentation ...
    ... Mention any workarounds or temporary solutions if available ...
    ... Provide any other relevant details that may assist in diagnosing or resolving the issue ...
    ... Specify the environment or configuration in which the issue occurs ...
    ... Use sublists to organize related pieces of additional information ...
    ... Provide screenshots if applicable ...
    ... Include any relevant error messages or stack traces ...
    ... Provide steps to reproduce the issue if possible ...
-->

{{ additional.information }} // e.g., Any extra context, logs, or relevant details

#### Possible Fixes

<!--
    ... Possible fixes for the issue ...
    ... List ideas for possible fixes here ...
    ... Use sublists to break down complex fixes into smaller steps ...
    ... Keep in mind, that these are only suggested fixes and may not fully resolve the issue ...
    ... Ensure that any proposed fixes are tested thoroughly before implementation ...
    ... Document any dependencies or prerequisites for the proposed fixes ...
    ... Include references to relevant documentation or resources if applicable ...
    ... Keep track of any changes made to the proposed fixes ...
    ... Update the documentation accordingly to reflect the current state of the fixes ...
-->

{{ possible.fixes }} // e.g., Suggested solutions or workarounds

---

## 🔖 Metadata

<!-- Metadata about the project and file, including project name, version, and last updated timestamp
    
    Example Metadata:
    - **Project**: HELIX-Discord-Bot **version**: 1.0.0
    - **Agent Ecosystem:** [`AGENTS`](./AGENTS) and [`.agents/`](.agents/) are tracked directly in repository git tracking.
    - **Last Updated**: Oct 05 2023 - 10:00 AM
-->


- **Project**: {{ project.name }} · **version** {{ project.version }}
- **Agent Ecosystem:** [`AGENTS`](./AGENTS) and [`.agents/`](.agents/) are tracked directly in repository git tracking.
- **Last Updated:** {{ MMM, dd yyyy }} - {{ hh:mm tt }}