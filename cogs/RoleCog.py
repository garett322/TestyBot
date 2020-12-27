import discord
from discord.ext import commands


class RoleCog(commands.Cog, name = "RoleCog" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
	
	@commands.command(name = 'role' )
	async def role(self, ctx, args):
		if not args:
			await ctx.send('No args')
			return
		else:
			if args.lower() == 'set':
				await ctx.send('The name of your role:')
				def check(message):
					return message.author == ctx.author
				try:
					msg = await self.bot.wait_for('message', timeout=15.0, check=check)
				except asyncio.TimeoutError:
					await ctx.send(ctx.author.mention + 'You took too long to reply. The command has been canceled.')
				else:
					for role in ctx.author.roles:
						if role.name.lower() == msg.content.lower():
							await ctx.send('You already have this role.')
							return
						else:
							pass
					await ctx.guild.create_role(name = msg.content)
					role = discord.utils.get(ctx.guild.roles, name = msg.content)
					user = ctx.message.author
					await user.add_roles(role)
					await ctx.send('Your custom role {} has been created and assigned to you!'.format(msg.content))
					return
			else:
				await ctx.send('Args failure.')




def setup(bot):
	bot.add_cog(RoleCog(bot))
