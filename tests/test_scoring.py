import unittest
from scoring import is_correct, points_for_answer, percentage, summarize


class ScoringTests(unittest.TestCase):
    def test_correct_and_incorrect_answers(self):
        self.assertTrue(is_correct("b", "B"))
        self.assertFalse(is_correct("A", "B"))

    def test_difficulty_points(self):
        self.assertEqual(points_for_answer("A", "A", "Easy"), 1)
        self.assertEqual(points_for_answer("A", "A", "Medium"), 2)
        self.assertEqual(points_for_answer("A", "A", "Hard"), 3)
        self.assertEqual(points_for_answer("B", "A", "Hard"), 0)

    def test_percentage_and_empty(self):
        self.assertEqual(percentage(3, 4), 75.0)
        self.assertEqual(percentage(1, 0), 0.0)

    def test_summary(self):
        self.assertEqual(summarize([True, False, True], "Medium")["score"], 4)


if __name__ == "__main__":
    unittest.main()
