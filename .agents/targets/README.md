# Target Evidence Records (`.agents/targets/`)

Per-styler-file selector evidence ledgers built from [`target-evidence-template`](../templates/target-evidence-template.md) and governed by **Rule 04 ([`target-evidence-protocol`](../rules/target-evidence-protocol.md))**.

> [!IMPORTANT]
> **Interim location**: `.agents/targets/` is the interim home for evidence records. The canonical future home is `docs/targets/` under the planned **GitHub Pages `docs/` site**, which is deferred until the style work is complete. Records will be migrated there when the site is built.

## Records

| Record | Styler File | Status |
|---|---|---|
| [notification-center-styler](notification-center-styler.md) | `src/windows-11-notification-center-styler.yml` | ✅ Active — Generated & verified |
| [file-explorer-styler](file-explorer-styler.md) | *— (no styler file)* | ⏸️ Deferred (ROADMAP M.03) — dormant reference |

## Conventions

- One record per styler file, named after the file.
- Every selector must trace to a documented evidence tier (T1–T5) — no guessing (Rule 04).
- Source selectors from official Windhawk mod source code, settings schemas, and community themes first; manual UWPSpy inspection is avoided per the accessibility invariant.
- When the future `docs/` site is created, move this directory to `docs/targets/` and update Rule 04/Rule 08 references.
