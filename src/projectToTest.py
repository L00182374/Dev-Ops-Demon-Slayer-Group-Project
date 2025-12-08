#projectToTest
import pydoc# for automatic documentation generation
import logging# for logging

logging.basicConfig(filename='projectToTest.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)# Create a logger for this module
logger.info('Module projectToTest loaded')# Log that the module has been loaded

def lessThan(a,b):# Function to check if a is less than b
    '''
    Parameters: integers a and b
    Returns: True if a is less than b, False otherwise
    Raises TypeError if inputs are of different types than integers
    '''
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):# Check for numeric types
        raise TypeError("lessThan expects numeric inputs")# Raise TypeError for invalid types
    
    if a < b:
        return True
    else:
        return False
    

def greaterThan(a,b):# Function to check if a is greater than b
    '''
    Parameters: integers a and b
    Returns: True if a is greater than b, False otherwise
    Raises TypeError if inputs are of different types than integers
    '''

    if not (isinstance(a, (int)) and isinstance(b, (int))):# Check for numeric types
        raise TypeError("greaterThan expects numeric inputs")# Raise TypeError for invalid types

    if a > b:
        logger.info(f'greaterThan called with a={a}, b={b}, returning True')
        return True
    else:
        logger.info(f'greaterThan called with a={a}, b={b}, returning False')
        return False
    

def equalTo(a,b):# Function to check if a is equal to b
    '''
    Parameters: integers a and b
    Returns: True if a is equal to b, False otherwise
    Raises TypeError if inputs are of different types than integers
    '''

    if not (isinstance(a, (int)) and isinstance(b, (int))):# Check for numeric types
        raise TypeError("equalTo expects numeric inputs")# Raise TypeError for invalid types

    if a == b:
        logger.info(f'equalTo called with a={a}, b={b}, returning True')
        return True
    else:
        logger.info(f'equalTo called with a={a}, b={b}, returning False')
        return False
    

def notEqualTo(a,b):# Function to check if a is not equal to b
    '''
    Parameters: integers a and b
    Returns: True if a is not equal to b, False otherwise
    Raises TypeError if inputs are of different types than integers
    '''

    if not (isinstance(a, (int)) and isinstance(b, (int))):# Check for numeric types
        raise TypeError("notEqualTo expects numeric inputs")# Raise TypeError for invalid types

    if a != b:
        logger.info(f'notEqualTo called with a={a}, b={b}, returning True')
        return True
    else:
        logger.info(f'notEqualTo called with a={a}, b={b}, returning False')
        return False

pydoc.writedoc('projectToTest')# This will automatically generate the documentation for this file
logger.info('Documentation for projectToTest generated')