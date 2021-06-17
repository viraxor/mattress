from discord.ext import commands
import discord
import aiohttp

def setup(bot):
    bot.add_cog(Anime(bot))
    
class Anime(commands.Cog):
    """I'm really sorry"""

    async def get(self, url):
        async with self.session.get(url) as response:
            text = await response.text()
            return text
        await self.session.close()

    def __init__(self, bot):
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def animequote(self, ctx):
        """Sends a quote from a random anime."""

        quote = eval(await self.get("https://animechan.vercel.app/api/random"))
        embed = discord.Embed(title="Here's an anime quote!", description=quote.get("quote"), color=0xff0000)
        embed.add_field(name="Anime", value=quote.get("anime"), inline=False)
        embed.add_field(name="Character", value=quote.get("character"), inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def waifu(self, ctx):
        """Sends a waifu."""

        image = eval(await self.get("https://api.waifu.pics/sfw/waifu"))
        embed = discord.Embed(title="Here's a waifu!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def neko(self, ctx):
        """Sends a neko."""

        image = eval(await self.get("https://api.waifu.pics/sfw/neko"))
        embed = discord.Embed(title="Here's a neko!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

        
