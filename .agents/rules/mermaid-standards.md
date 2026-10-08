# Rule 06: GitHub-Flavored Mermaid & Diagram Standards

This standard governs **every Mermaid diagram** in this repository — `AGENTS.md`, `.agents/`, `README.md`, and root tracking files, plus the planned `docs/` GitHub Pages site (future — see Rule 08). Diagrams target **GitHub's Mermaid renderer**, so they must use syntax it supports and be structured for legibility.

## Baseline

1. **Fence**: Every diagram is a fenced block with the `mermaid` language identifier.
2. **Render target**: GitHub's renderer. Do not rely on bleeding-edge Mermaid features.
3. **Diagram types**: Prefer `flowchart` (default), `sequenceDiagram`, `stateDiagram-v2`, `classDiagram`.

## Syntax Rules

1. **Quote every label** containing special characters (`(`, `)`, `[`, `]`, `:`, `#`, `|`, `"`, `/`, `<`, `>`, `&`, `=`, `$`, `@`). Windhawk selectors are full of `#`, `>`, and `@` — **always** quote them: `T["Grid#ControlCenterRegion"]`.
2. **Subgraph titles** use the quoted form: `subgraph id["Title"]`.
3. **Shapes**: stick to `A[text]`, `A{text}`, `A([text])`, `A[(text)]`, `A((text))`.
4. **No `%%{init:...}%%` directives**, no math/LaTeX in labels.
5. **No reserved-word node IDs** (`end`, `class`, `note`, `subgraph`, `link`, `default`, `style`).
6. **Header**: `flowchart TD` (default) or `flowchart LR` for short pipelines.

## Legibility

1. **One diagram = one concern.** Split unrelated flows.
2. **Keep it small**: roughly 8–12 nodes max; split larger flows by stage.
3. **Short labels**; detail goes in prose.
4. **Label every decision edge** (`-->|"Yes"|`, `-->|"No"|`).

## Conformity Checklist

- [ ] `mermaid` fence used
- [ ] Labels with special characters quoted (selectors especially)
- [ ] Quoted subgraph titles
- [ ] Standard shapes only
- [ ] No init directives or math
- [ ] No reserved-word IDs
- [ ] One concern, ≤ 12 nodes
