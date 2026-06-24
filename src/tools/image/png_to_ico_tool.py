from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QFileDialog
from src.core.tool import Tool
from src.tools.image.image_utils import png_to_ico


class PngToIcoTool(Tool):
    BROWSE_LABEL = "Browse..."
    CONVERT_LABEL = "Convert"

    def __init__(self) -> None:
        super().__init__(name="PNG → ICO", category="Image")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("PNG:", widget))
        self._path_edit = QLineEdit(widget)
        input_layout.addWidget(self._path_edit)
        browse = QPushButton(self.BROWSE_LABEL, widget)
        browse.clicked.connect(self._browse_file)
        input_layout.addWidget(browse)

        self._do_button = QPushButton(self.CONVERT_LABEL, widget)
        self._do_button.clicked.connect(self._do_convert)

        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)

        layout.addLayout(input_layout)
        layout.addWidget(self._do_button)
        layout.addWidget(self._output)
        widget.setLayout(layout)
        return widget

    def _browse_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(None, "Select PNG", "", "PNG Images (*.png)")
        if path:
            self._path_edit.setText(path)

    def _do_convert(self) -> None:
        try:
            input_path = self._path_edit.text().strip()
            if not input_path.lower().endswith('.png'):
                self._output.setPlainText('Please select a PNG file')
                return
            output_path = input_path.rsplit('.', 1)[0] + '.ico'
            png_to_ico(input_path, output_path)
            self._output.setPlainText(f"Saved: {output_path}")
        except Exception as exc:
            self._output.setPlainText(f"Error: {exc}")
