"""Entry point and menu workflow for Quiz Master."""
from datetime import datetime, timezone
from config import (QUESTIONS_FILE, LEADERBOARD_FILE, PERFORMANCE_FILE, CATEGORIES, DIFFICULTIES)
from question_manager import load_questions
from quiz_engine import QuizEngine
from leaderboard import top_entries, record_attempt as save_leaderboard
from performance import get_attempts, summarize_attempts, record_attempt as save_performance
from ui import main_menu, difficulty_menu, category_menu, question_screen, result_screen, stats_screen, leaderboard_screen, how_to_play


def choose(prompt: str, low: int, high: int, input_fn=input, output_fn=print):
    while True:
        value = input_fn(prompt).strip()
        try:
            number = int(value)
            if low <= number <= high:
                return number
        except ValueError:
            pass
        output_fn(f"⚠ Invalid selection. Please choose an option from {low} to {high}.")


def run_app(input_fn=input, output_fn=print):
    questions = load_questions(QUESTIONS_FILE)
    difficulty = "Easy"
    category = "Mixed Python"
    while True:
        output_fn(main_menu())
        choice = choose("", 1, 7, input_fn, output_fn)
        if choice == 1:
            output_fn(difficulty_menu())
            # Allow 0 as a back action while retaining strict validation.
            while True:
                raw = input_fn("Select [1-3] or 0 to return: ").strip()
                if raw in ("0", "1", "2", "3"):
                    break
                output_fn("⚠ Invalid selection. Choose 0, 1, 2, or 3.")
            if raw == "0":
                continue
            difficulty = DIFFICULTIES[int(raw) - 1]
            output_fn(category_menu())
            while True:
                raw = input_fn("Select [1-7] or 0 to return: ").strip()
                if raw.isdigit() and 0 <= int(raw) <= 7:
                    break
                output_fn("⚠ Invalid selection. Choose a category from 1 to 7, or 0 to return.")
            if raw == "0":
                continue
            category = CATEGORIES[int(raw) - 1]
            available = len([q for q in questions if q["difficulty"] == difficulty and
                             (category == "Mixed Python" or q["category"] == category)])
            if available == 0:
                output_fn("No questions are available for that selection.")
                continue
            count = choose(f"Number of questions (1-{available}): ", 1, available, input_fn, output_fn)
            engine = QuizEngine(questions, input_fn, output_fn)
            def ask(q, i, total, score):
                output_fn(question_screen(q, i, total, category, difficulty, score))
                while True:
                    answer = input_fn("Your answer [A-D]: ").strip().upper()
                    if answer in "ABCD" and len(answer) == 1:
                        return answer
                    output_fn("⚠ Enter A, B, C, or D.")
            result = engine.run(category, difficulty, count, ask)
            output_fn(result_screen(result))
            player = input_fn("Player name: ").strip() or "Anonymous"
            record = {**{k: v for k, v in result.items() if k not in ("results",)}, "player": player,
                      "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds")}
            save_performance(record, PERFORMANCE_FILE)
            save_leaderboard(record, LEADERBOARD_FILE)
        elif choice == 2:
            output_fn(stats_screen(summarize_attempts(get_attempts(PERFORMANCE_FILE))))
            input_fn("Press Enter to return...")
        elif choice == 3:
            output_fn(leaderboard_screen(top_entries(LEADERBOARD_FILE)))
            input_fn("Press Enter to return...")
        elif choice == 4:
            output_fn(category_menu())
            input_fn("Press Enter to return...")
        elif choice == 5:
            output_fn(difficulty_menu())
            input_fn("Press Enter to return...")
        elif choice == 6:
            output_fn(how_to_play())
            input_fn("Press Enter to return...")
        else:
            output_fn("Thank you for playing Quiz Master. Keep learning and see you next time!")
            return


if __name__ == "__main__":
    run_app()

