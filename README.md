# Quiz Master 🧠
### Your Knowledge Hub

Quiz Master is a Python 3 console application for practicing Python and programming concepts with multiple-choice questions. It provides a two-column dashboard menu, category and difficulty selection, scored quiz sessions, saved attempt statistics, and a local leaderboard.

## Problem statement

Learners need a simple way to practice programming concepts, receive immediate scoring, and review progress. Quiz Master combines question practice with transparent local performance tracking in a small, modular application.

## Features

- Dashboard menu that preserves the supplied two-column card layout.
- Seven categories and three difficulty levels with distinct question pools.
- MCQ answer validation and scoring of +1, +2, or +3 by difficulty; wrong answers earn zero.
- Result summary, aggregate performance statistics, recent attempts, and top-ten leaderboard.
- Local JSON storage that initializes missing files and tolerates empty or malformed data.
- Python `unittest` test suite and architecture/workflow diagrams.

## Technologies

Python 3 and its standard library only (`json`, `pathlib`, `datetime`, `random`, and `unittest`). No packages need installing.

## Project structure

```text
main.py                 Menu and application workflow
quiz_engine.py          Quiz session orchestration
question_manager.py     Question validation, filtering, selection
scoring.py              Answer and score calculations
leaderboard.py          Ranked attempt operations
performance.py          Statistics aggregation
storage.py              Defensive JSON persistence
ui.py                   Console screens and formatting
config.py               Paths, categories, and scoring rules
data/                   Question bank and saved attempt data
tests/                  unittest coverage
docs/                   Architecture, workflow, and diagrams
statement.md            Academic project statement
requirements.txt        Standard-library dependency note
```

## Installation and running

Install Python 3. Run from the project directory:

```bash
python main.py
```

On first launch, storage files are created if missing. Start a quiz from option 1, choose a difficulty and category, choose a question count, answer with A-D, then enter a player name to save the attempt.

## Testing

```bash
python -m unittest discover -s tests -v
```

Tests cover correct and incorrect answers, all difficulty point values, percentage calculations, question and difficulty/category filtering, JSON recovery, leaderboard ordering, invalid input retry, and empty performance data.

## Scoring system

| Difficulty | Correct answer | Incorrect answer |
|---|---:|---:|
| Easy | 1 | 0 |
| Medium | 2 | 0 |
| Hard | 3 | 0 |

Accuracy is correct answers divided by questions attempted, expressed as a percentage. A zero-question quiz has 0% accuracy.

## Data storage

`data/questions.json` contains validated question records. `data/performance.json` keeps attempt history for aggregate statistics. `data/leaderboard.json` keeps attempts for ranking by score, with accuracy as a tie-breaker. The JSON files are local to the project and are not sent anywhere.

## Example workflow

Choose **1 Play** → choose **2 Medium** → choose **4 Functions** → choose a question count → answer A-D → review the result → enter a player name. Use **2 Stats** or **3 Leaderboard** to review saved progress.

## Future enhancements

Possible extensions include configurable question banks, per-question explanations, timed rounds, CSV export, and richer terminal color support. These are ideas only and are not current features.
