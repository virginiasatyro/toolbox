from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QFileDialog
from src.core.tool import Tool
from src.tools.image.image_utils import rotate_image


class RotateTool(Tool):
    BROWSE_LABEL = "Browse..."
    ROTATE_LABEL = "Rotate"

    def __init__(self) -> None:
        super().__init__(name="Rotate Image", category="Image")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Image:", widget))
        self._path_edit = QLineEdit(widget)
        input_layout.addWidget(self._path_edit)
        browse = QPushButton(self.BROWSE_LABEL, widget)
        browse.clicked.connect(self._browse_file)
        input_layout.addWidget(browse)

        angle_layout = QHBoxLayout()
        angle_layout.addWidget(QLabel("Degrees:", widget))
        self._degrees = QLineEdit(widget)
        angle_layout.addWidget(self._degrees)

        self._do_button = QPushButton(self.ROTATE_LABEL, widget)
        self._do_button.clicked.connect(self._do_rotate)

        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)

        layout.addLayout(input_layout)
        layout.addLayout(angle_layout)
        layout.addWidget(self._do_button)
        layout.addWidget(self._output)
        widget.setLayout(layout)
        return widget

    def _browse_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(None, "Select image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self._path_edit.setText(path)

    def _do_rotate(self) -> None:
        try:
            input_path = self._path_edit.text().strip()
            degrees = int(self._degrees.text())
            output_path = input_path.rsplit(".", 1)[0] + f"_rotated.{input_path.rsplit('.',1)[1]}"
            rotate_image(input_path, output_path, degrees)
            self._output.setPlainText(f"Saved: {output_path}")
        except Exception as exc:
            self._output.setPlainText(f"Error: {exc}")
