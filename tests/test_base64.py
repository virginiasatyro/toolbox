import base64

from src.tools.text.base64_tool import Base64Tool


def test_base64_encode():
    tool = Base64Tool()
    tool._input = type("Dummy", (), {"toPlainText": lambda self: "test"})()
    tool._output = type("Dummy", (), {"setPlainText": lambda self, value: setattr(self, "value", value)})()

    tool._encode_text()

    assert tool._output.value == base64.b64encode(b"test").decode("utf-8")


def test_base64_decode_valid():
    tool = Base64Tool()
    tool._input = type("Dummy", (), {"toPlainText": lambda self: base64.b64encode(b"hello").decode("utf-8")})()
    tool._output = type("Dummy", (), {"setPlainText": lambda self, value: setattr(self, "value", value)})()

    tool._decode_text()

    assert tool._output.value == "hello"


def test_base64_decode_invalid():
    tool = Base64Tool()
    tool._input = type("Dummy", (), {"toPlainText": lambda self: "invalid!!"})()
    tool._output = type("Dummy", (), {"setPlainText": lambda self, value: setattr(self, "value", value)})()

    tool._decode_text()

    assert tool._output.value == "Invalid Base64 input"
