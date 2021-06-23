import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(Currencies(bot))

class Currencies(commands.Cog):
    """Commands about real-life and cryptocurrencies."""

    def __init__(self, bot):
        self.bot = bot

    async def get(self, url):
        async with self.bot.session.get(url) as response:
            text = await response.text()
        return text

    @commands.command()
    async def currency(self, ctx, cur1, cur2="usd"):
        """Information about currencies."""
        
        cur_result = await self.get("https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/" + cur1.lower() + ".json")
        if cur_result == "Failed to fetch fawazahmed0/currency-api@1 from GitHub.":
            embed = discord.Embed(title="Error", description="That currency does not exist!", color=0xff0000)
        else:
            cur_dict = eval(cur_result)
            cur_dict = cur_dict[cur1.lower()]
            embed = discord.Embed(title="Info about " + cur1.upper(), color=0xff0000)
            embed.add_field(name=cur2.upper(), value=cur_dict[cur2])
        await ctx.send(embed=embed)

    @commands.command()
    async def crypto(self, ctx, crypto="bitcoin"):
        """Information about cryptocurrencies."""

        null = "infinity"
        crypto_result = await self.get("https://api.coincap.io/v2/assets/" + crypto)
        crypto_result = eval(crypto_result)
        if crypto_result.get("error") != None:
            embed = discord.Embed(title="Error", description=crypto_result["error"], color=0xff0000)
        else:
            embed = discord.Embed(title="Information about " + crypto_result["data"]["name"], description="", url=crypto_result["data"]["explorer"], color=0xff0000)
            embed.add_field(name="Rank", value=crypto_result["data"]["rank"])
            embed.add_field(name="Symbol", value=crypto_result["data"]["symbol"])
            embed.add_field(name="Supply", value=crypto_result["data"]["supply"])
            if crypto_result["data"]["maxSupply"] == "infinity":
                embed.add_field(name="Max. supply", value="Infinity")
            else:
                embed.add_field(name="Max. supply", value=crypto_result["data"]["maxSupply"])
            embed.add_field(name="Market Cap (USD)", value=crypto_result["data"]["marketCapUsd"])
            embed.add_field(name="Volume (USD 24h)", value=crypto_result["data"]["volumeUsd24Hr"])
            embed.add_field(name="Price (USD)", value=crypto_result["data"]["priceUsd"])
            embed.add_field(name="Change percent (24h)", value=crypto_result["data"]["changePercent24Hr"])
            embed.add_field(name="VWAP (24h)", value=crypto_result["data"]["vwap24Hr"])
        await ctx.send(embed=embed)
