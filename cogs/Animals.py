from discord.ext import commands
import discord
import aiohttp

def setup(bot):
    bot.add_cog(Animals(bot))

class Animals(commands.Cog):
    """Commands about cats, dogs and more!"""
    
    async def get(self, url):
        async with self.session.get(url) as response:
            text = await response.text()
            return text
        await self.session.close()

    def __init__(self, bot):
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def fox(self, ctx):
        """Sends an image of a fox."""

        image = await self.get("https://randomfox.ca/floof/")
        image = eval(image).get("image")
        image = image.replace("\/", "/")
        embed = discord.Embed(title="Here's a cute fox!", color=0xff0000)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(aliases=["shibe"])
    async def doge(self, ctx):
        """Sends an image of a doge."""

        image = await self.get("http://shibe.online/api/shibes")
        image = eval(image)[0]
        embed = discord.Embed(title="Here's a cute doge!", color=0xff0000)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx):
        """Sends an image of a cat."""

        image = await self.get("http://shibe.online/api/cats")
        image = eval(image)[0]
        embed = discord.Embed(title="Here's a cute cat!", color=0xff0000)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command(aliases=["birb"])
    async def bird(self, ctx):
        """Sends an image of a bird."""

        image = await self.get("http://shibe.online/api/birds")
        image = eval(image)[0]
        embed = discord.Embed(title="Here's a cute bird!", color=0xff0000)
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def dogfact(self, ctx):
        """Sends a fact about dogs."""

        fact = await self.get("https://dog-facts-api.herokuapp.com/api/v1/resources/dogs?number=1")
        fact = eval(fact)[0]
        await ctx.send(fact.get("fact"))

    @commands.command()
    async def catfact(self, ctx):
        """Sends a fact about cats."""

        fact = await self.get("https://catfact.ninja/fact")
        fact = eval(fact)
        await ctx.send(fact.get("fact"))
        
        
