from PySide6.QtWidgets import QPlainTextEdit, QVBoxLayout, QWidget, QLabel
from PySide6.QtCore import Qt

from src.core.tool import Tool
from src.tools.text.hashtag_converter_logic import convert_text_to_hashtags


class HashtagConverterTool(Tool):
    def __init__(self) -> None:
        super().__init__(name="Hashtag Converter", category="Text")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel("Input:", widget))
        self._input = QPlainTextEdit(widget)
        layout.addWidget(self._input)

        layout.addWidget(QLabel("Output:", widget))
        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)
        layout.addWidget(self._output)

        self._input.textChanged.connect(self._update_output)

        widget.setLayout(layout)
        return widget

    def _update_output(self) -> None:
        content = self._input.toPlainText()
        result = convert_text_to_hashtags(content)
        self._output.setPlainText(result)
