# Rule 04: Target Evidence Protocol (No Guessed Selectors)

## Purpose

A Windhawk styler `target` that does not match any element **fails silently** — no error, no visual change. A wrong-but-matching target is worse: it restyles something unintended (e.g. a bare `ContentPresenter` matches hundreds of elements). This rule makes every target traceable to evidence so the suite never ships guesses.

---

## 1. Evidence Tiers

Every target added or changed must be backed by at least one of these, in order of preference:

| Tier | Evidence | How it is obtained |
|---|---|---|
| **T1 — Live tree** | The element was observed in the user's live visual tree | User inspects with UWPSpy (UWP surfaces) or the WinUI equivalent and shares the type/name/path, or a screenshot of the inspector |
| **T2 — Shipped suite** | The target already works in a shipped suite file **for the same mod** | `projects/<project>/windows-11-start-menu-styler.yml`, `projects/<project>/windows-11-taskbar-styler.yml` |
| **T3 — User scaffold** | The target was placed by the user in a suite file that was not yet shipped | `projects/<project>/windows-11-notification-center-styler.yml` (generated & verified) |
| **T4 — Official source** | The target appears in the mod's readme or a built-in/community theme in the official styling-guide repository | `ramensoftware/windhawk-mods`, `ramensoftware/windows-11-*-styling-guide` — cite the URL |
| **T5 — Inference** | Derived from WinUI/UWP control templates (e.g. `Border#BackgroundBorder` inside a `Button`) | Allowed **only** when paired with a T1 confirmation request in the live checklist |

T2 evidence **does not transfer across mods**. A target that works in the Start Menu Styler is only T5 inference for the Notification Center Styler, even if the element name looks identical.

---

## 2. Selector Hygiene

1. **Anchor broad types.** Never ship a bare common type (`ContentPresenter`, `Border`, `Grid`, `TextBlock`, `ListViewItem`) without a `#Name`, `[Property=Value]`, or a parent chain that confines it. If a bare type is genuinely intended (e.g. `MenuFlyoutItem` everywhere), document why in the evidence table.
2. **Prefer names over positions.** `Grid#ControlCenterRegion` beats `Grid > Grid > Border`.
3. **Localized names are fragile.** `[AutomationProperties.Name=All settings]` only matches English UI. Prefer `AutomationProperties.AutomationId` or `x:Name` (`#Name`). If a localized name must be used, flag it in the evidence table as **EN-only**.
4. **One concern per block.** Comma-joined multi-targets are allowed only when every member receives identical styles (taskbar precedent: `…TaskListButtonPanel@CommonStates > Grid > Border#BackgroundElement, …TaskListButtonPanel@CommonStates > Border#BackgroundElement` for Windows build variants).
5. **No duplicate targets.** The same selector must appear in only one block per file. Later duplicates silently override or merge with earlier ones and make intent ambiguous.

---

## 3. Evidence Recording

1. Each styler file has an evidence table in [`.agents/targets/`](../../.agents/targets/), named after the styler file (e.g. `.agents/targets/notification-center-styler.md`), built from [`target-evidence-template`](../templates/target-evidence-template.md). This is the **interim location**: the records migrate to `docs/targets/` when the planned `docs/` GitHub Pages site is built (deferred until style work is complete — Rule 08).
2. Columns: target · surface region · tier · source/citation · Windows build observed · status (`unverified` / `confirmed` / `broken`).
3. A target moves to `confirmed` only after the user reports the live result (Rule 07).
4. Targets reported `broken` after a Windows update are logged in `BUGS.md` with the build number — never silently deleted.

---

## 4. Accessibility Accommodation & Tooling Protocol

1. **User Accessibility Accommodation**:
   - The user has poor eyesight and has explicitly requested **not** having to manually navigate or inspect visual trees in UWPSpy.
   - Agents **must exhaust** all official mod source code (`mods/<id>.wh.cpp`), official community themes (e.g. `ramensoftware/windows-11-*-styling-guide`), and existing verified suite files before ever proposing visual inspection.
   - If live inspection is ever strictly unavoidable, agents must provide automated command-line queries or minimal, focused instructions rather than requiring the user to manually expand and read complex GUI tree hierarchies.
2. **When Evidence Is Missing**:
   - Consult official mod C++ source code in `ramensoftware/windhawk-mods` to inspect built-in theme targets.
   - If a target cannot be confirmed, state the assumption clearly as T5 inference and provide a simple, high-contrast visual check in [`live-verification-checklist`](../templates/live-verification-checklist.md).
