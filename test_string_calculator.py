import pytest
from string_calculator import StringCalculator


@pytest.fixture
def calculator():
    return StringCalculator()


def test_add_empty_string_returns_zero(calculator):
    result = calculator.add("")
    assert result == 0


def test_add_single_number_returns_number(calculator):
    result = calculator.add("1")
    assert result == 1

def test_add_multiple_numbers_returns_sum(calculator):
    result = calculator.add("1,5")
    assert result == 6