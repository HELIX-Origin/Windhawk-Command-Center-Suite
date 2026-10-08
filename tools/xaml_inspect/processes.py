"""Target process discovery for ``xaml_inspect``.

Only the suite's seven approved inspection targets are ever resolved
(Rule 01 runtime boundary). Enumeration uses the Toolhelp32 process
snapshot — a read-only kernel32 query.
"""

from __future__ import annotations

import ctypes
from ctypes import wintypes
from typing import Dict, List, Sequence

from . import safety

# The approved inspection targets (UIA reads only; never acted upon).
TARGET_PROCESSES: tuple[str, ...] = (
    "StartMenuExperienceHost.exe",
    "SearchHost.exe",
    "SearchApp.exe",
    "LockApp.exe",
    "ShellExperienceHost.exe",
    "ShellHost.exe",
    "explorer.exe",
)

TH32CS_SNAPPROCESS = 0x00000002
ERROR_NO_MORE_FILES = 18


class _ProcessEntry(ctypes.Structure):
    _fields_ = [
        ("dwSize", wintypes.DWORD),
        ("cntUsage", wintypes.DWORD),
        ("th32ProcessID", wintypes.DWORD),
        ("th32DefaultHeapID", ctypes.c_size_t),
        ("th32ModuleID", wintypes.DWORD),
        ("cntThreads", wintypes.DWORD),
        ("th32ParentProcessID", wintypes.DWORD),
        ("pcPriClassBase", ctypes.c_long),
        ("dwFlags", wintypes.DWORD),
        ("szExeFile", ctypes.c_wchar * 260),
    ]


def snapshot_processes() -> Dict[str, List[int]]:
    """Return ``{process_name_lower: [pids...]}`` for every running process."""
    create = safety.get_kernel32_function("CreateToolhelp32Snapshot")
    first = safety.get_kernel32_function("Process32FirstW")
    nxt = safety.get_kernel32_function("Process32NextW")
    close = safety.get_kernel32_function("CloseHandle")

    snap = create(TH32CS_SNAPPROCESS, 0)
    if snap in (0, ctypes.c_void_p(-1).value):
        raise OSError("CreateToolhelp32Snapshot failed")

    result: Dict[str, List[int]] = {}
    try:
        entry = _ProcessEntry()
        entry.dwSize = ctypes.sizeof(_ProcessEntry)
        ok = first(snap, ctypes.byref(entry))
        while ok:
            name = entry.szExeFile.lower()
            result.setdefault(name, []).append(entry.th32ProcessID)
            entry.dwSize = ctypes.sizeof(_ProcessEntry)
            ok = nxt(snap, ctypes.byref(entry))
    finally:
        close(snap)
    return result


def resolve(targets: Sequence[str] | None = None) -> Dict[str, List[int]]:
    """Resolve approved target process names to running PIDs.

    Returns ``{process_name: [pids...]}`` (original casing), including
    only processes that are currently running. Raises
    :class:`safety.SafetyViolation` for names outside the approved list.
    """
    wanted = list(targets) if targets else list(TARGET_PROCESSES)
    for name in wanted:
        if name.lower() not in {t.lower() for t in TARGET_PROCESSES}:
            raise safety.SafetyViolation(
                f"process not in the approved inspection target list: {name!r} "
                f"(approved: {', '.join(TARGET_PROCESSES)})"
            )
    snapshot = snapshot_processes()
    result: Dict[str, List[int]] = {}
    for name in wanted:
        pids = snapshot.get(name.lower())
        if pids:
            result[name] = sorted(pids)
    return result


def pid_to_name() -> Dict[int, str]:
    """Return ``{pid: process_name}`` for all running processes."""
    result: Dict[int, str] = {}
    for name, pids in snapshot_processes().items():
        for pid in pids:
            result[pid] = name
    return result
