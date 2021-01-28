import discord
from discord.ext import commands


class SkeletonCog(commands.Cog, name = "SkeletonCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'example' )
	async def example(self, ctx):
		return
      
        

def setup(bot):
	bot.add_cog(SkeletonCog(bot))
