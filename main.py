import discord
from dotenv import load_dotenv
import os
from discord.ext import commands
from discord import app_commands

load_dotenv()

token=os.getenv("TOKEN")
server_id = os.getenv("SERVER_ID")

def is_message_reply(message):
    """
    Returns true only if the given message is replying to another message.
    :param message: The message.
    :return: true only if the given message is replying to another message.
    """
    return message.reference and message.reference.message_id


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

@client.tree.command(name="react", description="Make the bot react to a message with a word formed with letters emojis.", guild=GUILD_ID)
async def react(interaction: discord.Interaction, message_id: str, word: str):
    await interaction.response.send_message(f'{message_id} : {word}')

client.run(token)