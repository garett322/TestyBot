import discord
from discord.ext import commands


class TestCog(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def testy(self, ctx):
		await ctx.send('It Works!')
		return
	
	@commands.command()
	async def avatar(self, ctx, *, member):
		for user in ctx.guild.members:
			if user.id == 684444511861997680:
				continue
			if user.name.lower().startswith(member.lower()):
				pfp = user.avatar_url
				await ctx.send(pfp)
				return
		return

def setup(bot):
	bot.add_cog(TestCog(bot))