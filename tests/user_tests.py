import unittest

from models.user import User

class TestUser(  unittest.TestCase  ):

    def setUp(self):
        self.user_1 = User("Matt", "Round", "male", 32, 90.82, 183, 8)