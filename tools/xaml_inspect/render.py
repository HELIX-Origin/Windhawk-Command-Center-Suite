"""Output renderers: text tree, JSON, Markdown."""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import List, Optional

from .walk import Node, count_nodes
from .windows import WindowInfo


@dataclass
class WindowCapture:
    """Captured tree for one top-level window."""

    window: WindowInfo
    root: Optional[Node]
    truncated: bool = False
    error: Optional[str] = None

    @property
    def node_count(self) -> int:
        return count_nodes(self.root) if self.root else 0


@dataclass
class ProcessCapture:
    """Captured data for one inspected process."""

    name: str
    pid: int
    windows: List[WindowCapture] = field(default_factory=list)


def _line(data) -> str:  # noqa: ANN001
    parts = [f"{data.control_type}", f"[{data.selector}]"]
    if data.framework_id:
        parts.append(f"fw={data.framework_id}")
    if data.name:
        quoted = data.name if len(data.name) <= 60 else data.name[:57] + "..."
        parts.append(f'name="{quoted}"')
    if data.rect:
        parts.append(
            "rect=({:.0f},{:.0f},{:.0f},{:.0f})".format(*data.rect)
        )
    if data.offscreen:
        parts.append("offscreen")
    return "  ".join(parts)


def render_tree(captures: List[ProcessCapture]) -> str:
    """Human-readable indented tree."""
    out: List[str] = []
    for proc in captures:
        out.append(f"=== {proc.name} (pid {proc.pid}) ===")
        if not proc.windows:
            out.append("  (no top-level windows found)")
        for cap in proc.windows:
            w = cap.window
            flags = "visible" if w.visible else "hidden"
            out.append(
                f"  --- hwnd {w.hex_hwnd} cls={w.class_name} "
                f"[{flags}] title={w.title!r} ---"
            )
            if cap.error:
                out.append(f"    ERROR: {cap.error}")
                continue
            if cap.root is None:
                out.append("    (no elements matched the filter)")
                continue
            lines = ["    " + _line(cap.root.data)]
            stack = [(cap.root, 1)]
            while stack:
                node, depth = stack.pop()
                for child in node.children:
                    lines.append(
                        "    " + "  " * depth + _line(child.data)
                    )
                stack.extend(
                    (child, depth + 1) for child in reversed(node.children)
                )
            out.extend(lines)
            if cap.truncated:
                out.append(
                    "    ... [truncated: node budget reached — "
                    "narrow with --filter / --window-class / --depth]"
                )
            out.append(f"    ({cap.node_count} elements)")
        out.append("")
    return "\n".join(out)


def _node_to_dict(node: Node) -> dict:
    d = node.data
    return {
        "controlType": d.control_type,
        "selector": d.selector,
        "className": d.class_name,
        "automationId": d.automation_id,
        "name": d.name,
        "frameworkId": d.framework_id,
        "rect": d.rect,
        "offscreen": d.offscreen,
        "children": [_node_to_dict(c) for c in node.children],
    }


def render_json(captures: List[ProcessCapture]) -> str:
    payload = []
    for proc in captures:
        windows = []
        for cap in proc.windows:
            windows.append(
                {
                    "hwnd": cap.window.hex_hwnd,
                    "className": cap.window.class_name,
                    "title": cap.window.title,
                    "visible": cap.window.visible,
                    "error": cap.error,
                    "truncated": cap.truncated,
                    "nodeCount": cap.node_count,
                    "root": _node_to_dict(cap.root) if cap.root else None,
                }
            )
        payload.append(
            {"process": proc.name, "pid": proc.pid, "windows": windows}
        )
    return json.dumps(payload, indent=2, ensure_ascii=False)


def render_markdown(captures: List[ProcessCapture]) -> str:
    out: List[str] = ["# Visual Tree Capture", ""]
    for proc in captures:
        out.append(f"## {proc.name} (pid {proc.pid})")
        out.append("")
        for cap in proc.windows:
            w = cap.window
            flags = "visible" if w.visible else "hidden"
            out.append(
                f"### hwnd {w.hex_hwnd} — `{w.class_name}` [{flags}] {w.title!r}"
            )
            out.append("")
            if cap.error:
                out.append(f"> ERROR: {cap.error}")
                out.append("")
                continue
            if cap.root is None:
                out.append("> (no elements matched the filter)")
                out.append("")
                continue

            def walk_md(node: Node, depth: int) -> None:
                bullet = "  " * depth + "- "
                out.append(f"{bullet}`{_line(node.data)}`")
                for child in node.children:
                    walk_md(child, depth + 1)

            walk_md(cap.root, 0)
            if cap.truncated:
                out.append("")
                out.append("> **Truncated**: node budget reached.")
            out.append("")
    return "\n".join(out)


def render(captures: List[ProcessCapture], fmt: str) -> str:
    if fmt == "json":
        return render_json(captures)
    if fmt == "markdown":
        return render_markdown(captures)
    return render_tree(captures)
