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
		key_check = requests.get('https://api.torn.com/user/?selections=&key={}'.format(api_key)).json()
		try:
		  playername = key_check['name']
		except KeyError:
		  await ctx.send(key_check['error'])
		else:
		  doc = {"name": playername,
		    "api_key": api_key,
		    "discord_username": ctx.author.id
		  }
		  await ctx.send(playername)
		  await ctx.send(api_key)
		  await ctx.send(doc['name'])
		  await ctx.send(doc['api_key'])
		  inserted_doc = KEYS.insert_one(doc)
		  found_doc = KEYS.find_one({"discord_username", ctx.author.id})
		  await ctx.send(found_doc)
		
		  

def setup(bot):
	bot.add_cog(TornCog(bot))
