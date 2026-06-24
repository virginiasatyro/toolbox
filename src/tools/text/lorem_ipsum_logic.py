from __future__ import annotations

import random

LOREM_START = "Lorem ipsum dolor sit amet"

LOREM_WORDS = (
    "adipiscing",
    "aliqua",
    "aliquip",
    "amet",
    "anim",
    "aute",
    "cillum",
    "commodo",
    "consectetur",
    "consequat",
    "culpa",
    "cupidatat",
    "deserunt",
    "do",
    "dolor",
    "dolore",
    "eiusmod",
    "elit",
    "enim",
    "esse",
    "est",
    "ex",
    "excepteur",
    "exercitation",
    "fugiat",
    "id",
    "in",
    "incididunt",
    "ipsum",
    "irure",
    "labore",
    "laboris",
    "laborum",
    "lorem",
    "magna",
    "minim",
    "mollit",
    "nisi",
    "non",
    "nostrud",
    "nulla",
    "occaecat",
    "officia",
    "pariatur",
    "proident",
    "qui",
    "quis",
    "reprehenderit",
    "sed",
    "sint",
    "sit",
    "sunt",
    "tempor",
    "ullamco",
    "ut",
    "velit",
    "veniam",
    "voluptate",
)

PUNCTUATION = (".", ".", ".", ";", ",")


def generate_lorem_ipsum(paragraphs: int, seed: int | None = None) -> str:
    if paragraphs < 1:
        return ""

    rng = random.Random(seed)
    return "\n\n".join(_generate_paragraph(rng, index) for index in range(paragraphs))


def _generate_paragraph(rng: random.Random, paragraph_index: int) -> str:
    sentence_count = rng.randint(4, 7)
    sentences = [
        _generate_sentence(
            rng,
            rng.randint(8, 16),
            starts_with_lorem=paragraph_index == 0,
        )
    ]

    for _ in range(sentence_count - 1):
        sentences.append(_generate_sentence(rng, rng.randint(7, 18)))

    return " ".join(sentences)


def _generate_sentence(
    rng: random.Random, word_count: int, starts_with_lorem: bool = False
) -> str:
    if starts_with_lorem:
        words = LOREM_START.split()
        word_count = max(word_count, len(words) + 1)
    else:
        words = [rng.choice(LOREM_WORDS)]

    while len(words) < word_count:
        next_word = rng.choice(LOREM_WORDS)
        if len(words) > 1 and words[-1] == next_word == words[-2]:
            continue
        words.append(next_word)

    words[0] = words[0].capitalize()
    return f"{' '.join(words)}{rng.choice(PUNCTUATION)}"
