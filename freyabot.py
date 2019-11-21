# bot.py
import os
import discord
import urllib
import re
import time
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import datetime
from discord.ext import commands
from discord.utils import get

custom_prefixes = {}
#You'd need to have some sort of persistance here,
#possibly using the json module to save and load
#or a database
default_prefixes = ['f!']

async def determine_prefix(bot, message):
    guild = message.guild
    #Only allow custom prefixs in guild
    if guild:
        return custom_prefixes.get(guild.id, default_prefixes)
    else:
        return default_prefixes

#bot setup
token = 'NjM2NzkxMzc2Nzg4MzI0MzUz.XdYVeg.x-IRmiyHjCq3v5WNcszuHeZTy4w'
bot = commands.Bot(command_prefix=determine_prefix)
admin = 170096122692501505
freyaid = 561053934589050880

#birthday
now = datetime.datetime.now()

#commands
@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    """loads a cog"""
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been loaded')
@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    """unloads a cog"""
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been unloaded')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    """reloads a cog"""
    bot.unload_extension(f'cogs.{extension}')
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'{extension} has been reloaded')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

#events
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    activity = discord.Activity(name='Wholesome Yuri', type=discord.ActivityType.watching)
    await bot.change_presence(activity=activity)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the correct role for this command.')

@bot.event
async def on_message(message):
    year = now.year
    if now == datetime.datetime(year, 11, 12):
        text = 'Happy birthday Chloe you brat!'
        await message.channel.send(text)
    if 'Chloe is cute' in message.content:
        text = 'No u'
        await message.channel.send(text)
    await bot.process_commands(message)

bot.run(token)