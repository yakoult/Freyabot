import discord
import random
import sys
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageFilter
from io import BytesIO
from discord.ext import commands

class Basics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None
        self.count = 0
        self.set_channel = 634939948222382082

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = self.bot.get_channel(self.set_channel)
        if channel is not None:
            text = f'Welcome! You are our #{ctx.guild.member_count} member!'
            img = Image.open(r'./banner/spicewolf.png')
            draw = ImageDraw.Draw(img)
            font = ImageFont.truetype(r'./fonts/Xlines.ttf', 30)
            draw.text((330, 250), text, (65,60,80), font=font)
            avatar = "https://cdn.discordapp.com/avatars/{0.id}/{0.avatar}.png".format(member)
            response = requests.get(avatar)
            avatar = Image.open(BytesIO(response.content))
            mask = Image.open(r'./banner/mask.png').convert('L')
            img.paste(avatar, (520, 80), mask)
            img.save('./banner/banner.png')
            file = discord.File('./banner/banner.png', filename='banner.png')
            embed = discord.Embed()
            embed.set_image(url="attachment://banner.png")
            await ctx.send(file=file, embed=embed)

    @commands.command()
    async def hello(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        if self._last_member is None or self._last_member.id != member.id:
            self.count = 0
            await ctx.send('Hello {0.name}~'.format(member))
        elif self._last_member.id == member.id and self.count == 0:
            self.count += 1
            await ctx.send('Hello {0.name}... This feels familiar.'.format(member))
        elif self._last_memder.id == member.id and self.count == 1:
            await ctx.send('Time to stop {0.name}...'.format(member))
        else:
            await ctx.sent('Hmph')
        self._last_member = member

    @commands.command()
    async def watch(self, ctx, *, message: str):
        """Changes bot watch status, only usable by freya or creator"""
        owner = self.bot.get_user(170096122692501505)
        freya = self.bot.get_user(561053934589050880)
        if ctx.author == freya or ctx.author == owner:
            activity = discord.Activity(name=message, type=discord.ActivityType.watching)
            emoji = '<a:kyokoThumb:636713935822651433>'
            mess = ctx.message
            await mess.add_reaction(emoji)
            await self.bot.change_presence(activity=activity)

    @commands.command()
    async def game(self, ctx, *, message: str):
        """Changes bot gaming status, only usable by freya or creator"""
        owner = self.bot.get_user(170096122692501505)
        freya = self.bot.get_user(561053934589050880)
        if ctx.author == freya or ctx.author == owner:
            emoji = '<a:kyokoThumb:636713935822651433>'
            mess = ctx.message
            await mess.add_reaction(emoji)
            await self.bot.change_presence(activity=discord.Game(name=message))

    @commands.command()
    async def talk(self, ctx):
        """make me talk"""
        bot_quotes = [
            "2AM ISN'T MORNING",
            '32Cs are best',
            f'Small boobs are in now, get with the times {ctx.message.author.mention}',
            'Yona is MINE back off!',
            'I love you all',
            'Ketchup is a blessing from the gods',
            '***Readies British accent*** Hitara',
            'Send me wholesome yuri please!',
            '***Cries***',
            "Pants r dumb, I shouldn't have to wear them inside my own house",
            "Help I catn tpye",
            'I never cry what do you mean?',
            "I want Gintoki's babies"
        ]
        response = random.choice(bot_quotes)
        await ctx.send(response)

    @commands.command()
    async def flirt(self, ctx):
        """Best way to pick up someone whos caught your interest"""
        bot_quotes = [
            'Are you a cake? Cuz I want a piece of that',
            "Are your legs tired? Cuz you've been running in my mind all day",
            "I don't need to see the future to be able to see our future together",
            "Tie your shoes dead, I don't want you falling for anyone else",
            "I know you're busy today but can you add me to your to-do list?",
            "My phone has a huge problem. It doesn't have your humber in it",
            "If nothing lasts forever, will you be my nothing?",
            "we're not socks but we'd still make a great pair",
            "I'm definitely no photographer but I can still picture us together",
            "I may not be an organ donor, but i'd willingly give you my heart",
            "Is your name Google? Because you've got everything I'm searching for",
            "You hands look heavy. Here, let me hold them for you",
            "Do you like sales? Because if you're looking for a good one, clothing is 100% off at my place",
            "If you were a triangle you'd be acute one",
            "Are you a camera? Because every time I see you, I smile",
            "Do you have a name, or can I call you mine?",
            "Are you craving Pizza? Because I’d love to get a pizz-a you",
            "Wouldn't we look cute on a wedding cake together",
            "I may not be a genie, but I can make all your wishes come true!",
            "I’m not drunk, I’m just intoxicated by you",
            "If I had a garden I’d put your tulips and my tulips together",
            "I thought Happiness starts with H. But why does mine starts with U"
        ]
        response = random.choice(bot_quotes)
        await ctx.send(response)

    @commands.command()
    async def dm(self, ctx, user: discord.Member = None, *, message: str):
        """dms you something"""
        owner = self.bot.get_user(170096122692501505)
        freya = self.bot.get_user(561053934589050880)
        if ctx.author == freya or ctx.author == owner:
            if user:
                await user.create_dm()
                await user.dm_channel.send(message)
            else:
                await ctx.send('Tag someone to dm please')

    @commands.command()
    async def echo(self, ctx, channel: discord.TextChannel, *, message: str):
        """Ill say whatever you want, wherever you want"""
        await channel.send(message)

    @commands.command()
    async def avatar(self, ctx, member: discord.Member):
        """retrieve user avatar"""
        e_title = "{0}'s Avatar".format(member)
        avatar = member.avatar_url
        em = discord.Embed(title=e_title)
        em.set_image(url=avatar)
        await ctx.send(embed=em)

    @commands.command()
    async def set_welcome(self, ctx, channel: discord.TextChannel):
        """set welcome image channel"""
        channelid = channel.id
        self.set_channel = channelid
        text = 'Welcome channel has been set for {0.mention}'.format(channel)
        await ctx.send(text)

def setup(bot):
    bot.add_cog(Basics(bot))