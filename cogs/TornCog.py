import discord
from discord.ext import commands
import json



class TornCog(commands.Cog, name = "TornCog" ):
	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return


	@commands.group()
	async def api(ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('Invalid command passed...')

	@api.command()
	async def set(ctx):
		api_key = ctx.message.content
		result = json.loads('https://api.torn.com/user/?selections=travel&key=${api_key}')
		await ctx.send(result['travel'])

def setup(bot):
	bot.add_cog(TornCog(bot))
