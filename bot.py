import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ".", selfbot = 'false')

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

client.load_extension('cogs.TestCog')
client.load_extension('cogs.RouletteCog')


client.run('Njc2ODk3NDE2NjQwOTg3MTQ3.XknFVQ.gZPzOHRgqOMCNkePNIpAP2iRvDk')