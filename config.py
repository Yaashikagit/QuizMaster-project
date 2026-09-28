"""Shared configuration for Quiz Master."""
from pathlib import Path

APP_TITLE = "QUIZ MASTER"
TAGLINE = "YOUR KNOWLEDGE HUB"
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
QUESTIONS_FILE = DATA_DIR / "questions.json"
LEADERBOARD_FILE = DATA_DIR / "leaderboard.json"
PERFORMANCE_FILE = DATA_DIR / "performance.json"
DIFFICULTIES = ("Easy", "Medium", "Hard")
CATEGORIES = ("Python Basics", "Control Flow", "Data Structures", "Functions", "File Handling", "Error Handling", "Mixed Python")
POINTS = {"Easy": 1, "Medium": 2, "Hard": 3}
MAX_RECENT_ATTEMPTS = 10

