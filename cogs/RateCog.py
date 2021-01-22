import discord
from discord.ext import commands
import random


class RateCog(commands.Cog, name = "RateCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'rank', description = 'Check to see somebody\'s REAL Rocket League rank.')
	async def rank(self, ctx, member = ctx.author.name):
		letter_vals = {'a': 84,
		'b': 28,
		'c': 60,
		'd': 4,
		'e': 64,
		'f': 40,
		'g': 32,
		'h': 88,
		'i': 20,
		'j': 24,
		'k': 52,
		'l': 72,
		'm'; 16,
		'n': 56,
		'o': 92,
		'p': 8,
		'q': 100,
		'r': 36,
		's': 44,
		't': 80,
		'u': 12,
		'v': 0,
		'w': 96,
		'x': 48,
		'y': 68,
		'z': 76
		}
		def rank_chk(name):
			rank_num = 0
			for i in name:
				if i in letter_vals:
					rank_num = rank_num + letter_vals[i]
				else:
					rank_num = rank_num + 50
			rank_num = rank_num / len(name)
			return rank_num
		
		rank_num = rank_chk(member)
		if rank_num >= 0 and rank_num < 13:
			rank = 'Bronze'
			if rank_num >= 0 and < 4:
				div = '1'
			elif rank_num >= 4 and < 8:
				div = '2'
			elif rank_num >= 8 and < 13:
				div = '3'
		elif rank_num >= 13 and rank_num < 25:
			rank = 'Silver'
			if rank_num >= 13 and < 17:
				div = '1'
			elif rank_num >= 17 and < 21:
				div = '2'
			elif rank_num >= 21 and < 25:
				div = '3'
		elif rank_num >= 25 and rank_num < 38:
			rank = 'Gold'
			if rank_num >= 25 and < 29:
					div = '1'
			elif rank_num >= 29 and < 33:
				div = '2'
			elif rank_num >= 33 and < 38:
				div = '3'
		elif rank_num >= 38 and rank_num < 50:
			rank = 'Platinum'
			if rank_num >= 38 and < 42:
				div = '1'
			elif rank_num >= 42 and < 46:
				div = '2'
			elif rank_num >= 46 and < 50:
				div = '3'
		elif rank_num >= 50 and rank_num < 63:
			rank = 'Diamond'
			if rank_num >= 50 and < 54:
				div = '1'
			elif rank_num >= 54 and < 58:
				div = '2'
			elif rank_num >= 58 and < 63:
				div = '3'
		elif rank_num >= 63 and rank_num < 75:
			rank = 'Champ'
			if rank_num >= 63 and < 67:
				div = '1'
			elif rank_num >= 67 and < 71:
				div = '2'
			elif rank_num >= 71 and < 75:
				div = '3'
		elif rank_num >= 75 and rank_num < 88:
			rank = 'Grand Champion'
			if rank_num >= 75 and < 79:
				div = '1'
			elif rank_num >= 79 and < 83:
				div = '2'
			elif rank_num >= 83 and < 88:
				div = '3'
		elif rank_num >= 88 and rank_num <= 100:
			rank = 'Supersonic Legend'
			if rank_num >= 88 and < 92:
				div = '1'
			elif rank_num >= 92 and < 96:
				div = '2'
			elif rank_num >= 96 and <= 100:
				div = '3'
			
		rank_gen = random.randint(1, 3)
		embed = discord.Embed(title = 'Rank Revealer', color = discord.coulour.dark_red()))
		embed.add_field(value = '{0} is a {1} {2}'.format{member, rank, div})
		await ctx.send(embed = embed)
		return
def setup(bot):
	bot.add_cog(RankCog(bot))
