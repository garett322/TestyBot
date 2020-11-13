import discord
from discord.ext import commands
import requests
import pymongo
from pymongo import MongoClient

mclient = MongoClient("mongodb+srv://garett32#00ccff2:13243546gareth@discordbotcluster.wshor.mongodb.net/API?retryWrites=true&w=majority")
db = mclient.API
KEYS = db.Keys

class GamblingCog(commands.Cog, name = "GamblingCog"):
def __init__(self, bot):
self.bot = bot

async def on_message(self, message):
if message.author == 'Test Bot#0806':
return



@commands.command(name= 'command1')
async def command1(self, ctx):
if ctx.guild is None:
await ctx.author.send('Please only use this command in DMs ' + ctx.author.mention + '. We dont want everybodyto know your API key.')
return






else :
  inserted_doc = KEYS.insert_one(doc)
  found_doc = KEYS.find_one({
  "discord_username": str(ctx.author.id)})
  










def setup(bot):
bot.add_cog(TornCog(bot))