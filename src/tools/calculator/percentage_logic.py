from typing import NamedTuple


class PercentageResult(NamedTuple):
    percentage_of_value: float
    value_plus_percentage: float


def calculate_percentage(value: float, percentage: float) -> PercentageResult:
    """Calculate percentage of a value and value + percentage.
    
    Args:
        value: The base value
        percentage: The percentage amount
    
    Returns:
        PercentageResult with percentage_of_value and value_plus_percentage
    """
    percentage_amount = (percentage / 100) * value
    return PercentageResult(
        percentage_of_value=percentage_amount,
        value_plus_percentage=value + percentage_amount,
    )
