import discord
from discord.ext import commands
import json
#import requests
import pymongo
from pymongo import MongoClient
mclient = MongoClient("mongodb+srv://garett322:spruce1253@botcluster.wshor.mongodb.net/API?retryWrites=true&w=majority")
DB = mclient.ServerConfig
ConfigDB = DB.Config

def ConfigUpdate(file):
	try:
		inserted_doc = Config.insert_one(file)
		return True
	except:
		return False

def ConfigSearch(item):
	try:
		found = Config.find_one(item)
		return found
	except:
		return False



class MuteCog(commands.Cog, name = "MuteCog" ):
	def __init__(self, bot):
		self.bot = bot
		
		
	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author is self.bot.user:
			return
		for role in message.author.roles:
			if role.name == 'A Fuckin Chad':
				break
		else:
			config = ConfigSearch({"name": message.guild.name})
			usermutes = config["Usermutes"]
			servermute = config["Servermute"]
			rolemutes = config["Rolemutes"]
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
		return

	@commands.command(name = 'mute' )
	async def mute(self, ctx, choice, *, muted = None):
		for role in ctx.author.roles:
			if role.name == 'A Fuckin Chad':
				await ctx.message.delete()
				
				config = ConfigSearch({"name": message.guild.name})
				usermutes = config["Usermutes"]
				servermute = config["Servermute"]
				rolemutes = config["Rolemutes"]
					
				if choice == 'all':
					if servermute == 'on':
						config["Servermute"] = 'off'
						await ctx.author.send('Server mute removed.')
						updated_file = config["Servermute"]
					elif servermute == 'off':
						config["Servermute"] = 'on'
						await ctx.author.send('Server mute applied.')
						updated_file = config["Servermute"]
				elif choice == 'user':
					if muted in usermutes:
						usermutes.remove(muted.name)
						updated_file = usermutes
						await ctx.author.send('{} has been unmuted'.format(muted))
					else:
						usermutes.append(muted.name)
						updated_file = usermutes
						await ctx.author.send('{} has been muted.'.format(muted))
				elif choice == 'role':
					if muted in rolemutes:
						rolemutes.remove(muted.name)
						updated_file = rolemutes
						await ctx.author.send('The {} role has been unmuted'.format(muted))
					else:
						rolemutes.append(muted.name)
						updated_file = rolemutes
						await ctx.author.send('The {} role has been muted.'.format(muted))
				Update = ConfigUpdate(updated_file)
				return
		else:
			await ctx.send('You don\'t got the perms bruh.')
			return
		
def setup(bot):
	bot.add_cog(MuteCog(bot))
