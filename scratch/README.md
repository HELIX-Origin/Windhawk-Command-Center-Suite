# Local Scratch Workspace (`scratch/`)

This directory is the dedicated local-only workspace for temporary files, experimental scripts, visual inspection dumps, and scratch data.

## Purpose & Usage

- **Local-Only**: All contents in this directory (with the exception of this `README.md`) are ignored by Git via `.gitignore`. Temporary scratch files are never tracked or committed.
- **Strict Format Organization**: Scratch files must never accumulate in the root of `scratch/`. Instead, sort all files into their dedicated format subfolders:
  - `cpp/` — Temporary C++ test snippets or headers
  - `docs/` — Scratch markdown notes or drafts
  - `images/` — Temporary screenshots or visual reference images
  - `json/` — Raw visual tree dumps from the inspection toolchain
  - `powershell/` — Ad-hoc PowerShell scripts or pipeline tests
  - `python/` — Scratch Python scripts or analysis tools
  - `text/` — Raw terminal logs or unformatted text dumps
  - `yml/` — Temporary or prototype YAML styler snippets
- New format subfolders should be created dynamically as needed when a new file extension or data type is introduced.
