# Version-Manager
## Simple Local Version Manager

A tiny Python-based **version** manager for your project.  
Each time you run it, it snapshots the current project into a zip archive and records metadata in a JSON file.

## Features

- Creates a `versions/` folder in your project root if it does not exist.
- Saves project snapshots as `versions/<version>.zip` (e.g. `v1.zip`, `v2.1.3.zip`).
- Stores per-version metadata in `versions/metadata.json`:
  - Human-readable description.
  - Timestamp (`created_at`).
- Prevents duplicate versions by refusing already-used version names.
- Excludes the `versions/` folder itself from every archive, so archives never contain previous versions.

## How It Works

- On run, the script:
  - Ensures `versions/` and `metadata.json` exist.
  - Prompts for:
    - A version name (must be unique).
    - A short description.
  - Walks the project directory, zipping everything except `versions/`.
  - Updates `metadata.json` with the new version entry.

Example `metadata.json`:

```json
{
  "v1": {
    "description": "Initial version",
    "created_at": "2026-01-19T18:42:12"
  },
  "v2.1.3": {
    "description": "Added feature X",
    "created_at": "2026-01-19T19:00:00"
  }
}
```

## Usage

1. Place `version_manager.py` in your project root.
2. From the project root, run:

   ```bash
   python version_manager.py
   ```

3. When prompted:
   - Enter a unique version name (e.g. `v1`, `v2.0`, `release-2026-01-19`).
   - Enter a short description of the changes.

4. After running:
   - Check `versions/` for `<version>.zip`.
   - Open `versions/metadata.json` to see stored descriptions and timestamps.

## Project Structure Example

After a few runs, your project might look like:

```text
my-project/
├─ src/
├─ assets/
├─ version_manager.py
└─ versions/
   ├─ v1.zip
   ├─ v2.1.3.zip
   └─ metadata.json
```

## Future Improvements

Potential extensions:

- Add CLI flags (e.g. `--version`, `--description`) instead of interactive prompts.
- Command to list all versions with descriptions.
- Command to restore a specific version into the working directory.
- Support for ignoring additional files/directories via a config file (e.g. `.versionignore`).
