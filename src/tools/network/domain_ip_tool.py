from PySide6.QtWidgets import QPushButton, QLineEdit, QPlainTextEdit, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from src.core.tool import Tool
from src.tools.network.domain_ip_logic import lookup_site_ip_info


class DomainToIpTool(Tool):
    RESOLVE_LABEL = "Resolve"

    def __init__(self) -> None:
        super().__init__(name="Domain → IP", category="Network")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Site URL:", widget))
        self._input = QLineEdit(widget)
        input_layout.addWidget(self._input)
        self._resolve_button = QPushButton(self.RESOLVE_LABEL, widget)
        self._resolve_button.clicked.connect(self._do_resolve)
        input_layout.addWidget(self._resolve_button)

        self._output = QPlainTextEdit(widget)
        self._output.setReadOnly(True)

        layout.addLayout(input_layout)
        layout.addWidget(self._output)
        widget.setLayout(layout)
        return widget

    def _do_resolve(self) -> None:
        site_url = self._input.text().strip()
        if not site_url:
            self._output.setPlainText("Please enter a site URL")
            return

        try:
            result = lookup_site_ip_info(site_url)
            self._output.setPlainText(result.to_display_text())
        except Exception as exc:
            self._output.setPlainText(f"Error: {exc}")
