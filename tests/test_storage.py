import json
import tempfile
import unittest
from pathlib import Path
from storage import load_json, save_json
from leaderboard import sorted_entries
from main import choose
from performance import summarize_attempts


class StorageTests(unittest.TestCase):
    def test_json_round_trip_and_missing_file(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "nested" / "data.json"
            self.assertEqual(load_json(path, []), [])
            self.assertTrue(path.exists())
            save_json(path, {"value": 7})
            self.assertEqual(load_json(path, {}), {"value": 7})

    def test_empty_and_invalid_json_recover(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "data.json"
            path.write_text("", encoding="utf-8")
            self.assertEqual(load_json(path, []), [])
            path.write_text("{broken", encoding="utf-8")
            self.assertEqual(load_json(path, {"safe": True}), {"safe": True})

    def test_leaderboard_sorting(self):
        rows = [{"score": 3}, {"score": 8}, {"score": 5}]
        self.assertEqual([r["score"] for r in sorted_entries(rows)], [8, 5, 3])

    def test_invalid_input_retries_then_accepts(self):
        values = iter(["x", "9", "2"])
        messages = []
        self.assertEqual(choose("", 1, 3, lambda _: next(values), messages.append), 2)
        self.assertEqual(len(messages), 2)

    def test_empty_performance_summary(self):
        summary = summarize_attempts([])
        self.assertEqual(summary["quizzes"], 0)
        self.assertEqual(summary["accuracy"], 0.0)


if __name__ == "__main__":
    unittest.main()
