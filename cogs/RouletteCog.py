import discord
from discord.ext import commands
import random


class RouletteCog(commands.Cog, name = "RouletteCog" ):
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author == 'Test Bot#0806':
            return
        
    @commands.command(name = 'roulette' )
    async def russian_roulette(self, ctx):
        try:
    	    msg = await commands.wait_for('message', check=pred, timeout=60.0)
        except asyncio.TimeoutError:
            await ctx.send('You took too long...')
        else:
            await ctx.send('You said {0.content}, {0.author}.'.format(msg))



def setup(bot):
    bot.add_cog(RouletteCog(bot))
