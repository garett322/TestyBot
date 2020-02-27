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
		opponent_id = ctx.mentions[0].id
		oponnent_user = self.bot.get_user(oponnent_id)
		if (!opponent_user):
			await ctx.send('Please mention the person you want to challenge:')
		else:
			await ctx.send(opponent_user.mention + ' Roulette Works!')
			#try:
			#msg = await self.bot.wait_for('message', timeout=15.0)
			#except asyncio.TimeoutError:
			#await ctx.send('You took too long... Game has been cancelled')
			#else:
			#await ctx.send('You said {0.content}, {0.author}.'.format(msg))
			
                           
def setup(bot):
    bot.add_cog(RouletteCog(bot))
