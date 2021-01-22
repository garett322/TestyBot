import discord
from discord.ext import commands
import PIL
from PIL import Image, ImageFont, ImageDraw
import tempfile
import urllib2
from urllib.parse import urlparse
import requests
import shutil


class ImageCog(commands.Cog, name = "ImageCog"):
	def __init__(self, bot):
		self.bot = bot
		
	@ commands.command(name = 'image')
	async def image(self, ctx, url, x_coord, y_coord, size = 100, * , text):
		try:
			urllib2.urlopen(url)
		except urllib2.HTTPError:
			await ctx.send('I couldn\'t find that url. Please try again.')
		except urllib2.URLError:
			await ctx.send('I couldn\'t find that url. Please try again.')
		file = requests.get(url)
		parsed_url = urlparse(url)
		filename = parsed_url.rsplit('/')[-1]
		filetype = filename.rsplit('.')[-1]
		original = tempfile.NamedTemporaryFile(suffix = '.{}'.format(filetype))
		with open(original, 'wb') as f:
			shutil.copyfileobj(file.raw, f)
		im = Image.open(original)
		draw = ImageDraw.Draw(im)
		font = ImageFont.truetype('./fonts/news-cycle.ttf', int(size))
		draw.text((int(x_coord), int(y_coord)), text, font = font, fill = 'black')
		if filetype.lower() == 'jpg':
			edited = tempfile.NamedTemporaryFile(suffix = '.jpg')
			im.save(edited, 'JPEG')
		elif filetype.lower() == 'png'
			edited = tempfile.NamedTemporaryFile(suffix = '.png')
			im.save(edited, 'PNG')
		else:
			await ctx.send('I don\'t recognize that file type. Please try a different picture.')
			return
		file = discord.File(edited.name, filename = 'image.jpg')
		embed = discord.Embed(color = discord.Colour.green())
		embed.set_image(url = 'attachment://image.jpg')
		await ctx.send(file = file, embed = embed)
		original.close()
		edited.close()
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
