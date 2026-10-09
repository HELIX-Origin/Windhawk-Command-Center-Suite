# Rule 01: Dependency, Mod & Asset Approval (Zero Unsolicited Injection)

## Purpose

The suite is a set of **settings files for specific Windhawk mods**. Its footprint on the user's machine must stay exactly what the user chose. Nothing new enters the suite — no mod, font, image, tool, or package — without explicit user approval.

---

## 1. Universal Multi-Mod Scope & Approved Runtime Surface

This repository's agent ecosystem and hybrid C++/Python toolchain are designed as a **universal standard** for managing Windhawk themes. While extensible to other Windhawk mods as needed, the architecture specifies **five official Windhawk styler mods as its base intended scope**:

| Styler File | Windhawk Mod ID | Target Process | Status |
|---|---|---|---|
| `projects/<project>/windows-11-taskbar-styler.yml` | `windows-11-taskbar-styler` | `explorer.exe` | ✅ Supported reference |
| `projects/<project>/windows-11-start-menu-styler.yml` | `windows-11-start-menu-styler` | `StartMenuExperienceHost.exe` | ✅ Supported reference |
| `projects/<project>/windows-11-notification-center-styler.yml` | `windows-11-notification-center-styler` | `ShellExperienceHost.exe` / `ShellHost.exe` | ✅ Generated & Verified (M.02b / W.04) |
| *No styler file — deferred* | `windows-11-file-explorer-styler` | `explorer.exe` | ⏸️ Deferred (ROADMAP M.03 / TODO W.03) |
| *No styler file — supported base* | `windows-11-settings-styler` | `SystemSettings.exe` | 🌐 In base scope (inspection & tooling supported) |

> [!IMPORTANT]
> **File Explorer stays deferred.** The mod remains inside this rule's five-mod base boundary, but `projects/<project>/windows-11-file-explorer-styler.yml` **does not exist** and must not be scaffolded or created without a new explicit user directive.
> **Locked user directive (2026-10-07)**: *"deferred due to lack of plausible customizations. there are other already existing styles that are too similar and as such there is no real benefit to having our own file explorer style just yet."*

Other Windhawk mods may be supported as requested, with corresponding target process additions and documentation updates.

### Out-of-Scope Companion Files

These files live in `projects/<project>/extras/` and are companion configurations. Agents must leave them byte-for-byte untouched unless the user explicitly asks otherwise.

---

## 2. Assets

1. **Fonts**: Only fonts already used by the suite may be referenced (`Morganite SemiBold`, `vivo Sans EN VF`, plus Windows-bundled `Segoe UI Variable`, `Segoe Fluent Icons`, `Segoe MDL2 Assets`). A missing font silently falls back and breaks the look — introducing a new font family needs approval.
2. **Images**: No `ImageBrush` / file-path backgrounds unless the user supplies the image and approves the path. Absolute paths are machine-specific and break portability.
3. **Colors**: Prefer `{ThemeResource …}` colors and `SystemAccentColor` over hard-coded hex so the suite follows the user's light/dark mode and accent. Hard-coded hex is reserved for the shared neutral-gray glass tokens defined in [Rule 03](design-language-standards.md).

---

## 3. Tooling

1. **Approved tooling**: Windows PowerShell 7 (`pwsh`), Python 3 with the already-installed `comtypes` package, and the repository's own scripts in `tools/` (the static gate `tools/Test-WindhawkStyles.ps1` uses no modules beyond what ships with PowerShell; the headless inspector `tools/inspect_xaml.py` is read-only by default, with UI automation only behind explicit per-run user consent — see `tools/README.md`).
2. **Forbidden without approval**: `npm`/`pip`/`winget`/`choco`/`scoop` installs, PowerShell Gallery modules (including `powershell-yaml`), CI services, formatters, or linters.
3. **Inspection tools on the user's machine** (e.g. UWPSpy) are **user-run**. Agents may recommend them and explain how to read their output; agents never download or execute them.

---

## 4. Forbidden Mods & Global Hooks (No TranslucentWindows)

> [!IMPORTANT]
> The **TranslucentWindows** mod (`translucent-windows`) is known to cause severe rendering conflicts, black boxes, and visual glitches with various external applications (e.g. Chromium, Electron, hardware-accelerated windows).
> - **All styles in this suite MUST use methods that do NOT require the TranslucentWindows mod to work.**
> - All styles rely exclusively on standard XAML visual tree injection (`WindhawkBlur`, `AcrylicBrush`, `LinearGradientBrush`) within the dedicated target processes (`ShellExperienceHost.exe`, `explorer.exe`, `StartMenuExperienceHost.exe`).
> - The deferred File Explorer surface must never rely on whole-window GDI alpha hooks: if a File Explorer styler file is ever created under a new explicit user directive, `backgroundTranslucentEffect` must start and remain `""` (empty/disabled) so that whole-window GDI alpha hooks are never invoked.
