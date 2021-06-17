import discord
from discord.ext import commands
import asyncio

def setup(bot):
    bot.add_cog(Moderation(bot))

class Moderation(commands.Cog):
    """Commands for keeping your server clean!"""

    def __init__(self, bot):
        self.bot = bot

    async def parse_time(self, time):
        if time.endswith("s"):
            time = int(time[:len(time)-1])
        elif time.endswith("m"):
            time = int(time[:len(time)-1]) * 60
        elif time.endswith("h"):
            time = int(time[:len(time)-1]) * 60 * 60
        elif time.endswith("d"):
            time = int(time[:len(time)-1]) * 60 * 60 * 24
        elif time.endswith("w"):
            time = int(time[:len(time)-1]) * 60 * 60 * 24 * 7
        elif time.endswith("y"):
            time = int(time[:len(time)-1]) * 60 * 60 * 24 * 365
        return time

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.User, *, reason=None):
        await ctx.guild.kick(member, reason=reason)
        await ctx.send("The user has been kicked!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.User, *, reason=None):
        await ctx.guild.ban(member, reason=reason)
        await ctx.send("The user has been banned!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, member : discord.User):
        await ctx.guild.unban(member)
        await ctx.send("The user has been unbanned!")

    @commands.command(aliases=["purge"])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, number : int):
        await ctx.channel.purge(limit=number)
        await ctx.send("I cleared " + str(number) + " messages.")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def tempban(self, ctx, member : discord.User, time, *, reason=None):
        await ctx.guild.ban(member)
        await ctx.send("The user has been banned!")
        await asyncio.sleep(await self.parse_time(time))
        await ctx.guild.unban(member)
        await ctx.send("The user has been unbanned!")
        
            
