"""xaml_inspect — headless, read-only UWP / WinUI 3 visual tree inspector.

Programmatically dumps the UI Automation trees of the suite's shell
processes to text / JSON / Markdown so agents can discover and verify
selectors (Rule 04) without UWPSpy, screenshots, or any interaction
with the user's desktop.

**Read-only by contract** — see :mod:`xaml_inspect.safety`. The tool
never injects input, never manipulates windows, and never sends
messages to other processes.
"""
