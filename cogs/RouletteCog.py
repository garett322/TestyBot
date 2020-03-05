import discord
from discord.ext import commands
import random
from random import choice
import asyncio


class RouletteCog(commands.Cog, name = "RouletteCog" ):
	def __init__(self, bot):
		self.bot = bot

	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
        
	@commands.command(name = 'roulette' )
	async def russian_roulette(self, ctx):
		opponent_id = ctx.message.mentions[0].id
		opponent_user = self.bot.get_user(opponent_id)
		if not opponent_id:
			await ctx.send('Please mention a valid user to challenge:')
		else:
			if opponent_id == ctx.author.id:
				await ctx.send('You cant challenge yourself ' + opponent_user.mention)
			elif opponent_id == self.bot.user.id:
				await ctx.send('You cant challenge me ' + ctx.author.mention + '. Lmao. I would kick your ass anyways.')
			else:
				await ctx.send('Hey ' + opponent_user.mention + ', ' + ctx.author.mention + ' has challenged you to a game of Russian Roulette! Would you like to accept?')
				
				
				def check(author):
					def inner_check(message):
						return author == opponent_user and (message.content.lower() == 'y' or message.content.lower() == 'yes')
					return inner_check
				
				
				try:
					msg = await self.bot.wait_for('message', timeout=15.0, check=check)
				except asyncio.TimeoutError:
					await ctx.send(opponent_user.mention + ' took too long to accept... Game has been cancelled')
				else:
					clip = [i for i in range(6)]
					bullet = choice(clip)
					await ctx.send(ctx.author.mention + ' slides a bullet into the revolver, closes it,  and spins the cylinder. They then hand the revolver to ' + opponent_user.mention)
					
					
					
										     
					def check(author):
						def inner_check(message):
							return author == opponent_user and (message.content == 'shoot')
						return inner_check
										     
					try:
						msg = await self.bot.wait_for('message', timeout=15.0, check=check)
					except asyncio.TimeoutError:
						await ctx.send(opponent_user.mention + ' took too long to pull the trigger. ' + ctx.author.mention + ' picks up the revolver and shoots ' + opponent_user.mention + ' in the foot.')
						await ctx.send(ctx.author.mention + ' Wins!!!')
					else:
						if bullet == 0:
							await ctx.send('BANG! ' + opponent_user.mention + ' looks down and sees blood slowly seeping through the new hole in their foot...')
							await ctx.send(ctx.author.mention + ' Wins!!!')
						else:
							await ctx.send('Click... ' + opponent_user.mention + ' hands the revolver over to ' + ctx.author.mention)
							
							
							def check(author):
								def inner_check(message):
									return author == message.author and (message.content == 'shoot')
								return inner_check
							try:
								msg = await self.bot.wait_for('message', timeout=15.0, check=check)
							except asyncio.TimeoutError:
								await ctx.send(ctx.author.mention + ' took too long to pull the trigger. ' + opponent_user.mention + ' picks up the revolver and shoots ' + ctx.author.mention + ' in the foot.')
								await ctx.send(opponent_user.mention + ' Wins!!!')
							else:
								if bullet == 1:
									await ctx.send('BANG! ' + ctx.author.mention + ' looks down and sees blood slowly seeping through the new hole in their foot...')
									await ctx.send(opponent_user.mention + ' Wins!!!')
								else:
									await ctx.send('Click... ' + ctx.author.mention + ' hands the revolver over to ' + opponent_user.mention)
									
									
									def check(author):
										def inner_check(message):
											return author == opponent_user and (message.content == 'shoot')
										return inner_check
									try:
										msg = await self.bot.wait_for('message', timeout=15.0, check=check)
									except asyncio.TimeoutError:
										await ctx.send(opponent_user.mention + ' took too long to pull the trigger. ' + ctx.author.mention + ' picks up the revolver and shoots ' + opponent_user.mention + ' in the foot.')
										await ctx.send(ctx.author.mention + ' Wins!!!')
									else:
										if bullet == 2:
											await ctx.send('BANG! ' + opponent_user.mention + ' looks down and sees blood slowly seeping through the new hole in their foot...')
											await ctx.send(ctx.author.mention + ' Wins!!!')
										else:
											await ctx.send('Click... ' + opponent_user.mention + ' hands the revolver over to ' + ctx.author.mention)
											
											
											def check(author):
												def inner_check(message):
													return author == message.author and (message.content == 'shoot')
												return inner_check
											try:
												msg = await self.bot.wait_for('message', timeout=15.0, check=check)
											except asyncio.TimeoutError:
												await ctx.send(ctx.author.mention + ' took too long to pull the trigger. ' + opponent_user.mention + ' picks up the revolver and shoots ' + ctx.author.mention + ' in the foot.')
												await ctx.send(opponent_user.mention + ' Wins!!!')
											else:
												if bullet == 3:
													await ctx.send('BANG! ' + ctx.author.mention + ' looks down and sees blood slowly seeping through the new hole in their foot...')
													await ctx.send(opponent_user.mention + ' Wins!!!')
												else:
													await ctx.send('Click... ' + ctx.author.mention + ' hands the revolver over to ' + opponent_user.mention)
													
													def check(author):
														def inner_check(message):
															return author == opponent_user and (message.content == 'shoot')
														return inner_check
													try:
														msg = await self.bot.wait_for('message', timeout=15.0, check=check)
													except asyncio.TimeoutError:
														await ctx.send(opponent_user.mention + ' took too long to pull the trigger. ' + ctx.author.mention + ' picks up the revolver and shoots ' + opponent_user.mention + ' in the foot.')
														await ctx.send(ctx.author.mention + ' Wins!!!')
													else:
														if bullet == 4:
															await ctx.send('BANG! ' + opponent_user.mention + ' looks down and sees blood slowly seeping through the new hole in their foot...')
															await ctx.send(ctx.author.mention + ' Wins!!!')
														else:
															await ctx.send('Click... ' + opponent_user.mention + ' hands the revolver over to ' + ctx.author.mention)
															
															def check(author):
																def inner_check(message):
																	return author == message.author and (message.content == 'shoot')
																return inner_check
															try:
																msg = await self.bot.wait_for('message', timeout=15.0, check=check)
															except asyncio.TimeoutError:
																await ctx.send(ctx.author.mention + ' took too long to pull the trigger. ' + opponent_user.mention + ' picks up the revolver and shoots ' + ctx.author.mention + ' in the foot.')
																await ctx.send(opponent_user.mention + ' Wins!!!')
															else:
																await ctx.send('BANG! ' + ctx.author.mention + ' looks down and sees blood slowly seeping through the new hole in their foot...')
																await ctx.send(opponent_user.mention + ' Wins!!!')
						
						
						
def setup(bot):
	bot.add_cog(RouletteCog(bot))
