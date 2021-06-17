from discord.ext import commands
import discord
import random
import aiohttp
from functools import partial

def setup(bot):
    bot.add_cog(Fun(bot))

class Fun(commands.Cog):
    """Fun commands with (almost) no use."""

    def __init__(self, bot):
        self.session = aiohttp.ClientSession()
        self.bot = bot

    async def get(self, url):
        async with self.session.get(url) as response:
            text = await response.text()
            return text
        await self.session.close()

    @commands.command(aliases=["howgay", "gaymeter"])
    async def gayrate(self, ctx, member : discord.User=None):
        """Says your amount of gayness."""
        self.percentage = random.randint(0, 100)

        if self.percentage == 0:
            self.gayrate_title = "Twitter hates you"
        elif self.percentage <= 20:
            self.gayrate_title = "You're good for now"
        elif self.percentage <= 40:
            self.gayrate_title = "Don't drop the soap!"
        elif self.percentage <= 60:
            self.gayrate_title = "You dropped the soap!"
        elif self.percentage == 69:
            self.gayrate_title = "Haha funi number"
        elif self.percentage <= 80:
            self.gayrate_title = "Stop it. Get some help."
        elif self.percentage == 100:
            self.gayrate_title = "You have a PhD in gay"

        if member == None:
            embed = discord.Embed(title=self.gayrate_title, description="You are " + str(self.percentage) + "% gay!", color=0xff0000)
        else:
            embed = discord.Embed(title=self.gayrate_title, description=member.mention + " is " + str(self.percentage) + "% gay!", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(aliases=["iq"])
    async def iqtest(self, ctx, member : discord.User=None):
        """Tests your IQ."""
        self.iq = random.randint(-300, 300)

        if self.iq == -300:
            self.iqtest_title = "9+10=21"
        elif self.iq <= -250:
            self.iqtest_title = "You are more stupid than the creator of this bot!"
        elif self.iq <= -200:
            self.iqtest_title = "Stop playing Fortnite"
        elif self.iq <= -150:
            self.iqtest_title = "Are you watching Morgz or something?"
        elif self.iq <= -100:
            self.iqtest_title = "Wait, that's my IQ!"
        elif self.iq <= -50:
            self.iqtest_title = "Do you use Twitter?"
        elif self.iq == 0:
            self.iqtest_title = "Absolute zero"
        elif self.iq <= 50:
            self.iqtest_title = "At least you're smarter than me!"
        elif self.iq <= 100:
            self.iqtest_title = "Average"
        elif self.iq <= 150:
            self.iqtest_title = "Nerd"
        elif self.iq <= 200:
            self.iqtest_title = "Congrats :D"
        elif self.iq <= 250:
            self.iqtest_title = "You know Obama's last name"
        elif self.iq <= 300:
            self.iqtest_title = "You know how to speak Minecraft enchanting table"
        elif self.iq == 300:
            self.iqtest_title = "You invented communism"

        if member == None:
            embed = discord.Embed(title=self.iqtest_title, description="Your IQ is " + str(self.iq) + "!", color=0xff0000)
        else:
            embed = discord.Embed(title=self.iqtest_title, description=member.mention + "'s IQ is " + str(self.iq) + "!", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command()
    async def advice(self, ctx):
        """Sends an advice."""
        
        advice = eval(await self.get("https://api.adviceslip.com/advice"))
        text = advice["slip"]["advice"]
        await ctx.send(text)

    @commands.command()
    async def httpcat(self, ctx, status_code : int):
        """Returns an HTTP cat."""
        
        embed = discord.Embed(title="Status code " + str(status_code), color=0xff0000)
        embed.set_image(url = "https://http.cat/" + str(status_code))
        await ctx.send(embed=embed)

    @commands.command()
    async def ppsize(self, ctx, member : discord.User=None):
        """Says your PP size."""

        equal_quantity = random.randint(1, 15)

        pp = "8" + "=" * equal_quantity + "D"
        if member == None:
            embed = discord.Embed(title="PP size", description="Your PP size is " + pp, color=0xff0000)
        else:
            embed = discord.Embed(title="PP size", description=member.mention + "'s PP size is " + pp, color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command()
    async def reverse(self, ctx, *, text):
        """Reverses your text."""
        
        embed = discord.Embed(title="Reversed text", description=text[::-1], color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command()
    async def say(self, ctx, *, text):
        """Says your text."""
        
        embed = discord.Embed(title="Text", description=text, color=0xff0000)
        await ctx.send(embed=embed)

    def randomize_text(self, textlist):
        return_this = ''
        for i in range(len(textlist)):
            return_this += textlist[i-1]
        return return_this

    @commands.command()
    async def randomtext(self, ctx, *, text):
        """Randomizes your text."""

        textlist = list(text)
        random.shuffle(textlist)
        fn = partial(self.randomize_text, textlist)
        self.text = await self.bot.loop.run_in_executor(None, fn)
        embed = discord.Embed(title="Random text", description=self.text, color=0xff0000)
        await ctx.send(embed=embed)

    def sort_text(self, text):
        textlist = sorted(text)
        return_this = ""
        for i in range(len(textlist)):
            return_this += textlist[i]
        return return_this

    @commands.command()
    async def sort(self, ctx, *, text):
        """Sorts the letters in your text."""

        fn = partial(self.sort_text, text)
        self.text = await self.bot.loop.run_in_executor(None, fn)
        embed = discord.Embed(title="Sorted text", description=self.text, color=0xff0000)
        await ctx.send(embed=embed)
        

    @commands.command()
    async def color(self, ctx, color : str):
        """Makes an embed with the specified color."""

        if color.startswith("#"):
            color = color[1:]
        elif color.startswith("0x"):
            color = color[2:]
        embed = discord.Embed(title='Color', description="Here's your color!", color=int(color, base=16))
        embed.add_field(name="Red", value=int(str(color)[:2], base=16))
        embed.add_field(name="Green", value=int(str(color)[2:4], base=16))
        embed.add_field(name="Blue", value=int(str(color)[4:6], base=16))
        await ctx.send(embed=embed)
