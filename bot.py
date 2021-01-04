import discord
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix = ".", intents = intents)

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	user = await client.fetch_user('316384336859627530')
	await user.send('Bot is ready to go!')
	
@client.event
async def on_message(message):
	if message.author is client.user:
		return
	if message.channel.type is discord.ChannelType.private:
		pass
	elif message.channel.type is discord.ChannelType.text:
		if message.channel.name == 'bot-commands' or message.channel.name == 'bot-commands-beta':
			pass
		else:
			if message.content.startswith('.'):
				await message.author.send('Please use the bot-commands channel. Thanks!')
				return
			else:
				return
	await client.process_commands(message)

	
@client.event
async def on_command_error(ctx, error):
	await ctx.send('We encountered a fatal error. Please check the command you entered and try again.')
	print(' ')
	print(error)
	return


client.load_extension('cogs.BetaCog')
client.load_extension('cogs.CodeCog')
client.load_extension('cogs.TestCog')
client.load_extension('cogs.RoleCog')
client.load_extension('cogs.VcCog')
client.load_extension('cogs.TrollCog')
#client.load_extension('cogs.MuteCog')
client.load_extension('cogs.GameCog')

client.run('Njc2ODk3NDE2NjQwOTg3MTQ3.XkMX2A.vfQROSktnxjkOTP5mWV4Y6eY_Ks')
