---
layout: documentation
title: "Wiki: Notification Center Configurations"
---

# Notification Center Styler Configuration Schema & Options

Complete technical reference for top-level YAML configuration directives, token mechanics, and process host nuances supported by `windows-11-notification-center-styler`.

---

## 1. Complete Top-Level Schema Definition

```yaml
theme: ''                              # Built-in preset theme name (empty string for custom suite theme)

styleConstants:                        # Shared token definitions and XAML object brushes
  - TokenName=ScalarValue              # Scalar tokens (e.g., margins, radii, dimensions)
  - TokenName:=<XAML Object>           # Complex XAML object brushes (WindhawkBlur, LinearGradientBrush)

themeResourceVariables:                # Global theme resource brush replacements across host process
  - variableKey: ResourceKeyName
    value: "{ThemeResource ...}"

controlStyles:                         # Target selectors and styling rules applied to visual tree nodes
  - target: SelectorExpression
    styles:
      - Property=ScalarValue
      - Property:=<InlineXAML>
      - Property@VisualState=Value
      - Property:=                     # Empty value clears/resets the property
```

> [!NOTE]
> **Unsupported Keys**: Unlike the Start Menu and File Explorer stylers, the Notification Center Styler does **not** support `webContentStyles`, `backgroundTranslucentEffect`, or `explorerFrameContainerHeight`.

---

## 2. Process Host Dual-Targeting: `ShellExperienceHost` vs `ShellHost`

A critical architectural aspect of styling the Notification Center on modern Windows 11 builds is the process migration:

* **Windows 11 21H2, 22H2, and 23H2**: Quick Settings and Notification Center run inside `ShellExperienceHost.exe`.
* **Windows 11 24H2 (build 26100+)**: Quick Settings migrated into a dedicated host process, `ShellHost.exe`, while toast notifications and certain legacy flyouts may still instantiate within `ShellExperienceHost.exe`.

`windows-11-notification-center-styler` automatically attaches to both process hosts. However, when inspecting elements using the hybrid C++/Python toolchain or UWPSpy, verify you are inspecting the appropriate process for your active build:
```powershell
# Querying Quick Settings on Win11 24H2:
python tools/inspect_xaml.py -p ShellHost.exe --find ControlCenterRegion
```

---

## 3. Deep Dive: `styleConstants` Token Mechanics

Tokens in `windows-11-notification-center-styler` define reusable design values across visual targets:

```yaml
styleConstants:
  # Blur & Glass Materials
  - Translucent=<WindhawkBlur BlurAmount="15" TintColor="#10808080"/>
  - Glass=<WindhawkBlur BlurAmount="5" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Frosted=<WindhawkBlur BlurAmount="20" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.7" />
  - Acrylic=<WindhawkBlur BlurAmount="30" TintColor="{ThemeResource SystemChromeMediumColor}" TintOpacity="0.8" />
  - Background=$Frosted
  
  # Border Lighting & Accents
  - BorderBrush=<LinearGradientBrush StartPoint="0,0" EndPoint="0,1"><GradientStop Color="#60808080" Offset="0.0" /><GradientStop Color="#50404040" Offset="0.25" /><GradientStop Color="#40808080" Offset="1" /></LinearGradientBrush>
  - BorderBrush2=<WindhawkBlur BlurAmount="10" TintColor="#909090" TintOpacity="0.3"/>
  - OverlayColor=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.8" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - OverlayColor2=<AcrylicBrush TintColor="{ThemeResource SystemAltLowColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - AccentColor=<AcrylicBrush TintColor="{ThemeResource SystemAccentColor}" TintOpacity="1" TintLuminosityOpacity="0.5" FallbackColor="{ThemeResource CardStrokeColorDefaultSolid}" />
  - ElementBackground=<SolidColorBrush Color="{ThemeResource SystemAltLowColor}" Opacity="0.25" />
  
  # Geometric Scale
  - BorderThickness=0.3,1,0.3,1
  - PanelRadius=13       # XL: Outermost flyout frame
  - CardRadius=10        # M: Quick action tiles, media card, calendar header
  - ChipRadius=6         # S: Repeat buttons, chevron buttons, back button
  - thumbnailImageSize=70
```

---

## 4. Double-Blur Mitigation Pattern

A common defect when styling UWP flyouts with custom `WindhawkBlur` is **double-blurring**, which produces an overly muddy or dark surface. In `windows-11-notification-center-styler`, this occurs because Windows renders a default system acrylic plate inside `RootGridBorder`.

To prevent double-blurring:
1. Apply `WindhawkBlur` to the outer container:
   ```yaml
   - target: Grid#ControlCenterRegion
     styles:
       - Background:=$Background
       - BorderBrush:=$BorderBrush
       - BorderThickness=$BorderThickness
       - CornerRadius=$PanelRadius
       - Shadow:=
   ```
2. Collapse or clear the internal plate:
   ```yaml
   - target: ControlCenter.ControlCenterView > Grid#RootGrid > Border#RootGridBorder
     styles:
       - Background:=<SolidColorBrush Color="Transparent"/>
   ```
