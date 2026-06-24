from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QComboBox

from src.core.tool import Tool
from src.tools.converter.temperature_logic import convert_temperature


class TemperatureConverterTool(Tool):
    CONVERT_LABEL = "Convert"
    UNITS = ["C", "F", "K"]

    def __init__(self) -> None:
        super().__init__(name="Temperature Converter", category="Converter")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Value:", widget))
        self._value = QLineEdit(widget)
        input_layout.addWidget(self._value)

        input_layout.addWidget(QLabel("Unit:", widget))
        self._unit = QComboBox(widget)
        self._unit.addItems(self.UNITS)
        input_layout.addWidget(self._unit)

        self._convert_button = QPushButton(self.CONVERT_LABEL, widget)
        self._convert_button.clicked.connect(self._do_convert)

        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)

        layout.addLayout(input_layout)
        layout.addWidget(self._convert_button)
        layout.addWidget(self._output)
        widget.setLayout(layout)
        return widget

    def _do_convert(self) -> None:
        try:
            value = float(self._value.text())
            from_unit = self._unit.currentText()
            result = convert_temperature(value, from_unit)
            output_text = f"{value}°{from_unit}\n"
            output_text += f"Celsius: {result.celsius}°C\n"
            output_text += f"Fahrenheit: {result.fahrenheit}°F\n"
            output_text += f"Kelvin: {result.kelvin}K"
            self._output.setPlainText(output_text)
        except ValueError:
            self._output.setPlainText("Please enter a valid number")
        except Exception as exc:
            self._output.setPlainText(f"Error: {exc}")
