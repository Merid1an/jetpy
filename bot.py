import discord
import random as r
import sqlite3
from discord.ext import commands
from discord.ext.commands import Bot

conn = sqlite3.connect("DiscordBot.db") 
cursor = conn.cursor() 

cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                id TEXT,
                nickname TEXT,
                mention TEXT)""")

Bot = commands.Bot(command_prefix= "!" )

@Bot.event
async def on_ready():
    print("JetBot за работой.")

    type = discord.ActivityType.watching
    activity = discord.Activity(name = "за нарушителями", type = type)
    status = discord.Status.dnd
    await Bot.change_presence(activity = activity, status = status)

@Bot.event
async def on_member_join ( member ):

    role = discord.utils.get(member.guild.roles, id = 515898519434035226 )

    await member.add_roles( role )

@Bot.event
async def on_message( message ):

    await Bot.process_commands(message)

    if 'discord.gg' in message.content.lower():
        await message.delete()
        await message.channel.send(embed = discord.Embed(description = f'{message.author}, реклама запрещена.',color=0x0c0c0c)) 
        return

@Bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound ):
        await ctx.send(embed = discord.Embed(description = f'**:exclamation: {ctx.author.name}, Данной команды не существует.**', color=0x0c0c0c)) 


token = os.environ.get("BOT_TOKEN")

Bot.run(str(token))