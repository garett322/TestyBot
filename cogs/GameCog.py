import discord
from discord.ext import commands
import random

class GameCog(commands.Cog, name = "GameCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'game' )
	async def game(self, ctx, num_length = 4):
		num_max = '9'
		while len(num_max) < num_length:
			num_max += num_max + '9'
		num_max += int(num_max)
		await ctx.send(num_max)
		return

def setup(bot):
	bot.add_cog(GameCog(bot))
