import unittest
from projectToTest import lessThan

class TestProjectToTest(unittest.TestCase):

    def test_lessThan(self):
        self.assertTrue(lessThan(1, 2))  # Should return True because 1 < 2
        self.assertFalse(lessThan(2, 1))  # Should return False because 2 is not less than 1
        self.assertFalse(lessThan(1, 1))  # Should return False because 1 is not less than 1
        self.assertFalse(lessThan('a',5))

if __name__ == '__main__':
    unittest.main()
