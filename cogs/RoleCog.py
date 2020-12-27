import discord
from discord.ext import commands


class RoleCog(commands.Cog, name = "RoleCog" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
	
	@commands.command(name = 'role' )
	async def role(self, ctx, args1, args2, args3: str = None):
		if not args1:
			await ctx.send('Please say whether you want to set or delete your custom role.')
			return
		elif not args2:
			await ctx.send('Please input the name of your custom role.')
			return
		else:
			if args1.lower() == 'set':
				for role in ctx.author.roles:
					if role.name.lower() == msg.content.lower():
						await ctx.send('You already have this role.')
						return
					else:
						pass
				if args3 == None:
					await ctx.guild.create_role(name = msg.content)
				else:
					await ctx.guild.create_role(name = msg.content, color = args3)
				role = discord.utils.get(ctx.guild.roles, name = msg.content)
				user = ctx.message.author
				await user.add_roles(role)
				await ctx.send('Your custom role {} has been created and assigned to you!'.format(msg.content))
				return
			else:
				await ctx.send('Args failure.')




def setup(bot):
	bot.add_cog(RoleCog(bot))
