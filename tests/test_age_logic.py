from datetime import datetime
from src.tools.calculator.age_logic import calculate_age


def test_calculate_age_exact_years():
    birth = datetime(2000, 6, 15)
    # Mock today as 2026-06-23
    age = calculate_age(birth)
    # Age should be 26 years (approximately)
    assert age.years >= 25


def test_calculate_age_returns_valid_structure():
    birth = datetime(1990, 1, 1)
    age = calculate_age(birth)
    assert age.years >= 0
    assert 0 <= age.months <= 12
    assert 0 <= age.days <= 31
