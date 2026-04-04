from unittest.mock import AsyncMock

import pytest

from main import is_word_valid, word_to_letters_emojis_array, letter_to_letter_emoji, react


def test_is_word_valid_happy_path():
    assert is_word_valid("hi")

def test_is_word_valid_repeating_letters():
    assert not is_word_valid("hhi")

def test_is_word_valid_non_alpha_letters():
    assert not is_word_valid("hi2")

def test_word_to_letters_emojis_array_happy_path():
    actual_array = word_to_letters_emojis_array("HI")
    assert ' '.join(actual_array) == "🇭 🇮"

def test_letter_to_letter_emoji_happy_path():
    assert letter_to_letter_emoji("H") == "🇭"

@pytest.mark.asyncio
async def test_react_invalid_word(mocker):
    mock_interaction = AsyncMock()
    message_id = "0"
    word = "hhi"
    mock_is_word_valid = mocker.patch("main.is_word_valid")
    mock_is_word_valid.return_value = False

    await react.callback(mock_interaction, message_id, word)

    expected_error_message = "Error: The letters should be in the union of A-Z and a-z and no letters should repeat."

    mock_interaction.response.send_message.assert_awaited_once_with(expected_error_message)


@pytest.mark.asyncio
async def test_react_happy_path(mocker):
    mock_interaction = AsyncMock()
    mocker.patch("main.is_word_valid").return_value = True
    mock_message_to_react_to = AsyncMock()
    mock_interaction.channel.fetch_message.return_value = mock_message_to_react_to
    mocker.patch("main.word_to_letters_emojis_array").return_value = ["🇭"]

    await react.callback(mock_interaction, "0", "h")

    mock_message_to_react_to.add_reaction.assert_awaited_once_with("🇭")
    mock_interaction.response.send_message.assert_awaited_once_with("Successfully reacted.")
