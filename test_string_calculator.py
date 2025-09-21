import pytest
import sys
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

def test_add_any_amount_of_numbers_returns_sum(calculator):
    result = calculator.add("1,2,3,4,5")
    assert result == 15

def test_add_sum_too_large_raises_overflow_error(calculator):
    large_number = str(sys.maxsize // 4)
    numbers = f"{large_number},{large_number},{large_number}"
    with pytest.raises(OverflowError, match="Sum too large to return safely"):
        calculator.add(numbers)

def test_add_many_numbers_handles_memory_efficiently(calculator):
    numbers = ",".join(str(i) for i in range(1, 1001))
    result = calculator.add(numbers)
    assert result == 500500

def test_add_too_many_numbers_raises_error(calculator):
    numbers = ",".join(str(i) for i in range(1, 10002))
    with pytest.raises(ValueError, match="Too many numbers to process"):
        calculator.add(numbers)
        
def test_add_with_newline_delimiter_returns_sum(calculator):
    result = calculator.add("1\n2,3")
    assert result == 6

def test_add_with_only_newline_delimiters(calculator):
    result = calculator.add("1\n2\n3")
    assert result == 6

def test_add_with_custom_delimiter_semicolon(calculator):
    result = calculator.add("//;\n1;2")
    assert result == 3


def test_add_with_custom_delimiter_pipe(calculator):
    result = calculator.add("//|\n1|2|3")
    assert result == 6


def test_add_with_custom_delimiter_mixed_with_default(calculator):
    result = calculator.add("//;\n1;2,3\n4")
    assert result == 10


def test_add_with_invalid_custom_delimiter_format(calculator):
    with pytest.raises(ValueError, match="Invalid custom delimiter format"):
        calculator.add("//;1;2")

def test_add_with_single_negative_number_raises_error(calculator):
    with pytest.raises(ValueError, match="negative numbers not allowed -1"):
        calculator.add("1,-1,2")


def test_add_with_multiple_negative_numbers_raises_error(calculator):
    with pytest.raises(ValueError, match="negative numbers not allowed -1, -2, -3"):
        calculator.add("1,-1,2,-2,3,-3")


def test_add_with_negative_numbers_and_custom_delimiter(calculator):
    with pytest.raises(ValueError, match="negative numbers not allowed -1, -2"):
        calculator.add("//;\n1;-1;2;-2")


def test_add_with_negative_numbers_and_newline_delimiter(calculator):
    with pytest.raises(ValueError, match="negative numbers not allowed -1, -2"):
        calculator.add("1\n-1\n2\n-2")