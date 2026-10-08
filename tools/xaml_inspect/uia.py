"""UI Automation session: element acquisition and property reads.

Wraps the COM UIA3 API (``UIAutomationCore.dll``) behind the
:mod:`xaml_inspect.safety` call whitelist. Every method call this
module makes is gated by ``safety.assert_uia_call``; property reads
(``Current*``) are pure getters supplied by the UIA provider.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, List, Optional

from . import safety

# Standard UIA control type ids (stable, documented by Microsoft).
CONTROL_TYPES: dict[int, str] = {
    50000: "Button",
    50001: "Calendar",
    50002: "CheckBox",
    50003: "ComboBox",
    50004: "Edit",
    50005: "Hyperlink",
    50006: "Image",
    50007: "ListItem",
    50008: "List",
    50009: "Menu",
    50010: "MenuBar",
    50011: "MenuItem",
    50012: "ProgressBar",
    50013: "RadioButton",
    50014: "ScrollBar",
    50015: "Slider",
    50016: "Spinner",
    50017: "StatusBar",
    50018: "Tab",
    50019: "TabItem",
    50020: "Text",
    50021: "ToolBar",
    50022: "ToolTip",
    50023: "Tree",
    50024: "TreeItem",
    50025: "Custom",
    50026: "Group",
    50027: "Thumb",
    50028: "DataGrid",
    50029: "DataItem",
    50030: "Document",
    50031: "SplitButton",
    50032: "Window",
    50033: "Pane",
    50034: "Header",
    50035: "HeaderItem",
    50036: "Table",
    50037: "TitleBar",
    50038: "Separator",
    50039: "SemanticZoom",
    50040: "AppBar",
}


def _control_type_name(type_id: int) -> str:
    return CONTROL_TYPES.get(type_id, f"Unknown({type_id})")


@dataclass
class ElementData:
    """Observed UIA properties of a single element (raw, no synthesis)."""

    control_type_id: int
    control_type: str
    class_name: str
    automation_id: str
    name: str
    framework_id: str
    rect: Optional[List[float]]
    offscreen: Optional[bool]

    @property
    def selector(self) -> str:
        """Windhawk-style selector candidate derived from observed fields.

        Built strictly from ``ClassName`` + ``AutomationId`` as reported
        live by the UIA provider — both values are evidence, not guesses.
        """
        if self.class_name and self.automation_id:
            return f"{self.class_name}#{self.automation_id}"
        if self.class_name:
            return self.class_name
        if self.automation_id:
            return f"#{self.automation_id}"
        return self.control_type


def _safe(getter, default=None):  # noqa: ANN001
    """Run a UIA property getter, returning ``default`` on COM failure."""
    try:
        value = getter()
        return default if value is None else value
    except Exception:
        return default


class UIASession:
    """A read-only UIA3 session bound to this (agent's) process only."""

    def __init__(self) -> None:
        safety.assert_safe_modules()
        try:
            import comtypes.client
        except ImportError as exc:  # pragma: no cover - environment dependent
            raise RuntimeError(
                "the 'comtypes' package is required (pip install comtypes)"
            ) from exc

        self._mod = comtypes.client.GetModule("UIAutomationCore.dll")

        # CUIAutomation8 (Win10+) is required for IUIAutomation2 timeouts;
        # its default interface is still IUIAutomation.
        self._auto = None
        for coclass_name, iface_name in (
            ("CUIAutomation8", "IUIAutomation"),
            ("CUIAutomation", "IUIAutomation"),
        ):
            coclass = getattr(self._mod, coclass_name, None)
            iface = getattr(self._mod, iface_name, None)
            if coclass is None or iface is None:
                continue
            try:
                self._auto = comtypes.client.CreateObject(coclass, interface=iface)
                break
            except Exception:
                continue
        if self._auto is None:
            raise RuntimeError("failed to create the UIA3 automation object")

        safety.assert_uia_call("CreateTrueCondition")
        self._true_condition = self._auto.CreateTrueCondition()

        # Bound every UIA round-trip so a wedged provider (e.g. idle
        # SystemUserAdapterWindowClass) fails fast instead of hanging
        # the whole run. IUIAutomation2::ResponseTimeout is in ms.
        try:
            auto2 = self._auto.QueryInterface(self._mod.IUIAutomation2)
            auto2.ConnectionTimeout = 3000
            auto2.ResponseTimeout = 3000
        except Exception:
            pass  # older client: timeouts unavailable, best effort only

        # TreeScope_Children == 2 (UIAutomationClient.h); prefer the
        # generated enum when the typelib exposed it.
        scope = getattr(self._mod, "TreeScope_Children", None)
        if scope is None:
            scope = getattr(self._mod, "UIA_TreeScope_Children", None)
        self._scope_children = int(scope) if scope is not None else 2

    # -- element acquisition ------------------------------------------------

    def element_from_hwnd(self, hwnd: int):
        """Return the root UIA element for a top-level window handle."""
        safety.assert_uia_call("ElementFromHandle")
        return self._auto.ElementFromHandle(int(hwnd))

    def children(self, element) -> List[Any]:
        """Return the direct children of ``element`` (document order)."""
        safety.assert_uia_call("FindAll")
        array = element.FindAll(self._scope_children, self._true_condition)
        if array is None:
            return []
        if hasattr(array, "Length") and hasattr(array, "GetElement"):
            return [array.GetElement(i) for i in range(int(array.Length))]
        return list(array)

    # -- property reads -----------------------------------------------------

    def read(self, element) -> ElementData:
        """Read the observed UIA properties of ``element``."""
        ct_id = _safe(lambda: int(element.CurrentControlType), 0)
        rect_raw = _safe(lambda: element.CurrentBoundingRectangle)
        rect: Optional[List[float]] = None
        if rect_raw is not None:
            try:
                rect = [
                    float(rect_raw.left),
                    float(rect_raw.top),
                    float(rect_raw.right),
                    float(rect_raw.bottom),
                ]
            except AttributeError:
                try:
                    rect = [float(v) for v in rect_raw]
                except Exception:
                    rect = None

        offscreen = _safe(lambda: element.CurrentIsOffscreen)
        return ElementData(
            control_type_id=ct_id,
            control_type=_control_type_name(ct_id),
            class_name=str(_safe(lambda: element.CurrentClassName, "") or ""),
            automation_id=str(_safe(lambda: element.CurrentAutomationId, "") or ""),
            name=str(_safe(lambda: element.CurrentName, "") or ""),
            framework_id=str(_safe(lambda: element.CurrentFrameworkId, "") or ""),
            rect=rect,
            offscreen=None if offscreen is None else bool(offscreen),
        )
