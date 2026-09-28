"""Leaderboard data operations."""
from config import LEADERBOARD_FILE
from storage import load_json, append_json_record


def get_entries(path=LEADERBOARD_FILE) -> list[dict]:
    value = load_json(path, [])
    return [x for x in value if isinstance(x, dict)] if isinstance(value, list) else []


def sorted_entries(entries: list[dict]) -> list[dict]:
    def number(value, fallback=0.0):
        try:
            return float(value)
        except (TypeError, ValueError):
            return fallback
    return sorted(entries, key=lambda x: (number(x.get("score")), number(x.get("accuracy"))), reverse=True)


def record_attempt(record: dict, path=LEADERBOARD_FILE) -> None:
    append_json_record(path, record)


def top_entries(path=LEADERBOARD_FILE, limit=10) -> list[dict]:
    return sorted_entries(get_entries(path))[:max(0, limit)]

