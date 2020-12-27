import discord
from discord.ext import commands


class HelpCog(commands.Cog, name = "HelpCog" ):
	def __init__(self, bot):
		self.bot = bot


	async def on_message(self, message):
		if message.author == 'Test Bot#0806':
			return
	
	@commands.command(name = 'shucks' )
	async def h(self, ctx, args):
		
		Help_List = {
			'role': '.role is for creating and deleting custom roles. Use ".role create (role name) (role color)" to create a custom role. To see the list of available colors use ".help colors". Use ".role delete" to delete your current custom role.',
			'help': '.help is the help command. Use ".help (command)" to see how to use that command.'
		}
		if args in Help_List:
			await ctx.send(Help_List[args])
			return
		else:
			await ctx.send('There is no help for that command because that command doesn\'t exist.')
			return
		

def setup(bot):
	bot.add_cog(HelpCog(bot))
