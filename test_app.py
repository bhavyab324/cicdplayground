import unittest
from app import sum


class TestApp(unittest.TestCase):
    def test_add(self):
        self.assertEqual(sum(2, 3), 5)
