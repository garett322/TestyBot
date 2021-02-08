import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import requests
import random
import asyncio
import html


class TriviaCog(commands.Cog, name = 'Trivia'):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.group(name = 'trivia', description = 'Trivia command')
	async def trivia(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send('The available options for trivia are: "start" and "categories"')
			return
		
		
	@trivia.command(name = 'start', description = 'Starts your trivia game')
	@trivia.max_concurrency(1, per=BucketType.guild, *, wait=True)
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
		
		question_str = html.unescape(str(question_json['results'][0]['question']))
		

		if question_json['results'][0]['category'].startswith('Entertainment:'):
			x = slice(15, None, None)
			category = str(question_json['results'][0]['category'])[x]
		elif question_json['results'][0]['category'].startswith('Science:'):
			x = slice(9, None, None)
			category = str(question_json['results'][0]['category'])[x]
		else:
			category = str(question_json['results'][0]['category'])
			
		difficulty = str(question_json['results'][0]['difficulty'])[0].upper() + str(question_json['results'][0]['difficulty'])[1:]
		
		embed = discord.Embed(title = question_str, description = f'Courtesy of {ctx.author.name}')
		if question_json['results'][0]['type'] == 'boolean':
			answer_place = random.randint(1,2)
			embed.add_field(name = 'Answers:', value = 'True\nFalse')
			embed.set_footer(text = f"Category: {category}; Difficulty: {difficulty}")
			question_embed = await ctx.send(embed = embed)
			await question_embed.add_reaction('☑️')
			await question_embed.add_reaction('❎')
			qtype = 1
				
		else:
			answer_place = random.randint(0,3)
			answer_str = str(question_json['results'][0]['correct_answer'])
			wrong_answer_list = question_json['results'][0]['incorrect_answers']
			answer_list = ''
			x = 0
			i = 0
			while i <= 3:
				if i == answer_place:
					answer_list = answer_list + answer_str + '\n'
				else:
					answer_list = answer_list + wrong_answer_list[x] + '\n'
					x = x + 1
				i = i + 1
			embed.add_field(name = 'Answers:', value = answer_list)
			embed.set_footer(text = f"Category: {category}; Difficulty: {difficulty}")
			question_embed = await ctx.send(embed = embed)
			await question_embed.add_reaction('1️⃣')
			await question_embed.add_reaction('2️⃣')
			await question_embed.add_reaction('3️⃣')
			await question_embed.add_reaction('4️⃣')
			qtype = 2
			
		mc_answer_emojis = ['1️⃣', '2️⃣', '3️⃣', '4️⃣']
		tf_answer_emojis = ['☑️', '❎']
		
		def answer_check(qtype, user_answer_emoji, answer_place):
			if qtype == 1:
				if user_answer_emoji == '☑️':
					user_answer_int = 0
				elif user_answer_emoji == '❎':
					user_answer_int = 1
			elif qtype == 2:
				if user_answer_emoji == '1️⃣':
					user_answer_int = 0
				elif user_answer_emoji == '2️⃣':
					user_answer_int = 1
				elif user_answer_emoji == '3️⃣':
					user_answer_int = 2
				elif user_answer_emoji == '4️⃣':
					user_answer_int = 3
			if user_answer_int == answer_place:
				return True
			else:
				return False
		
		await asyncio.sleep(15)
		cache_msg = discord.utils.get(self.bot.cached_messages, id = question_embed.id) #or client.messages depending on your variable
		correct_users = set()
		incorrect_users = set()
		cheaters = set()
		user_list = []
		for reaction in cache_msg.reactions:
			user_answer_emoji = str(reaction.emoji)
			if user_answer_emoji in tf_answer_emojis or str(reaction) in mc_answer_emojis:
				async for user in reaction.users():
					if user == self.bot.user:
						continue
					check_res = answer_check(qtype, user_answer_emoji, answer_place)
					if check_res == True:
						correct_users.add(f'<@{user.id}>')
					elif check_res == False:
						if user in incorrect_users:
							continue
						else:
							incorrect_users.add(f'<@{user.id}>')
					user_list.append(f'<@{user.id}>')
			else:
				continue
		correct_user_list = []
		incorrect_user_list = []
		cheater_list = []
		for user in user_list:
			if user in correct_user_list:
				if user in incorrect_users:
					cheater_list.append(user)
				else:
					correct_user_list.append(user)
			else:
				incorrect_user_list.append(user)
				
		if len(correct_user_list) == 0:
			correct_users = 'Nobody'
		if len(incorrect_user_list) == 0:
			incorrect_users = 'Nobody'
		if len(cheater_list) == 0:
			cheaters = 'Nobody'
		correct_users = str(correct_user_list).strip('][').replace("'", '')
		incorrect_users = str(incorrect_user_list).strip('][').replace("'", '')
		cheaters = str(cheater_list).strip('][').replace("'", '')
		
		embed = discord.Embed(title = 'Results!', description = question_str)
		embed.add_field(name = 'Correct answer:', value = answer_str)
		embed.add_field(name = 'Who got it right:', value = correct_users)
		embed.add_field(name = 'Who got it wrong:', value = incorrect_users)
		embed.add_field(name = 'Cheaters:', value = cheaters)
		await question_embed.delete()
		await ctx.send(embed = embed)



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
