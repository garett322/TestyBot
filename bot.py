import logging
import discord
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix = ".", intents = intents)

logger = logging.getLogger('discord')
logger.setLevel(logging.WARNING)

handler = logging.StreamHandler()
handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s - LINE %(lineno)d', datefmt='%m/%d/%Y %I:%M:%S %p')
handler.setFormatter(formatter)

logger.addHandler(handler)


@client.event
async def on_ready():
	print('Logged in as {}'.format(client.user))
	user = await client.fetch_user('316384336859627530')
	await user.send('Bot is ready to go!')
	
@client.event
async def on_message(message):
	if message.author is client.user:
		return
	if not message.content.startswith('.'):
		return
	if message.channel.name == 'bot-commands' or message.channel.name == 'bot-commands-beta':
		pass
	else:
		await message.author.send('Please use the bot-commands channel. Thanks!')
		return
	print('{0} used the command: {1}'.format(message.author.name, message.content))
	await client.process_commands(message)

	
#@client.event
#async def on_command_error(ctx, error):
	#logger.warning()
	#return
	



#client.load_extension('cogs.ImageCog')
client.load_extension('cogs.TestCog')
#client.load_extension('cogs.RoleCog')
#client.load_extension('cogs.VcCog')
#client.load_extension('cogs.TrollCog')
#client.load_extension('cogs.GameCog')
#client.load_extension('cogs.CodeCog')
client.load_extension('cogs.TriviaCog')
client.run('Njc2ODk3NDE2NjQwOTg3MTQ3.XkMX2A.vfQROSktnxjkOTP5mWV4Y6eY_Ks')
