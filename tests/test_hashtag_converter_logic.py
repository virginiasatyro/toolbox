from src.tools.text.hashtag_converter_logic import convert_text_to_hashtags


def test_convert_text_to_hashtags_single_word():
    result = convert_text_to_hashtags("hello")
    assert result == "#hello"


def test_convert_text_to_hashtags_multiple_words():
    result = convert_text_to_hashtags("hello world")
    assert result == "#hello #world"


def test_convert_text_to_hashtags_empty_string():
    result = convert_text_to_hashtags("")
    assert result == ""


def test_convert_text_to_hashtags_whitespace_only():
    result = convert_text_to_hashtags("   ")
    assert result == ""


def test_convert_text_to_hashtags_multiple_spaces():
    result = convert_text_to_hashtags("hello  world  python")
    assert result == "#hello #world #python"


def test_convert_text_to_hashtags_with_punctuation():
    result = convert_text_to_hashtags("hello, world!")
    assert result == "#hello #world"


def test_convert_text_to_hashtags_with_special_chars():
    result = convert_text_to_hashtags("hello@world #test $python")
    assert result == "#helloworld #test #python"


def test_convert_text_to_hashtags_only_punctuation():
    result = convert_text_to_hashtags("!!! ???")
    assert result == ""


def test_convert_text_to_hashtags_mixed():
    result = convert_text_to_hashtags("Hello, World! Python3.9 rocks!")
    assert result == "#Hello #World #Python39 #rocks"
