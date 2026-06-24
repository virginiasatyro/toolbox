import pytest
from src.tools.converter.datasize_logic import convert_data_size


def test_convert_bytes_to_kb():
    result = convert_data_size(1024, "B")
    assert result.kb == 1


def test_convert_kb_to_mb():
    result = convert_data_size(1, "KB")
    kb_in_bytes = 1 * 1024
    assert result.kb == 1


def test_convert_mb_to_gb():
    result = convert_data_size(1, "MB")
    assert result.mb == 1


def test_convert_datasize_invalid_unit():
    with pytest.raises(ValueError):
        convert_data_size(100, "ZB")
