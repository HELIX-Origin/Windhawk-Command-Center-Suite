#!/usr/bin/env python3
"""Launcher for the headless UWP / WinUI 3 visual tree inspector.

Usage examples:

    python tools/inspect_xaml.py --list
    python tools/inspect_xaml.py -p explorer.exe --window-class Shell_TrayWnd
    python tools/inspect_xaml.py -p ShellHost.exe -f NotificationCenter
    python tools/inspect_xaml.py -p StartMenuExperienceHost.exe --format json -o out.json

Read-only by contract — see tools/xaml_inspect/safety.py.
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from xaml_inspect.cli import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
