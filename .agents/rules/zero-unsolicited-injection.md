# Rule 01: Dependency, Mod & Asset Approval (Zero Unsolicited Injection)

## Purpose

The suite is a set of **settings files for specific Windhawk mods**. Its footprint on the user's machine must stay exactly what the user chose. Nothing new enters the suite — no mod, font, image, tool, or package — without explicit user approval.

---

## 1. Approved Runtime Surface

This repository exists to maintain the **Command Center suite** for exactly **four approved** Windhawk styler mods. **Three** of them have an active styler file in `src/`; the fourth (File Explorer) is approved but **deferred** and has no file:

| Style File | Windhawk Mod | Status |
|---|---|---|
| `src/windows-11-taskbar-styler.yml` | Windows 11 Taskbar Styler (`windows-11-taskbar-styler`) | ✅ Shipped — design reference |
| `src/windows-11-start-menu-styler.yml` | Windows 11 Start Menu Styler (`windows-11-start-menu-styler`) | ✅ Shipped — design reference |
| `src/windows-11-notification-center-styler.yml` | Windows 11 Notification Center Styler (`windows-11-notification-center-styler`) | ✅ Generated & Verified — follow-up polish active (ROADMAP M.02b, TODO W.04) |
| *No styler file — deferred* | Windows 11 File Explorer Styler (`windows-11-file-explorer-styler`) | ⏸️ Deferred — no file exists (generated, then discontinued — git 1cc49e9); ROADMAP M.03 / TODO W.03 |

> [!IMPORTANT]
> **File Explorer stays deferred.** The mod remains inside this rule's four-mod boundary, but `src/windows-11-file-explorer-styler.yml` **does not exist** and must not be scaffolded, generated, or created without a new explicit user directive.
> **Locked user directive (2026-10-07)**: *"deferred due to lack of plausible customizations. there are other already existing styles that are too similar and as such there is no real benefit to having our own file explorer style just yet."*

Adding a fifth mod to the suite requires explicit user approval and a [Rule 08](documentation-standards.md) catalog update. Reviving the File Explorer styler file likewise requires a new explicit user directive as noted above.

### Out-of-Scope Companion Files

These files live in `src/extras/` and are **not** part of the suite and are **not** maintained by this ecosystem. Agents must leave them byte-for-byte untouched unless the user explicitly asks otherwise.

---

## 2. Assets

1. **Fonts**: Only fonts already used by the suite may be referenced (`Morganite SemiBold`, `vivo Sans EN VF`, plus Windows-bundled `Segoe UI Variable`, `Segoe Fluent Icons`, `Segoe MDL2 Assets`). A missing font silently falls back and breaks the look — introducing a new font family needs approval.
2. **Images**: No `ImageBrush` / file-path backgrounds unless the user supplies the image and approves the path. Absolute paths are machine-specific and break portability.
3. **Colors**: Prefer `{ThemeResource …}` colors and `SystemAccentColor` over hard-coded hex so the suite follows the user's light/dark mode and accent. Hard-coded hex is reserved for the shared neutral-gray glass tokens defined in [Rule 03](design-language-standards.md).

---

## 3. Tooling

1. **Approved tooling**: Windows PowerShell 7 (`pwsh`) and the repository's own scripts in `tools/`. The static gate (`tools/Test-WindhawkStyles.ps1`) uses no modules beyond what ships with PowerShell.
2. **Forbidden without approval**: `npm`/`pip`/`winget`/`choco`/`scoop` installs, PowerShell Gallery modules (including `powershell-yaml`), CI services, formatters, or linters.
3. **Inspection tools on the user's machine** (e.g. UWPSpy) are **user-run**. Agents may recommend them and explain how to read their output; agents never download or execute them.

---

## 4. Forbidden Mods & Global Hooks (No TranslucentWindows)

> [!IMPORTANT]
> The **TranslucentWindows** mod (`translucent-windows`) is known to cause severe rendering conflicts, black boxes, and visual glitches with various external applications (e.g. Chromium, Electron, hardware-accelerated windows).
> - **All styles in this suite MUST use methods that do NOT require the TranslucentWindows mod to work.**
> - All styles rely exclusively on standard XAML visual tree injection (`WindhawkBlur`, `AcrylicBrush`, `LinearGradientBrush`) within the dedicated target processes (`ShellExperienceHost.exe`, `explorer.exe`, `StartMenuExperienceHost.exe`).
> - The deferred File Explorer surface must never rely on whole-window GDI alpha hooks: if a File Explorer styler file is ever created under a new explicit user directive, `backgroundTranslucentEffect` must start and remain `""` (empty/disabled) so that whole-window GDI alpha hooks are never invoked.
