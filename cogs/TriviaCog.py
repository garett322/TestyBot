import discord
from discord.ext import commands
import requests

categories_url = 'https://opentdb.com/api_category.php'
questions_url = 'https://opentdb.com/api.php?amount={}&category={}&difficulty={}'
token_url = 'https://opentdb.com/api_token.php?command=request'


class TriviaCog(commands.Cog, name = 'Trivia' ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(name = 'trivia')
	async def trivia(self, ctx):
		
		@trivia.command(name = 'start')
		async def start(self, ctx):
			token_api = requests.get(token_url)
			token = token_api['token']
			categories_api = requests.get(categories_url)
			category_names = categories_api['trivia_categories']['name']
			await ctx.send('Please choose a category:')
			await ctx.send(category_names)
			return
		


def setup(bot):
	bot.add_cog(TriviaCog(bot))
