# Git Commit & PR Message Guide

Guidelines for clear, human-readable commit messages and PR titles with fitting GitHub emojis for **Windhawk Command Center Suite**. Follows conventional commits with strict surface and subsystem scoping.

---

## Format Specification

```
<emoji> <type>(<scope>): <subject>

[optional body explaining design rationale, selector evidence, or verification outcomes]

[optional tracking references: Resolves #<issue>, Closes #<issue>]
```

---

## Standard Emoji & Commit Type Matrix

| Emoji | Type | Purpose | Example |
|---|---|---|---|
| ✨ | feat | New surface styles or major regions | ✨ feat(notification): add frosted glass styling for quick actions |
| 🐛 | fix | Bug fixes, selector corrections | 🐛 fix(explorer): repair command bar selector for build 26100 |
| 🎨 | style | Visual tweaks, radius adjustments, opacity | 🎨 style(start): refine press-scale transition on pinned tiles |
| 📝 | docs | Documentation, target evidence, rules | 📝 docs(evidence): add UWPSpy targets for action center sliders |
| 🧪 | test | Static test suite or validation checks | 🧪 test(gate): add validation rule for constant declaration order |
| ♻️ | refactor | Clean up selectors without visual change | ♻️ refactor(taskbar): deduplicate common visual state targets |
| 🔧 | chore | Repo maintenance, tooling, templates | 🔧 chore(tools): update static check script for CRLF enforcement |
| 🚀 | milestone | Milestone/sprint completion | 🚀 milestone: complete M.02b suite polish |

---

## Scopes

Target the exact surface or subsystem:
- **Surfaces**: `taskbar`, `start`, `notification`, `explorer` (File Explorer deferred — reserved)
- **Subsystems**: `tokens`, `materials`, `evidence`, `rules`, `agents`, `templates`, `tools`, `docs`

---

## Best Practices

1. **Imperative & Human-Readable**: Present tense, active voice (`✨ feat(notification): style calendar grid`, not `styled`).
2. **Surface Scopes**: Always identify which styler mod the change targets.
3. **Reference Tracking Files**: Reference corresponding entries in `TODO.md` and `BUGS.md`.
4. **Never Claim False Tests**: Clearly distinguish static validation from live user confirmation.
