import discord
from discord.ext import commands


class TestCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		
	
	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
			
	@commands.command()
	async def testy(self, ctx):
		await ctx.send('It Works!')
		return

def setup(bot):
	bot.add_cog(TestCog(bot))