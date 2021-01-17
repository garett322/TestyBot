import discord
from discord.ext import commands
import random

class GameCog(commands.Cog, name = "GameCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'game' )
	async def game(self, ctx, num_len_str = '4'):
		num_max_str = '9'
		num_len = int(num_len_str)
		while len(num_max_str) < num_len:
			num_max_str = num_max_str + '9'
		num_max = int(num_max_str)
		init_num_gen = random.randint(1, num_max)
		num_gen_str = str(init_num_gen)
		while len(num_gen_str) < num_len:
			num_gen_str = '0' + num_gen_str
		num_gen = int(num_gen_str)
		


		def check(author):
			def inner_check(message): 
				if message.author == author and message.content:
					return True
				else:
					return False
			return inner_check
			
		await ctx.send('You have 10 seconds to guess a number.')
		try:
			msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=10)
		except asyncio.TimeoutError:
			await ctx.send('You didn\'t guess in time {}. Game has been cancelled'.format(ctx.author.name))
			return
		
		def guess_chk(guess, answer):
			
		
		guess_result = guess_chk(msg, num_gen)
		
		

def setup(bot):
	bot.add_cog(GameCog(bot))
