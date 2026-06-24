from datetime import datetime
from typing import NamedTuple


class AgeResult(NamedTuple):
    years: int
    months: int
    days: int


def calculate_age(birth_date: datetime) -> AgeResult:
    """Calculate age in years, months, and days from a birth date to today.
    
    Args:
        birth_date: datetime object of birth
    
    Returns:
        AgeResult with years, months, days
    """
    today = datetime.today()
    
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day
    
    if days < 0:
        months -= 1
        days += 30
    
    if months < 0:
        years -= 1
        months += 12
    
    return AgeResult(years=years, months=months, days=days)
