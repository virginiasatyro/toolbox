from collections import OrderedDict
from typing import Dict, Iterable, List, Optional

from src.core.tool import Tool


class ToolRegistry:
    """Service that keeps registered tools and exposes them by category."""

    def __init__(self) -> None:
        self._registered_tools: List[Tool] = []

    def register(self, tool: Tool) -> None:
        if tool not in self._registered_tools:
            self._registered_tools.append(tool)

    def get_tools(self) -> List[Tool]:
        return list(self._registered_tools)

    def get_tool_by_name(self, tool_name: str) -> Optional[Tool]:
        for tool in self._registered_tools:
            if tool.name == tool_name:
                return tool
        return None

    def get_categories(self) -> List[str]:
        unique_categories: Dict[str, None] = OrderedDict()
        for tool in self._registered_tools:
            unique_categories.setdefault(tool.category, None)
        return list(unique_categories.keys())

    def get_tools_by_category(self, category_name: str) -> List[Tool]:
        return [tool for tool in self._registered_tools if tool.category == category_name]
