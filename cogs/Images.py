import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw, ImageOps, ImageFilter
import random
from typing import Optional
import aiohttp
from functools import partial
import io

red = 0xff0000

def setup(bot):
    bot.add_cog(Images(bot))

class Images(commands.Cog):
    """
    Fun image commands!
    """

    async def ping(self, url):
        async with self.session.get(url) as response:
            await self.session.close()

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

    def __init__(self, bot):
        self.bot = bot
        self.session = aiohttp.ClientSession()

    def spread_pil(self, distance):
        img = Image.open("avatar.png")
        img = img.effect_spread(distance)
        img.save("avatar.png")

    @commands.command()
    async def spread(self, ctx, distance : Optional[int]=50, user : discord.User=None):
        """Spreads pixels on an user's avatar. Usage: mt:spread @someone"""

        async with ctx.typing():
            if user == None:
                user = ctx.author
            if distance == 0:
                await ctx.send("You have mt:avatar for that!")
            else:
                await user.avatar_url.save("avatar.png")
                fn = partial(self.spread_pil, distance)
                await self.bot.loop.run_in_executor(None, fn)
                file = discord.File("avatar.png")
                embed = discord.Embed(title="Spreaded avatar", color=0xff0000)
                embed.set_image(url="attachment://avatar.png")
                await ctx.send(embed=embed, file=file)

    def blur_pil(self, radius):
        img = Image.open("avatar.png")
        img = img.filter(ImageFilter.GaussianBlur(radius))
        img.save("avatar.png")

    @commands.command()
    async def blur(self, ctx, radius : Optional[int]=2, user : discord.User=None):
        """Blurs an user's avatar. Usage: mt:blur @someone"""

        async with ctx.typing():
            if user == None:
                user = ctx.author
            await user.avatar_url.save("avatar.png")
            fn = partial(self.blur_pil, radius)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Blurred avatar", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    def flip_pil(self):
        img = Image.open("avatar.png")
        img = ImageOps.flip(img)
        img.save("avatar.png")

    @commands.command()
    async def flip(self, ctx, user : discord.User=None):
        """Flips an user's avatar. Usage: mt:flip @someone"""

        async with ctx.typing():
            if user == None:
                user = ctx.author
            await user.avatar_url.save("avatar.png")
            fn = partial(self.flip_pil)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Flipped avatar", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)
    
    def mirror_pil(self):
        img = Image.open("avatar.png")
        img = ImageOps.mirror(img)
        img.save("avatar.png")

    @commands.command()
    async def mirror(self, ctx, user : discord.User=None):
        """Mirrors an user's avatar. Usage: mt:mirror @someone"""

        async with ctx.typing():
            if user == None:
                user = ctx.author
            await user.avatar_url.save("avatar.png")
            fn = partial(self.mirror_pil)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Mirrored avatar", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    def grayscale_pil(self):
        img = Image.open("avatar.png")
        img = ImageOps.grayscale(img)
        img.save("avatar.png")


    @commands.command(aliases=["greyscale"])
    async def grayscale(self, ctx, user : discord.User=None):
        """Grayscales an user's avatar. Usage: mt:grayscale @someone"""

        async with ctx.typing():
            if user == None:
                user = ctx.author
            await user.avatar_url.save("avatar.png")
            fn = partial(self.grayscale_pil)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Grayscaled avatar", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    def quantize_pil(self, number):
        img = Image.open("avatar.png")
        img = img.quantize(colors=number)
        img.save("avatar.png")

    @commands.command()
    async def quantize(self, ctx, color_number : Optional[int]=50, user : discord.User=None):
        """Quantizes an user's avatar. Default: 256"""

        async with ctx.typing():
            if user == None:
                user = ctx.author
            await user.avatar_url.save("avatar.png")
            fn = partial(self.quantize_pil, color_number)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Quantized avatar", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    def blend_pil(self):
        img1 = Image.open("avatar1.png")
        img2 = Image.open("avatar2.png")
        img1 = img1.convert("RGBA")
        img2 = img2.convert("RGBA")
        if img1.height > img2.height and img1.width > img2.width:
            img1 = img1.resize((img2.width, img2.height))
        elif img2.height > img1.height and img2.width > img1.width:
            img2 = img2.resize((img1.width, img1.height))
        blendimg = Image.blend(img1, img2, 0.5)
        blendimg.save("avatar.png")

    @commands.command()
    async def blend(self, ctx, user : Optional[discord.User], user2 : discord.User=None):
        """Blends 2 avatars."""

        async with ctx.typing():
            if user2 == None:
                user2 = ctx.author
            await user.avatar_url.save("avatar1.png")
            await user2.avatar_url.save("avatar2.png")
            fn = partial(self.blend_pil)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Blended avatar", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)

    @commands.command()
    async def avatar(self, ctx, user : discord.User=None):
        """Sends an user's avatar. Usage: mt:avatar @someone"""
        
        if user == None:
            user = ctx.author
        embed = discord.Embed(title=str(user.display_name) + "'s avatar", color=red)
        embed.set_image(url=user.avatar_url)
        await ctx.send(embed=embed)

    def googlepfp_pil(self, letter):
        self.colorlist = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'a', 'b', 'c', 'd', 'e', 'f']
        self.color = "#" + random.choice(self.colorlist) + random.choice(self.colorlist) + random.choice(self.colorlist) + random.choice(self.colorlist) + random.choice(self.colorlist) + random.choice(self.colorlist) 

        self.image = Image.new('RGBA', (400, 400))
        self.draw = ImageDraw.Draw(self.image)

        self.draw.ellipse((20, 20, 380, 380), fill=self.color, outline=self.color)

        self.font = ImageFont.truetype("tests/font/Roboto-Medium.ttf", 172)
        if letter == None:
            self.letter = chr(random.randint(65, 90))
        elif len(letter) > 2:
            self.letter = letter[:2]
        else:
            self.letter = letter
                
        self.w, self.h = self.draw.textsize(self.letter, font=self.font)
        self.draw.text(((400-self.w)/2, (380-self.h)/2), self.letter, font=self.font, fill=(255, 255, 255, 255))

        self.image.save("googlepfp.png")

    @commands.command()
    async def googlepfp(self, ctx, letter=None):
        """Sends a Google profile picture (the circle with a white letter inside). Usage: mt:googlepfp <letter>"""

        async with ctx.typing():
            fn = partial(self.googlepfp_pil, letter)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("googlepfp.png", filename="googlepfp.png")
            await ctx.send(file=file)

    @commands.command()
    async def tombstone(self, ctx, *, things):
        """Makes a tombstone for you! Usage: mt:tombstone text1, text2, text3, text4"""

        async with ctx.typing():
            line1, line2, line3, line4 = things.split(", ")
            embed = discord.Embed(title="Here's your tombstone!", color=red)
            url = "http://www.tombstonebuilder.com/generate.php?top1=" + line1 + "&top2=" + line2 + "&top3=" + line3 + "&top4=" + line4 + "&sp="
            url = url.replace(r" ", "+")
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command(aliases=["award"])
    async def medal(self, ctx, *, things):
        """Makes a medal for you! Usage: mt:medal text1, text2, text3, text4"""

        async with ctx.typing():
            line1, line2, line3, line4 = things.split(", ")
            embed = discord.Embed(title="Here's your medal!", color=red)
            url = "http://www.getamedal.com/generate.php?top1=" + line1 + "&top2=" + line2 + "&top3=" + line3 + "&top4=" + line4 + "&sp="
            url = url.replace(r" ", "+")
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def roadsign(self, ctx, *, things):
        """Makes a road sign for you! Usage: mt:roadsign text1, text2, text3, text4"""

        async with ctx.typing():
            line1, line2, line3, line4 = things.split(", ")
            embed = discord.Embed(title="Here's your road sign!", color=red)
            url = "http://www.customroadsign.com/generate.php?line1=" + line1 + "&line2=" + line2 + "&line3=" + line3 + "&line4=" + line4
            url = url.replace(r" ", "%20")
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def cake(self, ctx, *, things):
        """Makes a cake for you! Usage: mt:cake text1, text2, text3, text4"""

        async with ctx.typing():
            line1, line2, line3, line4 = things.split(", ")
            embed = discord.Embed(title="Here's your cake!", color=red)
            url = "http://www.cakemessage.com/generate.php?top1=" + line1 + "&top2=" + line2 + "&top3=" + line3 + "&top4=" + line4 + "&sp="
            url = url.replace(r" ", "+")
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def weddingsign(self, ctx, *, things):
        """Makes a road sign for you! Usage: mt:weddingsign text1, text2, text3, text4"""

        async with ctx.typing():
            line1, line2, line3, line4 = things.split(", ")
            embed = discord.Embed(title="Here's your wedding sign!", color=red)
            url = "http://www.customweddingsign.com/generate.php?line1=" + line1 + "&line2=" + line2 + "&line3=" + line3 + "&line4=" + line4
            url = url.replace(r" ", "+")
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def mcachievement(self, ctx, *, text):
        """Makes a Minecraft Achievement for you! Usage: mt:mcachievement text"""

        async with ctx.typing():
            text = text.replace(" ", "+")
            embed = discord.Embed(title="Here's your Minecraft achievement!", color=red)
            url = "https://minecraftskinstealer.com/achievement/" + str(random.randint(1, 39)) + "/Achievement+Get%21/" + text
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def screenshot(self, ctx, url):
        """Screenshots a website. Usage: mt:screenshot url"""

        async with ctx.typing():
            url = "https://image.thum.io/get/" + url
            idk = await self.ping(url)
            embed = discord.Embed(title="Here's your screenshot!", color=red)
            embed.set_image(url=url)
            await ctx.send(embed=embed)

    @commands.command()
    async def blurpify(self, ctx, member : discord.User=None):
        """Turns somebody's avatar into blurple."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=blurpify&image=" + url)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Blurpified avatar", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def deepfry(self, ctx, member : discord.User=None):
        """Deepfries somebody's avatar."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=deepfry&image=" + url)
            endpoint = endpoint[:82] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Deepfried avatar", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def tweet(self, ctx, member : Optional[discord.User]=None, *, text):
        """Tweets as somebody."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=tweet&username=" + str(member.name) + "&text=" + text)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Did he get cancelled yet", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def trap(self, ctx, member : discord.User, member2 : Optional[discord.User]=None):
        """Traps an user."""

        async with ctx.typing():
            if member2 == None:
                member2 = ctx.author
            url = str(member.avatar_url)
            username = str(member.name)
            username2 = str(member2.name)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=trap&image=" + url + "&name=" + username + "&author=" + username2)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Trapped", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def awooify(self, ctx, member : discord.User=None):
        """Awooifies somebody's avatar."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=awooify&url=" + url)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Awooified avatar", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    @commands.command()
    async def iphonex(self, ctx, member : discord.User=None):
        """Fills somebody's avatar into an iPhone X."""

        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.get("https://nekobot.xyz/api/imagegen?type=iphonex&url=" + url)
            endpoint = endpoint[:81] + "}"
            endpoint = eval(endpoint)
            embed = discord.Embed(title="Shot on iPhone", color=0xff0000)
            embed.set_image(url=endpoint["message"])
            await ctx.send(embed=embed)

    def save_image(self, image_data):
        image = Image.open(io.BytesIO(image_data))
        image.save("avatar.png")

    @commands.command()
    async def wide(self, ctx, member : discord.User=None):
        """Makes your avatar w i d e."""
        
        async with ctx.typing():
            if member == None:
                member = ctx.author
            url = str(member.avatar_url)
            endpoint = await self.getbytes("https://vacefron.nl/api/wide?image=" + url)
            fn = partial(self.save_image, endpoint)
            await self.bot.loop.run_in_executor(None, fn)
            file = discord.File("avatar.png")
            embed = discord.Embed(title="Wide avatar", color=0xff0000)
            embed.set_image(url="attachment://avatar.png")
            await ctx.send(embed=embed, file=file)
            
            
