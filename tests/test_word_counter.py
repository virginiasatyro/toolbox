from src.tools.text.word_counter import build_word_count_result


@pytest.mark.parametrize(
    "content, expected",
    [
        ("", (0, 0, 0)),
        ("hello", (1, 5, 1)),
        ("hello world", (2, 11, 1)),
        ("line1\nline2\n", (2, 12, 3)),
    ],
)
def test_word_counter_counts_correctly(content, expected):
    result = build_word_count_result(content)

    assert result.words == expected[0]
    assert result.characters == expected[1]
    assert result.lines == expected[2]
