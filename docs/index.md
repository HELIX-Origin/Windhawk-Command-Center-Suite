---
layout: default
title: Windhawk Themes
summary: The universal framework for building custom Windhawk theme suites. A complete developer framework, autonomous multi-agent ecosystem, and hybrid C++/Python inspection toolchain designed for engineering, validating, and maintaining your own cohesive theme suites across Windows 11 shell surfaces.
nav_order: 1
notice: "<strong>Framework & Ecosystem.</strong> Built for developers and AI vibe coders creating custom theme suites. Provides full coverage for the 5 base Windhawk styler mods, companion mods, empirical visual tree inspection, and static syntax gates."
header_actions:
  - title: Browse Catalogue
    url: /catalogue/
    class: button--primary
  - title: Read Documentation
    url: /docs/
    class: button--secondary
  - title: Explore Wiki ↗
    url: /wiki/
    class: button--secondary
---

<section id="features" class="doc-section">
<div class="section-heading">
<span class="section-number">01</span>
<div>
<p class="eyebrow">Framework Architecture</p>
<h2>Why Windhawk Themes?</h2>
</div>
</div>
<p>
Building custom Windows 11 theme suites across multiple Windhawk mods often leads to fragile selectors, clashing styles, and broken layouts following Windows updates. The <strong>Windhawk Themes</strong> repository solves this by providing the tools, standards, and automation needed to build your own theme suites:
</p>

<div class="feature-grid">
<div class="feature-card">
<h3>Multi-Agent Ecosystem</h3>
<p>Specialized AI agents for style architecture, visual inspection, syntax linting, and surface engineering working under strict safety rules.</p>
</div>
<div class="feature-card">
<h3>Hybrid Inspection Toolchain</h3>
<p>Native C++ TAP engine and Python CLI utilizing UI automation to wake shell surfaces and dump live visual trees into JSON for AI vibe coding.</p>
</div>
<div class="feature-card">
<h3>Empirical Selector Evidence</h3>
<p>Strict target evidence protocol requiring verified element types and names from official source code and live visual tree dumps.</p>
</div>
<div class="feature-card">
<h3>Automated Quality Gates</h3>
<p>Built-in static validation gate verifying YAML syntax, constant ordering, and token references across all theme suite projects.</p>
</div>
</div>
</section>

<section id="surfaces" class="doc-section">
<div class="section-heading">
<span class="section-number">02</span>
<div>
<p class="eyebrow">Shell Architecture</p>
<h2>Supported Styler Surfaces</h2>
</div>
</div>
<p>
The framework targets five base official Windhawk styler mods covering primary Windows 11 shell experiences:
</p>

<div class="surfaces-table-wrap">
<table>
<thead>
<tr>
<th>Surface</th>
<th>Windhawk Mod ID</th>
<th>Target Process</th>
<th>Framework</th>
<th>Documentation</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Start Menu</strong></td>
<td><code>windows-11-start-menu-styler</code></td>
<td><code>StartMenuExperienceHost.exe</code></td>
<td>UWP / WinUI 2</td>
<td><a href="{{ '/docs/Start-Menu/' | relative_url }}">Start Menu Guide →</a></td>
</tr>
<tr>
<td><strong>Taskbar</strong></td>
<td><code>windows-11-taskbar-styler</code></td>
<td><code>explorer.exe</code></td>
<td>WinUI 3 / XAML</td>
<td><a href="{{ '/docs/Taskbar/' | relative_url }}">Taskbar Guide →</a></td>
</tr>
<tr>
<td><strong>Notification Center</strong></td>
<td><code>windows-11-notification-center-styler</code></td>
<td><code>ShellExperienceHost.exe</code> / <code>ShellHost.exe</code></td>
<td>UWP <code>Windows.UI.Xaml</code></td>
<td><a href="{{ '/docs/Notification-Center/' | relative_url }}">Notification Center Guide →</a></td>
</tr>
<tr>
<td><strong>Settings</strong></td>
<td><code>windows-11-settings-styler</code></td>
<td><code>SystemSettings.exe</code></td>
<td>UWP / WinUI <code>Windows.UI.Xaml</code></td>
<td><a href="{{ '/docs/Settings/' | relative_url }}">Settings Guide →</a></td>
</tr>
<tr>
<td><strong>File Explorer</strong></td>
<td><code>windows-11-file-explorer-styler</code></td>
<td><code>explorer.exe</code></td>
<td>WinUI 3 <code>Microsoft.UI.Xaml</code></td>
<td><a href="{{ '/docs/File-Explorer/' | relative_url }}">File Explorer Guide →</a></td>
</tr>
</tbody>
</table>
</div>
</section>

<section id="toolchain" class="doc-section">
<div class="section-heading">
<span class="section-number">03</span>
<div>
<p class="eyebrow">Diagnostics & Automation</p>
<h2>Hybrid C++/Python Toolchain</h2>
</div>
</div>
<p>
Reliable theming requires empirical visual tree inspection without manual burden.
Our high-speed native inspection suite combines direct C++ TAP hooks with a flexible Python CLI:
</p>
<ul>
<li><strong>Automated Surface Activation</strong>: Programmatically opens and closes shell surfaces (Start, Action Center, Notification Center, Search, Settings) via UI automation to ensure UWP visual trees are fully populated.</li>
<li><strong>Heartbeat Resiliency</strong>: Built-in 30-second heartbeat loops accommodate OS elevation and UAC security prompts without premature timeouts.</li>
<li><strong>ShareX Screenshot Integration</strong>: Auto-detects user keybindings (including <code>VK_SLEEP</code> PrintScreen mappings) to capture desktop verification evidence automatically.</li>
<li><strong>Automated Static Gate</strong>: <code>tools/Test-WindhawkStyles.ps1</code> verifies YAML syntax, constant ordering, token definitions, and safety rules before any style is published.</li>
</ul>
</section>
