import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
from collections import Counter

load_dotenv()

token = os.getenv("TOKEN")
server_id = os.getenv("SERVER_ID")


class Client(commands.Bot):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

        try:
            guild = discord.Object(id=server_id)
            synced = await self.tree.sync(guild=guild)
            print(f'Synced {len(synced)} commands to guild {guild.id}')

        except Exception as e:
            print(f'Error syncing commands: {e}')


intents = discord.Intents.default()
intents.message_content = True
client = Client(command_prefix="!", intents=intents)
GUILD_ID = discord.Object(id=server_id)


@client.tree.command(name="react",
                     description="Make the bot react to a message with a word formed with letters emojis.",
                     guild=GUILD_ID)
async def react(interaction: discord.Interaction, message_id: str, word: str):
    """
    Makes the bot react to a message with a word formed with letters emojis.
    :param interaction: The Discord Interaction.
    :param message_id: The ID of the message the bot has to react to.
    :param word: The word the bot has to react with using letters emojis. The letters should be in the union of A-Z and a-z and no letters should repeat.
    :return: Does not return anything.
    """
    if not is_word_valid(word):
        await interaction.response.send_message(
            "Error: The letters should be in the union of A-Z and a-z and no letters should repeat.")
        return

    message_to_react_to = await interaction.channel.fetch_message(message_id)

    word = word.upper()

    emojis_to_react_with = word_to_letters_emojis_array(word)

    for emoji in emojis_to_react_with:
        await message_to_react_to.add_reaction(emoji)

    await interaction.response.send_message("Successfully reacted.")


def is_word_valid(word):
    """
    Returns true only if the word is valid i.e. has letters in the union of A-Z and a-z and has no repeated letters.
    :param word: The word to check.
    :return: true only if the word is valid i.e. has letters in the union of A-Z and a-z and has no repeated letters.
    """
    return word.isalpha() and len(Counter(word)) == len(word)


def word_to_letters_emojis_array(word):
    """
    Returns an array of the emoji equivalents of each letter in a given uppercase word. The emoji for A is 0x1F1E6.
    :param word: The given word.
    :return: The resulting array.
    """
    return [letter_to_letter_emoji(letter) for letter in word]


def letter_to_letter_emoji(letter):
    """
    Returns the emoji equivalent of a given uppercase letter. The emoji for A is 0x1F1E6.
    :param letter: The letter to convert.
    :return: The emoji equivalent of the given uppercase letter.
    """
    base = ord('A')
    offset = ord(letter) - base

    # 0x1F1E6 is the Unicode of the emoji letter for the letter A.
    return chr(0x1F1E6 + offset)


client.run(token)
