from PySide6.QtWidgets import QPushButton, QSpinBox, QVBoxLayout, QWidget, QPlainTextEdit, QLabel, QHBoxLayout

from src.core.tool import Tool
from src.tools.text.lorem_ipsum_logic import generate_lorem_ipsum


class LoremIpsumTool(Tool):
    PARAGRAPH_LABEL = "Paragraphs:"
    GENERATE_LABEL = "Generate"
    MIN_PARAGRAPHS = 1
    MAX_PARAGRAPHS = 10
    DEFAULT_PARAGRAPHS = 3

    def __init__(self) -> None:
        super().__init__(name="Lorem Ipsum Generator", category="Text")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        control_layout = QHBoxLayout()
        control_layout.addWidget(QLabel(self.PARAGRAPH_LABEL, widget))

        self._paragraphs_input = QSpinBox(widget)
        self._paragraphs_input.setMinimum(self.MIN_PARAGRAPHS)
        self._paragraphs_input.setMaximum(self.MAX_PARAGRAPHS)
        self._paragraphs_input.setValue(self.DEFAULT_PARAGRAPHS)
        control_layout.addWidget(self._paragraphs_input)

        self._generate_button = QPushButton(self.GENERATE_LABEL, widget)
        self._generate_button.clicked.connect(self._generate_text)
        control_layout.addWidget(self._generate_button)

        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)

        layout.addLayout(control_layout)
        layout.addWidget(self._output)
        widget.setLayout(layout)
        return widget

    def _generate_text(self) -> None:
        paragraphs = self._paragraphs_input.value()
        generated = generate_lorem_ipsum(paragraphs)
        self._output.setPlainText(generated)
