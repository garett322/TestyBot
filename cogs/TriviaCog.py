import discord
from discord.ext import commands
import requests

categories_url = 'https://opentdb.com/api_category.php'
questions_url = 'https://opentdb.com/api.php?amount={}&category={}&difficulty={}'




class TriviaCog(commands.Cog, name = 'Trivia'):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(name = 'trivia')
	async def trivia(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('The available options for trivia are: start.')
			return
		
	@trivia.command(name = 'start')
	async def start(self, ctx):
		categories_json = requests.get(categories_url).json()
		category_list = ''
		
		for category in categories_json['trivia_categories']:
			if category['name'].startswith('Entertainment:'):
				x = slice(13, None, None)
				category_name = str(category['name'])[x]
			else:
				category_name = str(category['name'])
			
			category_list = category_list + ', ' + category_name
			
			
		category_list = category_list.strip(', ')
		await ctx.send('Please choose a category:')
		await ctx.send(category_list)
		return
		


def setup(bot):
	bot.add_cog(TriviaCog(bot))
