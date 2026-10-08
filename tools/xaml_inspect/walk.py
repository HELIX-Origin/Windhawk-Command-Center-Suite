"""Depth- and budget-limited visual tree walking with filter pruning."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Callable, List, Optional

from .uia import ElementData, UIASession

Predicate = Callable[[ElementData], bool]


@dataclass
class Node:
    """A node in the captured visual tree."""

    data: ElementData
    children: List["Node"] = field(default_factory=list)


def walk(
    session: UIASession,
    root_element,
    *,
    max_depth: int = 0,
    max_nodes: int = 5000,
) -> tuple[Node, bool]:
    """Walk the tree below ``root_element``.

    ``max_depth == 0`` means unlimited depth. Returns the root
    :class:`Node` plus a ``truncated`` flag (budget exhausted).
    """
    root_data = session.read(root_element)
    root = Node(data=root_data)
    # Stack entries: (element, node, depth). Document order preserved by
    # pushing children in reverse.
    stack: list[tuple[object, Node, int]] = [(root_element, root, 0)]
    count = 1
    truncated = False

    while stack:
        element, node, depth = stack.pop()
        if max_depth and depth >= max_depth:
            continue
        try:
            children = session.children(element)
        except Exception:
            children = []  # provider refused; treat as leaf
        # Append in document order; push in reverse so the first child
        # is expanded first (LIFO).
        child_nodes: list[tuple[object, Node, int]] = []
        for child in children:
            if count >= max_nodes:
                truncated = True
                break
            try:
                data = session.read(child)
            except Exception:
                continue
            child_node = Node(data=data)
            node.children.append(child_node)
            count += 1
            child_nodes.append((child, child_node, depth + 1))
        stack.extend(reversed(child_nodes))
        if truncated:
            break

    return root, truncated


def prune(node: Node, predicate: Predicate) -> Optional[Node]:
    """Keep nodes matching ``predicate``.

    A matching node keeps its **entire subtree** (the interesting part of
    a match is usually below it). Non-matching nodes are kept only when
    they have matching descendants, so context/ancestors survive.
    """
    if predicate(node.data):
        return node
    kept_children: List[Node] = []
    for child in node.children:
        pruned = prune(child, predicate)
        if pruned is not None:
            kept_children.append(pruned)
    if kept_children:
        node.children = kept_children
        return node
    return None


def count_nodes(node: Node) -> int:
    """Total number of nodes in the subtree rooted at ``node``."""
    return 1 + sum(count_nodes(child) for child in node.children)


def make_predicate(
    filter_regex=None,  # noqa: ANN001 - compiled pattern or None
    framework: Optional[str] = None,
) -> Optional[Predicate]:
    """Combine ``--filter`` (regex over observed fields) and ``--framework``."""
    if filter_regex is None and not framework:
        return None
    fw = framework.lower() if framework else None

    def predicate(data: ElementData) -> bool:
        if fw and fw not in data.framework_id.lower():
            return False
        if filter_regex is not None:
            haystacks = (
                data.name,
                data.class_name,
                data.automation_id,
                data.control_type,
                data.framework_id,
            )
            if not any(filter_regex.search(h) for h in haystacks):
                return False
        return True

    return predicate
