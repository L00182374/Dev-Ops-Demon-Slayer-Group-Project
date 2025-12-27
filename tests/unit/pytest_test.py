import pytest  # Using pytest for testing

# import logging# for logging
from projectToTest import (
    lessThan,
    greaterThan,
    equalTo,
    notEqualTo,
)  # import functions to be tested

# logger = logging.getLogger(__name__)# Create a logger for this test module


@pytest.mark.parametrize(
    "a,b,expected",
    [  # define test cases for lessThan
        (1, 2, True),
        (2, 1, False),
        (1, 1, False),
    ],
)
def test_less_than_param(a, b, expected):  # define a test method for lessThan
    assert lessThan(a, b) is expected  # Check the result against expected


# logger.info("lessThan(%s, %s) -> %s", a, b, expected)# Log each test case result


@pytest.mark.parametrize(
    "a,b,expected",
    [  # define test cases for greaterThan
        (2, 1, True),
        (1, 2, False),
        (1, 1, False),
    ],
)
def test_greater_than_param(a, b, expected):  # define a test method for greaterThan
    assert greaterThan(a, b) is expected  # Check the result against expected
    # logger.info("greaterThan(%s, %s) -> %s", a, b, expected)# Log each test case result


@pytest.mark.parametrize(
    "a,b,expected",
    [  # define test cases for equalTo
        (2, 2, True),
        (1, 2, False),
        (2, 1, False),
    ],
)
def test_equal_to_param(a, b, expected):  # define a test method for equalTo
    assert equalTo(a, b) is expected  # Check the result against expected


# logger.info("equalTo(%s, %s) -> %s", a, b, expected)# Log each test case result


@pytest.mark.parametrize(
    "a,b,expected",
    [  # define test cases for notEqualTo
        (1, 2, True),
        (2, 2, False),
        (2, 1, True),
    ],
)
def test_not_equal_to_param(a, b, expected):  # define a test method for notEqualTo
    assert notEqualTo(a, b) is expected  # Check the result against expected


# logger.info("notEqualTo(%s, %s) -> %s", a, b, expected)# Log each test case result


@pytest.mark.parametrize(
    "func", [lessThan, greaterThan, equalTo, notEqualTo]
)  # define test cases for invalid inputs
def test_invalid_inputs_raise_typeerror(
    func,
):  # define a test method for invalid inputs
    with pytest.raises(TypeError):  # expect TypeError for invalid inputs
        func("a", 5)  # Call the function with invalid inputs


# logger.info("Function %s raised TypeError for invalid inputs", func.__name__)# Log the exception occurrence
