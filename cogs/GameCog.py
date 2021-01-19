import discord
from discord.ext import commands
import random
import asyncio

class GameCog(commands.Cog, name = "GameCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'game' )
	async def game(self, ctx, num_max_str = '100'):
		try:
			num_max = int(num_max_str)
		except ValueError:
			await ctx.send('Please use a valid number for the maximum number. Game has been cancelled.')
			return
		num_len = len(num_max_str)
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
					result_bad = result_bad + guess[i]
				i = i + 1
			return (result_good, result_okay, result_bad)


		good_result_list = '-' * num_len
		bad_result_list = ''
		tries = 0
		while True:
			await ctx.send('You have 30 seconds to guess a number between 1 and {}. Say "cancel" to cancel the game.'.format(num_max))
			try:
				msg_obj = await self.bot.wait_for('message', check=check(ctx.author), timeout=30)
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
			embed = discord.Embed(title = 'Guessing Game', author = ctx.author.name, color = discord.Colour.blue())
			if okay_result == 'n/a'and bad_result == 'n/a':
				embed.clear_fields()
				embed.add_field(name = 'CORRECT!' value = 'You won!', inline = False)
				embed.add_field(name = 'Answer:', value = msg, inline = False)
				embed.add_field(name = 'Tries:', value = tries, inline = False)
				await ctx.send(embed = embed)
				return
			else:
				
				if good_result == good_result_list:
					pass
				else:
					x = 0
					while x < num_len:
						if good_result[x] == '-' or good_result[x] == good_result_list[x]:
							pass
						else:
							if x == 0:
								good_result_list = good_result[x] + good_result_list[x+1:]
							elif x == (num_len - 1):
								good_result_list = good_result_list[0:x] + good_result[x]
							else:
								good_result_list = good_result_list[0:x] + good_result[x] + good_result_list[x+1:]
						x = x + 1
				if bad_result == '':
					pass
				else:
					y = 0
					while y < len(bad_result):
						if bad_result[y] in bad_result_list:
							pass
						else:
							if bad_result_list == '':
								bad_result_list = bad_result[y]
							else:
								bad_result_list = bad_result[y] + ', ' + bad_result_list
						y = y + 1
											
											
				if okay_result == '':
					okay_result = 'None'
				if bad_result_list == '':
					bad_result_list = 'None'
				embed.clear_fields()
				embed.add_field(name = 'Answer:', value = good_result_list, inline = False)
				embed.add_field(name = 'Right number, wrong place:', value = okay_result, inline = False)
				embed.add_field(name = 'Wrong numbers:', value = bad_result_list, inline = False)
				await ctx.send(embed = embed)
		return

def setup(bot):
	bot.add_cog(GameCog(bot))
