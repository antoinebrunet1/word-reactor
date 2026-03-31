import discord
from dotenv import load_dotenv
import os

load_dotenv()

token=os.getenv("TOKEN")


def is_message_reply(message):
    """
    Returns true only if the given message is replying to another message.
    :param message: The message.
    :return: true only if the given message is replying to another message.
    """
    return message.reference and message.reference.message_id


class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if not is_message_reply(message):
            return
        
        replied = await message.channel.fetch_message(message.reference.message_id)
        print(replied.content)


intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(token)