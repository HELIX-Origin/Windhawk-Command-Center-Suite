# Rule 08: Documentation Standards & Ecosystem Synchronization

## Mandatory Standards

1. **Documentation Locations & Theme Boundary**:
   - `docs/` — active GitHub Pages site (deployed from `/docs` on `main`). All root non-wiki pages (`docs/*.md`, `Start-Menu.md`, `Taskbar.md`, `Architecture.md`, etc.) strictly use our **original custom GitHub Pages site theme** (`docs/_layouts/documentation.html`, `assets/css/site.css`) and are intentionally minimal/high-level.
   - `docs/wiki/` — community and development wiki pages. The wiki folder can leverage the `just-the-docs` Jekyll theme (or dedicated deep documentation layouts), while everything outside `wiki/` relies strictly on our own custom site theme. All wiki pages must be detailed and extensive.
   - `README.md` — user-facing: what the framework is, shell architecture overview, and quick installation guide.
   - `projects/<project>/extras/README.md` — companion mods technical documentation: configuration breakdown, themes, modules, and options for companion mods.
   - `AGENTS.md` + `.agents/` — agent operating manual, rules (Rules 00–09), domain skills, templates, and agent specs. Each `.agents/` subdirectory's `README.md` is its canonical index (`index.md` files are not used).
   - Root tracking files — `PLAN.md`, `TODO.md`, `BUGS.md`, `ROADMAP.md`, plus `CHANGELOG.md` (chronological entries with milestone release tags; no semantic versioning).

2. **Synchronization Triggers** — update all affected locations in the same change when:

   | Change | Must update |
   |---|---|
   | New/changed design token or recipe | Rule 03, affected styler files' headers |
   | New/changed companion mod config | `projects/<project>/extras/README.md`, `README.md`, `TODO.md` |
   | Surface status change (e.g. deferred → active, generated & verified → shipped) | Rule 01 table, `AGENTS.md`, `README.md`, `ROADMAP.md` |
   | New agent/rule/skill/template | The folder's `README.md` (its canonical index), `AGENTS.md`, `.agents/README.md` |
   | Windows update breaks a target | `BUGS.md` (with build number), `PLAN.md`, `TODO.md` |

3. **Tracking Files First**: Before starting any fix or feature, update `TODO.md` (and `BUGS.md` / `PLAN.md` / `ROADMAP.md` as applicable) using the matching `root-*-file-template`. Planned behavior is never described as shipped.

4. **Markdown Conventions**:
   - GitHub-Flavored Markdown; heading hierarchy H1 → H2 → H3.
   - Fenced code blocks with language identifiers (`yaml`, `powershell`, `xml`).
   - Mermaid diagrams follow [Rule 06](mermaid-standards.md).
   - Links between `.agents/` files use relative paths with the `.md` extension.

5. **Complete Theme Neutrality Invariant**:
   - The documentation (`docs/`), community wiki (`docs/wiki/`), rules, and agent instructions must **never** assume that configurations or visual treatments found in `projects/` represent the focus, defaults, or purpose of the repository.
   - All documentation and wiki pages must remain **completely ignorant of specific theme projects** (e.g. Command Center). Their purpose is exclusively to explain valid XAML visual tree targets, mod capabilities, supported dependency properties, and official mod/system schemas.
   - Theme options and XAML capabilities are not limited to any user's personal themes. Never use private or project-specific themes as the source of truth, defaults, or recommendations for documentation or wiki pages.

6. **No Personal Data**: No user names, profile paths, machine names, or emails in docs (Rule 00 §1.4).

7. **Commit Messages**: Follow [`commit-message-guide`](../templates/commit-message-guide.md).
