# Changelog

All notable changes to **Windhawk Command Center Suite** are documented here. Changes are grouped by date as work is completed. Tracking is done via `ROADMAP.md`, `PLAN.md`, `TODO.md`, and `BUGS.md` rather than formal releases.

## 2025-10-07

### Added
- `src/README.md` documenting base styler mods (Taskbar, Start Menu, Notification Center, File Explorer), canonical design tokens (materials, radii scale, layout), per-mod coverage, style constants reference, installation/validation, conventions/compliance, and related docs.
- Comprehensive root and `src/extras/README.md` restructuring to align with repository documentation standards (no `docs/` folder; root Markdown files + `src/extras/README.md` + `.agents/`).
- Root `CHANGELOG.md` with project changelog structure.

### Changed
- Root `README.md` reorganized for clearer purpose: highlights base mods + extras, design system, agent ecosystem, quality gates, and application instructions; includes File Explorer reference.
- `src/extras/README.md` restructured with purpose statement, companion mod matrix, detailed configuration notes, and import instructions aligned to suite standards.

### Notes
- Static validation gate: `pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1` must pass with 0 errors.
- Live verification: use `.agents/templates/live-verification-checklist.md` for desktop validation.

## 2025-10-07 (Earlier)

### Added
- Command Center Glass design system (frosted blur, top-lit rim, harmonized radii, theme-aware materials).
- Base YAMLs for Taskbar, Start Menu, Notification Center (generated baseline) and File Explorer (generated baseline) with canonical style constants.
- Extras companion configurations (Dynamic Island, Enhanced Disk Usage, File Operations Styler, Fully Customizable Winver, Shell Flyout Positions, Start Button Colorizer, Taskbar Clock Customization, Taskbar Tray and Icon Tweaks).
- Agent ecosystem under `.agents/` with rules (00–09), agents, skills, templates.
- Validation tool `tools/Test-WindhawkStyles.ps1`.
- Tracking files `PLAN.md`, `TODO.md`, `BUGS.md`, `ROADMAP.md`.
- Repository assets under `assets/`.

### Known
- Notification Center and File Explorer YAMLs marked generated/ready for verification; require live desktop verification.

## 2025-10-06

### Added
- Initial suite scaffolding and base mod references.
- Core design tokens and first shipped Taskbar/Start Menu styles.
- Extras pack groundwork.
