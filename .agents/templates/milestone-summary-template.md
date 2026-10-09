# 📌 Milestone Summary & Release Notes Template

Use this template when a milestone of a **Windhawk Theme** completes. Releases use milestone identifiers as release tags and versions (e.g., `M.01`, `M.02b`), with zero attached assets, tracked via `ROADMAP.md`, `PLAN.md`, `TODO.md`, and `CHANGELOG.md`.

---

# Milestone Summary — {{ milestone.id }}: {{ milestone.title }}

- **Date**: {{ YYYY-MM-DD }}
- **Release Tag**: {{ milestone.id }} (no attached assets)
- **Status**: {{ milestone.status }}

---

## Overview

{{ milestone.summary }}

---

## Per-Surface Status

| Surface / Styler File | Windhawk Mod | Mod Version | Windows 11 Build | Status |
|---|---|---|---|---|
| `projects/<project>/windows-11-taskbar-styler.yml` | Windows 11 Taskbar Styler | 1.10+ | 23H2 / 24H2 | {{ status }} |
| `projects/<project>/windows-11-start-menu-styler.yml` | Windows 11 Start Menu Styler | 1.7+ | 23H2 / 24H2 | {{ status }} |
| `projects/<project>/windows-11-notification-center-styler.yml` | Windows 11 Notification Center Styler | 1.7+ | 23H2 / 24H2 | {{ status }} |
| `projects/<project>/windows-11-settings-styler.yml` | Windows 11 Settings Styler | 1.0+ | 23H2 / 24H2 | {{ status }} |
| File Explorer | Windows 11 File Explorer Styler | 1.7+ | 23H2 / 24H2 | Deferred (ROADMAP M.03) |

*Mod versions are external Windhawk mod versions, not suite milestone versions.*

---

## Changes

### Added
- {{ list.item }}

### Changed
- {{ list.item }}

### Fixed
- {{ list.item }}

---

## Verification

- [ ] **Static Validation Gate**: `pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1` passed with 0 errors.
- [ ] **Live Checklist**: `.agents/templates/live-verification-checklist.md` completed for each changed surface.

---

## Known Issues

- {{ bug.item }} (tracked in `BUGS.md`)
- {{ deferred.item }} (tracked in `ROADMAP.md`, `TODO.md`)

---

## Next Steps

{{ next.steps }}
