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
	async def avatar(self, ctx):
		for user in ctx.guild.members:
			if user.id == 684444511861997680 or not user.voice:
				continue
			if user.name.lower().startswith(member.lower()):
				pfp = user.avatar_url
				embed = discord.Embed(title="test", description='test', color=0xecce8b)
				embed.set_image(url=(pfp))
				await ctx.send(embed)
				return
		return

def setup(bot):
	bot.add_cog(TestCog(bot))