import discord
from dotenv import load_dotenv
import os
from discord.ext import commands

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
                     description="Make the bot react to a message with a word formed with letters emojis. The word should not have any repeated letters.",
                     guild=GUILD_ID)
async def react(interaction: discord.Interaction, message_id: str, word: str):
    """
    Makes the bot react to a message with a word formed with letters emojis.
    :param interaction: The Discord Interaction.
    :param message_id: The ID of the message the bot has to react to.
    :param word: The word the bot has to react with using letters emojis. The case does not matter and no letters should repeat.
    :return: Does not return anything.
    """
    await interaction.response.send_message(f'{message_id} : {word}')


client.run(token)
