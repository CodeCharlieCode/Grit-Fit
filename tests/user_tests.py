import unittest

from models.user import User

class TestUser(  unittest.TestCase  ):

    def setUp(self):
        self.user_1 = User("Matt", "Round", "male", 32, 90.82, 183, 8)
        self.user_2 = User("Hannah", "Black", "female", 26, 57.6, 167, 10)

    def test_first_name(self):
        expected = "Matt"
        actual = self.user_1.first_name
        self.assertEqual(expected, actual)

    def test_last_name(self):
        expected = "Round"
        actual = self.user_1.last_name
        self.assertEqual(expected, actual)

    def test_gender(self):
        expected = "female"
        actual = self.user_2.gender
        self.assertEqual(expected, actual)

    def test_age(self):
        expected = 26
        actual = self.user_2.age
        self.assertEqual(expected, actual)

    def test_weight(self):
        expected = 90.82
        actual = self.user_1.weight
        self.assertEqual(expected, actual)

    def test_height(self):
        expected = 167
        actual = self.user_2.height
        self.assertEqual(expected, actual)

    def test_id(self):
        expected = 8
        actual = self.user_1.id
        self.assertEqual(expected, actual)

