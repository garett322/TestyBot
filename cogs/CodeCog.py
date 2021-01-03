import discord
from discord.ext import commands


class CodeCog(commands.Cog, name = "CodeCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'encrypt' )
	async def encrypt(self, ctx, message, key):
		await ctx.delete()
		if not message or not key:
			await ctx.send('You need to include a message to encypt and the encryption key.')
			return
		message = message.lower()
		key = key.lower()
		count = 0
		while len(message) < len(key):
			message += message + message[count]
			count += count + 1
		while len(key) < len(message):
			key += key + key[count]
			count += count + 1
			
		await ctx.send('message: {}, Key: {}'.format(message, key))
		return
def setup(bot):
	bot.add_cog(CodeCog(bot))
