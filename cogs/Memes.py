from discord.ext import commands
import discord
import aiohttp
import io
from functools import partial
from PIL import Image, ImageFont, ImageDraw
from typing import Optional
import random

def setup(bot):
    bot.add_cog(Memes(bot))

class Memes(commands.Cog):
    """Commands for meme generators."""

    def __init__(self, bot):
        self.session = aiohttp.ClientSession()
        self.bot = bot

    async def get(self, url):
        async with self.session.get(url) as response:
            text = await response.text()
            return text    
        await self.session.close()

    async def getbytes(self, url):
        async with self.session.get(url) as response:
            text = await response.content.read(n=-1)
            return text    
        await self.session.close()

    def save_image(self, image_data):
        image = Image.open(io.BytesIO(image_data))
        image.save("avatar.png")

    @commands.command()
    async def threats(self, ctx, member : discord.User=None):
        """The 3 biggest threats to society"""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=threats&url=" + url)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="The 3 biggest threats to society", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def baguette(self, ctx, member : discord.User=None):
        """Sends an image of someone eating a baguette."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=baguette&url=" + url)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Baguette", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def lolice(self, ctx, member : discord.User=None):
        """Sends an image of someone as a lolice chief."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=lolice&url=" + url)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Lolice chief", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)
            
    @commands.command()
    async def captcha(self, ctx, member : discord.User=None):
        """Sends a captcha."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            username = str(member.name)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=captcha&url=" + url + "&username=" + username)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Solve the captcha!", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def trash(self, ctx, member : discord.User=None):
        """Why Japan gotta turn everything into an anime girl? smh"""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=trash&url=" + url)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Why Japan gotta turn everything into an anime girl? smh", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def changemymind(self, ctx, *, text):
        """Sends a Change My Mind meme with the text you entered."""

        async with ctx.typing():
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=changemymind&text=" + text)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Change my mind", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def trumptweet(self, ctx, *, text):
        """Tweets as Trump."""
            
        async with ctx.typing():
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=trumptweet&text=" + text)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Trump tweeted", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def carreverse(self, ctx, *, text):
        """Makes a Car Reverse meme."""

        async with ctx.typing():
            endpoint = await self.getbytes("https://vacefron.nl/api/carreverse?text=" + text)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Car reverse", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def water(self, ctx, *, text):
        """Makes a Water meme."""

        async with ctx.typing():
            endpoint = await self.getbytes("https://vacefron.nl/api/water?text=" + text)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Water", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def emergencymeeting(self, ctx, *, text):
        """Makes an Emergency Meeting meme."""

        async with ctx.typing():
            endpoint = await self.getbytes("https://vacefron.nl/api/emergencymeeting?text=" + text)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Emergency Meeting", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def wolverine(self, ctx, member : discord.User=None):
        """Makes a meme of Wolverine holding the photo of the mentioned user."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            endpoint = await self.getbytes("https://vacefron.nl/api/wolverine?user=" + str(member.avatar_url)) 
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Wolverine", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def dockofshame(self, ctx, member : discord.User=None):
        """Puts the mentioned user on the Dock of Shame."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            endpoint = await self.getbytes("https://vacefron.nl/api/dockofshame?user=" + str(member.avatar_url)) 
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Dock of Shame", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def drip(self, ctx, member : discord.User=None):
        """Makes a drip character out of the mentioned user."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/drip?user=" + url) 
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="He got the drip", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def whowouldwin(self, ctx, member : discord.User, member2 : Optional[discord.User]=None):
        """Who would win?"""

        async with ctx.typing():
            if member2 == None:
                member2 = ctx.author
            url = str(member.avatar_url)
            url2 = str(member2.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=whowouldwin&user1=" + url + "&user2=" + url2)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Who would win?", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def grave(self, ctx, member : discord.User=None):
        """Makes a grave for the mentioned user."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/grave?user=" + url)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Rest in Pepperoni", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def heaven(self, ctx, member : discord.User=None):
        """Sends somebody to heaven."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/heaven?user=" + url)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Amen", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def iamspeed(self, ctx, member : discord.User=None):
        """Makes an I am speed meme."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/iamspeed?user=" + url)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Speed. I am speed.", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def firsttime(self, ctx, member : discord.User=None):
        """Makes a First time? meme."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/firsttime?user=" + url)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="First time?", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def stonks(self, ctx, member : discord.User=None):
        """Makes a Stonks meme."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/stonks?user=" + url + "&notstonks=" + random.choice(["True", "False"]))
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Stonks", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def npc(self, ctx, *, text : str):
        """Generates a meme of 2 NPCs talking. Usage: mt:npc text1, text2"""

        async with ctx.typing():
            text1, text2 = text.split(", ")
            endpoint = await self.getbytes("https://vacefron.nl/api/npc?text1=" + text1 + "&text2=" + text2)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Two NPCs", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def womanyellingatcat(self, ctx, member : discord.User, member2 : Optional[discord.User]=None):
        """Sends a Woman Yelling at Cat meme."""

        async with ctx.typing():
            if member2 == None:
                member2 = ctx.author
            url = str(member.avatar_url)
            url2 = str(member2.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/womanyellingatcat?woman=" + url + "&cat=" + url2)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Woman yelling at cat", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def icanmilkyou(self, ctx, member : discord.User, member2 : Optional[discord.User]=None):
        """Makes an I can milk you meme."""

        async with ctx.typing():
            if member2 == None:
                member2 = ctx.author
            url = str(member.avatar_url)
            url2 = str(member2.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/icanmilkyou?user1=" + url + "&user2=" + url2)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="I can milk you", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def ejected(self, ctx, *, name):
        """haha amogus sus haha funi impostor"""

        async with ctx.typing():
            endpoint = await self.getbytes("https://vacefron.nl/api/ejected?name=" + name + "&impostor=" + random.choice(["True", "False"]) + "&crewmate=" + random.choice(["lime", "red", "blue", "pink", "black", "yellow", "darkgreen", "orange", "white", "purple", "brown", "cyan"]))
            print(endpoint)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Is this sus?", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    def genfhl(self, member : discord.User):
        image = Image.open(r"images\furryhuntinglicense.webp")
        avatar = Image.open("avatar.png")
        avatar = avatar.resize((325, 360))
        image.paste(avatar, (44, 191))

        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(r"tests\font\Roboto-Medium.ttf", 72)
        w, h = draw.textsize(str(member.name), font=font)
        draw.text(((1068 - w) / 2, 55), str(member.name), font=font, fill=(0, 0, 0, 255))
        image.save("avatar.png")

    @commands.command()
    async def furryhuntinglicense(self, ctx, member : discord.User=None):
        """Makes you a furry hunting license."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            await member.avatar_url_as(size=256).save("avatar.png")
            fn = partial(self.genfhl, member)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Furry hunting license", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)
            
    
    
