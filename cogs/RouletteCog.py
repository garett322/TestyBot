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
        await ctx.send('Please mention the person you want to challenge:')
        try:
            msg = await self.bot.wait_for('message', timeout=10.0)
        except asyncio.TimeoutError:
            await ctx.send('You took too long... Game has been cancelled')
        else:
            #await ctx.send('You said {0.content}, {0.author}.'.format(msg))
            await ctx.send('You cant respond to this command right now.'.format(ctx.message.author.mention())
def setup(bot):
    bot.add_cog(RouletteCog(bot))
