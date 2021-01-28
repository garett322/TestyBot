import linecache
import sys
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

	
@client.event
async def on_command_error(ctx,error):
	exc_type, exc_obj, tb = sys.exc_info()
	f = tb.tb_frame
	lineno = tb.tb_lineno
	filename = f.f_code.co_filename
	linecache.checkcache(filename)
	line = linecache.getline(filename, lineno, f.f_globals)
	print('ERROR IN {}, LINE {} "{}": {}'.format(filename, lineno, line.strip(), exc_obj))
	for channel in ctx.guild.channels:
		if channel.name == 'errors':
			await channel.send('ERROR IN {}, LINE {} "{}": {}'.format(filename, lineno, line.strip(), exc_ob))
	if isinstance(error, commands.CommandNotFound):
		await ctx.send('Command not found.')
	else:
		await ctx.send('Unknown error encountered. Check logs or try again.')
	return


#client.load_extension('cogs.ImageCog')
client.load_extension('cogs.TestCog')
#client.load_extension('cogs.RoleCog')
#client.load_extension('cogs.VcCog')
#client.load_extension('cogs.TrollCog')
#client.load_extension('cogs.GameCog')
#client.load_extension('cogs.CodeCog')
client.load_extension('cogs.TriviaCog')
client.run('Njc2ODk3NDE2NjQwOTg3MTQ3.XkMX2A.vfQROSktnxjkOTP5mWV4Y6eY_Ks')
