import discord
from discord.ext import commands
import aiohttp



class COG_NAME_MUST_CHANGE(commands.Cog, name = "COG_NAME_MUST_CHANGE" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'COMMAND_NAME_MUST_CHANGE' )
	async def example(self, ctx):
		return
      
        

def setup(bot):
	bot.add_cog(COG_NAME_MUST_CHANGE(bot))
