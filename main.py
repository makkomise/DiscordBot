import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$carl'):
        await message.channel.send('CAAAAAAAAARRRRRLLLLL!')

client.run(TOKEN)