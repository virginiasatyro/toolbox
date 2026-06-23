from src.tools.text.base64_logic import decode_base64, encode_base64


def test_base64_encode_returns_correct_value():
    assert encode_base64("hello") == "aGVsbG8="


def test_base64_decode_returns_correct_value():
    assert decode_base64("aGVsbG8=") == "hello"


def test_base64_decode_raises_for_invalid_input():
    import pytest

    with pytest.raises((ValueError, TypeError)):
        decode_base64("!!!")
