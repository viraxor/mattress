from discord.ext import commands
import discord
from covid import Covid as CovidStats

def setup(bot):
    bot.add_cog(Covid(bot))

class Covid(commands.Cog):
    """Informations about COVID-19."""

    @commands.command()
    async def covid(self, ctx, *, country : str=None):
        """COVID-19 stats from John Hopkins University."""

        async with ctx.typing():
            self.covid_client = CovidStats()
            if country == None:
                embed = discord.Embed(title="COVID-19 cases in the world", color=0xff0000)
                embed.add_field(name="Confirmed cases", value=str(self.covid_client.get_total_confirmed_cases()))
                embed.add_field(name="Active cases", value=str(self.covid_client.get_total_active_cases()))
                embed.add_field(name="Recovered", value=str(self.covid_client.get_total_recovered()))
                embed.add_field(name="Deaths", value=str(self.covid_client.get_total_deaths()))
            else:
                embed = discord.Embed(title="COVID-19 cases in " + country, color=0xff0000)
                try:
                    self.country_cases = self.covid_client.get_status_by_country_name(country)
                except ValueError:
                    embed = discord.Embed(title="That country doesn't exist!", description="If you think this is an error, please contact Moonwo#9188.", color=0xff0000)
                else:
                    embed.add_field(name="Confirmed cases", value=str(self.country_cases.get("confirmed")))
                    embed.add_field(name="Active cases", value=str(self.country_cases.get("active")))
                    embed.add_field(name="Recovered", value=str(self.country_cases.get("recovered")))
                    embed.add_field(name="Deaths", value=str(self.country_cases.get("deaths")))
            await ctx.send(embed=embed)


            