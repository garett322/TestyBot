import discord
from discord.ext import commands


class RoleCog(commands.Cog, name = "RoleCog" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
	
	@commands.command(name = 'role' )
	async def role(self, ctx, args: str):
		if not args:
			await ctx.send('No args')
			return
		else:
			if args.lower == 'set':
				await ctx.send('The name of your role:')
				def check(message):
					return message.author == ctx.author and (message.content.lower() == 'test')
				try:
					msg = await self.bot.wait_for('message', timeout=15.0, check=check)
				except asyncio.TimeoutError:
					await ctx.send(ctx.author.mention + 'You took too long to reply. The command has been canceled.')
				else:
					for role in ctx.author.roles:
						if role.name == 'bot kings':
							ctx.send('dope!!!')
							return
						else:
							ctx.send('NOT DOPE!!!!')
							return




def setup(bot):
	bot.add_cog(RoleCog(bot))
