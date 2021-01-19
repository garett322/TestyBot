import discord
from discord.ext import commands
import random
import asyncio

class GameCog(commands.Cog, name = "GameCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'game' )
	async def game(self, ctx, num_len_str = '4'):
		try:
			num_len = int(num_len_str)
		except ValueError:
			await ctx.send('Please use a valid number for the answer length. Game has been cancelled.')
			return
		num_max = int('9' * num_len)
		init_num_gen = random.randint(1, num_max)
		num_gen = str(init_num_gen)
		while len(num_gen) < num_len:
			num_gen = '0' + num_gen



		def check(author):
			def inner_check(message): 
				if message.author == author and message.content:
					return True
				else:
					return False
			return inner_check
		
		def guess_chk(guess, answer):
			answer_len = len(answer)
			if guess == answer:
				return (guess, 'n/a', 'n/a')
			i = 0
			result_good = ''
			result_okay = ''
			result_bad = ''
			while i < answer_len:
				if guess[i] == answer[i]:
					result_good = result_good + guess[i]
				elif guess[i] in answer:
					result_good = result_good + '-'
					if result_okay == '':
						result_okay = guess[i]
					elif guess[i] in result_okay:
						pass
					else:
						result_okay = result_okay + ', ' + guess[i]
				else:
					result_good = result_good + '-'
					if result_bad == '':
						result_bad = guess[i]
					elif guess[i] in result_bad:
						pass
					else:
						result_bad = result_bad + ', ' + guess[i]
				i = i + 1
			return (result_good, result_okay, result_bad)

		tries = 0
		while True:
			await ctx.send('You have 15 seconds to guess a number between 1 and {}. Say "cancel" to cancel the game.'.format(num_max))
			try:
				msg_obj = await self.bot.wait_for('message', check=check(ctx.author), timeout=15)
			except asyncio.TimeoutError:
				await ctx.send('Time ran out. Game has been cancelled')
				return
			if msg_obj.content.lower() == 'cancel':
				await ctx.send('Game has been cancelled.')
				return
			try:
				msg = int(msg_obj.content)
			except ValueError:
				await ctx.send('Please only guess numbers.')
				continue
			msg = str(msg)
			if len(msg) > num_len:
				await ctx.send('Please guess a number that is between 1 and {}.'.format(num_max))
				continue
			while len(msg) < num_len:
				msg = '0' + msg
			
			tries = tries + 1
			(good_result, okay_result, bad_result) = guess_chk(msg, num_gen)
			await ctx.send('Guess: {}, Answer: {}'.format(msg, num_gen))
			embed = discord.Embed(title = 'Guessing Game', author = ctx.author, color = discord.Colour.blue())
			if okay_result == 'n/a'and bad_result == 'n/a':
				embed.clear_fields()
				embed.add_field(name = 'Answer:', value = msg, inline = False)
				embed.add_field(name = 'Tries:', value = tries, inline = False)
				await ctx.send(embed = embed)
				return
			else:
				if okay_result == '':
					okay_result = 'None'
				if bad_result == '':
					bad_result = 'None'
				embed.clear_fields()
				embed.add_field(name = 'Answer:', value = good_result, inline = False)
				embed.add_field(name = 'Right number, wrong place:', value = okay_result, inline = False)
				embed.add_field(name = 'Wrong numbers:', value = bad_result, inline = False)
				await ctx.send(embed = embed)
		return

def setup(bot):
	bot.add_cog(GameCog(bot))
