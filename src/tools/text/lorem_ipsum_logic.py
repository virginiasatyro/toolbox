from __future__ import annotations

LOREM_IPSUM_SAMPLE = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
    "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. "
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
)


def generate_lorem_ipsum(paragraphs: int) -> str:
    if paragraphs < 1:
        return ""
    return "\n\n".join(LOREM_IPSUM_SAMPLE for _ in range(paragraphs))
