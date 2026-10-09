# Style Architect Agent (Primary — Engineering Focus)

The **Style Architect Agent** is the **primary agent** for the **engineering focus**. It is responsible for the overall aesthetic coherence, token hierarchy, XAML grammar adherence, and selector architecture across the five base Windhawk styler mods (with extensibility to other mods). It coordinates the engineering sub-agents.

---

## Architecture & Sub-Agents

```mermaid
flowchart TD
    Architect["Style Architect (Primary)"] --> NC["Notification Center Specialist (Sub)"]
    Architect --> FE["File Explorer Specialist (Sub) (deferred)"]
    Architect --> Settings["Settings Specialist (Sub)"]
    Architect --> Inspect["Visual Inspector (Sub)"]
```

| Sub-Agent | Target Domain | Specification |
|---|---|---|
| **Notification Center Specialist** | UWP `Windows.UI.Xaml` in `ShellExperienceHost.exe` / `ShellHost.exe` | [notification-center-specialist](sub-agents/notification-center-specialist.md) |
| **File Explorer Specialist** | WinUI 3 `Microsoft.UI.Xaml` in `explorer.exe` — **deferred (ROADMAP M.03)** | [file-explorer-specialist](sub-agents/file-explorer-specialist.md) |
| **Settings Specialist** | UWP / WinUI `Windows.UI.Xaml` in `SystemSettings.exe` | [settings-specialist](sub-agents/settings-specialist.md) |
| **Visual Inspector** | Hybrid C++/Python TAP inspection, visual tree discovery | [visual-inspector](sub-agents/visual-inspector.md) |

---

## Standards & Constraints

- **Design Language Invariants (Rule 03)**: Every surface must derive its materials, edge gradients, and corner radii strictly from the theme's defined token scale.
- **Evidence-Based Selectors (Rule 04)**: Zero tolerance for guessed target selectors. All selectors must be backed by documented evidence in `.agents/targets/`.
- **Surface Scoping (Rule 05)**: Strictly respect mod process boundaries. Never inject WinUI 3 tags into UWP shells or vice versa.
- **Order of Constants**: Ensure `styleConstants` declare materials first and observe declaration-order dependency.

---

## Operational Commands

```powershell
# Verify syntax and token resolution
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
```
