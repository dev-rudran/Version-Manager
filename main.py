import json
import os
import zipfile
from datetime import datetime

VERSIONS_DIR = "versions"
METADATA_FILE = os.path.join(VERSIONS_DIR, "metadata.json")


def ensure_versions_dir():
    os.makedirs(VERSIONS_DIR, exist_ok=True)


def load_metadata():
    if not os.path.exists(METADATA_FILE):
        return {}
    with open(METADATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_metadata(metadata):
    with open(METADATA_FILE, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2)



def prompt_version(metadata):
    while True:
        version = input("Enter version name (e.g. v1, v2.1.3): ").strip()
        if not version:
            print("Version cannot be empty.")
            continue
        if version in metadata:
            print(f"Version '{version}' already exists. Please choose another.")
            continue
        return version


def prompt_description():
    return input("Enter a short description: ").strip()


def create_archive(version):
    project_root = os.getcwd()
    zip_path = os.path.join(VERSIONS_DIR, f"{version}.zip")

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(project_root):
            # Skip the versions directory itself
            rel_root = os.path.relpath(root, project_root)
            if rel_root == VERSIONS_DIR or rel_root.startswith(VERSIONS_DIR + os.sep):
                continue

            for file_name in files:
                abs_path = os.path.join(root, file_name)
                # Path inside the zip should be relative to project root
                rel_path = os.path.relpath(abs_path, project_root)
                zf.write(abs_path, rel_path)

    print(f"Created archive: {zip_path}")


def main():
    ensure_versions_dir()
    metadata = load_metadata()

    version = prompt_version(metadata)
    description = prompt_description()

    create_archive(version)

    metadata[version] = {
        "description": description,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    save_metadata(metadata)
    print(f"Saved metadata for version '{version}'.")


if __name__ == "__main__":
    main()
