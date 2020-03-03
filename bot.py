import discord
from discord.ext import commands
client = commands.Bot(command_prefix = ".", selfbot = 'false')

@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))
	
@client.event
async def on_message(message):
	if (message.channel.id == 676897947731886085):
        	pass
	else:
		await message.author.send('Please use the bot-commands channel. Thanks!')
		return
	await client.process_commands(message)
	
client.load_extension('cogs.TestCog')
client.load_extension('cogs.RouletteCog')

client.run('Njc2ODk3NDE2NjQwOTg3MTQ3.XknFVQ.gZPzOHRgqOMCNkePNIpAP2iRvDk')
