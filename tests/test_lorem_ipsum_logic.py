from src.tools.text.lorem_ipsum_logic import generate_lorem_ipsum


def test_generate_lorem_ipsum_single_paragraph():
    generated = generate_lorem_ipsum(1, seed=1)
    assert generated.count("\n\n") == 0
    assert generated.startswith("Lorem ipsum dolor sit amet")


def test_generate_lorem_ipsum_multiple_paragraphs():
    generated = generate_lorem_ipsum(3, seed=1)
    assert generated.count("\n\n") == 2
    assert len(set(generated.split("\n\n"))) == 3


def test_generate_lorem_ipsum_zero_returns_empty():
    assert generate_lorem_ipsum(0) == ""


def test_generate_lorem_ipsum_seed_is_deterministic():
    assert generate_lorem_ipsum(2, seed=42) == generate_lorem_ipsum(
        2, seed=42
    )


def test_generate_lorem_ipsum_changes_with_different_seeds():
    assert generate_lorem_ipsum(2, seed=1) != generate_lorem_ipsum(2, seed=2)
