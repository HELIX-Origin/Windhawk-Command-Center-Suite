---
layout: documentation
title: "Wiki: Taskbar Companions"
---

# Taskbar Companion Mods Configuration

Reference for settings schemas of companion mods that operate alongside `windows-11-taskbar-styler`.

---

## 1. Taskbar Clock Customization (`taskbar-clock-customization`)

* **`clockFormat`** (String): Date/time format specifier (e.g. `HH:mm:ss`, `ddd, MMM d`, or multiline `HH:mm\nMM/dd`).
* **`fontFamily`** (String): Font family (e.g. `Segoe UI Variable Display`).
* **`fontSize`** (Integer): Text size in points.
* **`showMilliseconds`** (Boolean): High-frequency milliseconds counter.

---

## 2. Taskbar Tray and Icon Tweaks (`taskbar-tray-and-icon-tweaks`)

* **`hideShowDesktop`** (Boolean): Hides the extreme right-hand desktop strip.
* **`hideNotificationCenter`** (Boolean): Hides the notification bell badge.
* **`iconPadding`** (Integer): Horizontal spacing around tray icons.
* **`alwaysShowIcons`** (Boolean): Disables overflow menu and keeps all icons on the bar.

---

## 3. Taskbar Tray Icon Spacing and Grid (`taskbar-tray-icon-spacing-and-grid`)

* **`gridRows`** (Integer): Number of rows (e.g. `2` or `3` for dense grid layout).
* **`horizontalSpacing`** / **`verticalSpacing`** (Integer): Pixel distance between icons.

---

## 4. Taskbar Height and Icon Size (`taskbar-height-and-icon-size`)

* **`taskbarHeight`** (Integer): Height in pixels (e.g. `36` for compact, `48` standard).
* **`iconSize`** (Integer): Icon dimension scale (e.g. `20`, `24`, `32`).
