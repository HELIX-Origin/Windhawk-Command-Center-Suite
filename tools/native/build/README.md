# Native Intermediate Build Artifacts (`tools/native/build/`)

This directory is used by the MSVC compilation pipeline (`tools/native/build.ps1`) to store intermediate build artifacts during compilation of the native C++ inspection engine.

## Purpose & Contents

- **Intermediate Files**: Contains `.obj` object files, compiler debug databases (`.pdb`), and generated batch scripts (`compile.bat`).
- **Ignored by Git**: All compiled intermediate files in this folder are untracked and excluded via `.gitignore`.
- **Rebuilding**: This directory can be safely cleaned and regenerated at any time by running:
  ```powershell
  pwsh -NoProfile -File tools/native/build.ps1 -Clean
  ```
