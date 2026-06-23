from abc import ABC, abstractmethod
from typing import Optional
from PySide6.QtWidgets import QWidget


class Tool(ABC):
    """Base class for application tools."""

    name: str
    category: str

    def __init__(self, name: str, category: str) -> None:
        self.name = name
        self.category = category

    @abstractmethod
    def build_widget(self, parent: Optional[QWidget] = None) -> QWidget:
        """Build and return the tool-specific widget."""
        raise NotImplementedError
