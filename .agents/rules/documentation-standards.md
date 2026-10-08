# Rule 08: Documentation Standards & Ecosystem Synchronization

## Mandatory Standards

1. **Documentation Locations** — permanent documentation lives in root Markdown files, `src/extras/README.md`, and `.agents/`. The `docs/` folder is a **planned future GitHub Pages site** and must not be created until style work is complete:
   - `README.md` — user-facing: what the suite is, desktop hero preview, primary and companion mod tables, and installation guide.
   - `src/extras/README.md` — companion mods technical documentation: full configuration breakdown, themes, modules, and options for all 8 companion mods.
   - `AGENTS.md` + `.agents/` — agent operating manual, rules (Rules 00–09), domain skills, templates, and agent specs. Each `.agents/` subdirectory's `README.md` is its canonical index (`index.md` files are not used).
   - Root tracking files — `PLAN.md`, `TODO.md`, `BUGS.md`, `ROADMAP.md`, plus `CHANGELOG.md` (date/time-grouped entries, `## YYYY-MM-DD - HH:MM`; no version numbers).

2. **Synchronization Triggers** — update all affected locations in the same change when:

   | Change | Must update |
   |---|---|
   | New/changed design token or recipe | Rule 03, affected styler files' headers |
   | New/changed companion mod config | `src/extras/README.md`, `README.md`, `TODO.md` |
   | Surface status change (e.g. deferred → active, generated & verified → shipped) | Rule 01 table, `AGENTS.md`, `README.md`, `ROADMAP.md` |
   | New agent/rule/skill/template | The folder's `README.md` (its canonical index), `AGENTS.md`, `.agents/README.md` |
   | Windows update breaks a target | `BUGS.md` (with build number), `PLAN.md`, `TODO.md` |

3. **Tracking Files First**: Before starting any fix or feature, update `TODO.md` (and `BUGS.md` / `PLAN.md` / `ROADMAP.md` as applicable) using the matching `root-*-file-template`. Planned behavior is never described as shipped.

4. **Markdown Conventions**:
   - GitHub-Flavored Markdown; heading hierarchy H1 → H2 → H3.
   - Fenced code blocks with language identifiers (`yaml`, `powershell`, `xml`).
   - Mermaid diagrams follow [Rule 06](mermaid-standards.md).
   - Links between `.agents/` files use relative paths with the `.md` extension.

5. **No Personal Data**: No user names, profile paths, machine names, or emails in docs (Rule 00 §1.4).

6. **Commit Messages**: Follow [`commit-message-guide`](../templates/commit-message-guide.md).
