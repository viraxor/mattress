from discord.ext import commands
import discord
import aiohttp

def setup(bot):
    bot.add_cog(Feelings(bot))

class Feelings(commands.Cog):
    """Use those commands to express your feelings."""

    async def get(self, url):
        async with self.session.get(url) as response:
            text = await response.text()
            return text
        await self.session.close()

    def __init__(self, bot):
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def hug(self, ctx, member : discord.User):
        """Hug someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/hug"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " hugs " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def bully(self, ctx, member : discord.User):
        """Bully someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/bully"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " bullies " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def cuddle(self, ctx, member : discord.User):
        """Cuddle someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/cuddle"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " cuddles " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def kiss(self, ctx, member : discord.User):
        """Kiss someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/kiss"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " kisses " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def lick(self, ctx, member : discord.User):
        """Lick someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/lick"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " licks " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def pat(self, ctx, member : discord.User):
        """Pat someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/pat"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " pats " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def bonk(self, ctx, member : discord.User):
        """Bonk someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/bonk"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " bonks " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def yeet(self, ctx, member : discord.User):
        """Yeet someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/yeet"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " yeets " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def bite(self, ctx, member : discord.User):
        """Bite someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/bite"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " bites " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def glomp(self, ctx, member : discord.User):
        """Glomp someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/glomp"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " glomps " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def slap(self, ctx, member : discord.User):
        """Slap someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/slap"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " slaps " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member : discord.User):
        """Kill someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/kill"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " kills " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def poke(self, ctx, member : discord.User):
        """Poke someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/poke"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " pokes " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def wave(self, ctx, member : discord.User):
        """Wave to someone using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/wave"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " waves to " + str(member.display_name) + "!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def highfive(self, ctx, member : discord.User):
        """Give someone a high five using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/highfive"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " gives " + str(member.display_name) + " a high five!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def cry(self, ctx):
        """Cry using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/cry"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " cries!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def blush(self, ctx):
        """Blush using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/blush"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " blushes!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def smile(self, ctx):
        """Smile using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/smile"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " smiles!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def happy(self, ctx):
        """Show the world your happiness!"""

        image = eval(await self.get("https://api.waifu.pics/sfw/happy"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " is happy!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def wink(self, ctx):
        """Wink using this command."""

        image = eval(await self.get("https://api.waifu.pics/sfw/wink"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " winks!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    @commands.command()
    async def dance(self, ctx):
        """Train for Just Dance 8392!"""

        image = eval(await self.get("https://api.waifu.pics/sfw/dance"))
        embed = discord.Embed(title=str(ctx.author.display_name) + " dances!", color=0xff0000)
        embed.set_image(url=image.get("url"))
        await ctx.send(embed=embed)

    
