import discord
from discord.ext import commands
client = commands.Bot(command_prefix = ".", selfbot = 'false')

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	
@client.event
async def on_message(message):
	if message.channel.type is discord.ChannelType.private:
		await ctx.send('dope')
		pass
	else:
		if (message.channel.name == 'bot-commands') or (message.guild is None) or (message.channel.name == 'bot-commands-beta'):
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
	
	
client.load_extension('cogs.MoveCog')
client.load_extension('cogs.TestCog')
#client.load_extension('cogs.RouletteCog')
#client.load_extension('cogs.GamblingCog')
client.load_extension('cogs.RoleCog')
#client.load_extension('cogs.NewCog')
client.load_extension('cogs.VcCog')

client.run('Njc2ODk3NDE2NjQwOTg3MTQ3.XkMX2A.vfQROSktnxjkOTP5mWV4Y6eY_Ks')
