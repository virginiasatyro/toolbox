import sys

from PySide6.QtWidgets import QApplication
from src.core.registry import ToolRegistry
from src.tools.text.base64_tool import Base64Tool
from src.tools.text.lorem_ipsum_tool import LoremIpsumTool
from src.tools.text.word_counter_tool import WordCounterTool
from src.tools.network.domain_ip_tool import DomainToIpTool
from src.tools.network.dns_lookup_tool import DNSLookupTool
from src.tools.image.resize_tool import ResizeTool
from src.tools.image.rotate_tool import RotateTool
from src.tools.image.flip_tool import FlipTool
from src.tools.image.png_to_ico_tool import PngToIcoTool
from src.ui.main_window import MainWindow


def build_registry() -> ToolRegistry:
    registry = ToolRegistry()
    registry.register(WordCounterTool())
    registry.register(LoremIpsumTool())
    registry.register(Base64Tool())
    registry.register(DomainToIpTool())
    registry.register(DNSLookupTool())
    registry.register(ResizeTool())
    registry.register(RotateTool())
    registry.register(FlipTool())
    registry.register(PngToIcoTool())
    return registry


DEFAULT_WINDOW_WIDTH = 1000
DEFAULT_WINDOW_HEIGHT = 700


def main() -> int:
    app = QApplication(sys.argv)
    registry = build_registry()
    window = MainWindow(registry)
    window.resize(DEFAULT_WINDOW_WIDTH, DEFAULT_WINDOW_HEIGHT)
    window.show()
    return app.exec()


if __name__ == "__main__":
    raise SystemExit(main())
