import discord
from discord.ext import commands
import asyncio


class TestCog(commands.Cog, name = 'Test Commands'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'test', description = 'A test command to check if the bot is running.')
	async def test(self, ctx):
		await ctx.send('Bot is up and running!')
		return
	
	@commands.command(name = 'avatar', description = 'A command to get a user\'s avatar.')
	async def avatar(self, ctx, *, member):
		for user in ctx.guild.members:
			if user.name.lower().startswith(member.lower()):
				pfp = user.avatar_url
				embed = discord.Embed(title=f'{user.name}\'s avatar')
				embed.set_image(url=(pfp))
				await ctx.send(embed = embed)
				return
		else:
			await ctx.send('No user found.')
			return
		
		
def setup(bot):
	bot.add_cog(TestCog(bot))