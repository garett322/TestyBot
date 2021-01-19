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
		num_max_str = '9'
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
		
		def guess_chk(guess_int, answer_int):
			guess = str(guess_int)
			answer = str(answer_int)
			answer_len = len(answer)
			if guess == answer:
				return (guess, 'n/a', 'n/a')
			i = 1
			result_good = ''
			result_okay = ''
			result_bad = ''
			while i <= answer_len:
				if guess[0] == answer[0]:
					result_good = result_good + guess[0]
				elif guess[0] in answer:
					result_good = result_good + '-'
					if result_okay == '':
						result_okay = guess[0]
					else:
						result_okay = result_okay + ', ' + guess[0]
				else:
					result_good = result_good + '-'
					result_bad = result_bad + guess[0]
				if i == answer_len:
					pass
				else:
					guess = guess[1:]
					answer = answer[1:]
				i = i + 1
			return (result_good, result_okay, result_bad)

		good_result_list = '-' * num_len
		bad_result_list = ''
		tries = 1
		while tries > 0:
			await ctx.send('You have 15 seconds to guess a number. Say "cancel" to cancel the game.')
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
				
			(good_result, okay_result, bad_result) = guess_chk(msg, num_gen)
			await ctx.send('Guess: {}, Answer: {}'.format(msg, num_gen))
			embed = discord.Embed(title = 'Guessing Game', author = ctx.author, color = discord.Colour.blue())
			if okay_result == 'n/a'and bad_result == 'n/a':
				embed.clear_fields()
				embed.add_field('Answer:', msg, inline = False)
				embed.add_field('Tries:', tries, inline = False)
				await ctx.send(embed = embed)
				return
			else:
				x = 0
				while x <= num_len:
					if good_result[x] == '-' or good_result[x] == good_result_list[x]:
						x = x + 1
						continue
					else:
						good_result_list = good_result_list[0:x] + good_result[x] + good_result_list[x+1:]
					x = x + 1
						
				if bad_result == '':
					pass
				else:
					while len(bad_result) > 0:
						if bad_result[0] in bad_result_list:
							bad_result = bad_result[1:]
						else:
							if bad_result_list == '':
								bad_result_list = bad_result[0]
							else:
								bad_result_list = bad_result_list + ', ' + bad_result[0]
						if len(bad_result) == 1:
							bad_result = ''
							continue
						elif len(bad_result) > 1:
							bad_result = bad_result[1:]
				
				embed.clear_fields()
				embed.add_field('Answer:', good_result_list, inline = False)
				embed.add_field('Right number, wrong place:', okay_result, inline = False)
				embed.add_field('Wrong number:', bad_result_list, inline = False)
				await ctx.send(embed = embed)
				tries = tries + 1
		return

def setup(bot):
	bot.add_cog(GameCog(bot))
