from discord.ext import commands
import discord
from samp_client.client import SampClient
from samp_client import exceptions
from mojang import MojangAPI
import asyncio, aiohttp

def setup(bot):
    bot.add_cog(Games(bot))

class Games(commands.Cog):
    """Commands about SA-MP, Minecraft, and more!"""

    async def get(self, url):
        async with self.session.get(url) as response:
            text = await response.text()
            return text
        await self.session.close()

    def __init__(self, bot):
        self.session = aiohttp.ClientSession()

    @commands.command()
    async def samp(self, ctx, address):
        """Sends some information about SA-MP servers."""
        
        async with ctx.typing():
            self.domain, self.port = address.split(":")
            with SampClient(address=self.domain, port=int(self.port)) as client:
                try:
                    serverinfo = client.get_server_info()
                #'NoneType' object is not subscriptable fix (not really, but okay)
                except TypeError:
                    embed = discord.Embed(color=0xff0000, title="An error occured", description="Try running the command again.")
                #the server is offline
                except exceptions.ConnectionError:
                    embed = discord.Embed(color=0xff0000, title="The server is offline!", description="If you think this is an error, you can report it to Moonwo#4768.")
                else:
                    embed = discord.Embed(color=0x00ff00, title="The server is online!")
                    embed.add_field(inline=False, name="Players", value=str(serverinfo[1]) + "/" + str(serverinfo[2]))
                    embed.add_field(inline=False, name="Hostname", value=serverinfo[3])
                    embed.add_field(inline=False, name="Gamemode", value=serverinfo[4])
                    embed.add_field(inline=False, name="Language", value=serverinfo[5])
                await ctx.send(embed=embed)

    @commands.command()
    async def mcprofile(self, ctx, username):
        """Sends some information about a Minecraft profile."""

        async with ctx.typing():
            self.uuid = MojangAPI.get_uuid(username)
            if not self.uuid:
                embed = discord.Embed(title="The user doesn't exist!", description="If you think this is an error, you can report it to Moonwo#4768.", color=0xff0000)
            else:
                self.profile = MojangAPI.get_profile(self.uuid)
                embed = discord.Embed(title="The user does exist!", color=0x00ff00)
                embed.add_field(name="UUID", value=self.profile.id, inline=False)
                embed.add_field(name="Skin model", value=self.profile.skin_model, inline=False)
                embed.set_thumbnail(url="https://crafatar.com/renders/body/" + self.profile.id)
            await ctx.send(embed=embed)

    @commands.command()
    async def retrommo_user(self, ctx, username):
        """Sends some information about a RetroMMO user."""
        
        info = await self.get("https://play.retro-mmo.com/users/" + username + ".json")
        if info == "Not Found":
            embed = discord.Embed(title="This user doesn't exist!", description="If you think this is an error, you can report it to Moonwo#4768.", color=0xff0000)
        else:
            info = eval(info)
            embed = discord.Embed(title=username + "'s account", color=0xff0000)
            embed.add_field(name="Rank", value=str(info.get("rank")), inline=False)
            embed.add_field(name="Lifetime Experience", value=str(info.get("lifetimeExperience")), inline=False)
        await ctx.send(embed=embed)
            
            


            
