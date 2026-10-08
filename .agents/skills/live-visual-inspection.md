# Skill: Live Visual Inspection & Diagnostic Tooling

## Purpose

Standard operating procedure for inspecting the live XAML visual trees of Windows 11 shell surfaces to discover, verify, or debug target selectors without guessing (Rule 04).

---

## 1. Preferred Tool: Headless Inspector (`tools/inspect_xaml.py`)

The repository's own inspector is the first choice: by default it dumps UIA trees as text / JSON / Markdown **without opening windows, without screenshots, and without touching input** — fully respecting the accessibility invariant (no manual UWPSpy burden on the user). See [`tools/README.md`](../../../tools/README.md) for options.

```powershell
python tools/inspect_xaml.py --list
python tools/inspect_xaml.py -p explorer.exe --window-class Shell_TrayWnd
python tools/inspect_xaml.py -p ShellHost.exe -f "NotificationCenter|ControlCenter"
```

Approved targets only: `StartMenuExperienceHost.exe`, `SearchHost.exe`, `SearchApp.exe`, `LockApp.exe`, `ShellExperienceHost.exe`, `ShellHost.exe`, `explorer.exe` (Rule 01). Closed/hidden surfaces are inspected as-is whenever possible.

### Consent-gated surface opening (Rule 00)

Only when a surface truly cannot be inspected closed — and only after asking the user *for that specific run* — the inspector can open it (and best-effort closes it with Escape afterwards):

```powershell
# Ask the user first, every time; consent is never stored between runs.
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --permit-ui-automation --open-surface start
```

Surfaces: `start` (Win) · `search` (Win+S) · `action-center` (Win+A) · `notification-center` (Win+N). For anything without a shortcut, `--click X Y` presses at pixel coordinates from a previous dump's bounding rects (`--leave-open` skips the closing Escape). **Never automate `LockApp.exe` / the lock screen** — it locks the system and cannot be inspected as a result. Mouse/keyboard automation outside the tool's own consent-gated path remains forbidden.

---

## 2. Fallback Tool: UWPSpy

UWPSpy remains the community standard for deep XAML property inspection when the headless tool's UIA-level data is insufficient (e.g. XAML property values, brush resolution). Launch it only when needed; the user should never have to drive it.

### 2.1 Process & Framework Selection

| Surface | Process to Select | Target Framework |
|---|---|---|
| **Notification Center / Action Center** | `ShellExperienceHost.exe` (or `ShellHost.exe` on Win11 24H2) | **UWP (`Windows.UI.Xaml`)** |
| **Start Menu** | `StartMenuExperienceHost.exe` | **UWP / WinUI 2** |
| **Taskbar** | `explorer.exe` | **WinUI 3 / XAML Island** |
| **File Explorer** *(deferred — reference only, ROADMAP M.03)* | `explorer.exe` | **WinUI 3 (`Microsoft.UI.Xaml`)** |

---

## 3. Step-by-Step UWPSpy Inspection Procedure

1. Launch **UWPSpy** as administrator.
2. Select the target process and framework from the dropdown.
3. Open the shell UI you wish to inspect (e.g. click Notification Center; open File Explorer only if that deferred surface is resumed).
4. Click the **Pick Element** icon in UWPSpy and hover over the desired UI control.
5. In the visual tree panel:
   - Identify the control's class name (e.g. `Grid`, `Border`, `TabViewItem`).
   - Look for an `x:Name` or `FrameworkElement.Name` attribute (e.g. `NotificationCenterGrid`, `CommandBarControlRootGrid`).
   - If no name exists, inspect unique attached properties (e.g. `[AutomationProperties.AutomationId=Microsoft.QuickAction.Volume]`).
   - Note the immediate parent container to form a robust direct child chain (`Parent > Child`).

---

## 4. Selector Quality Checklist

- [ ] Does the selector uniquely identify the intended control without bleeding into unrelated controls?
- [ ] Is it anchored with a `#Name` or property filter rather than a bare common type?
- [ ] Is the selector documented in the surface's target evidence table (`.agents/targets/`)? *(Schema: `.agents/templates/target-evidence-template.md`; records currently live in `.agents/targets/` — migrated from the earlier `docs/targets/` location.)*
