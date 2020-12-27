import re
import discord
from discord.ext import commands


class RoleCog(commands.Cog, name = "RoleCog" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
	
	@commands.command(name = 'role' )
	async def role(self, ctx, args1, args2, args3 = None):

		color_list = {
			'blue': discord.Colour.blue,
			'violet': discord.Colour.blurple,
			'dark_blue': discord.Colour.dark_blue,
			'dark_gold': discord.Colour.dark_gold,
			'dark_gray': discord.Colour.dark_gray,
			'dark_grey': discord.Colour.dark_grey,
			'dark_green': discord.Colour.dark_green,
			'dark_magenta': discord.Colour.dark_magenta,
			'dark_orange': discord.Colour.dark_orange,
			'dark_purple': discord.Colour.dark_purple,
			'dark_red': discord.Colour.dark_red,
			'dark_teal': discord.Colour.dark_teal,
			'darker_gray': discord.Colour.darker_gray,
			'darker_grey': discord.Colour.darker_grey,
			'gray': discord.Colour.gray,
			'grey': discord.Colour.grey,
			'green': discord.Colour.green,
			'gold': discord.Colour.gold,
			'light_gray': discord.Colour.light_gray,
			'light_grey': discord.Colour.light_grey,
			'lighter_gray': discord.Colour.lighter_gray,
			'lighter_grey': discord.Colour.lighter_grey,
			'magenta': discord.Colour.magenta,
			'purple': discord.Colour.purple,
			'orange': discord.Colour.orange,
			'random': discord.Colour.random,
			'red': discord.Colour.red,
			'teal': discord.Colour.teal}


		if not args1:
			await ctx.send('Please say whether you want to set or delete your custom role.')
			return
		elif not args2:
			await ctx.send('Please input the name of your custom role.')
			return
		else:
			if args1.lower() == 'set':
				for role in ctx.author.roles:
					if role.name.lower() == args2.lower():
						await ctx.send('You already have this role.')
						return
					else:
						pass
				if args3 == None:
					await ctx.guild.create_role(name = args2)
				else:
					if args3 in color_list:
						await ctx.guild.create_role(name = args2, colour = color_list[args3])
					else:
						await ctx.send('Please choose a supported color.')
						return
				role = discord.utils.get(ctx.guild.roles, name = args2)
				user = ctx.message.author
				await user.add_roles(role)
				await ctx.send('Your custom role {} has been created and assigned to you!'.format(args2))
				return
					
			else:
				await ctx.send('Args failure.')



def setup(bot):
	bot.add_cog(RoleCog(bot))
