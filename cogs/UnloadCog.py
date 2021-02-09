import discord
from discord.ext import commands


class UnloadCog(commands.Cog, name = "Error handler" ):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.group(name = 'cog', description = 'Cog manager')
	@commands.is_owner()
	async def errors(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('The available options are: "list", "enable", and "disable"')
			return
			
			
	@errors.command(name = 'list', description = 'Enables cogs' )
	async def list(self, ctx):
		ListOfCogs = self.bot.cogs
		cog_list = []
		for NameOfCog,ClassOfCog in ListOfCogs.items():
			cog_list.append(ClasdOfCog)
		await ctx.send(str(cog_list).strip('][').replace("'", ''))

	@errors.command(name = 'enable', description = 'Enables cogs' )
	async def enable(self, ctx, cog_name):
		try:
			self.bot.load_extension(f'cogs.{cog_name}')
		except commands.ExtensionAlreadyLoaded:
			await ctx.send(f'{cog_name} is already loaded')
		except commands.ExtensionNotFound:
			await ctx.send('Cog not found')
		else:
			await ctx.send(f'{cog_name} has been loaded')


	@errors.command(name = 'disable', description = 'Disables cogs' )
	async def disable(self, ctx, cog_name):
		try:
			self.bot.unload_extension(f'cogs.{cog_name}')
		except commands.ExtensionNotLoaded:
			await ctx.send(f'{cog_name} is already unloaded')
		except commands.ExtensionNotFound:
			await ctx.send('Cog not found')
		else:
			await ctx.send(f'{cog_name} has been unloaded')
		
		
def setup(bot):
	bot.add_cog(UnloadCog(bot))
