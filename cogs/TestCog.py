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
	async def avatar(self, ctx, *,  avamember : discord.Member=None):
		userAvatarUrl = avamember.avatar_url
		await ctx.send(userAvatarUrl)
		return
		

		
def setup(bot):
	bot.add_cog(TestCog(bot))