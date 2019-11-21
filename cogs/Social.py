import discord
import os
import urllib
import re
import time
import requests
import json
import random
from discord.ext import commands
from discord.utils import get
from bs4 import BeautifulSoup

class Social(commands.Cogs):
    
    @commands.command()
    async def hug(self, ctx, user: discord.Member = None):
        """Hugs a user, you're hugged if no one is mentioned"""
        if user:
            message = "{0.mention} has hugged {1.mention}".format(ctx.author,user)
        else:
            message = "{self.bot.user.name} has hugged {0.mention}".format(ctx.author)
        await ctx.send(message)

    @commands.command()
    async def kiss(self, ctx, user: discord.Member = None):
        """Kisses a user, you're kissed if no one is mentioned"""
        if user:
            message = "{0.mention} has kissed {1.mention}".format(ctx.author,user)
        else:
            message = "{self.bot.user.name} has kissed {0.mention}".format(ctx.author)
        await ctx.send(message)

    @commands.command()
    async def slap(self, ctx, user: discord.Member = None):
        """Slaps a user, slaps you instead if you don't mention anyone"""
        if user:
            message = "{0.mention} has hugged {1.mention}".format(ctx.author,user)
        else:
            message = "{self.bot.user.name} has slapped {0.mention}".format(ctx.author)
        await ctx.send(message)

    @commands.command()
    async def cuddle(self, ctx, user: discord.Member = None):
        """Cuddle someone, cuddles you instead if you don't mention anyone"""
        if user:
            message = "{0.mention} has hugged {1.mention}".format(ctx.author,user)
        else:
            message = "{self.bot.user.name} has slapped {0.mention}".format(ctx.author)
        await ctx.send(message)

def setup(bot):
    bot.add_cog(Social(bot))
    def __init__(self, bot):
        self.bot = bot