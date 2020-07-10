import discord
from discord.ext import commands


class TestCog(commands.Cog, name = "TestCog" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
	
	@commands.command(name = 'check' )
	async def check(self, ctx, *args):
		if not args:
			await ctx.send('No args')
			return
		else:
			await ctx.send('Args confirmed')
			return
      
        

def setup(bot):
	bot.add_cog(TestCog(bot))
