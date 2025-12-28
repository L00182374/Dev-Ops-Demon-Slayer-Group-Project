import pytest

from projectToTest import lessThan, greaterThan, equalTo, notEqualTo


@pytest.mark.integration
def test_lessThan():
    assert lessThan(3, 5) is True
    assert lessThan(5, 3) is False
    assert lessThan(5, 5) is False


@pytest.mark.integration
def test_greaterThan():

    assert greaterThan(5, 3) is True
    assert greaterThan(3, 5) is False
    assert greaterThan(5, 5) is False


@pytest.mark.integration
def test_equalTo():
    assert equalTo(5, 5) is True
    assert equalTo(3, 5) is False
    assert equalTo(5, 3) is False


@pytest.mark.integration
def test_notEqualTo():
    assert notEqualTo(3, 5) is True
    assert notEqualTo(5, 3) is True
    assert notEqualTo(5, 5) is False


@pytest.mark.integration
def test_combined_conditions():
    assert lessThan(2, 4) and greaterThan(6, 4) is True
    assert equalTo(3, 3) or notEqualTo(3, 4) is True
    assert notEqualTo(5, 5) or lessThan(1, 0) is False
    assert greaterThan(10, 5) and equalTo(10, 10) is True


@pytest.mark.integration
def test_edge_cases():
    assert lessThan(-1, 0) is True
    assert greaterThan(0, -1) is True
    assert equalTo(0, 0) is True
    assert notEqualTo(-1, -1) is False


@pytest.mark.integration
def test_performance():
    import time

    start_time = time.time()
    for _ in range(100000):
        lessThan(1, 2)
        greaterThan(2, 1)
        equalTo(3, 3)
        notEqualTo(4, 5)
    end_time = time.time()

    assert (end_time - start_time) < 1  # Ensure the operations complete within 1 second
