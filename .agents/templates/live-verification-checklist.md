# 📋 Live Verification Checklist Template

Use this checklist when preparing a handoff for the user to verify a style change live on Windows 11. Copy this template into session plans, pull requests, or issue updates.

---

## 🎯 Verification Scope

- **Surface**: `{{ surface.name }}` (e.g. Notification Center)
- **Target File**: `{{ target.file }}`
- **Windhawk Mod**: `{{ mod.name }}` (`{{ mod.id }}`)
- **Target Process**: `{{ target.process }}` (`explorer.exe` / `ShellExperienceHost.exe`)
- **Windows 11 Build**: `{{ win.build }}` (e.g. 23H2 / 24H2 build 26100.x)

---

## 🚀 How to Apply

1. Open the **Windhawk** client application.
2. Navigate to the **Details** tab for `{{ mod.name }}`.
3. Switch to the **Settings** or **Advanced** tab.
4. Replace or merge the YAML content with the newly generated `{{ target.file }}` content.
5. Click **Save** (Windhawk applies styles live without restarting processes in most cases).
<!-- Reference only — File Explorer deferred (ROADMAP M.03); do not verify unless the surface is resumed -->
6. *(If testing File Explorer background changes — reference only, File Explorer deferred)*: Open a new File Explorer window (`Win + E`).

---

## 🔍 Visual Inspection Checklist

### 1. Light & Dark Theme Parity
- [ ] **Dark Mode**: Background blur tint renders smoothly without jarring white artifacts.
- [ ] **Light Mode**: Background blur tint and text contrast remain legible.
- [ ] **Accent Color Change**: Change Windows Accent Color (Settings → Personalization → Colors). Verify active indicators and accent fills adapt dynamically.

### 2. Panel Chrome & Borders
- [ ] **Outer Rim**: Panel border gradient displays the subtle top-lit rim highlight (`$BorderBrush`).
- [ ] **Corner Radii**: Corners are cleanly rounded (`$CornerRadius`) without jagged clipping.
- [ ] **Intentional Glass Layering**: Foundation frosted surface hosts layered glassy cards and controls cleanly; native opaque system fills are collapsed.
- [ ] **Shadow Collapse**: Native drop shadows or hard acrylic plates are properly collapsed where intended.

### 3. Interactive States
- [ ] **Hover State**: Buttons and list items display subtle hover feedback (`$OverlayColor2` or border highlight).
- [ ] **Pressed State**: Controls show instantaneous press feedback (`ScaleTransform 0.8` or `$OverlayColor`).
- [ ] **Active/Selected State**: Selected tab or toggle button displays accent or active highlight (`$ActiveColor` / `$AccentColor`).

### 4. Surface-Specific Scenarios

<!-- Select the applicable surface scenarios below -->

#### Notification Center & Control Center
- [ ] **Empty State**: Displays clean glass when no notifications are present.
- [ ] **Active Notifications**: Toast items render inside rounded cards with readable text.
- [ ] **Calendar**: Month grid renders cleanly; expand/collapse functions smoothly.
- [ ] **Quick Settings (L1)**: Toggles (Wi-Fi, Bluetooth, Audio) show distinct On/Off states.
- [ ] **Sliders**: Volume and Brightness slider tracks and fill bars match the glass theme.
- [ ] **Media Controls**: Album art thumbnail and playback transport buttons render properly.
- [ ] **Jump Lists**: Right-clicking taskbar items shows styled glass jump lists.

<!-- Reference only — File Explorer deferred (ROADMAP M.03); do not verify unless the surface is resumed -->
#### File Explorer (Reference only — deferred, ROADMAP M.03)
- [ ] **Tab Bar**: Active tab, inactive tab, and hover states render with rounded glass.
- [ ] **Add Tab Button**: "+" button matches tab bar styling.
- [ ] **Navigation Bar**: Back, Forward, Up, and Refresh buttons display clean icons without solid box artifacts.
- [ ] **Address Bar**: Breadcrumb path and edit mode render smoothly.
- [ ] **Search Box**: Search pill/box displays rounded border and placeholder text cleanly.
- [ ] **Command Bar**: Modern command bar buttons (Cut, Copy, Paste, New) render with transparent background and hover states.
- [ ] **Details / Preview Pane**: Side pane matches background translucency when toggled on.
- [ ] **Context Menus**: Modern XAML command bar flyouts render with glass styling.

---

## 📝 Verification Feedback Report

Please record the findings below:
- **Observed Result**: [Pass / Visual Regression / Selector Not Applying]
- **Anomalies Observed**: Describe any visual clipping, hard borders, or missing styles.
- **UWPSpy / Inspector Notes**: (If a target failed to apply, include the actual visual tree class/name from UWPSpy).
