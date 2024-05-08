import unittest
from test import say_hi  

class TestSayHi(unittest.TestCase):
    def test_say_hi(self):
        # Test case 1: When passing a name, it should return "Hi" followed by the name
        self.assertEqual(say_hi("Alice"), "Hi Alice")

        # Test case 2: When passing an empty string, it should return "Hi"
        self.assertEqual(say_hi(""), "Hi ")

        # Test case 3: When passing None, it should return "Hi None"
        self.assertEqual(say_hi(None), "Hi None")

if __name__ == '__main__':
    unittest.main()
