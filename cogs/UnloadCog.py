import discord
from discord.ext import commands

sys.path.append('.')
from ErrorCog import ErrorCog

class UnloadCog(commands.Cog, name = "Error handler" ):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.group(name = 'cog', description = 'Cog manager')
	@commands.is_owner()
	async def coggers(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('The available options are: "load" and "unload"')
			return
			
	@coggers.command(name = 'Unload', description = 'Unloads error handler' )
	async def unload(self, ctx):
		try:
			bot.remove_cog('ErrorCog')
		except:
			await ctx.send('ErrorCog not unloaded.')
		
	@coggers.command(name = 'Load', description = 'Loads error handler' )
	async def load(self, ctx):
		try:
			bot.add_cog(ErrorCog(bot))
		except:
			await ctx.send('Cog not Loaded.')
      
        

def setup(bot):
	bot.add_cog(UnloadCog(bot))
