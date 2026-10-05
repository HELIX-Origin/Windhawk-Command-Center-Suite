# Rule 09: Semantic Versioning & Release Standards

## 1. Suite Versioning

The suite carries **one** version for the whole set, `MAJOR.MINOR.PATCH`, recorded in `CHANGELOG.md` and the `README.md` badge.

| Bump | When | Examples |
|---|---|---|
| **MAJOR** | Design-language change that alters the look of every surface, or a token rename users' forks would break on | New material default, new radius scale, token-name unification |
| **MINOR** | A surface ships or gains a new styled region | Notification Center ships; File Explorer gains tab styling |
| **PATCH** | Fixes with no intended visual change, or repairs after a Windows update | Repair a selector broken by build 26100.x; remove a duplicate target |

Pre-release surfaces are labelled `-preview` in `CHANGELOG.md` (e.g. `1.1.0-preview.1`) until the user completes the live checklist.

## 2. Per-Surface Compatibility Record

Each release lists, per styler file: the Windhawk mod version it was verified against and the Windows build(s) it was confirmed on. Unverified combinations are written as **unverified**, never omitted.

## 3. Release Notes

Use [`release-notes-template`](../templates/release-notes-template.md): emoji section headers, per-surface changes, compatibility table, apply/upgrade steps, known issues linked to `BUGS.md`.

## 4. Release Gate

1. Static gate passes with zero errors (Rule 07 §1).
2. Every surface changed in the release has a completed live checklist.
3. `CHANGELOG.md`, `README.md`, `ROADMAP.md`, and Rule 01's status table agree on surface status.
