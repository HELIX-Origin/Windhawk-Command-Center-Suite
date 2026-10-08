# Rule 00: Agent Safety, Instruction Compliance & Damage Prevention

## Purpose

This is the foundational safety rule for all AI agents working on **Windhawk Command Center Suite**. It guarantees that no irreversible damage is done to the style files, the user's live Windhawk installation, the Windows shell session, or repository history, and that agents strictly obey user instructions without regression or unintended side effects.

Rule 00 and [Rule 01](zero-unsolicited-injection.md) supersede every other rule.

---

## 1. Zero Irreversible Damage (Safety Invariants)

1. **Style File Preservation**:
   - The YAML files in `src/` are the product. Never delete, truncate, rename, or wholesale-overwrite an existing style file without explicit user authorization.
   - Edits to an existing style file are **surgical**: change only the targets/constants the task requires. Never reformat, reorder, or "clean up" unrelated blocks.
   - Never "fix" a perceived bug in a file the task does not cover. Log it in `BUGS.md` instead (see [Rule 07](verification-standards.md)).
   - The repository **is** under Git version control — Git history is the primary safety net: before any destructive or bulk edit, commit or stash current work and review `git diff` so the original state stays recoverable. Copying originals into `.backups/<yyyy-mm-dd>/<file>` is a **fallback for non-git contexts only** and is not used in this repository.

2. **Live System Protection**:
   - Agents **never** write to the user's live Windhawk configuration (`%ProgramData%\Windhawk\`, the `HKLM\SOFTWARE\Windhawk` registry tree, or any mod settings store).
   - Agents **never** kill, restart, or inject into `explorer.exe`, `StartMenuExperienceHost.exe`, `ShellExperienceHost.exe`, `ShellHost.exe`, or `windhawk.exe` without explicit, per-occurrence user consent. Restarting Explorer closes every open File Explorer window the user has.
   - Agents never install, uninstall, enable, or disable Windhawk mods on the user's machine. Applying a style is a **user action**: the agent hands over YAML; the user pastes/imports it into the mod's **Advanced → Settings** editor.
   - **UI automation (keyboard chords, mouse clicks, opening shell surfaces over the user's screen) is allowed only with the user's explicit, per-instance permission**: the agent must ask the user directly *before each such run* — never automatically, never pre-batched, never unattended — and then pass the tool's per-run consent flag (`tools/inspect_xaml.py --permit-ui-automation ...`). Consent lives in process memory for that run only and is never stored or reused; without it the tool refuses at the safety layer (exit code 3). The one absolute bar is `LockApp.exe`: the lock screen is **never automated** — opening it locks the user's machine and it cannot be inspected as a result — so lock screen customization remains research-only (Rule 04 sources).

3. **Repository Safety**:
   - The repository **is** under Git — this is the current, active procedure: **never** force-push, never discard or reset uncommitted user work, and always inspect `git status` / `git diff` before staging.
   - Only if the repository ever loses Git tracking (a non-git context): treat every overwrite as irreversible and fall back to the `.backups/` copy rule in §1.1.

4. **Personal Data Protection**:
   - Style files and documentation must never contain user names, local paths containing a user profile (`C:\Users\<name>\…`), machine names, account emails, or tokens.
   - Screenshots used as evidence must be cropped to the shell surface being verified.

---

## 2. Strict Instruction Following & Anti-Regression

1. **Unconditional Obedience to Explicit User Directives**:
   - User directives are recorded verbatim (typo-fixed) as **Locked user directives** in `TODO.md` and implemented exactly.
   - Example locked directive: *"Build the agents ecosystem first. Until that is built and completed, we don't generate the YAML code at all."*

2. **Design Fidelity (Rule 03)**:
   - New surfaces must visually belong to the existing suite. Never invent a new visual language, palette, or radius scale. See [Rule 03](design-language-standards.md).

3. **No Fabricated Targets (Rule 04)**:
   - Never ship a target selector that has not been sourced from evidence (visual-tree inspection, official mod readme/theme, or an already-working suite file). Guessed selectors fail silently and hide real problems.

4. **No Fabricated Verification (Rule 07)**:
   - Agents cannot see the user's desktop. Never claim a style "works", "looks right", or "was tested" unless the user confirmed it or the evidence is attached. Report static validation and live validation separately.

5. **Verification Gate Before Task Completion**:
   - No task is complete until it passes the static gate:

     ```powershell
     pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
     ```

   - A style task is only **done** after the user completes the live checklist in [`live-verification-checklist`](../templates/live-verification-checklist.md).

6. **Documentation & Agent Synchronization (Rule 08)**:
   - Changes to surfaces, constants, rules, or agent roles must be reflected in `AGENTS.md`, the `.agents/` catalogs, and the root tracking files.
