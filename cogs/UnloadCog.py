import discord
from discord.ext import commands
import sys

sys.path.append('./cogs')
from ErrorCog import ErrorCog

class UnloadCog(commands.Cog, name = "Error handler" ):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.group(name = 'errors', description = 'Cog manager')
	@commands.is_owner()
	async def errors(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('The available options are: "enable" and "disable"')
			return
			
	@errors.command(name = 'enable', description = 'Unloads cogs' )
	async def enable(self, ctx):
		try:
			bot.load_extension(f'cogs.{cog_name}')
		except commands.ExtensionAlreadyLoaded:
			await ctx.send(f'{cog_name} is already loaded')
		except commands.ExtensionNotFound:
			await ctx.send('Cog not found')
		else:
			await ctx.send(f'{cog_name} has been loaded')


	@errors.command(name = 'disable', description = 'Loads cogs' )
	async def disable(self, ctx):
		try:
			bot.unload_extension(f'cogs.{cog_name}')
		except commands.ExtensionNotLoaded:
			await ctx.send(f'{cog_name} is already unloaded')
		except commands.ExtensionNotFound:
			await ctx.send('Cog not found')
		else:
			await ctx.send(f'{cog_name} has been unloaded')
		
		
def setup(bot):
	bot.add_cog(UnloadCog(bot))
