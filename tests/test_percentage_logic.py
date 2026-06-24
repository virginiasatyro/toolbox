import pytest
from datetime import datetime
from src.tools.calculator.percentage_logic import calculate_percentage


def test_calculate_percentage_of_value():
    result = calculate_percentage(500, 15)
    assert result.percentage_of_value == 75


def test_calculate_percentage_value_plus_percentage():
    result = calculate_percentage(500, 15)
    assert result.value_plus_percentage == 575


def test_calculate_percentage_zero_value():
    result = calculate_percentage(0, 50)
    assert result.percentage_of_value == 0
    assert result.value_plus_percentage == 0


def test_calculate_percentage_negative_percentage():
    result = calculate_percentage(100, -10)
    assert result.percentage_of_value == -10
    assert result.value_plus_percentage == 90
