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
		if not opponent_user:
			await ctx.send('Please mention a valid user to challenge:')
		else:
			if opponent_id == ctx.author.id:
				await ctx.send('You cant challenge yourself ' + opponent_user.mention)
			elif opponent_id == 'Test Bot#0806':
				await ctx.send('You cant challenge me ' + opponent_user.mention + '. Lmao. I would kick your ass anyways.')
			else:
				await ctx.send('Hey ' + opponent_user.mention + ', ' + ctx.author.mention + ' has challenged you to a game of Russian Roulette! Would you like to accept?')
				try:
					msg = await self.bot.wait_for('message', timeout=15.0)
				except asyncio.TimeoutError:
					await ctx.send('You took too long... Game has been cancelled')
				else:
					if 0.content.lower() == 'y' or 0.content.lower() == 'yes':
						await ctx.send('You said {0.content}, {0.author}.'.format(msg))
					else:
						await ctx.send("Mission failed. We'll get 'em next time")

					
					
			
                           
def setup(bot):
	bot.add_cog(RouletteCog(bot))
