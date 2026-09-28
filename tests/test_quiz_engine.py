import unittest
from question_manager import filter_questions, valid_question
from quiz_engine import QuizEngine

QUESTION = {"question": "2 + 2?", "options": {"A":"3", "B":"4", "C":"5", "D":"6"},
            "answer": "B", "category": "Python Basics", "difficulty": "Easy"}


class QuestionTests(unittest.TestCase):
    def test_category_and_difficulty_filter(self):
        bank = [QUESTION, {**QUESTION, "category": "Functions"}, {**QUESTION, "difficulty": "Hard"}]
        self.assertEqual(len(filter_questions(bank, "Python Basics", "Easy")), 1)
        self.assertEqual(len(filter_questions(bank, "Mixed Python", "Easy")), 2)
        self.assertEqual(len(filter_questions(bank, difficulty="Hard")), 1)

    def test_question_validation(self):
        self.assertTrue(valid_question(QUESTION))
        self.assertFalse(valid_question({"question": "incomplete"}))

    def test_engine_records_correct_answer(self):
        result = QuizEngine([QUESTION]).run("Python Basics", "Easy", 1, lambda *_: "b")
        self.assertEqual(result["correct"], 1)
        self.assertEqual(result["score"], 1)

    def test_engine_records_incorrect_answer(self):
        result = QuizEngine([QUESTION]).run("Python Basics", "Easy", 1, lambda *_: "A")
        self.assertEqual(result["incorrect"], 1)
        self.assertEqual(result["score"], 0)


if __name__ == "__main__":
    unittest.main()
