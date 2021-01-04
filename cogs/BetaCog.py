import discord
from discord.ext import commands


			
			
class BetaCog(commands.Cog, name = "BetaCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'userchk' )
	async def userchk(self, ctx, target):
		
		def TargetCheck(target):
			try:
				user = commands.converter.MemberConverter().convert(target)
				return user
			except:
				try:
					role = commands.converter.MemberConverter().convert(target)
					return role
				except:
					return False
			
		target_result = TargetCheck(target)
		if target_result == False:
			await ctx.send('No role or user found.')
			return
		for user in ctx.guild.members:
			if user == target_result:
				await ctx.send('User verified: {}'.format(target_result))
				return
		else:
			for role in ctx.guild.roles:
				if role == target_result:
					await crx.send('Role verified: {}'.format(target_result))
					return
			else:
				await ctx.send('Something fucked up. I have no clue what tho.')
				return


	@commands.command(name = 'botrole' )
	async def botrole(self, ctx):
		for role in ctx.guild.roles:
			if role in self.bot.user.roles:
				continue
			else:
				await self.bot.user.add_roles(role)
				await ctx.author.send('{} role has been added.'.format(role))
		return



def setup(bot):
	bot.add_cog(BetaCog(bot))
