import discord
from discord.ext import commands
import PIL
from PIL import Image, ImageFont, ImageDraw
import tempfile

class ImageCog(commands.Cog, name = "ImageCog" ):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'image' )
	async def image(self, ctx, x, y, size, *, text):
		im = Image.open("./images/BreakingNews.jpg")
		draw = ImageDraw.Draw(im)
		font = ImageFont.truetype('./fonts/news-cycle.ttf', size)
		draw.text((x, y), text, font=font, fill='black')
		temp_jpg = tempfile.NamedTemporaryFile(suffix='.jpg')
		im.save(temp_jpg, 'JPEG')
		file = discord.File(temp_jpg.name, filename = 'image.jpg')
		embed = discord.Embed(title = 'test', color = discord.Colour.red())
		embed.set_image(url='attachment://image.jpg')
		await ctx.send(file=file, embed=embed)
		temp_jpg.close()
		return
		
		
		#Channel=ctx.message.channel
		#logs = await client.logs_from(Channel, limit=20)
		#async for msg in logs:
			#if msg.author == ctx.message.mentions[0]:
				#msg_text = msg.content
				#break
		#else:
			#await ctx.send('No messages found from that user.')
		



def setup(bot):
	bot.add_cog(ImageCog(bot))
