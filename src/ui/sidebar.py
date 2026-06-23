from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QListWidget, QVBoxLayout, QWidget


class SidebarWidget(QWidget):
    category_selected = Signal(str)

    def __init__(self, categories: list[str], parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self._list = QListWidget()
        self._list.addItems(categories)
        self._list.currentTextChanged.connect(self.category_selected.emit)

        layout = QVBoxLayout()
        layout.addWidget(self._list)
        self.setLayout(layout)

    def set_current_category(self, category_name: str) -> None:
        items = self._list.findItems(category_name, Qt.MatchExactly)
        if items:
            self._list.setCurrentItem(items[0])
