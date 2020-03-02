import discord
from discord.ext import commands
import random
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
				
				def check(m):
					return m.content.lower() == 'y' or m.content.lower() == 'yes'
				
				try:
					msg = await self.bot.wait_for('message', timeout=15.0, check=check)
				except asyncio.TimeoutError:
					await ctx.send('You took too long to accept... Game has been cancelled')
				else:
					await ctx.send('You said {.content}, {.author}.'.format(msg))

					
					
			
                           
def setup(bot):
	bot.add_cog(RouletteCog(bot))
