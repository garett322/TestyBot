import discord
from discord.ext import commands
import random
import asyncio


class TrollCog(commands.Cog, name = "TrollCog" ):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name = 'troll' )
	async def troll(self, ctx, *, member):
		if ctx.author.id != 316384336859627530:
			await ctx.send('Only trees can use this command. Are you a tree? y/n:')
			
			def check(author):
				def inner_check(message): 
					if message.author == author:
						return True
					else:
						return False
				return inner_check
				
			try:
				msg = await self.bot.wait_for('message', check=check(context.author), timeout=10)
			except asyncio.TimeoutError:
				await ctx.send('No answer eh? In the future, don\'t waste my fuckin time.')
				return
			if msg.content.lower() == 'y' or msg.conent.lower() == 'yes':
				await ctx.send('LIAR. YOU\'RE NOT A TREE AND YOU KNOW IT. GUARDS, ARREST {} FOR IMPERSONATING A TREE.'.format(msg.author))
				return
			elif msg.content.lower() == 'n' or msg.content.lower() == 'no':
				await ctx.send('That\'s what I thought.')
				return

		await ctx.message.delete()
		for user in ctx.guild.members:
			if user.id == 684444511861997680 or not user.voice:
				continue
			if user.name.lower().startswith(member.lower()):
				await ctx.author.send('Do you want to troll {}?'.format(user.name))
				
				def check(author):
					def inner_check(message):
						if message.author == author:
							if message.content.lower() == "y":
								if message.channel.type is discord.ChannelType.private:
									return True
								else:
									return False
							else:
								return False
						else:
							return False
					return inner_check
				
				try:
					msg = await self.bot.wait_for('message', check=check(ctx.author), timeout=10)
				except asyncio.TimeoutError:
					await ctx.send('Troll cancelled.')
					return
				
				num = random.randint(1, 10)
				sound = './trollsounds/{}.mp3'.format(num)
				vc_object = user.voice.channel
				vc_connection = await vc_object.connect()
				audio_source = discord.FFmpegPCMAudio(sound)
				await asyncio.sleep(2)
				start = vc_connection.play(audio_source, after = None)
				await asyncio.sleep(10)
				stop = vc_connection.stop()
				await vc_connection.disconnect()
				return
		await ctx.author.send('No user found.')
		return
	
	
	@commands.command(name = 'rekt' )
	async def rekt(self, ctx):
		await ctx.send('It\'s still not a command Sage. Get fuckin rekt.')

	@commands.command(name = 'epic' )
	async def epic(self, ctx):
		if ctx.author.name == 'Spruce#7339':
			sage = ctx.message.server.get_member("464988691950075914")
			sage.edit(mute=True, deafen = True)
			return

def setup(bot):
	bot.add_cog(TrollCog(bot))
	
	
	if member.id == "464988691950075914":
			counter = 0
			while counter < 10:
