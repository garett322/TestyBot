import discord
from discord.ext import commands
from discord import ChannelType


class VcCog(commands.Cog, name = "VC Entrance Sound" ):
	def __init__(self, bot):
		self.bot = bot
		states = ['deaf', 'mute', 'self_mute', 'self_deaf', 'self_stream', 'self_video', 'afk']

	async def on_message(self, message):
		if message.author == 'Test Bot#0806' or message.channel.name != 'bot-commands':
			return


	async def on_voice_state_update(member, before, after):
		#if before is None and after is not None:
		for r in member.roles:
			if r == 'pogrole':
				print('POG POG')
		return
	#	else:
	#		return
				
	        
	
	@commands.command(name = 'vcstart' )
	async def vcstart(self, ctx):
		voice_channel_list = ctx.guild.voice_channels
		for x in voice_channel_list:
			await ctx.send('channel id: {0.id}'.format(x))
			mem = x.members
			for m in mem:
				await ctx.send('members: {0.name}'.format(m))
		return
		
def setup(bot):
	bot.add_cog(VcCog(bot))













# @client.command(
#    name='vuvuzela',
#    description='Plays an awful vuvuzela in the voice channel',
#    pass_context=True,
#)
#async def vuvuzela(context):
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
        