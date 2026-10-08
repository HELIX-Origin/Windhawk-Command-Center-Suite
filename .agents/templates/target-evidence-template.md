# 🔬 Target Evidence Record: {{ surface.name }}

This document records the empirical evidence, visual tree inspection, and verification history for target selectors used in `src/{{ target.file }}` per **Rule 04 (Target Evidence Protocol)**.

---

## 📋 Surface Overview

- **Style File**: `src/{{ target.file }}`
- **Windhawk Mod**: `{{ mod.name }}` (`{{ mod.id }}`)
- **Target Process**: `{{ target.process }}`
- **XAML Framework**: `{{ xaml.framework }}` (UWP `Windows.UI.Xaml` or WinUI 3 `Microsoft.UI.Xaml`)

---

## 🎯 Target Evidence Ledger

| Selector | Surface Region | Tier | Source / Citation | Build Observed | Status | Notes |
|---|---|---|---|---|---|---|
| `{{ selector.target }}` | `{{ region }}` | `{{ tier }}` | `{{ citation }}` | `{{ build }}` | `{{ status }}` | `{{ notes }}` |

### Legend

#### Evidence Tiers

- **T1 — Live Tree**: Directly observed in the user's running visual tree using UWPSpy or Visual Studio XAML Diagnostics.
- **T2 — Shipped Suite**: Proven working in an existing, shipped suite file for the **same** mod.
- **T3 — User Scaffold**: Explicitly identified by the user in a project scaffold file.
- **T4 — Official Source**: Sourced from official Windhawk mod source code (`ramensoftware/windhawk-mods`) or official styling guides.
- **T5 — Inference**: Derived from standard WinUI/UWP template hierarchies. Requires T1 live verification.

#### Verification Status

- 🟢 **Confirmed**: Verified functional and visually correct on user desktop.
- 🟡 **Unverified**: Implemented based on T3/T4 evidence, awaiting user live verification.
- 🔴 **Broken / Changed**: Known to fail or deprecated by a Windows update (logged in `BUGS.md`).

---

## 🛠️ Inspection Instructions

To inspect and capture new targets for this surface:

1. Launch **UWPSpy** (or Visual Studio Live Visual Tree).
2. Select target process: `{{ target.process }}`.
3. Select target framework: `{{ xaml.framework }}`.
4. Hover and pick the control to view its type hierarchy, `x:Name`, and attached properties.
5. Record the minimal unique selector in the table above.
