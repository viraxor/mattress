from discord.ext import commands
import discord
import time

def setup(bot):
    bot.add_cog(Info(bot))

class Info(commands.Cog):
    """Information about the bot."""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def credits(self, ctx):
        """Sends the credits about the bot."""

        embed = discord.Embed(title="Credits", color=0xff0000)
        embed.add_field(name="Owner", value="Moonwo#3310")
        embed.add_field(name="Tester", value="Durlic42O#0001")
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        """Sends the bot invite."""
        
        await ctx.send("https://discord.com/oauth2/authorize?client_id=823994332372795392&scope=bot")

    @commands.command()
    async def uptime(self, ctx):
        """Sends the bot's uptime."""

        self.uptime_seconds = int(round(time.perf_counter()))
        self.uptime_total_hours = self.uptime_seconds // (60 * 60)
        self.uptime_total_minutes = self.uptime_seconds // 60
        self.uptime_days = self.uptime_seconds // (60 * 60 * 24)
        self.uptime_hours = self.uptime_seconds // (60 * 60) - self.uptime_days * 24
        self.uptime_minutes = self.uptime_seconds // 60 - self.uptime_total_hours * 60
        self.uptime_seconds = self.uptime_seconds - self.uptime_total_minutes * 60
        embed = discord.Embed(title="Bot uptime", description="The bot is online for " + str(self.uptime_days) + " days, " + str(self.uptime_hours) + " hours, " + str(self.uptime_minutes) + " minutes and " + str(self.uptime_seconds) + " seconds.", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command()
    async def command_usage(self, ctx):
        """Sends the amount of commands that have been used since the last shutdown."""

        embed = discord.Embed(title="Command usage", description=str(self.bot.counter + 1) + " commands were used since the last restart.", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(aliases=["command_count"])
    async def total_commands(self, ctx):
        """Sends the amount of commands."""

        embed = discord.Embed(title="Total commands", description="There are " + str(len(self.bot.commands)) + " commands.", color=0xff0000)
        await ctx.send(embed=embed)

    @commands.command(aliases=['servers'])
    async def server_count(self, ctx):
        """Sends the number of servers Mattress is in."""

        embedVar = discord.Embed(title="Server count", description="I'm in " + str(len(self.bot.guilds)) + ' servers.', color=0xff0000)
        await ctx.send(embed=embedVar)

    @commands.command()
    async def ping(self, ctx):
        """Sends the bot latency."""

        embed = discord.Embed(title="Pong!", description="The bot latency is " + str(round(self.bot.latency, 3)).replace('0.', '') + 'ms.', color=0xff0000)
        await ctx.send(embed=embed)
