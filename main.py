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

    if message.content.startswith('$kebab'):
        await message.channel.send('Oispa kebab...')

    if message.content.startswith('$kisso'):
        await message.channel.send('https://tenor.com/view/i-want-food-gif-22483506')

client.run(TOKEN)