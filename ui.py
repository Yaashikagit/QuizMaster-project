"""Console presentation layer: consistent framed dashboard screens."""
WIDTH = 52


def frame(title: str, lines: list[str]) -> str:
    inner = WIDTH - 4
    rows = ["╭" + "─" * (WIDTH - 2) + "╮", "│" + title.center(WIDTH - 2) + "│",
            "├" + "─" * (WIDTH - 2) + "┤"]
    rows.extend("│  " + line[:inner].ljust(inner) + "│" for line in lines)
    rows.append("╰" + "─" * (WIDTH - 2) + "╯")
    return "\n".join(rows)


def main_menu() -> str:
    # Preserve the requested two-column dashboard card layout.
    return "\n".join([
        "╭──────────────────────────────────────────────────╮",
        "│                 🧠 QUIZ MASTER                   │",
        "│              YOUR KNOWLEDGE HUB                  │",
        "├─────────────────────────┬────────────────────────┤",
        "│                         │                        │",
        "│  🎯 PLAY                │  📊 YOUR STATS        │",
        "│  Start a challenge      │  Track your progress  │",
        "│                         │                        │",
        "├─────────────────────────┼────────────────────────┤",
        "│                         │                        │",
        "│  🏆 LEADERBOARD         │  📚 CATEGORIES        │",
        "│  See top performers     │  Pick your topic      │",
        "│                         │                        │",
        "├─────────────────────────┼────────────────────────┤",
        "│                         │                        │",
        "│  ⚡ DIFFICULTY          │  ❓ HOW TO PLAY        │",
        "│  Set your challenge     │  Learn the rules      │",
        "│                         │                        │",
        "├─────────────────────────┴────────────────────────┤",
        "│                                                  │",
        "│              🚪 EXIT APPLICATION                 │",
        "│                                                  │",
        "│  ──────────────────────────────────────────────  │",
        "│  1 Play  2 Stats  3 Board  4 Topics  5 Level     │",
        "│  6 How to play  7 Exit                           │",
        "│  Choose an option: [                             ]│",
        "╰──────────────────────────────────────────────────╯",
    ])


def difficulty_menu() -> str:
    return frame("⚡ SELECT DIFFICULTY", ["", "1  🟢 EASY", "   Beginner-friendly • +1 per correct answer", "",
        "2  🟡 MEDIUM", "   Intermediate • +2 per correct answer", "", "3  🔴 HARD",
        "   Advanced • +3 per correct answer", "", "Select [1-3] or 0 to return:"])


def category_menu() -> str:
    return frame("📚 QUIZ CATEGORIES", ["", "1  🐍 Python Basics", "2  🔀 Control Flow", "3  🗂 Data Structures",
        "4  ⚙ Functions", "5  📁 File Handling", "6  ⚠ Error Handling", "7  🧠 Mixed Python", "",
        "Select [1-7] or 0 to return:"])


def question_screen(question: dict, index: int, total: int, category: str, difficulty: str, score: int) -> str:
    lines = [f"QUESTION {index:02d} / {total:02d}", "", question["question"], ""]
    lines.extend(f"{letter}) {question['options'][letter]}" for letter in "ABCD")
    lines += ["", f"Score: {score}", "Your answer [A-D]:"]
    return frame(f"🧠 QUIZ MASTER  •  {category.upper()} • {difficulty.upper()}", lines)


def result_screen(result: dict) -> str:
    return frame("QUIZ COMPLETE", ["", f"Questions Attempted : {result['questions_attempted']}",
        f"Correct Answers     : {result['correct']}", f"Incorrect Answers   : {result['incorrect']}",
        f"Score               : {result['score']} / {result['max_score']}",
        f"Accuracy            : {result['accuracy']}%", f"Difficulty          : {result['difficulty'].upper()}", ""])


def stats_screen(summary: dict) -> str:
    if not summary["quizzes"]:
        return frame("📊 YOUR STATS", ["", "No quiz attempts recorded yet.", ""])
    lines = ["", f"Quizzes Attempted  : {summary['quizzes']}", f"Questions Answered : {summary['questions']}",
        f"Correct Answers    : {summary['correct']}", f"Incorrect Answers  : {summary['incorrect']}",
        f"Overall Accuracy   : {summary['accuracy']}%", f"Highest Score      : {summary['highest_score']}",
        f"Average Score      : {summary['average_score']}", "", "RECENT PERFORMANCE", "─" * 43]
    lines.extend(f"{x.get('category','')} • {x.get('difficulty','')} • {x.get('score',0)}/{x.get('max_score',0)}"
                 for x in summary["recent"])
    return frame("📊 YOUR STATS", lines)


def leaderboard_screen(entries: list[dict]) -> str:
    if not entries:
        return frame("🏆 LEADERBOARD", ["", "No quiz attempts recorded yet.", ""])
    lines = ["", "RANK  PLAYER             SCORE  LEVEL", "─" * 44]
    lines.extend(f"{i:>2}    {str(x.get('player','Anonymous'))[:17]:<17} {x.get('score',0):>5}  {x.get('difficulty','')}"
                 for i, x in enumerate(entries, 1))
    return frame("🏆 LEADERBOARD", lines)


def how_to_play() -> str:
    return frame("❓ HOW TO PLAY", ["", "Choose Play, then set difficulty and category.",
        "Choose how many questions (up to those available).", "Answer each question with A, B, C, or D.",
        "Correct answers earn +1 Easy, +2 Medium, +3 Hard.", "Incorrect answers earn 0 points.",
        "Results are saved to your local JSON data files.", "The leaderboard ranks attempts by score.", ""])

