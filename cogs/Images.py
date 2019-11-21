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

class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.imgur_base_url = "https://api.imgur.com/3/image/"
        self.client_id = '04a4fe685658760'

    @commands.command()
    async def kitty(self, ctx, user: discord.Member = None ):
        """sends a random cat image, tag someone to send them a cat"""
        html_page = urllib.request.urlopen("https://imgur.com/r/cats")
        soup = BeautifulSoup(html_page, "html.parser")
        images = []
        for img in soup.findAll('a'):
            if 'r/cat' not in img.get('href'):
                pass
            else:
                images.append(img.get('href'))
        author = ctx.author
        link = random.choice(images)
        imghash = link[8:15]
        response = requests.get(self.imgur_base_url+imghash,headers={'Authorization':'Client-ID '+self.client_id})
        content = response.content
        imgcontent = json.loads(content)
        if imgcontent['data']['type'] != 'video/mp4':
            text = imgcontent['data']['link']
            if user:
                embed=discord.Embed(title=f'{author.name} has sent you a cat {user.name}!', color=0xffb9b9)
                embed.set_image(url=text)
                await user.create_dm()
                await user.dm_channel.send(embed=embed)
            else:
                embed=discord.Embed(title=f'Have a cat {author.name}', color=0xffb9b9)
                embed.set_image(url=text)
                await ctx.send(embed=embed)
        else:
            text = imgcontent['data']['gifv']
            if user:
                await user.create_dm()
                await user.dm_channel.send(text)
            else:
                await ctx.send(text)

    @commands.command()
    async def bunny(self, ctx, user: discord.Member = None ):
        """sends a random rabbit image, tag someone to send them a rabbit"""
        html_page = urllib.request.urlopen("https://imgur.com/r/Rabbits")
        soup = BeautifulSoup(html_page, "html.parser")
        images = []
        for img in soup.findAll('a'):
            if 'r/Rabbits' not in img.get('href'):
                pass
            else:
                images.append(img.get('href'))
        author = ctx.author
        link = random.choice(images)
        imghash = link[11:18]
        response = requests.get(self.imgur_base_url+imghash,headers={'Authorization':'Client-ID '+self.client_id})
        content = response.content
        imgcontent = json.loads(content)
        if imgcontent['data']['type'] != 'video/mp4':
            text = imgcontent['data']['link']
            if user:
                embed=discord.Embed(title=f'{author.name} has sent you a Rabbit {user.name}!', color=0xffb9b9)
                embed.set_image(url=text)
                await user.create_dm()
                await user.dm_channel.send(embed=embed)
            else:
                embed=discord.Embed(title=f'Have a Rabbit {author.name}', color=0xffb9b9)
                embed.set_image(url=text)
                await ctx.send(embed=embed)
        else:
            text = imgcontent['data']['gifv']
            if user:
                await user.create_dm()
                await user.dm_channel.send(text)
            else:
                await ctx.send(text)

    @commands.command()
    async def puppy(self, ctx, user: discord.Member = None ):
        """sends a random puppy image, tag someone to send them a puppy"""
        html_page = urllib.request.urlopen("https://imgur.com/r/puppies")
        soup = BeautifulSoup(html_page, "html.parser")
        images = []
        for img in soup.findAll('a'):
            if 'r/puppies' not in img.get('href'):
                pass
            else:
                images.append(img.get('href'))
        author = ctx.author
        link = random.choice(images)
        imghash = link[11:18]
        response = requests.get(self.imgur_base_url+imghash,headers={'Authorization':'Client-ID '+self.client_id})
        content = response.content
        imgcontent = json.loads(content)
        if imgcontent['data']['type'] != 'video/mp4':
            text = imgcontent['data']['link']
            if user:
                embed=discord.Embed(title=f'{author.name} has sent you a Puppy {user.name}!', color=0xffb9b9)
                embed.set_image(url=text)
                await user.create_dm()
                await user.dm_channel.send(embed=embed)
            else:
                embed=discord.Embed(title=f'Have a Puppy {author.name}', color=0xffb9b9)
                embed.set_image(url=text)
                await ctx.send(embed=embed)
        else:
            text = imgcontent['data']['gifv']
            if user:
                await user.create_dm()
                await user.dm_channel.send(text)
            else:
                await ctx.send(text)

    @commands.command()
    async def gintama(self, ctx, user: discord.Member = None ):
        """Gintama for you"""
        html_page = urllib.request.urlopen("https://imgur.com/r/Gintama")
        soup = BeautifulSoup(html_page, "html.parser")
        images = []
        for img in soup.findAll('a'):
            if 'r/Gintama' not in img.get('href'):
                pass
            else:
                images.append(img.get('href'))
        author = ctx.author
        link = random.choice(images)
        imghash = link[11:18]
        response = requests.get(self.imgur_base_url+imghash,headers={'Authorization':'Client-ID '+self.client_id})
        content = response.content
        imgcontent = json.loads(content)
        if imgcontent['data']['type'] != 'video/mp4':
            text = imgcontent['data']['link']
            if user:
                embed=discord.Embed(title=f'Gintama pic for you you damn weeb!', color=0x00B9FF)
                embed.set_image(url=text)
                await user.create_dm()
                await user.dm_channel.send(embed=embed)
            else:
                embed=discord.Embed(title=f'Gintama pic for you you damn weeb! {author.name}', color=0x00B9FF)
                embed.set_image(url=text)
                await ctx.send(embed=embed)
        else:
            text = imgcontent['data']['gifv']
            if user:
                await user.create_dm()
                await user.dm_channel.send(text)
            else:
                await ctx.send(text)

    @commands.command()
    async def birb(self, ctx, user: discord.Member = None ):
        """sends a random bird image, tag someone to send them a birb"""
        html_page = urllib.request.urlopen("https://imgur.com/r/birb")
        soup = BeautifulSoup(html_page, "html.parser")
        images = []
        for img in soup.findAll('a'):
            if 'r/birb' not in img.get('href'):
                pass
            else:
                images.append(img.get('href'))
        author = ctx.author
        link = random.choice(images)
        imghash = link[8:15]
        response = requests.get(self.imgur_base_url+imghash,headers={'Authorization':'Client-ID '+self.client_id})
        content = response.content
        imgcontent = json.loads(content)
        if imgcontent['data']['type'] != 'video/mp4':
            text = imgcontent['data']['link']
            if user:
                embed=discord.Embed(title=f'{author.name} has sent you a birb {user.name}!', color=0xffb9b9)
                embed.set_image(url=text)
                await user.create_dm()
                await user.dm_channel.send(embed=embed)
            else:
                embed=discord.Embed(title=f'Have a birb {author.name}', color=0xffb9b9)
                embed.set_image(url=text)
                await ctx.send(embed=embed)
        else:
            text = imgcontent['data']['gifv']
            if user:
                await user.create_dm()
                await user.dm_channel.send(text)
            else:
                await ctx.send(text)

    @commands.command()
    async def yona(self, ctx, user: discord.Member = None):
        """Random yona hopefully"""
        url = f'https://api.imgur.com/3/gallery/search/time/all/0?q=yona'
        response = requests.get(url, headers={'Authorization':'Client-ID '+self.client_id})
        content = response.content
        data = json.loads(content)
        if data["success"]:
            results = data["data"]
            random.shuffle(results)
            if results[0]:
                if "gifv" in results[0]:
                    await ctx.send(results[0]["gifv"])
                else:
                    await ctx.send(results[0]["link"])

    @commands.group(name="imgur")
    async def _imgur(self, ctx):
        """Retrieves Pictures from Imgur."""
        pass

    @_imgur.command(name="search")
    async def imgur_search(self, ctx, *, term:str):
        """Search Imgur for a specific term, returns 3 results"""
        url = f'https://api.imgur.com/3/gallery/search/time/all/0?q='+term
        response = requests.get(url, headers={'Authorization':'Client-ID '+self.client_id})
        content = response.content
        data = json.loads(content)
        if data["success"]:
            results = data["data"]
            if not results:
                await ctx.send(_("No results for "+term+'.'))
                return
            random.shuffle(results)
            for r in results[:1]:
                if "gifv" in r:
                    await ctx.send(r["gifv"])
                else:
                    await ctx.send(r["link"])
        else: 
            await ctx.send(
                _("Something went wrong. Error code is {code}.").format(code=data["status"])
                )

def setup(bot):
    bot.add_cog(Images(bot))