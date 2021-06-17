import discord
from discord.ext import commands
from os.path import exists, abspath

def setup(bot):
    bot.add_cog(Tags(bot))

class Tags(commands.Cog):
    """Tag commands."""

    @commands.command()
    async def create_tag(self, ctx, name, *, text):
        if not exists(abspath("tags/" + name + ".txt")):
            with open(abspath("tags/" + name + ".txt"), "w") as tag_file:
                tag_file.write(text + "\nauthor: " + ctx.author.id)
                await ctx.send("Done!")
        else:
            await ctx.send("This tag already exists.")
    
    @commands.command()
    async def tag(self, ctx, name):
        if exists(abspath("tags/" + name + ".txt")):
            with open(abspath("tags/" + name + ".txt"), "r") as tag_file:
                tag_text = tag_file.read()
                await ctx.send(tag_text)
        else:
            await ctx.send("This tag does not exist.")
