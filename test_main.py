from main import is_word_valid

def test_is_word_valid_happy_path():
    assert is_word_valid("hi")

def test_is_word_valid_repeating_letters():
    assert not is_word_valid("hhi")