"""Utilities for loading and saving JSON data files."""

import json
from pathlib import Path
from typing import Any


BASE_PATH = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_PATH / "data"
LISTS_PATH = BASE_PATH / "lists"


def load_json(path: Path) -> Any:
    """Load JSON from *path*."""
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def save_json(obj: Any, path: Path) -> None:
    """Write *obj* as JSON to *path*."""
    with path.open("w", encoding="utf-8") as fh:
        json.dump(obj, fh, indent=2)
