import discord
from discord.ext import commands
import requests
import pymongo
from pymongo import MongoClient
import urllib.request, json 

mclient = MongoClient("mongodb+srv://garett322:13243546gareth@discordbotcluster.wshor.mongodb.net/API?retryWrites=true&w=majority")
db = mclient.API
KEYS = db.Keys


class TornCog(commands.Cog, name = "TornCog" ):
	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
			
			
			
	@commands.command()
	async def api_set(self, ctx, api_key):
		if ctx.guild is None:
			
			if not api_key:
				await ctx.author.send('You need to put in your API Key for this command.')
				return
			else:
				API_DOC = requests.get('https://api.torn.com/user/?selections=&key={}'.format(api_key)).json()
			
				try:
					playername = API_DOC['name']
				except KeyError:
					await ctx.author.send('There seems to have been an error...')
					await ctx.author.send('The error is as follows: ' + API_DOC['error'])
				else:
					try_doc = KEYS.find_one({"discord_username": str(ctx.author.id)})
		
				
				try:
					if try_doc['discord_username'] == str(ctx.author.id):
						await ctx.author.send('You have already registered your API key with me ' + playername + '.')
				except TypeError:
					doc = {"name": playername,
					"api_key": api_key,
					"discord_username": str(ctx.author.id)}
					
					inserted_doc = KEYS.insert_one(doc)		    
					await ctx.author.send('Your API key has been registered ' + playername + '!!')
					found_doc = KEYS.find_one({"discord_username": str(ctx.author.id)})
					
		else:	
			await ctx.message.delete()
			await ctx.author.send('Please only use this command in DMs ' + ctx.author.mention + '. We dont want everybodyto know your API key.')
			return
	@commands.command()
	async def check(self, ctx, args):
		
		
		
		#with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as API_data:
		#	data = json.loads(API_data.read().decode())
		#	print(data)
			
		if args[1] != "":
			await ctx.send('Please only use one argument with this command')
			return
		
		args_string = str(args[0])	
		if args_string.lower() == 'stats':
			await ctx.send('It works!')
			return

def setup(bot):
	bot.add_cog(TornCog(bot))
