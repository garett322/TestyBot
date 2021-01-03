import discord
from discord.ext import commands
from discord import ChannelType
import asyncio


class VcCog(commands.Cog, name = "VC Entrance Sound" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		if not before.channel and after.channel:
			for r in member.roles:
				
				vc_roles = {'MoFo': './vc_sounds/fuckfuck.mp3',
						'Best RL Player': './vc_sounds/goldstar.mp3',
						'Spoopy Bois': './vc_sounds/heresjohnny.mp3',
						'Kitten': './vc_sounds/meow.mp3',
						'Einstein Gang': './vc_sounds/einstein.mp3',
						'Sage\'s Hoes': './vc_sounds/hoes.mp3',
						'Big Dick Energy': './vc_sounds/suck_a_dick.mp3'
						}
				
				if r.name in vc_roles:
					sound = vc_roles[r.name]
					vc_object = member.voice.channel
					vc_connection = await vc_object.connect()
					audio_source = discord.FFmpegPCMAudio(sound)
					await asyncio.sleep(2)
					start = vc_connection.play(audio_source, after = None)
					await asyncio.sleep(10)
					stop = vc_connection.stop()
					await vc_connection.disconnect()
					return
			return
		else:
			return
def setup(bot):
	bot.add_cog(VcCog(bot))