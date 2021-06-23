from discord.ext import commands, tasks
import discord
from dotenv import load_dotenv
from os import getenv
from pretty_help import PrettyHelp
import random

activities = [discord.Activity(type=discord.ActivityType.listening, name="deadmau5"),
              discord.Game(name="with hot anime girls"),
              discord.Activity(type=discord.ActivityType.watching, name="new Dank Memer commands to steal"),
              discord.Game(name="Rock, Paper, Scissors"),
              discord.Activity(type=discord.ActivityType.listening, name="farts"),
              discord.Game(name="Super Mario Bros."),
              discord.Activity(type=discord.ActivityType.watching, name="ads"),
              discord.Game(name="Mindustry"),
              discord.Activity(type=discord.ActivityType.watching, name="anime"),
              discord.Game(name="retro-mmo.com")]

load_dotenv(".env")
token = getenv("TOKEN")

bot = commands.Bot(command_prefix="mt:")

bot.counter = 0

@bot.command(name="reload", hidden=True)
async def _reload(ctx, cogName):
    if ctx.author.id == 543404497456726027:
        bot.reload_extension(cogName)
        await ctx.send("restarted!")

@bot.command(name="disable", hidden=True, aliases=["unload", "delete"])
async def _disable(ctx, cogName):
    if ctx.author.id == 543404497456726027:
        bot.unload_extension(cogName)
        await ctx.send("unloaded!")

@bot.command(name="enable", hidden=True, aliases=["load", "add"])
async def _enable(ctx, cogName):
    if ctx.author.id == 543404497456726027:
        bot.load_extension(cogName)
        await ctx.send("unloaded!")

@tasks.loop(seconds=20.0)
async def presence():
    await bot.change_presence(activity=random.choice(activities))
    print("changed")

bot.load_extension("cogs.Images")
bot.load_extension("cogs.Games")
bot.load_extension("cogs.Fun")
bot.load_extension("cogs.Covid")
bot.load_extension("cogs.Info")
bot.load_extension("cogs.Animals")
bot.load_extension("cogs.Anime")
bot.load_extension("cogs.Feelings")
bot.load_extension("cogs.Moderation")
bot.load_extension("cogs.Memes")
bot.load_extension("cogs.Currencies")
bot.load_extension("jishaku")

bot.help_command = PrettyHelp(color=0xff0000)

@bot.event
async def on_ready():
    print("running = True")
    presence.start()

@bot.event
async def on_command_error(ctx, error):
    embed = discord.Embed(title='Error', description=str(error), color=0xff0000)
    await ctx.send(embed=embed)
    raise(error)

@bot.event
async def on_message(message):
    if message.content.startswith("mt:"):
        await bot.process_commands(message)
        bot.counter += 1

bot.run(token)
