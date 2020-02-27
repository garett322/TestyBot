import discord
from discord.ext import commands


class TestCog(commands.Cog, name = "TestCog" ):
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author == 'Test Bot#0806':
            return

    @commands.command(name = 'test' )
    async def testy(self, ctx):
    	await ctx.send('It Works!'.format(ctx.message.author.mention())

def setup(bot):
    bot.add_cog(TestCog(bot))
