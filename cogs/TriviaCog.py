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
				await message.add_reaction('✔️')
				await message.add_reaction('🚫')
				
				
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
			counter = counter + 1
			return


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
