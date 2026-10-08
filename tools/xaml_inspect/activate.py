"""Consent-gated UI automation: opening shell surfaces for inspection.

Every function in this module is **tier 2** in the safety contract
(``safety.py``): input injection that only works after
:func:`safety.grant_ui_automation_consent`, which the CLI sets exclusively
when the user passes ``--permit-ui-automation`` for that run (Rule 00).
The agent must ask the user immediately before each consented run — never
automatic, never unattended, never stored between runs.

Keyboard shortcuts (Windows 11):

- ``start``               — Win
- ``search``              — Win+S
- ``action-center``       — Win+A  (Quick Settings / Action Center)
- ``notification-center`` — Win+N

Surfaces with no keyboard shortcut are reached with :func:`click` at
pixel coordinates (e.g. from a previous dump's bounding rects).

``LockApp.exe`` / the lock screen is **barred from all automation** (it
locks the system and cannot be inspected as a result) — there is no
lock-screen surface here, and :func:`safety.assert_automation_target`
refuses explicit LockApp targeting. Lock screen customization is
research-only (Rule 04 sources).
"""

from __future__ import annotations

import ctypes
import time
from ctypes import wintypes
from typing import Dict, Sequence, Tuple

from . import safety

__all__ = [
    "SURFACES",
    "open_surface",
    "press_escape",
    "click",
]

# --- virtual keys -----------------------------------------------------------
VK_LWIN = 0x5B
VK_S = 0x53
VK_A = 0x41
VK_N = 0x4E
VK_ESCAPE = 0x1B

# --- SendInput plumbing -----------------------------------------------------
ULONG_PTR = ctypes.c_size_t

INPUT_KEYBOARD = 1
KEYEVENTF_KEYUP = 0x0002
MOUSEEVENTF_LEFTDOWN = 0x0002
MOUSEEVENTF_LEFTUP = 0x0004

# Delay between key transitions so the shell registers chords, and after a
# surface opens so its window exists before the walk starts.
_HOLD_SECONDS = 0.05
_SETTLE_SECONDS = 0.8


class KEYBDINPUT(ctypes.Structure):
    _fields_ = [
        ("wVk", wintypes.WORD),
        ("wScan", wintypes.WORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG),
        ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD),
        ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class HARDWAREINPUT(ctypes.Structure):
    _fields_ = [
        ("uMsg", wintypes.DWORD),
        ("wParamL", wintypes.WORD),
        ("wParamH", wintypes.WORD),
    ]


class _INPUTUNION(ctypes.Union):
    _fields_ = [("mi", MOUSEINPUT), ("ki", KEYBDINPUT), ("hi", HARDWAREINPUT)]


class INPUT(ctypes.Structure):
    _anonymous_ = ("u",)
    _fields_ = [("type", wintypes.DWORD), ("u", _INPUTUNION)]


# --- surface registry -------------------------------------------------------
# name -> (label, key chord as virtual keys pressed in order, host process)
SURFACES: Dict[str, Tuple[str, Tuple[int, ...], str]] = {
    "start": ("Start menu", (VK_LWIN,), "StartMenuExperienceHost.exe"),
    "search": ("Search", (VK_LWIN, VK_S), "SearchHost.exe"),
    "action-center": (
        "Quick Settings / Action Center",
        (VK_LWIN, VK_A),
        "ShellExperienceHost.exe",
    ),
    "notification-center": (
        "Notification Center",
        (VK_LWIN, VK_N),
        "ShellHost.exe",
    ),
}

# Never automated under any consent level (Rule 00).
BARRED_SURFACES = frozenset({"lock", "lock screen", "lockscreen", "lockapp"})


def _send_chord(vks: Sequence[int]) -> None:
    """Press every key in order, then release in reverse order."""
    send_input = safety.get_user32_function("SendInput")
    send_input.argtypes = [
        ctypes.c_uint,
        ctypes.POINTER(INPUT),
        ctypes.c_int,
    ]
    send_input.restype = ctypes.c_uint

    def _one(vk: int, up: bool) -> None:
        inp = INPUT(type=INPUT_KEYBOARD)
        inp.ki = KEYBDINPUT(
            wVk=vk,
            wScan=0,
            dwFlags=KEYEVENTF_KEYUP if up else 0,
            time=0,
            dwExtraInfo=0,
        )
        if send_input(1, ctypes.byref(inp), ctypes.sizeof(INPUT)) != 1:
            raise OSError(
                "SendInput inserted no events (input may be blocked by an "
                "elevated/secure window — UIPI)"
            )
        time.sleep(_HOLD_SECONDS)

    for vk in vks:
        _one(vk, up=False)
    for vk in reversed(vks):
        _one(vk, up=True)


def open_surface(name: str) -> str:
    """Open a shell surface via its keyboard shortcut. Returns its label.

    Consent-gated: raises :class:`safety.SafetyViolation` unless
    ``--permit-ui-automation`` granted consent for this run.
    """
    key = name.strip().lower()
    if key in BARRED_SURFACES:
        raise safety.SafetyViolation(
            f"surface {name!r} is barred from all UI automation: the lock "
            "screen locks the system and cannot be inspected as a result — "
            "lock screen customization is research-only (Rule 00)."
        )
    safety.require_ui_consent(f"open surface '{name}'")
    if key not in SURFACES:
        raise safety.SafetyViolation(
            f"unknown surface {name!r} (available: {', '.join(sorted(SURFACES))})"
        )
    label, chord, _host = SURFACES[key]
    _send_chord(chord)
    time.sleep(_SETTLE_SECONDS)
    return label


def press_escape() -> None:
    """Best-effort close of whatever surface this run opened."""
    safety.require_ui_consent("press Escape")
    _send_chord((VK_ESCAPE,))
    time.sleep(_HOLD_SECONDS)


def click(x: int, y: int) -> None:
    """Move the cursor to ``(x, y)`` and left-click. Consent-gated.

    Used only for surfaces with no keyboard shortcut. The cursor is left
    at the click position (documented in ``tools/README.md``).
    """
    safety.require_ui_consent(f"mouse click at ({x}, {y})")

    set_cursor_pos = safety.get_user32_function("SetCursorPos")
    set_cursor_pos.argtypes = [ctypes.c_int, ctypes.c_int]
    set_cursor_pos.restype = wintypes.BOOL
    if not set_cursor_pos(x, y):
        raise OSError(f"SetCursorPos({x}, {y}) failed")

    mouse_event = safety.get_user32_function("mouse_event")
    mouse_event.argtypes = [
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.DWORD,
        wintypes.DWORD,
        ULONG_PTR,
    ]
    mouse_event.restype = None

    time.sleep(_HOLD_SECONDS)
    mouse_event(MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    time.sleep(_HOLD_SECONDS)
    mouse_event(MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    time.sleep(_SETTLE_SECONDS)
