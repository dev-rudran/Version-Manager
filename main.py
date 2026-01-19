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



