"""Question bank loading, validation, filtering, and sampling."""
import random
from storage import load_json

REQUIRED = ("question", "options", "answer", "category", "difficulty")


def valid_question(item: object) -> bool:
    return (isinstance(item, dict) and all(key in item for key in REQUIRED)
            and isinstance(item["options"], dict)
            and all(letter in item["options"] for letter in "ABCD")
            and str(item["answer"]).upper() in ("A", "B", "C", "D")
            and item["difficulty"] in ("Easy", "Medium", "Hard"))


def load_questions(path) -> list[dict]:
    data = load_json(path, [])
    return [item for item in data if valid_question(item)] if isinstance(data, list) else []


def filter_questions(questions: list[dict], category: str | None = None,
                     difficulty: str | None = None) -> list[dict]:
    return [q for q in questions if (category is None or category == "Mixed Python" or q["category"] == category)
            and (difficulty is None or q["difficulty"].casefold() == difficulty.casefold())]


def select_questions(questions: list[dict], count: int, category: str, difficulty: str,
                     rng=random) -> list[dict]:
    pool = filter_questions(questions, category, difficulty)
    return rng.sample(pool, min(max(0, count), len(pool)))

