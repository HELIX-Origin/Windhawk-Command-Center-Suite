# Changelog

All notable changes to **Windhawk Command Center Suite** are documented here. One entry per update (`## YYYY-MM-DD - HH:MM`), newest first. Each entry has at most one `Added`, `Removed`, `Changed`, and `Fixed` section — omit sections with no items, and put every item of a type in that type's single list (never a second section of the same type). Items are `- **Title**: description` with nested `**Title**: description` sub-items as needed. Tracking is done via `ROADMAP.md`, `PLAN.md`, `TODO.md`, and `BUGS.md` rather than formal releases.

## 2026-10-07 - 23:13

### Added
- **`.agents/targets/` evidence directory**: Interim home for per-styler selector evidence records (Notification Center and File Explorer restored from git history), with a folder `README.md`; will migrate to `docs/targets/` when the planned GitHub Pages site is built.
- **`root-changelog-file-template.md`**: Blueprint for this changelog in `.agents/templates/`.

### Removed
- **`index.md` files**: Deleted from `.agents/rules/`, `.agents/skills/`, `.agents/templates/`, and `.agents/agents/`; folder `README.md` files are now the canonical indexes (Surface Ownership Matrix merged into `.agents/agents/README.md`).
- **Version metadata**: `1.0.0-preview` removed from `PLAN.md`, `TODO.md`, and `BUGS.md` (the suite has no versions).

### Changed
- **Agent ecosystem realignment**: Full audit of `AGENTS.md` and `.agents/` against repository reality.
  - **Rule 09 reworked**: `release-standards.md` → `milestone-standards.md` ("Milestone & Sprint Tracking Standards"); `release-notes-template.md` → `milestone-summary-template.md`; all SemVer/version/release framing removed project-wide (external Windhawk mod versions retained).
  - **File Explorer deferred (ROADMAP M.03)**: Reframed everywhere with the official rationale — lack of plausible customizations; existing styles too similar; no real benefit yet. Notification Center status corrected to Generated & Verified (polish active — M.02b).
  - **Stale references corrected**: Old styler filenames updated to `windows-11-*-styler.yml`; `docs/targets/` references redirected to interim `.agents/targets/`; `docs/` documented as a planned future GitHub Pages site (deferred until style work completes).
  - **Root tracking templates**: Realigned with the actual root files (including a new changelog blueprint).
- **Documentation sync**: Restructured root `README.md`, `src/README.md`, and `src/extras/README.md` to align with documentation standards (root Markdown files + `src/extras/README.md` + `.agents/`; `docs/` deferred for a planned GitHub Pages site).
- **Static gate**: `pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1` passes — 0 errors, 0 warnings.

## 2026-10-07 - 21:36

### Added
- **`tools/style-baseline.ini`**: Style baseline ledger for pre-existing static-gate warnings.

### Changed
- **Documentation standards**: Updated documentation standards and enhanced companion mod configurations in `src/extras/README.md`.

## 2026-10-05 - 16:26

### Added
- **Design system**: Command Center Glass design language (frosted blur, top-lit rim, harmonized radii, theme-aware materials).
- **Base styler YAMLs**: `src/windows-11-taskbar-styler.yml`, `src/windows-11-start-menu-styler.yml`, and `src/windows-11-notification-center-styler.yml` with canonical style constants.
- **Extras configurations**: Dynamic Island, Enhanced Disk Usage, File Operations Styler, Fully Customizable Winver, Shell Flyout Positions, Start Button Colorizer, Taskbar Clock Customization, Taskbar Tray and Icon Tweaks.
- **Agent ecosystem**: `.agents/` with rules (00–09), agents, skills, and templates; root tracking files `PLAN.md`, `TODO.md`, `BUGS.md`, `ROADMAP.md`.
- **Validation tooling**: `tools/Test-WindhawkStyles.ps1` static gate.
- **Target evidence records**: Per-styler selector ledgers (since relocated from `docs/targets/` to interim `.agents/targets/` — git `a4e4c76`).

### Removed
- **File Explorer styler**: Generated, then discontinued per user directive (git `1cc49e9`) — deferred (ROADMAP M.03); rationale: lack of plausible customizations, existing styles too similar, no real benefit yet.

### Changed
- **Notification Center polish**: Iterated styling through several commits; completed live desktop verification (M.02) with follow-up polish tracked under M.02b / W.04.
