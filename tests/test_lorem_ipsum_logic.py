from src.tools.text.lorem_ipsum_logic import generate_lorem_ipsum


def test_generate_lorem_ipsum_single_paragraph():
    generated = generate_lorem_ipsum(1)
    assert generated.count("\n\n") == 0


def test_generate_lorem_ipsum_multiple_paragraphs():
    generated = generate_lorem_ipsum(3)
    assert generated.count("\n\n") == 2


def test_generate_lorem_ipsum_zero_returns_empty():
    assert generate_lorem_ipsum(0) == ""
