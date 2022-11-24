import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('TOKEN')
bot = commands.Bot(command_prefix='!', help_command=None)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')  


#tuhmien sanojen filtteri



@bot.event 
async def on_message(message):

    if message.author == bot.user:
        return

    with open ('blacklist.txt', 'r') as file:  #jos joku kirjoittaa sanan mikä filtterissä, botti reagoi
        blacklist = file.read().split("\n")
        
    for word in blacklist:  #jos tuhma sana löytyy filtteristä niin botti poistaa sen ja lähettää viestin 
        if word in message.content.lower():
            await message.delete()  
            await message.channel.send(f' {message.author.mention} your message was removed due to channel rules' )    
      
    file.close()
    await bot.process_commands(message)


@bot.command(name='help')   #botin helppikomento, miten lisätä sanoja kirosanafiltteriin
async def help(ctx):   
    await ctx.send('`!add xxxxxx to add words to blacklist`')


#BOTIN KOMENNOT 

@bot.command(name='carl')   #hassunhauska testikomento, pyydettiin laittamaan
async def carl(message):   
    await message.send('CAAAAAAAAAARRRLLLLLLLLLLLLLL')

@bot.command(name='add')    #sanojen lisääminen kirosanafiltteriin
async def add(message, arg):
    if message.message.author.guild_permissions.administrator:
        word = arg
        file = open('blacklist.txt', 'a+')
        file.write("\n" + word)
        file.close()
        await message.send('Word '+ word +' has been added to blacklist.')

    else:
        await message.send('You shall not pass')


    

bot.run(TOKEN)