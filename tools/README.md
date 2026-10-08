# Tools (`tools/`)

Repository tooling for **Windhawk Command Center Suite**. Everything here is
invoked from the repository root and requires no interaction with the user's
desktop.

| Tool | Purpose | Invocation |
|---|---|---|
| [`Test-WindhawkStyles.ps1`](Test-WindhawkStyles.ps1) | **Static validation gate (Rule 07)** — YAML syntax, constant ordering, token checks for every styler file in `src/`. Must pass with 0 errors before handoff. | `pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1` |
| [`style-baseline.ini`](style-baseline.ini) | Baseline ledger of pre-existing static-gate warnings in shipped files. Read by the gate; may only shrink (Rule 07 §2). | *(consumed automatically)* |
| [`inspect_xaml.py`](inspect_xaml.py) | **Headless visual tree inspector** — dumps the UI Automation trees of the approved UWP / WinUI 3 shell processes as text, JSON, or Markdown for selector discovery and evidence (Rule 04). | `python tools/inspect_xaml.py --help` |

---

## `inspect_xaml.py` — headless UWP / WinUI 3 inspector

Programmatic replacement for manual UWPSpy sessions: it reads the live UIA
trees and writes them to stdout or a file. **Read-only by default: no
windows are opened, nothing is drawn on screen, no screenshots are taken,
and the mouse/keyboard are never touched** — unless the user grants
explicit per-run consent for UI automation (below).

### Safety contract (enforced, not aspirational)

[`xaml_inspect/safety.py`](xaml_inspect/safety.py) whitelists every OS call
the package may make. Anything else raises `SafetyViolation`:

- **Tier 1 — read-only (always allowed)**: UIA property reads and tree
  enumeration; Win32 calls limited to query-only enumeration (`EnumWindows`,
  `FindWindowExW`, `GetClassNameW`, `GetWindowTextW`, `IsWindowVisible`,
  `GetWindowThreadProcessId`, Toolhelp snapshot). No messages to other
  processes, no screenshots — output is textual only.
- **Tier 2 — UI automation (consent-gated)**: `SendInput`, `SetCursorPos`,
  `mouse_event`, `keybd_event`, `SetForegroundWindow`, `ShowWindow` unlock
  only when the run passes `--permit-ui-automation` (Rule 00). Consent is
  process memory for that run only — never stored, never reused — and the
  agent must ask the user directly before *each* such run. Input libraries
  (pyautogui / pynput / keyboard / mouse / uiautomation) stay banned even
  with consent: the tool's own gated path is the only sanctioned route.
- **Never allowed (no consent exists)**: window move/resize/reorder
  (`SetWindowPos`, `MoveWindow`, `SetWindowPlacement`,
  `AttachThreadInput`), `SendMessage` / `PostMessage` traffic, clipboard
  access — and **any automation of `LockApp.exe` / the lock screen**, which
  locks the system and cannot be inspected as a result (lock screen
  customization is research-only).

### Consent-gated surface opening

Keyboard shortcuts open the four inspectable surfaces; `--click X Y` is the
fallback for areas with no shortcut (coordinates come from a previous
dump's bounding rects). Surfaces opened this run are closed with one
Escape afterwards unless `--leave-open` is passed.

| Surface | Shortcut | Flag |
|---|---|---|
| Start menu | Win | `--open-surface start` |
| Search | Win+S | `--open-surface search` |
| Action Center / Quick Settings | Win+A | `--open-surface action-center` |
| Notification Center | Win+N | `--open-surface notification-center` |
| *(no shortcut)* | mouse click | `--click X Y` |

Using `--open-surface` or `--click` **without** `--permit-ui-automation`
is refused at the CLI (exit 3) with a message telling the agent to ask
the user first.

### Approved target processes

Only these seven processes may be inspected (Rule 01 runtime boundary);
`--process` / `--pid` reject anything else:

`StartMenuExperienceHost.exe` · `SearchHost.exe` · `SearchApp.exe` ·
`LockApp.exe` · `ShellExperienceHost.exe` · `ShellHost.exe` · `explorer.exe`

### Examples

```powershell
# List target processes and their windows (no tree walk)
python tools/inspect_xaml.py --list

# Taskbar XAML tree
python tools/inspect_xaml.py -p explorer.exe --window-class Shell_TrayWnd

# Notification Center surface (hidden/idle windows included by default —
# surfaces do NOT need to be opened to be inspected)
python tools/inspect_xaml.py -p ShellHost.exe

# Search for specific elements, keep matching subtrees + context
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe -f "SearchBox|PinnedList"

# Only XAML-framework elements, capped depth, JSON to a file
python tools/inspect_xaml.py -p explorer.exe --framework XAML --max-depth 8 --format json -o out.json

# Markdown dump for pasting into a target evidence table
python tools/inspect_xaml.py -p ShellHost.exe --format markdown -o .agents/targets/draft.md

# --- UI automation: requires the user's explicit permission EACH run ---
# (ask the user directly first; consent is never stored between runs — Rule 00)
# Open the Start menu, dump it, then close it again with Escape
python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --permit-ui-automation --open-surface start

# Notification Center via Win+N, left open afterwards
python tools/inspect_xaml.py -p ShellHost.exe --permit-ui-automation --open-surface notification-center --leave-open

# Click at pixel coordinates (e.g. from a previous dump's bounding rect)
python tools/inspect_xaml.py -p explorer.exe --permit-ui-automation --click 1870 1050
```

### Key options

| Option | Effect |
|---|---|
| `-p / --process NAME` | Target process (repeatable); default = all approved targets that are running. |
| `--pid N` | Inspect one PID (must belong to an approved target). |
| `--window-class CLS` | Only top-level windows of this class (e.g. `Shell_TrayWnd`). |
| `--window-title REGEX` | Only windows whose title matches. |
| `--visible-only` | Skip hidden windows (default includes them so closed surfaces are inspectable). |
| `-d / --max-depth N` | Depth cap (0 = unlimited). |
| `-n / --max-nodes N` | Node budget per window (default 5000). |
| `-f / --filter REGEX` | Keep matching elements **and their full subtree**; ancestors kept for context. |
| `--framework SUBSTR` | Keep elements whose `frameworkId` contains the substring (e.g. `XAML`, `WinUI`). |
| `--format {text,json,markdown}` | Output format (default `text`). |
| `-o / --output FILE` | Write to a file instead of stdout. |
| `--list` | Enumerate processes/windows only (fast, no UIA walk). |
| `--permit-ui-automation` | Grant **this run** consent for tier-2 UI automation (Rule 00); required by `--open-surface` / `--click`. Never stored between runs. |
| `--open-surface SURFACE` | Open `start`, `search`, `action-center`, or `notification-center` before capture (repeatable; requires `--permit-ui-automation`), then close it with Escape afterwards. |
| `--click X Y` | Left-click at screen pixel `(X, Y)` before capture, for surfaces with no keyboard shortcut (requires `--permit-ui-automation`); the cursor stays at that position. |
| `--leave-open` | Skip the closing Escape for surfaces opened by this run. |

### Output notes

- Each element shows: control type, selector candidate
  (`ClassName#AutomationId` from observed UIA values — evidence, not
  guesses), framework id (`XAML` / `WinUI` / `Win32`), name, bounding rect.
- Hung or wedged window providers fail per-window after a 3 s UIA timeout
  (`IUIAutomation2::ConnectionTimeout` / `ResponseTimeout`) and are reported
  as `ERROR:` lines instead of blocking the run.
- Requires Python 3 and the `comtypes` package.

### Package layout

```
tools/inspect_xaml.py        CLI launcher
tools/xaml_inspect/
  safety.py                  three-tier safety contract + call whitelists
  activate.py                consent-gated UI automation (Win chords, click)
  processes.py               approved-target PID resolution (Toolhelp)
  windows.py                 top-level + message-only window enumeration
  uia.py                     UIA3 session and element property reads
  walk.py                    depth/budget-limited walk + filter pruning
  render.py                  text / JSON / Markdown renderers
  cli.py                     argparse orchestration + consent gate
```
