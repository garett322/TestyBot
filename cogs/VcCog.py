import discord
from discord.ext import commands
from discord import ChannelType


class VcCog(commands.Cog, name = "VC Entrance Sound" ):
	def __init__(self, bot):
		self.bot = bot
		states = ['deaf', 'mute', 'self_mute', 'self_deaf', 'self_stream', 'self_video', 'afk']
		discord.opus.load_opus()
		if not discord.opus.is_loaded():
			raise RunTimeError('Opus failed to load')

	@commands.Cog.listener()
	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return

	@commands.Cog.listener()
	async def on_voice_state_update(self, member, before, after):
		if not before.channel and after.channel:
			for r in member.roles:
				if r.name == 'pogrole':
					vc_object = member.voice.channel
					vc_connection = await vc_object.connect()
					audio_source = discord.FFmpegPCMAudio('./vc_sounds/Spruce.mp3')
					start = vc_connection.play(audio_source, after = None)
					while vc_connection.is_playing:
						await asyncio.sleep(1)
					await vc_connection.disconnect()
					return
			return
		else:
			return
	        
	
	@commands.command(name = 'vcstart' )
	async def vcstart(self, ctx):
		if message.channel.name != 'bot-commands-beta':
			return
		
		voice_channel_list = ctx.guild.voice_channels
		for x in voice_channel_list:
			await ctx.send('channel id: {0.id}'.format(x))
			mem = x.members
			for m in mem:
				await ctx.send('members: {0.name}'.format(m))
		return
		
def setup(bot):
	bot.add_cog(VcCog(bot))













#    # grab the user who sent the command
#    user=context.message.author
#    voice_channel=user.voice.voice_channel
#    channel=None
#    # only play music if user is in a voice channel
#    if voice_channel!= None:
#        # grab user's voice channel
#        channel=voice_channel.name
#        await client.say('User is in channel: '+ channel)
#        # create StreamPlayer
#        vc= await client.join_voice_channel(voice_channel)
#        player = vc.create_ffmpeg_player('vuvuzela.mp3', after=lambda: print('done'))
#        player.start()
#        while not player.is_done():
#            await asyncio.sleep(1)
#        # disconnect after the player has finished
#        player.stop()
#        await vc.disconnect()
#    else:
#        await client.say('User is not
        