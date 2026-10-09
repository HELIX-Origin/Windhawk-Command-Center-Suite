# 📜 Mandatory Agent Rules (`.agents/rules/`)

This directory contains the permanent, non-negotiable architectural, safety, syntax, and design rules governing all automated agents, coding assistants, and contributors working on **Windhawk Theme Repositories**.

---

## 🚦 Enforcement & Rule Hierarchy

1. **Rule 00 (Safety & Compliance)** and **Rule 01 (Zero Unsolicited Injection)** supersede all other implementation decisions without exception.
2. **Rule 03 (Design Language Standards)** and **Rule 05 (Surface Scope Standards)** govern visual fidelity and mod boundaries across the suite.
3. **Rule 04 (Target Evidence Protocol)** strictly forbids unverified or guessed XAML selectors.
4. Every change must pass the static validation gate (`pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1`) before handoff.

---

## 📋 Rules Catalog

| Rule | Title | Scope & Invariants | Specification File |
|---|---|---|---|
| **Rule 00** | Agent Safety, Instruction Compliance & Damage Prevention | Core Safety, Data Protection & System Invariants | [agent-safety-compliance](agent-safety-compliance.md) |
| **Rule 01** | Dependency, Mod & Asset Approval (Zero Unsolicited Injection) | Runtime Boundary — 5 Base Approved Mods (Universal Scope) | [zero-unsolicited-injection](zero-unsolicited-injection.md) |
| **Rule 02** | Windhawk Styler YAML & XAML Syntax Standards | Parser Grammar, Quoting, Constant Order & Styles Format | [windhawk-styler-syntax](windhawk-styler-syntax.md) |
| **Rule 03** | Theme Design Language & Token Standards | Canonical Glass Tokens, Radii Scale & Recipes | [design-language-standards](design-language-standards.md) |
| **Rule 04** | Target Evidence Protocol (No Guessed Selectors) | Sourced Selectors Only, UWPSpy & Verification Tiers | [target-evidence-protocol](target-evidence-protocol.md) |
| **Rule 05** | Surface Scope, Mod Capabilities & Invariants | Process Targets (explorer.exe vs ShellExperienceHost), WinUI 3 vs UWP | [surface-scope-standards](surface-scope-standards.md) |
| **Rule 06** | GitHub-Flavored Mermaid & Diagram Standards | GitHub-Compatible Syntax, Quoted Selectors, Max 12 Nodes | [mermaid-standards](mermaid-standards.md) |
| **Rule 07** | Verification Standards (Static Gate + Live Checklist) | `tools/Test-WindhawkStyles.ps1` Codes & User Live Protocol | [verification-standards](verification-standards.md) |
| **Rule 08** | Documentation Standards & Ecosystem Synchronization | Docs Structure, Tracking Files & Sync Triggers | [documentation-standards](documentation-standards.md) |
| **Rule 09** | Milestone & Sprint Tracking Standards | Milestones, Sprints, Compatibility Record & Completion Gate | [milestone-standards](milestone-standards.md) |

---

## 🔍 Static Verification

All rules are statically validated via:
```powershell
pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1
```
