import unittest

from models.exercise import Exercise

class TestExercise(  unittest.TestCase  ):

    def setUp(self):
        self.exercise_1 = Exercise("Loaded", "Squat", 100, 98.5, 3)
        self.exercise_2 = Exercise("Bodyweight","Push-up", 30, 32, 17)
        