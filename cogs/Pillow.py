import discord
import requests
import sys
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageFilter
from io import BytesIO


class Pillow(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def bannertest(self, ctx, member: discord.Member = None):
        """Test for banner"""
        if member != None:
            text = f'Welcome {member.name}'
            img = Image.open(r'./banner/spicewolf.png')
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(r'./fonts/Xlines.ttf', 30)
            if len(member.name) <= 10:
                draw.text((290, 150), text, (65,60,80), font=font)
            else:
                draw.text((320, 130), 'Welcome', (65,60,80), font=font)
                draw.text((280, 170), member.name, (65,60,80), font=font)
            avatar = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png".format(member)
            response = requests.get(avatar)
            avatar = Image.open(BytesIO(response.content))
            mask = Image.open(r'./banner/mask.png').convert('L')
            img.paste(avatar, (300, 0), mask)
            img.save('./banner/banner.png')
            file = discord.File('./banner/banner.png', filename='banner.png')
            embed = discord.Embed()
            embed.set_image(url="attachment://banner.png")
            await ctx.send(file=file, embed=embed)
        else:
            await ctx.send('Error, pass a user')

    @commands.command()
    async def ac(self, ctx, member: discord.Member = None):
        """Test for banner avatar"""
        if member != None:
            avatar = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png".format(member)
            response = requests.get(avatar)
            img = Image.open(BytesIO(response.content))
            mask = Image.open(r'./banner/mask.png').convert('L')
            output = ImageOps.fit(img, mask.size, centering=(0.5, 0.5))
            output.putalpha(mask)
            output.save('./banner/avatartest.png')
            file = discord.File('./banner/avatartest.png')
            await ctx.send(file=file)

def setup(bot):
    bot.add_cog(Pillow(bot))
