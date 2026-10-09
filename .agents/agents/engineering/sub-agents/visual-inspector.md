# Visual Inspector Agent (Sub-Agent)

**Parent Primary**: [Style Architect](../style-architect.md)  
**Focus**: Engineering

The **Visual Inspector Agent** is responsible for visual tree auditing, selector discovery, and translating diagnostic logs into strict target evidence records.

---

## Domain Responsibilities

1. **Hybrid XAML Inspection**: Operates the hybrid inspector (`python tools/inspect_xaml.py` driving `tools/native/bin/xaml_dump.exe`) to capture live, fully populated UWP and WinUI visual trees without manual UWPSpy burden.
2. **Automated Surface Activation**: Coordinates surface opening (`start`, `action-center`, `notification-center`, `search`) and auto-clean closure via UI automation.
3. **ShareX Screenshot Auditing**: Utilizes `--screenshot` (`-ss`) to capture live desktop state during surface inspection, respecting the user's custom ShareX keybinds (`HotkeysConfig.json`).
4. **Selector Extraction**: Analyzes live visual tree elements (names, types, parent-child relations) and maps them into concise, robust XAML selectors.
5. **Rule 04 Compliance**: Verifies that every proposed selector has a corresponding evidence entry in `.agents/targets/` before code generation begins.
6. **Collision Detection**: Identifies broad selectors that risk unintentionally matching controls outside the intended scope.
