"""Defensive JSON persistence helpers."""
import json
from pathlib import Path
from typing import Any


def load_json(path: str | Path, default: Any) -> Any:
    """Load JSON; create absent files and recover from empty/corrupt files."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    if not target.exists():
        save_json(target, default)
        return default
    try:
        raw = target.read_text(encoding="utf-8")
        if not raw.strip():
            return default
        return json.loads(raw)
    except (OSError, json.JSONDecodeError, UnicodeDecodeError):
        return default


def save_json(path: str | Path, value: Any) -> None:
    """Atomically write JSON, creating parent directories as needed."""
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".tmp")
    temporary.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    temporary.replace(target)


def append_json_record(path: str | Path, record: dict, default: list | None = None) -> list:
    records = load_json(path, default if default is not None else [])
    if not isinstance(records, list):
        records = []
    records.append(record)
    save_json(path, records)
    return records

