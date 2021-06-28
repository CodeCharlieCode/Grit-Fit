import unittest

from models.user import User

class TestUser(  unittest.TestCase  ):

    def setUp(self):
        self.user_1 = User("Matt", "Round", "male", 32, 90.82, 183, 8)
        self.user_2 = User("Hannah", "Black", "female", 26, 57.6, 167)

    def test_first_name(self):
        expected = "Matt"
        actual = self.user_1.first_name
        self.assertEqual(expected, actual)

    def test_last_name(self):
        expected = "Round"
        actual = self.user_1.last_name
        self.assertEqual(expected, actual)