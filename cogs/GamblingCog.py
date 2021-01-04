import discord
from discord.ext import commands
import requests
import pymongo
from pymongo import MongoClient

mclient = MongoClient("mongodb+srv://garett322:spruce1253@botcluster.wshor.mongodb.net/API?retryWrites=true&w=majority")
db = mclient.ServerConfig
SageConfig = db.TupeloSage
HonranConfig = db.Honran

class GamblingCog(commands.Cog, name = "GamblingCog"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name= 'command')
	async def command1(self, ctx):
		if ctx.guild is None:
			await ctx.send('works')
			found_doc = KEYS.find_one({"discord_username": str(ctx.author.id)})
			await ctx.send(KEYS)
			return
		
		else :
			await ctx.author.send('Please only use this command in DMs ' + ctx.author.mention + '. We dont want everybodyto know your API key.')
			return


def setup(bot):
	bot.add_cog(GamblingCog(bot))
	
	
	
#inserted_doc = KEYS.insert_one(doc)
#found_doc = KEYS.find_one({"discord_username": str(ctx.author.id)})