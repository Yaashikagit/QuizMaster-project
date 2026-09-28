"""Answer validation and quiz score calculations."""
from config import POINTS


def is_correct(answer: str, correct_answer: str) -> bool:
    return str(answer).strip().upper() == str(correct_answer).strip().upper()


def points_for_answer(answer: str, correct_answer: str, difficulty: str) -> int:
    if not is_correct(answer, correct_answer):
        return 0
    return POINTS.get(str(difficulty).title(), 0)


def percentage(correct: int, total: int) -> float:
    return round((correct / total) * 100, 1) if total > 0 else 0.0


def summarize(answers: list[bool], difficulty: str) -> dict:
    correct = sum(bool(value) for value in answers)
    total = len(answers)
    multiplier = POINTS.get(str(difficulty).title(), 0)
    return {"questions_attempted": total, "correct": correct, "incorrect": total - correct,
            "score": correct * multiplier, "max_score": total * multiplier,
            "accuracy": percentage(correct, total)}

