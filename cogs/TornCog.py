import discord
from discord.ext import commands
import requests
import pymongo
from pymongo import MongoClient

mclient = MongoClient('mongodb://heroku_zb0mj906:9dhrt56f6gdaprvdu1dg0am4eo@ds061787.mlab.com:61787/heroku_zb0mj906?retryWrites=false')
KEYS = mclient.heroku_zb0mj906.API_KEYS



class TornCog(commands.Cog, name = "TornCog" ):
	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
			
			
			
	@commands.command()
	async def api_set(self, ctx, api_key):
		if ctx.guild is None:
		
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

def setup(bot):
	bot.add_cog(TornCog(bot))
