# Mandatory Rules Index

Index of permanent, non-negotiable rules for all AI coding assistants, automated agents, and contributors working on **Windhawk Command Center Suite**. These rules enforce safety, prevent desktop/Explorer crashes, guarantee visual harmony across all four styler mods, and mandate evidence-based styling.

---

## Active Rules Directory

| Rule | Title | Primary Scope | Specification File |
|---|---|---|---|
| **Rule 00** | Agent Safety, Instruction Compliance & Damage Prevention | Core Safety, Data Protection & System Invariants | [agent-safety-compliance](agent-safety-compliance.md) |
| **Rule 01** | Dependency, Mod & Asset Approval (Zero Unsolicited Injection) | Runtime Boundary — 4 Styler Mods Only | [zero-unsolicited-injection](zero-unsolicited-injection.md) |
| **Rule 02** | Windhawk Styler YAML & XAML Syntax Standards | Parser Grammar, Quoting, Constant Order & Styles Format | [windhawk-styler-syntax](windhawk-styler-syntax.md) |
| **Rule 03** | Suite Design Language — "Command Center Glass" | Canonical Glass Tokens, Radii Scale & Recipes | [design-language-standards](design-language-standards.md) |
| **Rule 04** | Target Evidence Protocol (No Guessed Selectors) | Sourced Selectors Only, UWPSpy & Verification Tiers | [target-evidence-protocol](target-evidence-protocol.md) |
| **Rule 05** | Surface Scope, Mod Capabilities & Invariants | Process Targets (explorer.exe vs ShellExperienceHost), WinUI 3 vs UWP | [surface-scope-standards](surface-scope-standards.md) |
| **Rule 06** | GitHub-Flavored Mermaid & Diagram Standards | GitHub-Compatible Syntax, Quoted Selectors, Max 12 Nodes | [mermaid-standards](mermaid-standards.md) |
| **Rule 07** | Verification Standards (Static Gate + Live Checklist) | `tools/Test-WindhawkStyles.ps1` Codes & User Live Protocol | [verification-standards](verification-standards.md) |
| **Rule 08** | Documentation Standards & Ecosystem Synchronization | Docs Structure, Tracking Files & Sync Triggers | [documentation-standards](documentation-standards.md) |
| **Rule 09** | Semantic Versioning & Release Standards | Suite-Level SemVer, Previews & Compatibility Ledger | [release-standards](release-standards.md) |

---

## Enforcement Hierarchy

1. **Rule 00 (Safety)** and **Rule 01 (Zero Unsolicited Injection)** supersede all other implementation decisions.
2. **Rule 03 (Design Language Standards)** defines the visual identity of the Command Center Suite. All new styles must inherit its tokens, materials, and radii.
3. **Rule 04 (Target Evidence Protocol)** and **Rule 05 (Surface Scope)** ensure that selectors are physically real in the target process visual tree and never guessed.
4. Every change must pass `tools/Test-WindhawkStyles.ps1` before completion.
