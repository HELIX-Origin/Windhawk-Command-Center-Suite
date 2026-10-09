# Native Compiled Binaries (`tools/native/bin/`)

This directory contains the compiled 64-bit native Windows binaries produced by `tools/native/build.ps1` for the hybrid XAML inspection toolchain.

## Binaries

- **`xaml_dump.exe`**: Native C++ process enumerator and DLL injector driver.
- **`xaml_dump_agent.dll`**: In-process diagnostic agent injected via `xamlOM.h` to capture live XAML visual trees.

## Purpose & Usage

- **Local Compilation**: Compiled binaries are untracked by Git via `.gitignore` to prevent binary bloat in repository history.
- **AppContainer Permissions**: During compilation, `tools/native/build.ps1` automatically grants `xaml_dump_agent.dll` AppContainer Read & Execute permissions (`*S-1-15-2-1:(RX)`) to allow attachment into sandboxed UWP processes (like `StartMenuExperienceHost.exe`).
- **Compilation Command**:
  ```powershell
  pwsh -NoProfile -File tools/native/build.ps1
  ```
