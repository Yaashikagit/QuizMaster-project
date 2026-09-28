"""Aggregate and format saved quiz performance."""
from config import PERFORMANCE_FILE, MAX_RECENT_ATTEMPTS
from storage import load_json, append_json_record


def get_attempts(path=PERFORMANCE_FILE) -> list[dict]:
    value = load_json(path, [])
    return [x for x in value if isinstance(x, dict)] if isinstance(value, list) else []


def record_attempt(record: dict, path=PERFORMANCE_FILE) -> None:
    append_json_record(path, record)


def summarize_attempts(attempts: list[dict]) -> dict:
    def number(record, key):
        try:
            return max(0, int(record.get(key, 0)))
        except (TypeError, ValueError):
            return 0
    questions = sum(number(x, "questions_attempted") for x in attempts)
    correct = sum(number(x, "correct") for x in attempts)
    scores = [number(x, "score") for x in attempts]
    return {"quizzes": len(attempts), "questions": questions, "correct": correct,
            "incorrect": max(0, questions - correct),
            "accuracy": round(correct * 100 / questions, 1) if questions else 0.0,
            "highest_score": max(scores, default=0),
            "average_score": round(sum(scores) / len(scores), 1) if scores else 0.0,
            "recent": list(reversed(attempts[-MAX_RECENT_ATTEMPTS:]))}

