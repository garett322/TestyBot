import logging
import discord
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix = ".", intents = intents)



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



#client.load_extension('cogs.ImageCog')
client.load_extension('cogs.TestCog')
#client.load_extension('cogs.RoleCog')
#client.load_extension('cogs.VcCog')
client.load_extension('cogs.ErrorCog')
client.load_extension('cogs.TriviaCog')

client.run('Njc2ODk3NDE2NjQwOTg3MTQ3.XkMX2A.vfQROSktnxjkOTP5mWV4Y6eY_Ks')
