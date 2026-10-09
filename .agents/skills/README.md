# 🧠 Agent Technical Skills & Domain Guides (`.agents/skills/`)

This directory contains technical skill guides, visual tree domain architectures, and styling recipes for **Windhawk Theme Engineering**.

---

## 📋 Skills Catalog

| Skill | Target Domain | Core Focus | Guide File |
|---|---|---|---|
| **Windhawk Styler Engineering** | Core Engine | Dynamic visual tree hook, selector resolution, precedence | [windhawk-styler-engineering](windhawk-styler-engineering.md) |
| **Glass Material & Chrome Recipes** | Visual Aesthetics | `WindhawkBlur`, `AcrylicBrush`, gradient rims, inner resets | [glass-material-recipes](glass-material-recipes.md) |
| **Notification Center Theming** | Surface S1 | UWP visual tree, Quick Settings, calendar, media, jump lists | [notification-center-theming](notification-center-theming.md) |
| **File Explorer Theming** *(deferred — reference)* | Surface S2 | WinUI 3 tabs, nav bar, command bar, Win32 file list boundary | [file-explorer-theming](file-explorer-theming.md) |
| **Settings Theming** | Surface S5 | UWP/WinUI Settings cards, navigation pane, search pill | [settings-theming](settings-theming.md) |
| **Live Visual Inspection** | Tooling | Hybrid C++/Python XAML inspector, automated surface activation, ShareX screenshots | [live-visual-inspection](live-visual-inspection.md) |

---

## 🗺️ Subsystem Architecture Mapping

```mermaid
flowchart TD
    Suite["Windhawk Theme Suite"] --> Engine["Windhawk Styler Engineering"]
    Suite --> Glass["Glass Material & Chrome Recipes"]
    Suite --> NC["Notification Center Theming"]
    Suite --> Settings["Settings Theming"]
    Suite --> FE["File Explorer Theming (deferred)"]
    Suite --> Inspect["Live Visual Inspection"]
```
