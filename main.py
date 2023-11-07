import os
import re				#import the regular expressions library
from datetime import datetime
import requests			#import string parser
import asyncio		#asynchronous concurrency
import discord          #import discord lib
from dotenv import load_dotenv
import DannyVuonglab1q5 #import from my custom lib
#import math				#import math methods
from bs4 import BeautifulSoup	#import string parser
import subprocess
import ak_operators
#parserny = DannyVuonglab1q5.soupny()

load_dotenv()
token = os.getenv('SOUPER_DISCORD_TOKEN')	#Load the discord token value from the .env file
guild = os.getenv('SOUPER_DISCORD_GUILD')	#Load the guild name from the .env file
admin_id = int(os.getenv('ADMIN_USER_ID'))

intents = discord.Intents.default()
intents.typing = False
intents.presences = False

client = discord.Client(intents=intents)

# schedule to send list of ak chars every monday at 10:00
async def schedule_ak_chars():
	await client.wait_until_ready()		#wait until the bot is fully initialized before continuing

	channel = client.get_channel(915077470280122388)	#Right click text channel and select "Copy Channel ID"
	try:
		while not client.is_closed():
			current_time = datetime.now()
			if current_time.weekday() == 0 and current_time.hour == 10 and current_time.minute == 0:
				await channel.send("**Automated Task** Scheduled for Monday 10:00 EST, executed on `" + str(datetime.now().strftime("%Y%m%d-%H:%M:%S")) + "`")
				await channel.send("> Fetching data...")
				ak_operators.get_data()		# Fetches, scrapes, and parses the data from an online blog
				await channel.send(file=discord.File(r'/home/ubuntu/Documents/souperbeautiful/ak.txt'))
				await channel.send("Upload complete! Click Expand to see more (mobile support coming soon)")
	
				# clear the file
				with open('/home/ubuntu/Documents/souperbeautiful/ak.txt', 'w+') as tempfile:
					tempfile.write('')
			await asyncio.sleep(60)
	except Exception as e:
		try:
			await channel.send(f"**Exception caught in `schedule_ak_chars()`**\n```{e}```")
		finally:
			print(f"Exception caught in schedule_ak_chars()\n{e}")

'''
async def news_hna(channel):
	await client.wait_until_ready()
	await channel.send("Hikari no Akari OST 音楽 [HNA Updates]")
	article = 1		#start counter at 1
	url = 'https://hikarinoakari.com/'      #domain https://hikarinoakariost.info deprecated? Anyways, using new domain

	r = requests.get(url)	#get method to get url
	r_html = r.text		    #convert html into text

	soup = BeautifulSoup(r_html)	#parser to parse all the text

	for title in soup.find_all('h3'):		#print out all the strings starting with the h3 tag
		try:
			await channel.send(str(article) + ") [song] " + "**" + title.find('a').text + "**")	#print the article count number followed by the name of the headline
			#print(article)
		except AttributeError:
			print("ERROR: AttributeError")
			break
		article += 1		#increment counter by 1 for every loop
		if article == 16:
			article = 1
			break
	await channel.send("Those are the top releases for today! Find more at " + "<" + url + ">")

async def schedule_news_hna():
	await client.wait_until_ready()

	channel = client.get_channel(652711785023143936)
	try:
		while not client.is_closed():
			current_time = datetime.now()
			if (current_time.weekday() == 0 and current_time.hour == 10 and current_time.minute == 1) \
			or (current_time.weekday() == 2 and current_time.hour == 10 and current_time.minute == 1) \
			or (current_time.weekday() == 4 and current_time.hour == 13 and current_time.minute == 11):
				try:
					await news_hna(channel)
				except Exception as e:
					print(f"Exception caught within news_hna()\n{e}")
					channel.send("Exception caught within news_hna()\n```" + str(e) + "```")
			await asyncio.sleep(60)
	except Exception as e:
		print(f"Exception caught in schedule_news_hna()\n{e}")
		await channel.send("Exception caught in schedule_news_hna()\n```" + str(e) + "```")
'''
			

@client.event
async def on_ready():	#The following scripts in on_ready() will only run everytime the bot comes online
	for guild in client.guilds:
			if guild.name == guild:
				break

	#GUILD = discord.utils.get(client.guilds, name=guild)
	print("[debug] Souperbeautiful started at system time " + (str(datetime.now().strftime("%Y%m%d-%H:%M:%S")) + ". All systems go!!\n(Press CTRL + C to terminate script at any time. There will be a delay before bot logs off."))
	#print("{client.user} is online in {guild.name} (id: {guild.id}) at system time " + str(datetime.now()) + ".")
	#print(GUILD)
	#members = '\n - '.join([member.name for member in guild.members])
	#print(f'Guild Members:\n - {members}')

	print("[debug] Initializing loops...")
	client.loop.create_task(schedule_ak_chars())	#init ak loop task
	#client.loop.create_task(schedule_news_hna())	#init hna loop task

	print("[debug] Updating activity name...")
	await client.change_presence(activity=discord.Game(name='instead of working'))

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif message.content == ("!soup news-ny"):
		await message.channel.send("News Articles ニュース記事 [New York Times]")
		article = 1		#start counter at 1
		url = 'https://www.nytimes.com/ca/'

		r = requests.get(url)	#get method to get url
		r_html = r.text		    #convert html into text

		soup = BeautifulSoup(r_html)	#parser to parse all the text

		for title in soup.find_all('article'):		#print out all the strings starting with the h2 tag
			try:
				await message.channel.send(str(article) + "........[article] " + "**" + title.find('h1').text + "**")	#print the article count number followed by the name of the headline
				#print(article)
			except AttributeError:
				print("ERROR: AttributeError")
				break
			article += 1		#increment counter by 1 for every loop
			if article == 16:
				article = 1
				break
		await message.channel.send("These are the top headlines for today! Find them at "+ "<" + url + ">")

	elif message.content == ("!soup news-tom"):
		await message.channel.send("News Articles ニュース記事 [Tom's Hardware")
		article = 1		#start counter at 1
		url = 'https://www.tomshardware.com/'

		r = requests.get(url)	#get method to get url
		r_html = r.text		    #convert html into text

		soup = BeautifulSoup(r_html)	#parser to parse all the text

		for title in soup.find_all('figcaption'):		#print out all the strings referenced by article-name class
			try:
				await message.channel.send(str(article) + "........[article] "  + "**" + title.find(class_="article-name").text + "**" )	#print the article count number followed by the name of the headline
				#print(article)
			except AttributeError:
				print("ERROR: AttributeError")
				break
			article += 1		#increment counter by 1 for every loop
			if article == 16:
				article = 1
				break
		await message.channel.send("Those are the top headlines for today! Find more at " + "<" + url + ">")

	elif message.content == ("!soup news-hna"):
		await message.channel.send("Hikari no Akari OST 音楽 [HNA Updates]")
		article = 1		#start counter at 1
		url = 'https://hikarinoakari.com/'      #domain https://hikarinoakariost.info deprecated? Anyways, using new domain

		r = requests.get(url)	#get method to get url
		r_html = r.text		    #convert html into text

		soup = BeautifulSoup(r_html)	#parser to parse all the text

		for title in soup.find_all('h3'):		#print out all the strings starting with the h3 tag
			try:
				await message.channel.send(str(article) + "........[song] " + "**" + title.find('a').text + "**")	#print the article count number followed by the name of the headline
				#print(article)
			except AttributeError:
				print("ERROR: AttributeError")
				break
			article += 1		#increment counter by 1 for every loop
			if article == 16:
				article = 1
				break
		await message.channel.send("Those are the top releases for today! Find more at " + "<" + url + ">")

	elif message.content == ("!soup hello"):
		await message.channel.send("Hello, souper!")

	#elif message.content == ("ayy"):
	#	await message.channel.send("lmao")

	#elif message.content == ("lmao"):
	#	await message.channel.send("ayy")

	elif message.content == ("!soup eat") and message.author.id == admin_id:
		await message.channel.send("Bye bye! じゃあまたね~")
		await asyncio.sleep(1)
		await message.channel.send("> **Shutting down...**")
		await asyncio.sleep(3)
		await client.close()

	elif message.content == ("!soup eat") and not message.author.id == admin_id:
		await message.channel.send("You are not authorized to issue that command!")

	elif message.content == ("!soup spill") and message.author.id == admin_id:
		await message.channel.send("> **Emergency shutdown**")
		await client.close()

	elif message.content == ("!soup spill") and not message.author.id == admin_id:
		await message.channel.send("You are not authorized to issue that command!")

#	elif message.content == ("!soup refill"):
#		await message.channel.send("> **Rebooting...**")
#		await asyncio.sleep(3)
#		await client.clear()

#	elif message.content == ("!soup headpat"):
#		await message.channel.send("> Uploading...")
#		await message.channel.send(file=discord.File(r'/home/ubuntu/Documents/PixivUtil2/Gree_N (83399472)/103079168_p0.jpg'))
#		
#		fs = subprocess.Popen('df | head -1 && df -hV | grep -i blk', stdout=subprocess.PIPE, shell=True)
#		await message.channel.send(f"> Uploading finished\n```df | head -1 && df -hV | grep -i blk\n{fs}```")

	elif message.content == ("!soup ak-chars"):
		await message.channel.send("> Fetching data...")
		ak_operators.get_data()
		await message.channel.send(file=discord.File(r'/home/ubuntu/Documents/souperbeautiful/ak.txt'))
		await message.channel.send("Upload complete! Click Expand to see more (mobile support coming soon)")
		
		with open('/home/ubuntu/Documents/souperbeautiful/ak.txt', 'w+') as tempfile:
			tempfile.write('')

	elif message.content == ("!soup bc"):
		await message.channel.send("Have fun in BC!")

	elif message.content == ("!soup help"):
		await message.author.send(
		"> **List of Commands**\n"
		"```\n"
		"!soup news-ny			- Receiving the first 15 headlines in NYTimes\n"
		"!soup news-tom		   - Receiving the first 15 headlines in Toms Hardware\n"
		"!soup news-hna		   - Get the first 15 headlines from Hikari no Akari OST\n"
		"!soup news-slash	     - Get the first 15 headlines from SlashDot news\n"
		"!soup ak-chars		   - List upcoming Arknights operators (NA)\n"
		"!soup hello			  - Talk with a robot\n"
		"!soup eat				- Normal shutdown\n"
		"!soup spill			  - Emergency shutdown (immediate shutdown)\n"
		"```"
		)

#	elif message.content == ("!soup newsapi"):
#		url = ('https://newsapi.org/v2/top-headlines?'
#        'country=us&'
#        'apiKey=7f2826a87e5a4061af386613e358c664')
#		response = requests.get(url)
#		print(response.json())


client.run(token)
