from typing import NamedTuple


class WordCountResult(NamedTuple):
    words: int
    characters: int
    lines: int


def count_words(text: str) -> int:
    return len([token for token in text.split() if token])


def count_characters(text: str) -> int:
    return len(text)


def count_lines(text: str) -> int:
    if not text:
        return 0
    return text.count("\n") + 1


def build_word_count_result(text: str) -> WordCountResult:
    return WordCountResult(
        words=count_words(text),
        characters=count_characters(text),
        lines=count_lines(text),
    )
