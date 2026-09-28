"""Interactive quiz session orchestration."""
from question_manager import select_questions
from scoring import points_for_answer, summarize


class QuizEngine:
    def __init__(self, questions: list[dict], input_fn=input, output_fn=print):
        self.questions, self.input, self.output = questions, input_fn, output_fn

    def run(self, category: str, difficulty: str, count: int, ask_answer=None) -> dict:
        selected = select_questions(self.questions, count, category, difficulty)
        results = []
        score = 0
        for index, question in enumerate(selected, 1):
            if ask_answer:
                answer = ask_answer(question, index, len(selected), score)
            else:
                self.output(f"\nQUESTION {index:02d} / {len(selected):02d}\n{question['question']}")
                for letter in "ABCD":
                    self.output(f"{letter}) {question['options'][letter]}")
                while True:
                    answer = self.input("Your answer [A-D]: ").strip().upper()
                    if answer in "ABCD" and len(answer) == 1:
                        break
                    self.output("⚠ Enter A, B, C, or D.")
            correct = str(answer).strip().upper() == question["answer"].upper()
            results.append(correct)
            score += points_for_answer(answer, question["answer"], difficulty)
        summary = summarize(results, difficulty)
        summary.update({"category": category, "difficulty": difficulty, "score": score,
                        "max_score": len(selected) * {"Easy": 1, "Medium": 2, "Hard": 3}.get(difficulty, 0),
                        "results": results, "questions": len(selected)})
        return summary

