import discord
from discord.ext import commands
import requests

categories_url = 'https://opentdb.com/api_category.php'
questions_url = 'https://opentdb.com/api.php?amount={}&category={}&difficulty={}'




class TriviaCog(commands.Cog, name = 'Trivia' ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(name = 'trivia')
	async def trivia(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('The available options for trivia are: start.')
			return
		
	@trivia.command(name = 'start')
	async def start(self, ctx):
		categories_response = requests.get(categories_url)
		categories_api = categories_url.json()
		category_list = ''
		for category in catagories_api:
			category_list = category_list + ', ' + category['name']
		category_list = category_list.strip(', ')
		await ctx.send('Please choose a category:')
		await ctx.send(category_list)
		return
		


def setup(bot):
	bot.add_cog(TriviaCog(bot))
