import discord
from discord.ext import commands


class MoveCog(commands.Cog, name = "CheckCog" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author != 'Spruce#7339':
			return
	
	@commands.command(name = 'test' )
	async def test(self, ctx, args = None):
		if args == None:
			return
		user_get = bot.get_user(args)
		if not user_get.voice.channel:
			return
		channel_get = user_get.voice.channel
		if ctx.channel.type is discord.ChannelType.private and ctx.author.id == '316384336859627530':
			if ctx.author.voice and ctx.author.voice.channel:
				await ctx.author.move_to(channel_get)
				await ctx.send('Done')
				return
			else:
				await ctx.send('Join a vc')
				return
		return
		
		
		
def setup(bot):
	bot.add_cog(MoveCog(bot))
