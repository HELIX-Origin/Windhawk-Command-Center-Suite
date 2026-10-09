# Local Backups (`.backups/`)

This directory is reserved for local, timestamped safety backups and fallback snapshots created during non-git operations or before destructive manual refactoring.

## Purpose & Usage

- **Local-Only**: The contents of this directory are strictly ignored by Git (via `.gitignore`), ensuring temporary local backups and snapshot files are never accidentally tracked or pushed to remote repositories.
- **Whitelisted Documentation**: This `README.md` file is explicitly whitelisted in `.gitignore` so that the directory structure is preserved and visible on remote while all backup files remain untracked.
- **Organization Convention**: When creating local fallback backups, place files in date-stamped subfolders:
  ```
  .backups/<YYYY-MM-DD>/<filename>
  ```
