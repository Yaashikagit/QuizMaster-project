# Quiz Master — Project Statement

## Project title

**QUIZ MASTER 🧠 — Your Knowledge Hub**

## Problem statement

Python learners benefit from frequent low-friction practice, but static notes do not provide immediate checks or a record of progress. This project provides an interactive multiple-choice console quiz with difficulty-aware scoring and locally persisted results.

## Scope

The application supports Python-focused questions, category and difficulty selection, quiz execution, answer validation, score summaries, performance statistics, and a top-ten leaderboard. It runs in a terminal and stores data as JSON. It does not require a network connection or external service.

## Target users

Python Essentials learners and instructors who want a small, inspectable example of a modular Python console application.

## Functional modules

| Module | Responsibility |
|---|---|
| `main.py` | Main menu and application workflow |
| `quiz_engine.py` | Quiz session and response processing |
| `question_manager.py` | Question loading, validation, filtering, sampling |
| `scoring.py` | Correctness, points, accuracy, summaries |
| `leaderboard.py` | Ranking and top-ten records |
| `performance.py` | Attempt history and aggregate statistics |
| `storage.py` | JSON reads, writes, and safe recovery |
| `ui.py` | Dashboard, quiz screens, tables, and messages |
| `config.py` | Shared paths, categories, and score rules |

## High-level features

- Two-column dashboard navigation.
- Seven quiz categories and Easy, Medium, and Hard question levels.
- Multiple-choice answer validation and difficulty-based points.
- Result, statistics, recent-attempt, and leaderboard screens.
- Robust local JSON persistence with clean behavior for empty or malformed data.

## Expected outcome

The learner can start a quiz, see an immediate score and accuracy result, and return later to review locally saved progress. The source code demonstrates separation of concerns and standard-library testing.

## Technical approach

The entry point coordinates the UI and domain modules. Question records are validated and filtered before random sampling. The quiz engine delegates point calculations to the scoring module. Completed attempts are appended to performance and leaderboard JSON stores. `unittest` verifies key calculations, filtering, persistence, and input validation.
