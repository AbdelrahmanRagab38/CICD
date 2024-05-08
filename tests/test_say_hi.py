import unittest
from test import say_hi  

class TestSayHi(unittest.TestCase):
    def test_say_hi(self):
        # Test case 1: When passing a name, it should return "Hi" followed by the name
        self.assertEqual(say_hi("Alice"), "Hi Alice")

        # Test case 2: When passing an empty string, it should return "Hi"
        self.assertEqual(say_hi(""), "Hi ")


if __name__ == '__main__':
    unittest.main()
