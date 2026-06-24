import pytest
from src.tools.converter.temperature_logic import convert_temperature


def test_convert_celsius_to_fahrenheit():
    result = convert_temperature(0, "C")
    assert result.fahrenheit == 32
    assert result.celsius == 0


def test_convert_fahrenheit_to_celsius():
    result = convert_temperature(32, "F")
    assert result.celsius == 0
    assert result.fahrenheit == 32


def test_convert_kelvin():
    result = convert_temperature(273.15, "K")
    assert result.celsius == 0
    assert result.kelvin == 273.15


def test_convert_temperature_invalid_unit():
    with pytest.raises(ValueError):
        convert_temperature(100, "X")
