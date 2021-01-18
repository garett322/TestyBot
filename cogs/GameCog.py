import discord
from discord.ext import commands
import random
import asyncio

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
		try:
			msg = int(msg)
		except ValueError:
			await ctx.send('Please only guess numbers. Game has been cancelled')
			return
		if len(msg) > num_len:
			await ctx.send('Please guess a number that is between 1 and {}. Game has been cancelled'.format(num_max))
			return
		while len(msg) < num_len:
			msg = '0' + str(msg)
			msg = int(msg)
		
		def guess_chk(guess_int, answer_int):
			guess = str(guess_int)
			answer = str(answer_int)
			if guess == answer:
				return (guess, 'n/a', 'n/a')
			i = 1
			result = ''
			result_okay = ''
			result_bad = ''
			while i < len(answer):
				if guess[i] == answer[i]:
					result_good = result_good + guess[i]
					result_okay = result_okay + '_'
					result_bad = result_bad + '_'
					i = i + 1
					continue
				for answer_digit in answer:
					if guess[i] == answer_digit:
						result_good = result_good + '_'
						result_okay = result_okay + guess[i]
						result_bad = result_bad + '_'
						break
				else:
					result_good = result_good + '_'
					result_okay = result_okay + '_'
					result_bad = result_bad + guess[i]
				i = i + 1
				continue
			return (result_good, result_okay, result_bad)


		(good_result, okay_result, bad_result) = guess_chk(msg, num_gen)
		await ctx.send('{}, {}, {}'.format(good_result, okay_result, bad_result))
		return
		
		

def setup(bot):
	bot.add_cog(GameCog(bot))
