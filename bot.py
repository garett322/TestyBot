import os
import discord
from discord.ext import commands
intents = discord.Intents.all()
client = commands.Bot(command_prefix = ".", intents = intents)



@client.event
async def on_ready():
	print('Logged in as {}'.format(client.user))
	with open('BOT_TOKEN.txt','r') as file:
    		bot_token = " ".join(line.rstrip() for line in file)
    		
	
	
@client.event
async def on_message(message):
	if message.author is client.user:
		return
	elif not message.content.startswith('.'):
		return
	elif message.channel.name == 'bot-commands':
		pass
	else:
		return
	print('{0} used the command: {1}'.format(message.author.name, message.content))
	await client.process_commands(message)



client.load_extension('cogs.TestCog')
client.load_extension('cogs.ErrorCog')
client.load_extension('cogs.UnloadCog')

client.run(bot_token)
