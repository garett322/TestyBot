import discord
from discord.ext import commands
import requests
import random

categories_url = 'https://opentdb.com/api_category.php'
questions_url = 'https://opentdb.com/api.php?amount={}&category={}&difficulty={}'




class TriviaCog(commands.Cog, name = 'Trivia'):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(name = 'trivia', description = 'Trivia command')
	async def trivia(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('The available options for trivia are: start.')
			return
		
		
	@trivia.command(name = 'start', description = 'Starts your trivia game')
	async def start(self, ctx, difficulty = None, questions = 5, category = None):
		
		if difficulty == None:
			difficulty = ''
		else:
			difficulty = f'&difficulty={difficulty}'
		
		if category == None:
			category = ''
		else:
			categories_json = requests.get(categories_url).json()
			for category_chk in categories_json['trivia_categories']:
				if category_chk['name'].startswith('Entertainment:'):
					x = slice(15, None, None)
					category_name = str(category_chk['name'])[x]
				elif category_chk['name'].startswith('Science:'):
					x = slice(9, None, None)
					category_name = str(category_chk['name'])[x]
				else:
					category_name = str(category_chk['name'])
					
				if category.lower() == category_name.lower():
					category = f"&category={category_chk['id']}"
					break
			else:
				await ctx.send(f'I couldn\'t find a category called "{category}". Use the command ".trivia categories" to get a list of available categories.')
		
		try:
			questions = int(questions)
		except:
			await ctx.send(f'{questions} is not a valid number. Please try again.')
			return
			
		questions_json = requests.get(f'https://opentdb.com/api.php?amount={questions}{category}{difficulty}').json()
		if questions_json['response_code'] == 0:
			pass
		elif questions_json['response_code'] == 1:
			await ctx.send(f'I couldn\'t find {questions} questions. Please try a smaller number.')
			return
		elif questions_json['response_code'] == 2:
			await ctx.send('An argument you gave caused an error. Please try again.')
			return
		else:
			await ctx.send('Unknown error.')
			return
		counter = 1
		fails = 0
		for question in questions_json['results']:
			
			if question['category'].startswith('Entertainment:'):
				x = slice(15, None, None)
				category = str(question['category'])[x]
			elif question['category'].startswith('Science:'):
				x = slice(9, None, None)
				category = str(question['category'])[x]
			else:
				category = str(question['category'])
				
			difficulty = str(question['difficulty'])[0].upper() + str(question['difficulty'])[1:]
				
			if question['type'] == 'boolean':
				answer_place = random.randint(1,2)
				embed = discord.Embed(title = question['question'], description = f'Question {counter} of {questions}')
				embed.add_field(name = 'Answers:', value = 'True\nFalse')
				embed.set_footer(text = f"Category: {category}; Difficulty: {difficulty}")
				message = await ctx.send(embed = embed)
				await message.add_reaction('☑️')
				await message.add_reaction('❎')
				qtype = 1
				
			else:
				answer_place = random.randint(0,3)
				wrong_answer_list = question['incorrect_answers']
				embed = discord.Embed(title = question['question'], description = f'Question {counter} of {questions}')
				answer_list = ''
				x = 0
				i = 0
				while i <= 3:
					if i == answer_place:
						answer_list = answer_list + question['correct_answer'] + '\n'
					else:
						answer_list = answer_list + wrong_answer_list[i] + '\n'
						x = x + 1
					i = i + 1
				embed.add_field(name = 'Answers:', value = answer_list)
				embed.set_footer(text = f"Category: {category}; Difficulty: {difficulty}")
				message = await ctx.send(embed = embed)
				await message.add_reaction('1️⃣')
				await message.add_reaction('2️⃣')
				await message.add_reaction('3️⃣')
				await message.add_reaction('4️⃣')
				qtype = 2
				
			emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
			mc_answer_emojis = {'1️⃣': 0, '2️⃣': 1, '3️⃣': 2, '4️⃣': 3}
			tf_answer_emojis = {'☑️': 0, '❎': 1}
			def check(reaction, user):
				if qtype == 1:
					return user == ctx.author and (str(reaction.emoji) is in tf_answer_emojis or str(reaction.emoji) == '⛔')
				elif qtype == 2:
					return user == ctx.author and (str(reaction.emoji) is in mc_answer_emojis or str(reaction.emoji) == '⛔')
					
			try:
				reaction, user = await client.wait_for('reaction_add', timeout=20.0, check=check)
			except asyncio.TimeoutError:
				await ctx.send('You ran out of time to answer. Next question.')
				fails = fails + 1
				if fails == 3:
					await ctx.send('You ran out of time 3 times in a row. Trivia has been automatically cancelled.')
					return
			else:
				if qtype = 1:
					answer_emojis = tf_answer_emojis
				elif qtype = 2:
					answer_emojis = tf_answer_emojis
					
				user_answer = str(reaction.emoji)
				if answer_emojis[user_answer] == answer_place:
					await ctx.send('CORRECT!')
					await ctx.send('Next question...')
				elif user_answer == '⛔':
					await ctx.send('Trivia cancelled.')
					await message.delete()
					return
				else:
					await ctx.send('INCORRECT.')
					await ctx.send(f"The correct answer was: {question['correct_answer']}.")
					await ctx.send('Next question...')
				fails = 0
				
			await asyncio.sleep(2)
			await message.delete()
			counter = counter + 1


	@trivia.command(name = 'categories', description = 'Shows all available catagories.')
	async def categories(self, ctx):
		categories_json = requests.get(categories_url).json()
		category_list = ''
		
		for category in categories_json['trivia_categories']:
			if category['name'].startswith('Entertainment:'):
				x = slice(15, None, None)
				category_name = str(category['name'])[x]
			elif category['name'].startswith('Science:'):
				x = slice(9, None, None)
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
