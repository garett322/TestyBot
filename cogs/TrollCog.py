import discord
from discord.ext import commands
import random


class TrollCog(commands.Cog, name = "TrollCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'troll' )
	async def troll(self, ctx, member):
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
				msg = await client.wait_for('message', check=check(context.author), timeout=10)
			except asyncio.TimeoutError:
				await ctx.send('No answer eh? In the future, don\'t waste my fuckin time.')
				return
			if msg.content.lower() == 'y' or msg.conent.lower() == 'yes':
				await ctx.send('LIAR. YOU\'RE NOT A TREE AND YOU KNOW IT. GUARDS, ARREST {} FOR IMPERSONATING A TREE.'.format(msg.author))
				return
			elif msg.content.lower() == 'n' or msg.content.lower() == 'no':
				await ctx.send('That\'s what I thought.')
				return


		for user in ctx.guild.members:
			if user.name.startswith(member):
				await ctx.author.send('Do you want to troll {}?'.format(user.name))
				
				def check(author):
					def inner_check(message):
						if message.author == author and message.content.lower() == "y":
							return True
						else:
							return False
					return inner_check
				
				try:
					msg = await client.wait_for('message', check=check(context.author), timeout=10)
				except asyncio.TimeoutError:
					await ctx.send('Troll cancelled.')
					return
				num = random.randint(1, 10)
				sound = './trollsounds/{}.mp3'.format(num)
				vc_object = target.voice.channel
				vc_connection = await vc_object.connect()
				audio_source = discord.FFmpegPCMAudio(sound)
				await asyncio.sleep(2)
				start = vc_connection.play(audio_source, after = None)
				await asyncio.sleep(10)
				stop = vc_connection.stop()
				await vc_connection.disconnect()
				return

def setup(bot):
	bot.add_cog(TrollCog(bot))
