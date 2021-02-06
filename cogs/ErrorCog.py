import discord
from discord.ext import commands
	
	
class ErrorCog(commands.Cog, name = "Error Handler"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		"""
		The event triggered when an error is raised while invoking a command.
		Parameters
		------------
		ctx: commands.Context
		The context used for command invocation.
		error: commands.CommandError
		The Exception raised.
			"""
		
		if hasattr(ctx.command, 'on_error'):
			return
		
		cog = ctx.cog
		if cog:
			if cog._get_overridden_method(cog.cog_command_error) is not None:
				return
	
		error = getattr(error, 'original', error)
		
		if isinstance(error, commands.CommandNotFound):
			return
		
		if isinstance(error, commands.DisabledCommand):
			await ctx.send('{} has been disabled.'.format(ctx.command))
		
		elif isinstance(error, commands.NoPrivateMessage):
			try:
				await ctx.author.send(f'{ctx.command} can not be used in Private Messages.')
			except discord.HTTPException:
				pass
		
		elif isinstance(error, commands.BadArgument):
			await ctx.send('That argument didn\'t work. Please try the command again with a different argument.')
		
		else:
			print(error)
		
		return
	
	
def setup(bot):
	bot.add_cog(ErrorCog(bot))
	