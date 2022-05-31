import discord
import os

from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')  

with open('blacklist.txt', 'a+') as blacklist: #opens up blacklist

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content == ('$carl'):    #testi carl-viesti
            await message.channel.send('CAAAAAAAAARRRRRLLLLL!')

        if message.content.lower in blacklist.read():
            await message.channel.send('Eipä kiroilla, helvetti sentään.')

client.run(TOKEN)