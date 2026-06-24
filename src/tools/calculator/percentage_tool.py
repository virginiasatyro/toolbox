from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from src.core.tool import Tool
from src.tools.calculator.percentage_logic import calculate_percentage


class PercentageCalculatorTool(Tool):
    CALCULATE_LABEL = "Calculate"

    def __init__(self) -> None:
        super().__init__(name="Percentage Calculator", category="Calculator")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel("Value:", widget))
        self._value = QLineEdit(widget)
        layout.addWidget(self._value)

        layout.addWidget(QLabel("Percentage:", widget))
        self._percentage = QLineEdit(widget)
        layout.addWidget(self._percentage)

        self._calculate_button = QPushButton(self.CALCULATE_LABEL, widget)
        self._calculate_button.clicked.connect(self._do_calculate)

        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)

        layout.addWidget(self._calculate_button)
        layout.addWidget(self._output)
        widget.setLayout(layout)
        return widget

    def _do_calculate(self) -> None:
        try:
            value = float(self._value.text())
            percentage = float(self._percentage.text())
            result = calculate_percentage(value, percentage)
            output_text = f"{percentage}% of {value} = {result.percentage_of_value}\n"
            output_text += f"{value} + {percentage}% = {result.value_plus_percentage}"
            self._output.setPlainText(output_text)
        except ValueError:
            self._output.setPlainText("Please enter valid numbers")
        except Exception as exc:
            self._output.setPlainText(f"Error: {exc}")
