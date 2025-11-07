import unittest# for unit testing
from projectToTest import lessThan# import the function to be tested

class TestProjectToTest(unittest.TestCase):# create a test case class

    def test_lessThan(self):# define a test method
        self.assertTrue(lessThan(1, 2))  # Should return True because 1 < 2
        self.assertFalse(lessThan(2, 1))  # Should return False because 2 is not less than 1
        self.assertFalse(lessThan(1, 1))  # Should return False because 1 is not less than 1
        #self.assertFalse(lessThan('a',5)) # creates an error because 'a' and 5 are of different types

if __name__ == '__main__':# run the unit tests
    unittest.main()
