import unittest  # for unit testing
import logging  # for logging
from src.projectToTest import lessThan  # import the function to be tested
from src.projectToTest import greaterThan  # import the second function to be tested
from src.projectToTest import equalTo  # import the third function to be tested
from src.projectToTest import notEqualTo  # import the fourth function to be tested

# logging.basicConfig(filename='tests.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Create a logger for this test module
logger.info('Test module loaded')  # Log that the test module has been loaded

class TestProjectToTest(unittest.TestCase):  # create a test case class


    logger.info('Starting tests for projectToTest functions')  # Log the start of tests

    def test_lessThan(self):  # define a test method
        self.assertTrue(lessThan(1, 2))  # Should return True because 1 < 2
        self.assertFalse(lessThan(2, 1))  # Should return False because 2 is not less than 1
        self.assertFalse(lessThan(1, 1))  # Should return False because 1 is not less than 1
        # self.assertFalse(lessThan('a',5)) # creates an error because 'a' and 5 are of different types
        logger.info('Completed tests for lessThan function')  # Log completion of this test

    def test_greaterThan(self):  # define another test method
        self.assertTrue(greaterThan(2, 1))  # Should return True because 2 > 1
        self.assertFalse(greaterThan(1, 2))  # Should return False because 1 is not greater than 2
        self.assertFalse(greaterThan(1, 1))  # Should return False because 1 is not greater than 1
        # self.assertFalse(greaterThan('a',5)) # creates an error because 'a' and 5 are of different types
        logger.info('Completed tests for greaterThan function')  # Log completion of this test

    def test_equalTo(self):  # define another test method
        self.assertTrue(equalTo(2, 2))  # Should return True because 2 == 2
        self.assertFalse(equalTo(1, 2))  # Should return False because 1 != 2
        self.assertFalse(equalTo(2, 1))  # Should return False because 2 != 1
        logger.info('Completed tests for equalTo function')  # Log completion of this test

    def test_notEqualTo(self):  # define another test method
        self.assertTrue(notEqualTo(1, 2))  # Should return True because 1 != 2
        self.assertFalse(notEqualTo(2, 2))  # Should return False because 2 == 2
        self.assertTrue(notEqualTo(2, 1))  # Should return True because 2 != 1
        logger.info('Completed tests for notEqualTo function')  # Log completion of this test

    def test_invalidInputs(self):  # define a test method for invalid inputs
        with self.assertRaises(TypeError):
            lessThan('a', 5)
        with self.assertRaises(TypeError):
            greaterThan('a', 5)
        with self.assertRaises(TypeError):
            equalTo('a', 5)
        with self.assertRaises(TypeError):
            notEqualTo('a', 5)
        logger.info('Completed tests for invalid inputs')  # Log completion of this test

if __name__ == '__main__':  # run the unit tests
    logger.info('Running all tests')  # Log that tests are being run
    unittest.main()

# might need to remove logging from tests.py if it causes issues
