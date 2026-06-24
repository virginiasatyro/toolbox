from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QFileDialog
from src.core.tool import Tool
from src.tools.image.image_utils import resize_image


class ResizeTool(Tool):
    BROWSE_LABEL = "Browse..."
    RESIZE_LABEL = "Resize"

    def __init__(self) -> None:
        super().__init__(name="Resize Image", category="Image")

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

        size_layout = QHBoxLayout()
        size_layout.addWidget(QLabel("Width:", widget))
        self._width = QLineEdit(widget)
        size_layout.addWidget(self._width)
        size_layout.addWidget(QLabel("Height:", widget))
        self._height = QLineEdit(widget)
        size_layout.addWidget(self._height)

        self._do_button = QPushButton(self.RESIZE_LABEL, widget)
        self._do_button.clicked.connect(self._do_resize)

        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)

        layout.addLayout(input_layout)
        layout.addLayout(size_layout)
        layout.addWidget(self._do_button)
        layout.addWidget(self._output)
        widget.setLayout(layout)
        return widget

    def _browse_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(None, "Select image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self._path_edit.setText(path)

    def _do_resize(self) -> None:
        try:
            input_path = self._path_edit.text().strip()
            width = int(self._width.text())
            height = int(self._height.text())
            output_path = input_path.rsplit(".", 1)[0] + f"_resized.{input_path.rsplit('.',1)[1]}"
            resize_image(input_path, output_path, width, height)
            self._output.setPlainText(f"Saved: {output_path}")
        except Exception as exc:
            self._output.setPlainText(f"Error: {exc}")
