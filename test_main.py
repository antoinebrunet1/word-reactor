from main import is_word_valid, word_to_letters_emojis_array


def test_is_word_valid_happy_path():
    assert is_word_valid("hi")

def test_is_word_valid_repeating_letters():
    assert not is_word_valid("hhi")

def test_is_word_valid_non_alpha_letters():
    assert not is_word_valid("hi2")

def test_word_to_letters_emojis_array_happy_path():
    actual_array = word_to_letters_emojis_array("HI")
    assert ' '.join(actual_array) == "🇭 🇮"