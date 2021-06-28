import unittest

from models.workout import Workout

class TestWorkout(  unittest.TestCase ):

    def setUp(self):
        self.workout_1 = Workout("Squat",30, 5, 5, 4, "Felt hard today, feeling tired", 8)
        self.workout_2 = Workout("Bicep Curl",7, 4, 12, 1.5, "Felt really easy", 56)

    def test_exercise(self):
        expected = "Bicep Curl"
        actual = self.workout_2.exercise
        self.assertEqual(expected, actual)

    def test_weight(self):
        expected = 30
        actual = self.workout_1.weight
        self.assertEqual(expected, actual)

    def test_sets(self):
        expected = 5
        actual = self.workout_1.sets
        self.assertEqual(expected, actual)

    def test_repetitions(self):
        expected = 12
        actual = self.workout_2.repetitions
        self.assertEqual(expected, actual)

    def test_rest_time(self):
        expected = 1.5
        actual = self.workout_2.rest_time
        self.assertEqual(expected, actual)

    def test_comments(self):
        expected = "Felt hard today, feeling tired"
        actual = self.workout_1.comments
        self.assertEqual(expected, actual)

    def test_id(self):
        expected = 56
        actual = self.workout_2.id
        self.assertEqual(expected, actual)