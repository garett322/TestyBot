import re
import discord
from discord.ext import commands


class RoleCog(commands.Cog, name = "Roles"):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
	
	@commands.command(name = 'role', description = '.role is for creating and deleting custom roles. Use ".role create (role color) (role name)" to create a custom role. To see the list of available colors use ".colors". Use ".role delete" to delete your current custom role.')
	async def role(self, ctx, command_type = None, role_color = None, *, role_name = None):

		async def color_check(inp):
			rgb = inp.split(',')
			for num in rgb:
				if int(num) >= 0 and int(num) <= 255:
					continue
				else:
					return False
					break
			return True


		role_list = {'KingHon', 'bot kings', 'kool kids', 'Channel Points', 'stream gang', 'Server Booster', '@everyone', 'Bot Tester'}

		color_list = {
			'blue': discord.Colour.blue(),
			'violet': discord.Colour.blurple(),
			'dark_blue': discord.Colour.dark_blue(),
			'dark_gold': discord.Colour.dark_gold(),
			'dark_gray': discord.Colour.dark_gray(),
			'dark_grey': discord.Colour.dark_grey(),
			'dark_green': discord.Colour.dark_green(),
			'dark_magenta': discord.Colour.dark_magenta(),
			'dark_orange': discord.Colour.dark_orange(),
			'dark_purple': discord.Colour.dark_purple(),
			'dark_red': discord.Colour.dark_red(),
			'dark_teal': discord.Colour.dark_teal(),
			'darker_gray': discord.Colour.darker_gray(),
			'darker_grey': discord.Colour.darker_grey(),
			'green': discord.Colour.green(),
			'gold': discord.Colour.gold(),
			'light_gray': discord.Colour.light_gray(),
			'light_grey': discord.Colour.light_grey(),
			'lighter_gray': discord.Colour.lighter_gray(),
			'lighter_grey': discord.Colour.lighter_grey(),
			'magenta': discord.Colour.magenta(),
			'purple': discord.Colour.purple(),
			'orange': discord.Colour.orange(),
			'random': discord.Colour.random(),
			'red': discord.Colour.red(),
			'teal': discord.Colour.teal()}
		if command_type == None:
			await ctx.send('No such command. Use either ".role create" or ".role delete".')
			return
		if command_type.lower() == 'create':
			if not command_type:
				await ctx.send('Please say whether you want to set or delete your custom role and try again.')
				return
			elif not role_name:
				await ctx.send('Please input the name of your custom role and try again.')
				return
			for role in ctx.author.roles:
				if role.name not in role_list:
					await ctx.send('You already have a cutom role. Delete your current role and try again.')
					return
			if role_color == None:
				await ctx.guild.create_role(name = role_name)
			else:
				if role_color in color_list:
					await ctx.guild.create_role(name = role_name, colour = color_list[role_color])
				elif color_check(role_color) == True:
					await ctx.guild.create_role(name = role_name, colour = discord.colour.from_rgb(role_color.replace(',', ', ')))
				else:
					await ctx.send('Please choose a supported color and try again.')
					return
			role = discord.utils.get(ctx.guild.roles, name = role_name)
			user = ctx.message.author
			await user.add_roles(role)
			await ctx.send('Your custom role {} has been created and assigned to you!'.format(role_name))
			return
					
		elif command_type.lower() == 'delete':
			for role in ctx.author.roles:
				if role.name not in role_list:
					await role.delete()
					#role_del = role.delete
					await ctx.send('Your custom role "{}" has been removed.'.format(role.name))
					return
			await ctx.send('There weren\'t any custom roles to delete. Use ".role create" to make one.')
			return
				
					
					
		else:
			await ctx.send('No such command. Use either ".role create" or ".role delete".')
			return

	@commands.command(name = 'colors', description = 'Lists the available colors for the role command.')
	async def colors(self, ctx):
		color_list = {'blue', 'violet', 'dark_blue', 'dark_gold', 'dark_gray', 'dark_grey', 'dark_green', 'dark_magenta', 'dark_orange', 'dark_purple', 'dark_red', 'dark_teal', 'darker_gray', 'darker_grey', 'green','gold', 'light_gray', 'light_grey', 'lighter_gray', 'lighter_grey', 'magenta', 'purple', 'orange', 'random', 'red', 'teal'}
		await ctx.send(str(color_list).strip('{}').replace("'", ''))
		return
		
		
def setup(bot):
	bot.add_cog(RoleCog(bot))
