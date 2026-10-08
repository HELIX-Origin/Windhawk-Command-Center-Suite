"""Runtime safety contract for the ``xaml_inspect`` package.

The tool is **read-only by default**: property reads, tree walks, and
process/window enumeration are pure queries with no side effects on the
target. Everything is enforced at runtime by whitelisting every Win32 /
UI Automation entry point the package may call — anything outside the
whitelists raises :class:`SafetyViolation`.

Three tiers:

1. **Read-only** — always allowed: UIA property reads and tree
   enumeration, query/enum Win32 calls only.
2. **UI automation (consent-gated)** — ``SendInput`` and ``SetCursorPos``
   for opening a shell surface via its keyboard shortcut, or a synthetic
   click for surfaces that have none. Available only after
   :func:`grant_ui_automation_consent`, which the CLI sets **only** when
   the user grants explicit permission for that run
   (``--permit-ui-automation``). Consent lives in this process's memory
   for this run only — never persisted, and every new run starts
   read-only again. The agent must ask the user immediately before each
   consented run; never run automation unattended (Rule 00).
3. **Always forbidden** — no consent exists for these:
   - **No window manipulation.** ``SetWindowPos``, ``ShowWindow``,
     ``SetForegroundWindow``, ``MoveWindow``, ``BringWindowToTop``,
     ``AttachThreadInput`` — nothing is ever moved or activated.
   - **No messages sent to other processes.** No ``SendMessage`` /
     ``PostMessage`` / ``WM_*`` traffic; only COM UIA reads that the UIA
     provider answers on its own.
   - **No screenshots / capture.** Output is textual only.
   - **No input-automation library imports** (pyautogui, pynput,
     keyboard, mouse, uiautomation, ...):
     :func:`assert_safe_modules` verifies this at startup.
   - **No lock screen automation.** ``LockApp.exe`` is never an
     automation target: opening the lock screen locks the user's machine
     and it cannot be inspected as a result. Lock screen customization
     is research-only (Rule 04 sources) — Rule 00.
"""

from __future__ import annotations

import ctypes

__all__ = [
    "SafetyViolation",
    "assert_safe_modules",
    "assert_uia_call",
    "get_user32_function",
    "get_kernel32_function",
    "grant_ui_automation_consent",
    "has_ui_consent",
    "require_ui_consent",
]


class SafetyViolation(RuntimeError):
    """Raised when code attempts a non-read-only operation."""


# ---------------------------------------------------------------------------
# Import guard: input-automation libraries must never be loaded.
# ---------------------------------------------------------------------------
FORBIDDEN_IMPORTS = frozenset(
    {
        "pyautogui",
        "pywinauto",
        "pynput",
        "keyboard",
        "mouse",
        "autopy",
        "uiautomation",  # third-party helper with SendKeys/Click APIs
    }
)


def assert_safe_modules() -> None:
    """Fail fast if an input-automation module has been imported."""
    loaded = sorted(FORBIDDEN_IMPORTS.intersection(__import__("sys").modules))
    if loaded:
        raise SafetyViolation(
            "input-automation module(s) imported by this process: "
            + ", ".join(loaded)
            + " — xaml_inspect refuses to run alongside them; all input "
            "goes through this package's consent-gated path only."
        )


# ---------------------------------------------------------------------------
# UIA call whitelist: only these UIA3 methods may ever be invoked.
# (All Current* property reads are attribute reads on an element and are
# permitted by design; method calls are gated here.)
# ---------------------------------------------------------------------------
UIA_READ_ONLY_CALLS = frozenset(
    {
        "ElementFromHandle",
        "CreateTrueCondition",
        "FindAll",
        "FindFirst",
    }
)


def assert_uia_call(name: str) -> None:
    if name not in UIA_READ_ONLY_CALLS:
        raise SafetyViolation(f"blocked non-read-only UIA call: {name}")


# ---------------------------------------------------------------------------
# Win32 whitelists: only query/enum functions, never state-changing ones.
# ---------------------------------------------------------------------------
_USER32_READ_ONLY = frozenset(
    {
        # window enumeration & queries (no side effects)
        "EnumWindows",
        "FindWindowExW",
        "GetClassNameW",
        "GetWindowTextW",
        "GetWindowTextLengthW",
        "IsWindow",
        "IsWindowVisible",
        "GetWindowThreadProcessId",
        "GetParent",
        "GetWindow",
    }
)

_KERNEL32_READ_ONLY = frozenset(
    {
        # process snapshot (Toolhelp) — read-only
        "CreateToolhelp32Snapshot",
        "Process32FirstW",
        "Process32NextW",
        "CloseHandle",
    }
)

# Documented examples of what is blocked (not exhaustive; the whitelists
# above are the actual gate — anything not listed is refused). The
# input-injection functions below become available only in tier 2, after
# consent (see _CONSENT_GATED_USER32).
FORBIDDEN_USER32 = (
    "BringWindowToTop",
    "SetWindowPos",
    "SetWindowPlacement",
    "MoveWindow",
    "AttachThreadInput",
    "SendMessageW",
    "SendMessageTimeoutW",
    "PostMessageW",
    "OpenClipboard",
    "EmptyClipboard",
    "SetClipboardData",
)

# Tier 2 — UI automation: input injection + foreground activation, usable
# ONLY after grant_ui_automation_consent() for this run (Rule 00).
_CONSENT_GATED_USER32 = frozenset(
    {
        "SendInput",
        "SetCursorPos",
        "mouse_event",
        "keybd_event",
        "SetForegroundWindow",
        "ShowWindow",
    }
)

# Lock screen — automation is always barred, consent or not (Rule 00).
BARRED_AUTOMATION_PROCESSES = frozenset({"lockapp.exe"})

_ui_consent = False


def grant_ui_automation_consent() -> None:
    """Record that the operator granted consent for UI automation THIS run.

    The CLI calls this only when the user passed ``--permit-ui-automation``
    after being asked directly. The flag is process memory only — it is
    never written to disk or config, so every new run starts read-only.
    """
    global _ui_consent
    _ui_consent = True


def has_ui_consent() -> bool:
    return _ui_consent


def require_ui_consent(action: str) -> None:
    """Raise :class:`SafetyViolation` unless consent was granted this run."""
    if not _ui_consent:
        raise SafetyViolation(
            f"UI automation blocked ({action}): per-run user consent required. "
            "Ask the user for permission, then re-run with "
            "--permit-ui-automation."
        )


def assert_automation_target(process_name: str) -> None:
    """Barred targets (LockApp.exe) may never receive automation, ever."""
    if process_name.lower() in BARRED_AUTOMATION_PROCESSES:
        raise SafetyViolation(
            f"{process_name} is barred from all UI automation (it locks the "
            "system and cannot be inspected as a result) — lock screen "
            "customization is research-only, never live-automated."
        )


_user32: ctypes.WinDLL | None = None
_kernel32: ctypes.WinDLL | None = None


def get_user32_function(name: str):
    """Return a user32 function allowed in the current consent tier.

    Tier 1 (read-only) functions return immediately. Tier 2 (consent-gated
    UI automation) functions additionally require
    :func:`require_ui_consent`. Anything else raises.
    """
    if name in _USER32_READ_ONLY:
        pass
    elif name in _CONSENT_GATED_USER32:
        require_ui_consent(name)
    else:
        raise SafetyViolation(
            f"blocked non-read-only user32 function: {name} "
            "(xaml_inspect may only query, or inject input after "
            "explicit per-run user consent)"
        )
    global _user32
    if _user32 is None:
        _user32 = ctypes.WinDLL("user32", use_last_error=True)
    return getattr(_user32, name)


def get_kernel32_function(name: str):
    """Return a kernel32 function *only* if it is on the read-only whitelist."""
    if name not in _KERNEL32_READ_ONLY:
        raise SafetyViolation(f"blocked non-read-only kernel32 function: {name}")
    global _kernel32
    if _kernel32 is None:
        _kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    return getattr(_kernel32, name)
