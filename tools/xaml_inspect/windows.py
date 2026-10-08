"""Top-level window enumeration for ``xaml_inspect``.

Purely observational: ``EnumWindows`` + window property queries through
the safety whitelist. No window is ever activated, shown, hidden, moved,
or messaged.
"""

from __future__ import annotations

import ctypes
from ctypes import wintypes
from dataclasses import dataclass
from typing import Dict, List, Optional

from . import safety


@dataclass(frozen=True)
class WindowInfo:
    """A top-level window belonging to an inspected process."""

    hwnd: int
    pid: int
    class_name: str
    title: str
    visible: bool

    @property
    def hex_hwnd(self) -> str:
        return f"0x{self.hwnd:08X}"


def list_windows_for_pid(pid: int) -> List[WindowInfo]:
    """Enumerate every top-level window owned by ``pid`` (query-only).

    ``EnumWindows`` only reports top-level desktop windows; idle shell
    hosts (LockApp, SearchHost, StartMenuExperienceHost, ...) often keep
    their window as a child of the message-only ``HWND_MESSAGE`` parent.
    Those are enumerated separately via ``FindWindowExW`` so hidden /
    not-yet-opened surfaces remain inspectable without opening them.
    """
    enum_windows = safety.get_user32_function("EnumWindows")
    find_window_ex = safety.get_user32_function("FindWindowExW")
    get_class = safety.get_user32_function("GetClassNameW")
    get_text = safety.get_user32_function("GetWindowTextW")
    is_visible = safety.get_user32_function("IsWindowVisible")
    get_pid = safety.get_user32_function("GetWindowThreadProcessId")

    get_class.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
    get_class.restype = ctypes.c_int
    get_text.argtypes = [wintypes.HWND, wintypes.LPWSTR, ctypes.c_int]
    get_text.restype = ctypes.c_int
    is_visible.argtypes = [wintypes.HWND]
    is_visible.restype = wintypes.BOOL
    get_pid.argtypes = [wintypes.HWND, ctypes.POINTER(wintypes.DWORD)]
    get_pid.restype = wintypes.DWORD
    enum_windows.argtypes = [
        ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM),
        wintypes.LPARAM,
    ]
    enum_windows.restype = wintypes.BOOL
    find_window_ex.argtypes = [
        wintypes.HWND,
        wintypes.HWND,
        wintypes.LPCWSTR,
        wintypes.LPCWSTR,
    ]
    find_window_ex.restype = wintypes.HWND

    found: Dict[int, WindowInfo] = {}

    def record(hwnd: int) -> None:
        owner_pid = wintypes.DWORD(0)
        get_pid(hwnd, ctypes.byref(owner_pid))
        if owner_pid.value != pid:
            return
        class_buf = ctypes.create_unicode_buffer(512)
        get_class(hwnd, class_buf, 512)
        text_buf = ctypes.create_unicode_buffer(512)
        get_text(hwnd, text_buf, 512)
        found[hwnd] = WindowInfo(
            hwnd=hwnd,
            pid=pid,
            class_name=class_buf.value,
            title=text_buf.value,
            visible=bool(is_visible(hwnd)),
        )

    @ctypes.WINFUNCTYPE(wintypes.BOOL, wintypes.HWND, wintypes.LPARAM)
    def callback(hwnd, _lparam):  # noqa: ANN001 - ctypes types
        record(int(hwnd))
        return True

    enum_windows(callback, 0)

    # Message-only windows (HWND_MESSAGE parent = -3, not a real handle).
    hwnd_message = ctypes.c_void_p(-3)
    child = 0
    while True:
        child = find_window_ex(hwnd_message, child, None, None)
        if not child:
            break
        record(int(child))

    return list(found.values())


def filter_windows(
    windows: List[WindowInfo],
    class_names: Optional[List[str]] = None,
    title_regex: Optional[str] = None,
    visible_only: bool = False,
) -> List[WindowInfo]:
    """Apply optional ``--window-class`` / ``--window-title`` / ``--visible-only`` filters."""
    import re

    result = windows
    if class_names:
        wanted = {c.lower() for c in class_names}
        result = [w for w in result if w.class_name.lower() in wanted]
    if title_regex:
        pattern = re.compile(title_regex, re.IGNORECASE)
        result = [w for w in result if pattern.search(w.title)]
    if visible_only:
        result = [w for w in result if w.visible]
    return result
