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
	async def avatar(self, ctx):
		mentions = ctx.message.mentions[0]
		await ctx.send(mentions)
		await ctx.send (mentions.avatar)
		await ctx.send (mentions.avatar_url)
		

		
def setup(bot):
	bot.add_cog(TestCog(bot))