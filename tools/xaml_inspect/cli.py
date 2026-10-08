"""Command-line interface for the headless UWP / WinUI 3 tree inspector.

Read-only by default: window enumeration, UIA property reads, and tree
walks only — no input is ever sent. Opening a surface or clicking is
tier-2 UI automation, available solely with the user's explicit per-run
consent (``--permit-ui-automation``, Rule 00). The agent must ask the
user directly before each such run; consent is never stored.
"""

from __future__ import annotations

import argparse
import re
import sys
from typing import List, Optional

from . import activate, processes, safety, windows
from .render import ProcessCapture, WindowCapture, render
from .uia import UIASession
from .walk import make_predicate, prune, walk


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="inspect_xaml",
        description=(
            "Headless visual tree inspector for UWP / WinUI 3 shell "
            "surfaces. Dumps element trees as text, JSON, or Markdown. "
            "Read-only by default; opening surfaces or clicking requires "
            "explicit per-run consent via --permit-ui-automation "
            "(Rule 00), enforced at runtime."
        ),
    )
    parser.add_argument(
        "-p",
        "--process",
        action="append",
        dest="processes",
        metavar="NAME",
        help=(
            "target process name (repeatable). Must be one of: "
            + ", ".join(processes.TARGET_PROCESSES)
            + ". Default: all approved targets that are running."
        ),
    )
    parser.add_argument(
        "--pid",
        type=int,
        help="inspect a single PID instead of resolving by process name "
        "(must still belong to an approved target process).",
    )
    parser.add_argument(
        "--window-class",
        action="append",
        dest="window_classes",
        metavar="CLASS",
        help="only inspect top-level windows with this class name (repeatable, e.g. Shell_TrayWnd).",
    )
    parser.add_argument(
        "--window-title",
        metavar="REGEX",
        help="only inspect top-level windows whose title matches this regex.",
    )
    parser.add_argument(
        "--visible-only",
        action="store_true",
        help="skip hidden top-level windows (default: include hidden windows "
        "so closed surfaces like Start menu can be inspected without opening them).",
    )
    parser.add_argument(
        "-d",
        "--max-depth",
        type=int,
        default=0,
        metavar="N",
        help="maximum tree depth to descend (0 = unlimited, default 0).",
    )
    parser.add_argument(
        "-n",
        "--max-nodes",
        type=int,
        default=5000,
        metavar="N",
        help="node budget per window (default 5000).",
    )
    parser.add_argument(
        "-f",
        "--filter",
        metavar="REGEX",
        help="keep elements whose name / className / automationId / "
        "controlType / frameworkId matches this regex (matching nodes keep "
        "their subtree; ancestors are kept for context).",
    )
    parser.add_argument(
        "--framework",
        metavar="SUBSTR",
        help="keep only elements whose frameworkId contains this substring "
        "(e.g. 'XAML' or 'WinUI'), case-insensitive.",
    )
    parser.add_argument(
        "-o",
        "--output",
        metavar="FILE",
        help="write to FILE instead of stdout.",
    )
    parser.add_argument(
        "--format",
        choices=("text", "json", "markdown"),
        default="text",
        help="output format (default: text).",
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="list matching processes and their top-level windows, then exit "
        "(no tree walk).",
    )
    parser.add_argument(
        "--permit-ui-automation",
        action="store_true",
        help="grant THIS RUN consent for UI automation: opening surfaces "
        "via keyboard shortcuts and synthetic clicks (Rule 00). The agent "
        "must ask the user directly before each such run; consent is never "
        "stored between runs. LockApp.exe / the lock screen is never "
        "automated.",
    )
    parser.add_argument(
        "--open-surface",
        action="append",
        dest="open_surfaces",
        metavar="SURFACE",
        choices=sorted(activate.SURFACES),
        help="open a shell surface before inspection, then best-effort "
        "close it with Escape afterwards (repeatable; requires "
        "--permit-ui-automation). Choices: "
        + ", ".join(sorted(activate.SURFACES))
        + ".",
    )
    parser.add_argument(
        "--click",
        nargs=2,
        type=int,
        metavar=("X", "Y"),
        help="left-click at screen pixel (X, Y) before inspection, for "
        "surfaces with no keyboard shortcut (requires "
        "--permit-ui-automation); the cursor is left at that position.",
    )
    parser.add_argument(
        "--leave-open",
        action="store_true",
        help="do not send Escape to close surfaces opened by this run "
        "(default: close them after capture).",
    )
    return parser


def _resolve_targets(args) -> List[tuple[str, int]]:
    """Return (process_name, pid) pairs to inspect."""
    if args.pid:
        names = processes.pid_to_name()
        name = names.get(args.pid)
        if name is None:
            raise safety.SafetyViolation(
                f"pid {args.pid} is not a running process"
            )
        if name.lower() not in {t.lower() for t in processes.TARGET_PROCESSES}:
            raise safety.SafetyViolation(
                f"pid {args.pid} belongs to {name!r}, which is not an "
                "approved inspection target "
                f"(approved: {', '.join(processes.TARGET_PROCESSES)})"
            )
        return [(name, args.pid)]

    resolved = processes.resolve(args.processes)
    return [
        (name, pid)
        for name, pids in sorted(resolved.items())
        for pid in pids
    ]


def main(argv: Optional[List[str]] = None) -> int:
    safety.assert_safe_modules()
    # Element names come from the live shell and may contain emoji or
    # non-cp1252 text; never let console encoding crash the dump.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError):
            pass
    args = build_parser().parse_args(argv)

    filter_pattern = None
    if args.filter:
        try:
            filter_pattern = re.compile(args.filter, re.IGNORECASE)
        except re.error as exc:
            print(f"error: invalid --filter regex: {exc}", file=sys.stderr)
            return 2

    # --- Consent gate (Rule 00): UI automation only on explicit request ---
    automation_requested = bool(args.open_surfaces) or args.click is not None
    if automation_requested and not args.permit_ui_automation:
        print(
            "error: --open-surface/--click are UI automation and require "
            "the user's explicit permission. Ask the user directly, then "
            "re-run with --permit-ui-automation (Rule 00). Without it the "
            "inspector stays strictly read-only.",
            file=sys.stderr,
        )
        return 3
    if args.permit_ui_automation:
        safety.grant_ui_automation_consent()
        print(
            "UI automation consent active for this run "
            "(--permit-ui-automation).",
            file=sys.stderr,
        )
    if automation_requested:
        # LockApp.exe / lock screen: never automated, no exceptions.
        try:
            for name in args.processes or ():
                safety.assert_automation_target(name)
            if args.pid:
                name = processes.pid_to_name().get(args.pid)
                if name is not None:
                    safety.assert_automation_target(name)
        except safety.SafetyViolation as exc:
            print(f"safety violation: {exc}", file=sys.stderr)
            return 3

    opened: List[str] = []
    try:
        # --- Automation phase: runs BEFORE target resolution so surfaces
        # that spawn their host process are visible to the walk. ---
        for surface in args.open_surfaces or ():
            label = activate.open_surface(surface)
            opened.append(surface)
            print(f"opened: {label}", file=sys.stderr)
        if args.click is not None:
            activate.click(args.click[0], args.click[1])
            opened.append("click")
            print(
                f"clicked at ({args.click[0]}, {args.click[1]})",
                file=sys.stderr,
            )

        try:
            targets = _resolve_targets(args)
        except safety.SafetyViolation as exc:
            print(f"safety violation: {exc}", file=sys.stderr)
            return 3

        if not targets:
            print("no approved target processes are running.", file=sys.stderr)
            return 1

        # Window enumeration (query-only).
        per_process: List[tuple[str, int, List[windows.WindowInfo]]] = []
        for name, pid in targets:
            wins = windows.filter_windows(
                windows.list_windows_for_pid(pid),
                class_names=args.window_classes,
                title_regex=args.window_title,
                visible_only=args.visible_only,
            )
            per_process.append((name, pid, wins))

        if args.list:
            for name, pid, wins in per_process:
                print(f"{name} (pid {pid}): {len(wins)} top-level window(s)")
                for w in wins:
                    flags = "visible" if w.visible else "hidden"
                    print(
                        f"  {w.hex_hwnd}  cls={w.class_name:<30} "
                        f"[{flags}] {w.title!r}"
                    )
            return 0

        predicate = make_predicate(filter_pattern, args.framework)

        try:
            session = UIASession()
        except RuntimeError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1

        captures: List[ProcessCapture] = []
        for name, pid, wins in per_process:
            capture = ProcessCapture(name=name, pid=pid)
            for w in wins:
                cap = WindowCapture(window=w, root=None)
                try:
                    root_el = session.element_from_hwnd(w.hwnd)
                    root, truncated = walk(
                        session,
                        root_el,
                        max_depth=args.max_depth,
                        max_nodes=args.max_nodes,
                    )
                    if predicate is not None:
                        kept = prune(root, predicate)
                        root = kept  # None means no matches in this window
                    cap.root = root
                    cap.truncated = truncated
                except Exception as exc:  # COM / provider failures per window
                    cap.error = f"{type(exc).__name__}: {exc}"
                capture.windows.append(cap)
            captures.append(capture)

        output = render(captures, args.format)
        if args.output:
            with open(args.output, "w", encoding="utf-8") as fh:
                fh.write(output + "\n")
            total = sum(c.node_count for p in captures for c in p.windows)
            print(
                f"wrote {args.output} ({total} elements across "
                f"{len(captures)} process(es))",
                file=sys.stderr,
            )
        else:
            print(output)
        return 0
    finally:
        # Best-effort restore: one Escape closes what this run opened,
        # unless the operator asked to leave it open.
        if opened and not args.leave_open:
            try:
                activate.press_escape()
                print(
                    "closed opened surface(s) with Escape "
                    "(--leave-open to skip)",
                    file=sys.stderr,
                )
            except (safety.SafetyViolation, OSError):
                pass


if __name__ == "__main__":
    raise SystemExit(main())
