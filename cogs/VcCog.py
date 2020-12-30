import discord
from discord.ext import commands
from discord import ChannelType


class VcCog(commands.Cog, name = "VC Entrance Sound" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806' or message.channel.name != 'bot-commands':
			return
	
	@commands.command(name = 'vcstart' )
	async def vcstart(self, ctx):
		voice_channel_list = ctx.guild.voice_channels
		for x in voice_channel_list:
			await ctx.send(x)
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
        