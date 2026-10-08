# Notification Center Specialist Agent (Sub-Agent)

**Parent Primary**: [Style Architect](../style-architect.md)  
**Focus**: Engineering

The **Notification Center Specialist Agent** is the domain engineer for `src/notification-center-styler.yml` targeting the `windows-11-notification-center-styler` mod.

---

## Domain Responsibilities

1. **Target Environment**:
   - Host Processes: `ShellExperienceHost.exe` and `ShellHost.exe` (Win11 24H2 Action Center).
   - Framework: UWP `Windows.UI.Xaml`.
2. **Surface Coverage**:
   - Notification Center panel (`Grid#NotificationCenterGrid`)
   - Calendar Center panel (`Grid#CalendarCenterGrid`)
   - Quick Settings Control Center (`Grid#ControlCenterRegion`, `Grid#L1Grid`, toggles, sliders)
   - Media transport controls (`Grid#MediaTransportControlsRegion`)
   - Toasts (`Border#ToastBackgroundBorder`, `ActionCenter.FlexibleToastView#FlexibleNormalToastView`)
   - Taskbar Jump Lists (`Border#JumpListRestyledAcrylic`)
3. **Invariants**:
   - Never inject `webContentStyles` or `explorerFrameContainerHeight`.
   - Do not use the `skip()` expression (unsupported in NC mod).
   - Collapse native chrome backgrounds and shadows (`Shadow:=`, `Visibility=1`) to let intentional layered glass and acrylic controls shine through cleanly.
   - Maintain full light and dark theme contrast.
