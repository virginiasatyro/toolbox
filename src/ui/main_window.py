from PySide6.QtGui import QFont
from PySide6.QtWidgets import QHBoxLayout, QLabel, QListWidget, QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from src.core.registry import ToolRegistry
from src.ui.sidebar import SidebarWidget

DEFAULT_FONT_POINT_SIZE = 12

class MainWindow(QMainWindow):
    TOOL_AREA_LABEL = "Tool Area"
    SIDEBAR_STRETCH = 1
    CONTENT_STRETCH = 4

    def __init__(self, registry: ToolRegistry, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.registry = registry
        self._apply_default_font()
        self.setWindowTitle("Toolbox")
        self._sidebar = SidebarWidget(self.registry.get_categories())
        self._sidebar.category_selected.connect(self._handle_category_selection)

        self._content_stack = QStackedWidget()
        self._category_pages: dict[str, QWidget] = {}

        self._build_user_interface()
        if self._sidebar._list.count():
            self._sidebar.set_current_category(self._sidebar._list.item(0).text())

    def _apply_default_font(self) -> None:
        default_font = QFont()
        default_font.setPointSize(DEFAULT_FONT_POINT_SIZE)
        self.setFont(default_font)

    def _build_user_interface(self) -> None:
        self._create_category_pages()

        main_layout = QHBoxLayout()
        main_layout.addWidget(self._sidebar, self.SIDEBAR_STRETCH)
        main_layout.addWidget(self._content_stack, self.CONTENT_STRETCH)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def _create_category_pages(self) -> None:
        for category_name in self.registry.get_categories():
            page = self._build_category_page(category_name)
            self._category_pages[category_name] = page
            self._content_stack.addWidget(page)

    def _build_category_page(self, category_name: str) -> QWidget:
        page_widget = QWidget()
        layout = QVBoxLayout()

        header = QLabel(f"{category_name} \u2014 {self.TOOL_AREA_LABEL}")
        layout.addWidget(header)

        tools_widget = QListWidget()
        for tool in self.registry.get_tools_by_category(category_name):
            tools_widget.addItem(tool.name)

        tools_stack = QStackedWidget()
        for tool in self.registry.get_tools_by_category(category_name):
            tools_stack.addWidget(tool.build_widget())

        tools_widget.currentRowChanged.connect(tools_stack.setCurrentIndex)
        if tools_widget.count() > 0:
            tools_widget.setCurrentRow(0)

        layout.addWidget(tools_widget)
        layout.addWidget(tools_stack)
        page_widget.setLayout(layout)
        return page_widget

    def _handle_category_selection(self, category_name: str) -> None:
        if category_name in self._category_pages:
            self._content_stack.setCurrentWidget(self._category_pages[category_name])
