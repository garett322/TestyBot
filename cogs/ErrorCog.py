import discord
from discord.ext import commands
	
	
class ErrorCog(commands.Cog, name = "Error Handler"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		
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
				await ctx.author.send('{} can not be used in Private Messages.'.format(ctx.command))
			except discord.HTTPException:
				pass
		
		elif isinstance(error, commands.BadArgument):
			await ctx.send('That argument didn\'t work. Please try the command again with a different argument.')
		
		else:
			print(error)
			spruce = await self.bot.fetch_user('316384336859627530')
			await spruce.send(f'Error occured. Command: .{ctx.command}; Server: {ctx.guild}; User: {ctx.author}. Check logs.')
			await ctx.send('An unknown error occurred. <@201909896357216256> will fix it soon.')
			
		return
	
	
def setup(bot):
	bot.add_cog(ErrorCog(bot))
	