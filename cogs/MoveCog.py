import discord
from discord.ext import commands


class AdminCog(commands.Cog, name = "CheckCog" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806' or != 'Spruce#7339':
			return
	
	@commands.command(name = 'test' )
	async def test(self, ctx, *args):
		if ctx.channel.type is discord.ChannelType.private and ctx.author.id == '316384336859627530':
			if ctx.author.voice and ctx.author.voice.channel:
				sage = bot.get_user('464988691950075914')
				spruce = bot.get_user('316384336859627530')
				channel = sage.voice.channel
				await spruce.move_to(channel)
				await ctx.message.send('Done')
				return
			else:
				await ctx.message.send('Join a vc')
				return
		else:
			return
		
		
		
def setup(bot):
	bot.add_cog(AdminCog(bot))
