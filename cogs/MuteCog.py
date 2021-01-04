import discord
from discord.ext import commands
import json
#import requests
import pymongo
from pymongo import MongoClient
mclient = MongoClient('mongodb+srv://garett322:spruce1253@botcluster.wshor.mongodb.net/ServerConfig?retryWrites=true&w=majority
DB = mclient.ServerConfig
ConfigDB = DB.Config

def ConfigUpdate(file):
	try:
		inserted_doc = Config.update_one(file)
		return True
	except:
		return False

def ConfigSearch(item):
	try:
		found = Config.find_one(item)
		return found
	except:
		return False
		
def TargetCheck(target):
	try:
		user = commands.converter.MemberConverter().convert(target)
	



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
			usermutes_og = config["Usermutes"]
			servermute_og = config["Servermute"]
			rolemutes_og = config["Rolemutes"]
			if servermute_og == 'on':
				await message.delete()
				return
			elif message.author.name in usermutes_og:
				await message.delete()
				return
			for role in message.author.roles:
				if role.name in rolemutes_og:
					await message.delete()
					return
		return

	@commands.command(name = 'mute' )
	async def mute(self, ctx, choice, *, muted = None):
		for role in ctx.author.roles:
			if role.name == 'A Fuckin Chad':
				await ctx.message.delete()
				
				config = ConfigSearch({"name": message.guild.name})
				usermutes_og = config["Usermutes"]
				servermute_og = config["Servermute"]
				rolemutes_og = config["Rolemutes"]
					
				if choice == 'all':
					if servermute_og == 'on':
						servermute_new = 'off'
						await ctx.author.send('Server mute removed.')
					elif servermute_og == 'off':
						servermute_new = 'on'
						await ctx.author.send('Server mute applied.')
					updated_file = {"Servermute": servermute_new}
				elif choice == 'user':
					if muted in usermutes_og:
						usermutes_new = usermutes_og
						usermutes_new.remove(muted.name)
						await ctx.author.send('{} has been unmuted'.format(muted))
					else:
						usermutes_new = usermutes_og
						usermutes_new.append(muted.name)
						await ctx.author.send('{} has been muted.'.format(muted))
					updated_file = {"Usermutes": usermutes_new}
				elif choice == 'role':
					if muted in rolemutes_og:
						rolemutes_new = rolemutes_og
						rolemutes_new.remove(muted.name)
						await ctx.author.send('The {} role has been unmuted'.format(muted))
					else:
						rolemutes_new = rolemutes_og
						rolemutes_new.append(muted.name)
						await ctx.author.send('The {} role has been muted.'.format(muted))
					updated_file = {"Rolemutes": rolemutes_new}
				Update = ConfigUpdate(updated_file)
				return
		else:
			await ctx.send('You don\'t got the perms bruh.')
			return
		
def setup(bot):
	bot.add_cog(MuteCog(bot))
