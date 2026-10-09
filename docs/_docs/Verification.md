---
title: Verification & Quality Gates
---

# Verification & Quality Gates

Because Windows shell styles render within closed desktop processes, quality assurance is divided into two distinct gates: an automated **Static Gate** and a human **Live Checklist**.

---

## 1. Automated Static Validation Gate

Run the automated test runner to validate all style files:

```powershell
# Run validation across all projects
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1

# Validate a specific styler file
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1 -Path projects/<project>/windows-11-taskbar-styler.yml
```

### Static Gate Error Codes:

| Code | Severity | Description |
|---|---|---|
| `E001` | Error | Tab characters detected (must use 2 spaces). |
| `E002` | Error | Non-CRLF line endings detected. |
| `E003` | Error | Undefined token referenced (e.g. `$UndefinedToken`). |
| `E004` | Error | Malformed constant declaration (e.g. `- $Token=...`). |
| `E005` | Error | Empty `styles` block under a target selector. |
| `E006` | Error | Unsupported top-level key for that specific mod. |
| `E007` | Error | Hardcoded personal path or username (`C:\Users\...`). |
| `E008` | Error | Duplicate constant declaration name. |
| `W101` | Warning | Duplicate target selector within a single file. |

The static validation gate must pass with **0 errors and 0 warnings** before any work is considered complete.

---

## 2. Desktop Live Verification Checklist

Once static validation passes, the style file is imported into Windhawk for live desktop verification:

- [ ] **Light Mode Contrast**: Text remains fully legible; cards do not wash out.
- [ ] **Dark Mode Contrast**: Text remains crisp; borders and specular rims are clearly defined.
- [ ] **Interactive Hover States**: Buttons and tiles smoothly respond to pointer hover and press.
- [ ] **Dynamic Windows Accent**: Accent colors adapt immediately when changed in Windows Settings.
- [ ] **Redraw & Animation**: Surfaces open and close smoothly without flicker or black artifacts.

---

## 3. Milestone-Based Releases

Progress in this repository is tracked via **Milestones** (e.g., `M.01`, `M.02b`, `M.03`):
- Releases use **milestones as release tags and versions** rather than arbitrary semantic versioning numbers.
- Releases carry **no attached assets** (no zips, binaries, or installers). The release represents the verified repository tree and commit tag itself.
- When all quality gates are satisfied, a milestone checkpoint release can be tagged for clean version control.
