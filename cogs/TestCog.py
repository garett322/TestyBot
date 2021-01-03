import discord
from discord.ext import commands


class TestCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def testy(self, ctx):
		await ctx.send('It Works!')
		return

def setup(bot):
	bot.add_cog(TestCog(bot))