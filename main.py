import discord
from dotenv import load_dotenv
import os

load_dotenv()

token=os.getenv("TOKEN")

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        # If the message is a reply
        if message.reference and message.reference.message_id:
            replied = await message.channel.fetch_message(message.reference.message_id)
            print(replied.content)

intents = discord.Intents.default()
intents.message_content = True

client = Client(intents=intents)
client.run(token)