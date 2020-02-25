import discord
from discord.ext import commands
import random


class RouletteCog(commands.Cog, name = "RouletteCog" ):
    def __init__(self, bot):
        self.bot = bot

    async def on_message(self, message):
        if message.author == 'Test Bot#0806':
            return


def setup(bot):
    bot.add_cog(RouletteCog(bot))