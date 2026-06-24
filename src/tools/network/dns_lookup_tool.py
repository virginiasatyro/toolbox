from PySide6.QtWidgets import QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QLabel, QHBoxLayout

from src.core.tool import Tool
from src.tools.network.dns_lookup_logic import lookup_dns_records


class DNSLookupTool(Tool):
    LOOKUP_LABEL = "Lookup"

    def __init__(self) -> None:
        super().__init__(name="DNS Lookup", category="Network")

    def build_widget(self, parent: QWidget | None = None) -> QWidget:
        widget = QWidget(parent)
        layout = QVBoxLayout(widget)

        input_layout = QHBoxLayout()
        input_layout.addWidget(QLabel("Domain:", widget))
        self._input = QLineEdit(widget)
        input_layout.addWidget(self._input)
        self._lookup_button = QPushButton(self.LOOKUP_LABEL, widget)
        self._lookup_button.clicked.connect(self._do_lookup)
        input_layout.addWidget(self._lookup_button)

        self._table = QTableWidget(widget)
        self._table.setColumnCount(2)
        self._table.setHorizontalHeaderLabels(["Type", "Record"])

        layout.addLayout(input_layout)
        layout.addWidget(self._table)
        widget.setLayout(layout)
        return widget

    def _do_lookup(self) -> None:
        domain = self._input.text().strip()
        if not domain:
            self._table.setRowCount(0)
            return

        results = lookup_dns_records(domain)
        rows = []
        for rtype, records in results.items():
            for rec in records:
                rows.append((rtype, rec))

        self._table.setRowCount(len(rows))
        for idx, (rtype, rec) in enumerate(rows):
            self._table.setItem(idx, 0, QTableWidgetItem(rtype))
            self._table.setItem(idx, 1, QTableWidgetItem(rec))
