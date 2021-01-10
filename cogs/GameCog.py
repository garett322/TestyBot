import discord
from discord.ext import commands
import random

class GameCog(commands.Cog, name = "GameCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'game' )
	async def game(self, ctx, num_len_str = '4'):
		num_max = '9'
		num_len = int(num_len_str)
		while len(num_max) < num_len:
			num_max += str(num_max) + '9'
		num_max += int(num_max)
		await ctx.send(num_max)
		return

def setup(bot):
	bot.add_cog(GameCog(bot))
