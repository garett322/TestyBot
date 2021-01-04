import discord
from discord.ext import commands
import json


class MuteCog(commands.Cog, name = "MuteCog" ):
	def __init__(self, bot):
		self.bot = bot
		
		
	@commands.Cog.listener()
	async def on_message(self, message):
		for role in message.author.roles:
			if role.name == 'A Fuckin Chad':
				pass
		else:
			with open('./config/config.json', 'r') as f:
				config = json.load(f)
			usermutes = config[message.guild.name]["mutes"]["usermute"]
			servermute = config[message.guild.name]["mutes"]["servermute"]
			rolemutes = config[message.guild.name]["mutes"]["rolemute"]
			if servermute == 'on':
				await message.delete()
				return
			elif message.author.name in usermutes:
				await message.delete()
				return
			for role in message.author.roles:
				if role.name in rolemutes:
					await message.delete()
					return

	@commands.command(name = 'mute' )
	async def mute(self, ctx, choice, muted = None):
		for role in ctx.author.roles:
			if role.name == 'A Fuckin Chad':
				await ctx.message.delete()
				with open('./config/config.json', 'r') as f:
					config = json.load(f)
					
				if choice == 'all':
					servermute = config[ctx.guild.name]["mutes"]["servermute"]
					if servermute == 'on':
						config[ctx.guild.name]["mutes"]["servermute"] = 'off'
						await ctx.author.send('Server mute removed.')
					elif servermute == 'off':
						config[ctx.guild.name]["mutes"]["servermute"] = 'on'
						await ctx.author.send('Server mute applied.')
					with open('./config/config.json', 'w') as f:
						json.dump(config, f, indent = 2)
					return
				elif choice == 'user':
					usermutes = config[ctx.guild.name]["mutes"]["usermute"]
					if muted in usermutes:
						usermutes.remove(member.name)
						config[ctx.guild.name]["mutes"]["usermute"] = usermutes
						await ctx.author.send('{} has been unmuted'.format(muted))
					else:
						usermutes.append(member.name)
						config[ctx.guild.name]["mutes"]["usermute"] = usermutes
						await ctx.author.send('{} has been muted.'.format(muted))
					with open('./config/config.json', 'w') as f:
						json.dump(usermutes, f, indent = 2)
					return
				elif choice == 'role':
					rolemutes = config[ctx.guild.name]["mutes"]["rolemute"]
					if muted in rolemutes:
						rolemutes.remove(member.name)
						config[ctx.guild.name]["mutes"]["rolemute"] = rolemutes
						await ctx.author.send('The {} role has been unmuted'.format(muted))
					else:
						rolemutes.append(member.name)
						config[ctx.guild.name]["mutes"]["rolemute"] = rolemutes
						await ctx.author.send('The {} role has been muted.'.format(muted))
					with open('./config/config.json', 'w') as f:
						json.dump(rolemutes, f, indent = 2)
					return
		else:
			await ctx.send('You don\'t got the perms bruh.')
			return
		
def setup(bot):
	bot.add_cog(MuteCog(bot))
