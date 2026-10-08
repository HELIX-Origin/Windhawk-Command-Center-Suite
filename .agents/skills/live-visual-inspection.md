# Skill: Live Visual Inspection & Diagnostic Tooling

## Purpose

Standard operating procedure for inspecting the live XAML visual trees of Windows 11 shell surfaces to discover, verify, or debug target selectors without guessing (Rule 04).

---

## 1. Primary Tool: UWPSpy

UWPSpy is the community standard tool for inspecting Windows shell XAML trees.

### 1.1 Process & Framework Selection

| Surface | Process to Select | Target Framework |
|---|---|---|
| **Notification Center / Action Center** | `ShellExperienceHost.exe` (or `ShellHost.exe` on Win11 24H2) | **UWP (`Windows.UI.Xaml`)** |
| **Start Menu** | `StartMenuExperienceHost.exe` | **UWP / WinUI 2** |
| **Taskbar** | `explorer.exe` | **WinUI 3 / XAML Island** |
| **File Explorer** *(deferred — reference only, ROADMAP M.03)* | `explorer.exe` | **WinUI 3 (`Microsoft.UI.Xaml`)** |

---

## 2. Step-by-Step Inspection Procedure

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

## 3. Selector Quality Checklist

- [ ] Does the selector uniquely identify the intended control without bleeding into unrelated controls?
- [ ] Is it anchored with a `#Name` or property filter rather than a bare common type?
- [ ] Is the selector documented in the surface's target evidence table (`.agents/targets/`)? *(Schema: `.agents/templates/target-evidence-template.md`; records currently live in `.agents/targets/` — migrated from the earlier `docs/targets/` location.)*
