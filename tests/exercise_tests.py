import unittest

from models.exercise import Exercise

class TestExercise(  unittest.TestCase  ):

    def setUp(self):
        self.exercise_1 = Exercise("Loaded", "Squat", 100, 98.5, 3)
        self.exercise_2 = Exercise("Bodyweight","Push-up", 30, 32, 17)

    def test_exercise_type(self):
        expected = "Loaded"
        actual = self.exercise_1.exercise_type
        self.assertEqual(expected, actual)

    def test_name_of_exercsie(self):
        expected = "Push-up"
        actual = self.exercise_2.name_of_exercise
        self.assertEqual(expected, actual)

    def test_rep_max(self):
        expected = 100
        actual = self.exercise_1.rep_max
        self.assertEqual(expected, actual)

    def test_personal_best(self):
        expected = 32
        actual = self.exercise_2.personal_best
        self.assertEqual(expected, actual)

    def test_id(self):
        expected = 17
        actual = self.exercise_2.id
        self.assertEqual(expected, actual)
        