# Rule 08: Documentation Standards & Ecosystem Synchronization

## Mandatory Standards

1. **Documentation Locations**:
   - `README.md` — user-facing: what the suite is, screenshots, how to apply each style.
   - `docs/` — technical documentation: per-surface guides (`docs/surfaces/`), target evidence tables (`docs/targets/`), design token reference.
   - `AGENTS.md` + `.agents/` — agent operating manual, rules, skills, templates.
   - Root tracking files — `PLAN.md`, `TODO.md`, `BUGS.md`, `ROADMAP.md`, `CHANGELOG.md`.

2. **Synchronization Triggers** — update all affected locations in the same change when:

   | Change | Must update |
   |---|---|
   | New/changed design token or recipe | Rule 03, `docs/design-tokens.md`, affected styler files' headers |
   | New/changed target | `docs/targets/<file>.md` evidence table |
   | Surface status change (scaffold → shipped) | Rule 01 table, `AGENTS.md`, `README.md`, `ROADMAP.md`, `CHANGELOG.md` |
   | New agent/rule/skill/template | The folder's `README.md` **and** `index.md`, `AGENTS.md`, `.agents/README.md` |
   | Windows update breaks a target | `BUGS.md` (with build number), evidence table status |

3. **Tracking Files First**: Before starting any fix or feature, update `TODO.md` (and `BUGS.md` / `PLAN.md` / `ROADMAP.md` as applicable) using the matching `root-*-file-template`. Planned behavior is never described as shipped.

4. **Markdown Conventions**:
   - GitHub-Flavored Markdown; heading hierarchy H1 → H2 → H3.
   - Fenced code blocks with language identifiers (`yaml`, `powershell`, `xml`).
   - Mermaid diagrams follow [Rule 06](mermaid-standards.md).
   - Links between `.agents/` files use relative paths with the `.md` extension.

5. **No Personal Data**: No user names, profile paths, machine names, or emails in docs (Rule 00 §1.4).

6. **Commit Messages**: Follow [`commit-message-guide`](../templates/commit-message-guide.md).
