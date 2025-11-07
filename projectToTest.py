#projectToTest
import pydoc# for automatic documentation generation

def lessThan(a,b):# Function to check if a is less than b
    '''
    Parameters: integers a and b
    Returns: True if a is less than b, False otherwise
    '''

    if a < b:
        return True
    else:
        return False
    

def greaterThan(a,b):# Function to check if a is greater than b
    '''
    Parameters: integers a and b
    Returns: True if a is greater than b, False otherwise
    '''

    if a > b:
        return True
    else:
        return False

pydoc.writedoc('projectToTest')# This will automatically generate the documentation for this file
