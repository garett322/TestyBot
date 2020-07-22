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
					print('The error is as follows: ' + API_DOC['error'])
					return
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
					return
					
		else:	
			await ctx.message.delete()
			await ctx.author.send('Please only use this command in DMs ' + ctx.author.mention + '. We dont want everybodyto know your API key.')
			return
		
		
		
	@commands.command()
	async def torn(self, ctx, args = None):
		
		if not args:
			await ctx.send('no args')
			return
			
			
			
			
			
		args_string = str(args)	
		if args_string.lower() == 'battlestats':
			
			user_check_doc = KEYS.find_one({"discord_username": str(ctx.author.id)})
			if user_check_doc['discord_username'] == str(ctx.author.id):
				
				api_pull = user_check_doc['api_key']
				API_DOC = requests.get('https://api.torn.com/user/?selections=battlestats&key={}'.format(api_pull)).json()
					
				try:
					str_pull= API_DOC['strength']
					dex_pull= API_DOC['dexterity']
					def_pull= API_DOC['defense']
					spd_pull= API_DOC['speed']
					total_pull= API_DOC['total']
				except KeyError:
					print('The error is as follows: ' + API_DOC['error'])
					return
				else:
					embed=discord.Embed(title=user_check_doc['name'] + '\'s Battle Stats', color=0x00ffff)
					embed.add_field(name='Strength:', value=str_pull, inline=True)
					embed.add_field(name='Speed:', value=spd_pull, inline=True)
					embed.add_field(name='------------------------------------------------------', value="----------------------------------------------------", inline=False)
					embed.add_field(name='Defense:', value=def_pull, inline=True)
					embed.add_field(name='Dexterity', value=dex_pull, inline=True)
					embed.add_field(name="------------------------------------------------------", value="----------------------------------------------------", inline=False)
					embed.add_field(name='Total:', value=total_pull, inline=False)
					await ctx.send(embed=embed)
					await ctx.send('+----------------------+-------------+\n|             Strength             |  ' + str(str_pull) + ' |') 
					return
			 
			else:
				await ctx.send('You have to register your API Key with the "api_set" command before you can use this.')
				return
			
			
		else:
			await ctx.send('not battlestats')
			return
		
		
		
		
		
		
			       
			       
			       

def setup(bot):
	bot.add_cog(TornCog(bot))
