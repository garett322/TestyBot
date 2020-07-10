import discord
from discord.ext import commands
client = commands.Bot(command_prefix = ".", selfbot = 'false')

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	
@client.event
async def on_message(message):
	if (message.channel.id == 676897947731886085) or (message.guild is None):
        	pass
	else:
		if message.content.startswith('.'):
			await message.author.send('Please use the bot-commands channel. Thanks!')
			return
		else:
			return
	await client.process_commands(message)

	
@client.event
async def on_command_error(error, ctx):
	await ctx.send('There was a fatal error. Please make sure you used the command properly and try again.')
	return
	
	

client.load_extension('cogs.TestCog')
client.load_extension('cogs.RouletteCog')
client.load_extension('cogs.TornCog')
client.load_extension('cogs.NewCog')

client.run('Njc2ODk3NDE2NjQwOTg3MTQ3.XknFVQ.gZPzOHRgqOMCNkePNIpAP2iRvDk')
