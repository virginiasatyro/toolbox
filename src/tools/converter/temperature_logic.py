from typing import NamedTuple


class TemperatureConversion(NamedTuple):
    celsius: float
    fahrenheit: float
    kelvin: float


def convert_temperature(value: float, from_unit: str) -> TemperatureConversion:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin.
    
    Args:
        value: Temperature value
        from_unit: "C", "F", or "K"
    
    Returns:
        TemperatureConversion with all three units
    """
    from_unit = from_unit.strip().upper()
    
    if from_unit == "C":
        celsius = value
        fahrenheit = (celsius * 9 / 5) + 32
        kelvin = celsius + 273.15
    elif from_unit == "F":
        fahrenheit = value
        celsius = (fahrenheit - 32) * 5 / 9
        kelvin = celsius + 273.15
    elif from_unit == "K":
        kelvin = value
        celsius = kelvin - 273.15
        fahrenheit = (celsius * 9 / 5) + 32
    else:
        raise ValueError("from_unit must be 'C', 'F', or 'K'")
    
    return TemperatureConversion(
        celsius=round(celsius, 2),
        fahrenheit=round(fahrenheit, 2),
        kelvin=round(kelvin, 2),
    )
