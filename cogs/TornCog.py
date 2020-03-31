import discord
from discord.ext import commands
import requests



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
				  result = key_check['"gender"']
				except KeyError:
				  await ctx.send(result)
				else:
				  await ctx.send(key_check['"error"'])
		
		  

def setup(bot):
	bot.add_cog(TornCog(bot))
