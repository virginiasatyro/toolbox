from PySide6.QtWidgets import QLabel, QPlainTextEdit, QVBoxLayout, QWidget
from PySide6.QtCore import Qt

from src.core.tool import Tool
from src.tools.text.word_counter import build_word_count_result


class WordCounterTool(Tool):
    INITIAL_STATUS_TEXT = "Words: 0, Characters: 0, Lines: 0"

    def __init__(self) -> None:
        super().__init__(name="Word Counter", category="Text")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        self._editor = QPlainTextEdit(widget)
        self._status = QLabel(self.INITIAL_STATUS_TEXT, widget)
        self._status.setAlignment(Qt.AlignmentFlag.AlignLeft)

        self._editor.textChanged.connect(self._update_counters)

        layout.addWidget(self._editor)
        layout.addWidget(self._status)
        widget.setLayout(layout)
        return widget

    def _update_counters(self) -> None:
        content = self._editor.toPlainText()
        result = build_word_count_result(content)
        self._status.setText(
            f"Words: {result.words}, Characters: {result.characters}, Lines: {result.lines}"
        )
