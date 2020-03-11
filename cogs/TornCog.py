import discord
from discord.ext import commands


class TestCog(commands.Cog, name = "TornCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
		
	@commands.command(name = 'torn' )
		async def torny(self, ctx):
			
def setup(bot):
	bot.add_cog(TornCog(bot))
