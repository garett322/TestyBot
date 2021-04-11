import discord
from discord.ext import commands
from PIL import Image, ImageFont, ImageDraw
import tempfile
import aiohttp
import shutil


class ImageCog(commands.Cog, name = "Image Manipulator"):
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command(name = 'image')
	async def image(self, ctx, url = 'https://cdn2.vectorstock.com/i/1000x1000/94/06/loser-hand-sign-vector-25169406.jpg', x_coord = 0, y_coord = 0, size = 1, * , text = ':)'):
		if url == None:
			await ctx.send('You need to give me the link to an image you want to use.')
			return
		async with aiohttp.ClientSession() as session:
			async with session.get(url) as resp:
				await ctx.send(resp.status)
		return
	
		"""
		if resp.status == 200:
			pass
		elif resp.status == 400:
			await ctx.send('I couldn\'t find that url. Please try again.')
			return
		else:
			await ctx.send('An unknown error has occurred.')
			return
		
		image_formats = ("image/png", "image/jpeg", "image/jpg")
		if resp.headers['content-type'] not in image_formats:
			await ctx.send('The url you gave is not an image.')
			return
		else:
			filetype = '.' + resp.headers['content-type'].slice(6, 11).strip(';')
		
		original = tempfile.NamedTemporaryFile(suffix = filetype)
		with open(original, 'wb') as f:
			resp.raw.decode_content = True
			shutil.copyfileobj(resp.raw, f)

		im = Image.open(original)
		draw = ImageDraw.Draw(im)
		font = ImageFont.truetype('./fonts/news-cycle.ttf', int(size))
		draw.text((int(x_coord), int(y_coord)), text, font = font, fill = 'black')
		
		edited = tempfile.NamedTemporaryFile(suffix = filetype)
		if filetype == '.jpg':
			filetype = '.jpeg'
		filetype = filetype.strip('.')
		im.save(edited, filetype)
		
		final_file = discord.File(edited.name, filename = 'image.jpg')
		embed = discord.Embed(color = discord.Colour.green())
		embed.set_image(url = 'attachment://image.jpg')
		await ctx.send(file = final_file, embed = embed)
		
		original.close()
		edited.close()
		
		return
		"""
		
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
