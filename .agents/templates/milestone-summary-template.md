# 📌 Milestone Summary Template

Use this template when a milestone/sprint of the **Windhawk Command Center Suite** completes. The suite does not use versioned releases — progress is tracked via milestones/sprints in `ROADMAP.md`, `PLAN.md`, `TODO.md`, and `BUGS.md`.

---

# Milestone Summary — {{ milestone.id }}: {{ milestone.title }}

- **Date**: {{ YYYY-MM-DD }}
- **Status**: {{ milestone.status }}

---

## Overview

{{ milestone.summary }}

---

## Per-Surface Status

| Surface / Styler File | Windhawk Mod | Mod Version | Windows 11 Build | Status |
|---|---|---|---|---|
| `src/windows-11-taskbar-styler.yml` | Windows 11 Taskbar Styler | 1.10+ | 23H2 / 24H2 | {{ status }} |
| `src/windows-11-start-menu-styler.yml` | Windows 11 Start Menu Styler | 1.7+ | 23H2 / 24H2 | {{ status }} |
| `src/windows-11-notification-center-styler.yml` | Windows 11 Notification Center Styler | 1.7+ | 23H2 / 24H2 | {{ status }} |
| File Explorer | Windows 11 File Explorer Styler | 1.7+ | 23H2 / 24H2 | Deferred (ROADMAP M.03) — no styler file |

*Mod versions are external Windhawk mod versions, not suite versions.*

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

- [ ] **Static Validation Gate**: `pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1` passed with target 0 errors.
- [ ] **Live Checklist**: `.agents/templates/live-verification-checklist.md` completed for each changed surface (taskbar / start menu / notification center).

---

## Known Issues

- {{ bug.item }} (tracked in `BUGS.md`)
- {{ deferred.item }} (tracked in `ROADMAP.md`, `TODO.md`)

---

## Next Steps

- {{ next.step }} (see `ROADMAP.md` and `PLAN.md` for the next active milestone/sprint).
