from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QFileDialog, QComboBox
from src.core.tool import Tool
from src.tools.image.image_utils import flip_image


class FlipTool(Tool):
    BROWSE_LABEL = "Browse..."
    FLIP_LABEL = "Flip"

    def __init__(self) -> None:
        super().__init__(name="Flip Image", category="Image")

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

        mode_layout = QHBoxLayout()
        mode_layout.addWidget(QLabel("Mode:", widget))
        self._mode = QComboBox(widget)
        self._mode.addItems(["Horizontal", "Vertical"])
        mode_layout.addWidget(self._mode)

        self._do_button = QPushButton(self.FLIP_LABEL, widget)
        self._do_button.clicked.connect(self._do_flip)

        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)

        layout.addLayout(input_layout)
        layout.addLayout(mode_layout)
        layout.addWidget(self._do_button)
        layout.addWidget(self._output)
        widget.setLayout(layout)
        return widget

    def _browse_file(self) -> None:
        path, _ = QFileDialog.getOpenFileName(None, "Select image", "", "Images (*.png *.jpg *.jpeg *.bmp)")
        if path:
            self._path_edit.setText(path)

    def _do_flip(self) -> None:
        try:
            input_path = self._path_edit.text().strip()
            horizontal = self._mode.currentText() == "Horizontal"
            output_path = input_path.rsplit(".", 1)[0] + f"_flipped.{input_path.rsplit('.',1)[1]}"
            flip_image(input_path, output_path, horizontal=horizontal)
            self._output.setPlainText(f"Saved: {output_path}")
        except Exception as exc:
            self._output.setPlainText(f"Error: {exc}")
