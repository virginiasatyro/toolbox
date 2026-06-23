from PySide6.QtWidgets import QPushButton, QPlainTextEdit, QVBoxLayout, QWidget, QHBoxLayout, QLabel

from src.core.tool import Tool
from src.tools.text.base64_logic import decode_base64, encode_base64


class Base64Tool(Tool):
    ENCODE_LABEL = "Encode"
    DECODE_LABEL = "Decode"
    INVALID_MESSAGE = "Invalid Base64 input"

    def __init__(self) -> None:
        super().__init__(name="Base64 Encode / Decode", category="Text")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel("Input", widget))
        self._input = QPlainTextEdit(widget)
        layout.addWidget(self._input)

        button_layout = QHBoxLayout()
        self._encode_button = QPushButton(self.ENCODE_LABEL, widget)
        self._decode_button = QPushButton(self.DECODE_LABEL, widget)
        self._encode_button.clicked.connect(self._encode_text)
        self._decode_button.clicked.connect(self._decode_text)
        button_layout.addWidget(self._encode_button)
        button_layout.addWidget(self._decode_button)

        layout.addLayout(button_layout)
        layout.addWidget(QLabel("Output", widget))
        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)
        layout.addWidget(self._output)

        widget.setLayout(layout)
        return widget

    def _encode_text(self) -> None:
        raw = self._input.toPlainText()
        self._output.setPlainText(encode_base64(raw))

    def _decode_text(self) -> None:
        input_text = self._input.toPlainText()
        try:
            self._output.setPlainText(decode_base64(input_text))
        except (ValueError, TypeError):
            self._output.setPlainText(self.INVALID_MESSAGE)
