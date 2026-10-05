# 🚀 Release Notes Template

Use this template when publishing a new version of the **Windhawk Command Center Suite**.

---

# Windhawk Command Center Suite v{{ version }}

> 🌟 {{ release.summary }}

---

## 🎨 Surface Status Overview

| Surface / Styler File | Windhawk Mod | Version | Windows 11 Build | Status |
|---|---|---|---|---|
| `src/taskbar-customizer.yml` | Windows 11 Taskbar Styler | 1.10+ | 23H2 / 24H2 | {{ status }} |
| `src/start-menu-customizer.yml` | Windows 11 Start Menu Styler | 1.7+ | 23H2 / 24H2 | {{ status }} |
| `src/notification-center-styler.yml` | Windows 11 Notification Center Styler | 1.7+ | 23H2 / 24H2 | {{ status }} |
| `src/file-explorer.styler.yml` | Windows 11 File Explorer Styler | 1.7+ | 23H2 / 24H2 | {{ status }} |

---

## ✨ What's New

### 🔔 Notification Center
- {{ list.item }}

### 📁 File Explorer
- {{ list.item }}

### ⚡ Taskbar & Start Menu Refinements
- {{ list.item }}

---

## 🛠️ Verification & Quality Gate

- [x] **Static Validation Gate**: `pwsh -NoProfile -File tools/Test-WindhawkStyles.ps1` (0 errors, 0 warnings).
- [x] **Design Token Compliance**: Rule 03 material and radius scales strictly adhered to.
- [x] **Target Evidence**: All selectors verified against official mod sources or live visual tree.
- [x] **Live Desktop Verification**: Verified on Windows 11 (Build {{ build.number }}).

---

## 📥 How to Install / Upgrade

1. Open **Windhawk**.
2. For each mod you want to update, click on the mod card and go to **Details → Advanced**.
3. Copy the YAML text from the corresponding file in `src/` into the Settings editor.
4. Click **Save**.

---

## 🐛 Known Issues & Limitations

- {{ bug.item }} (Tracked in [`BUGS.md`](./BUGS.md))
