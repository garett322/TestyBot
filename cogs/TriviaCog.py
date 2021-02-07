import discord
from discord.ext import commands
import requests
import random
import asyncio


class TriviaCog(commands.Cog, name = 'Trivia'):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(name = 'trivia', description = 'Trivia command')
	async def trivia(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('The available options for trivia are: "start" and "categories"')
			return
		
		
	@trivia.command(name = 'start', description = 'Starts your trivia game')
	async def start(self, ctx, difficulty = None, *, category = None):
		
		if difficulty == None:
			difficulty = ''
		else:
			difficulty = f'&difficulty={difficulty}'
		
		if category == None:
			category = ''
		else:
			categories_json = requests.get('https://opentdb.com/api_category.php').json()
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
				await ctx.send(f'I couldn\'t find a category called "{category}". Use the command ".trivia categories" to get a list of all available categories.')
		
		
			
		question_json = requests.get(f'https://opentdb.com/api.php?amount=1{category}{difficulty}').json()
		if question_json['response_code'] == 0:
			pass
		elif question_json['response_code'] == 2:
			await ctx.send('An argument you gave caused an error. Please try again.')
			return
		else:
			await ctx.send('Unknown error.')
			return
		
		if '&quot;' in question_json['results'][0]['correct_answer']:
			question_str = str(question_json['results'][0]['correct_answer']).replace("'&quot;", '')
		else:
			question_str = str(question_json['results'][0]['correct_answer'])
		
		
		if question_json['results'][0]['category'].startswith('Entertainment:'):
			x = slice(15, None, None)
			category = str(question_json['results'][0]['category'])[x]
		elif question_json['results'][0]['category'].startswith('Science:'):
			x = slice(9, None, None)
			category = str(question_json['results'][0]['category'])[x]
		else:
			category = str(question_json['results'][0]['category'])
			
		difficulty = str(question_json['results'][0]['difficulty'])[0].upper() + str(question_json['results'][0]['difficulty'])[1:]
		
		embed = discord.Embed(title = question_json['results'][0]['question'], description = f'Courtesy of {ctx.author.name}')
		if question_json['results'][0]['type'] == 'boolean':
			answer_place = random.randint(1,2)
			embed.add_field(name = 'Answers:', value = 'True\nFalse')
			embed.set_footer(text = f"Category: {category}; Difficulty: {difficulty}")
			message = await ctx.send(embed = embed)
			await message.add_reaction('☑️')
			await message.add_reaction('❎')
			qtype = 1
				
		else:
			answer_place = random.randint(0,3)
			wrong_answer_list = question_json['results'][0]['incorrect_answers']
			answer_list = ''
			x = 0
			i = 0
			while i <= 3:
				if i == answer_place:
					answer_list = answer_list + question_str + '\n'
				else:
					answer_list = answer_list + wrong_answer_list[x] + '\n'
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
			if user == ctx.author:
				if qtype == 1:
					return str(reaction.emoji) in tf_answer_emojis
				elif qtype == 2:
					return str(reaction.emoji) in mc_answer_emojis
					
		try:
			reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)
		except asyncio.TimeoutError:
			await ctx.send('You ran out of time to answer. Next question.')
			return
		else:
			fails = 0
			if qtype == 1:
				answer_emojis = tf_answer_emojis
			elif qtype == 2:
				answer_emojis = tf_answer_emojis
				
			user_answer = str(reaction.emoji)
			if answer_emojis[user_answer] == answer_place:
				await ctx.send(f'CORRECT! Good job {user.name}!')
			else:
				await ctx.send('INCORRECT.')
				await ctx.send(f"The correct answer was: {question_str}.")


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
