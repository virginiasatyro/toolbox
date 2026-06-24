from datetime import datetime
from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from src.core.tool import Tool
from src.tools.calculator.age_logic import calculate_age


class AgeCalculatorTool(Tool):
    CALCULATE_LABEL = "Calculate"
    DATE_FORMAT = "DD/MM/YYYY"

    def __init__(self) -> None:
        super().__init__(name="Age Calculator", category="Calculator")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        layout.addWidget(QLabel(f"Birth Date ({self.DATE_FORMAT}):", widget))
        self._birth_date = QLineEdit(widget)
        layout.addWidget(self._birth_date)

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
            date_str = self._birth_date.text().strip()
            birth_date = datetime.strptime(date_str, "%d/%m/%Y")
            result = calculate_age(birth_date)
            output_text = f"Age: {result.years} years, {result.months} months, {result.days} days"
            self._output.setPlainText(output_text)
        except ValueError:
            self._output.setPlainText(f"Invalid date format. Use {self.DATE_FORMAT}")
        except Exception as exc:
            self._output.setPlainText(f"Error: {exc}")
