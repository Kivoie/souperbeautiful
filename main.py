import os
from datetime import datetime
import discord          #import discord lib
from dotenv import load_dotenv
import DannyVuonglab1q5 #import from my custom lib
import re				#import the regular expressions library
#import math				#import math methods
from bs4 import BeautifulSoup	#import string parser
import requests			#import string parser
import asyncio

#parserny = DannyVuonglab1q5.soupny()

load_dotenv()
token = os.getenv('SOUPER_DISCORD_TOKEN')	#Load the discord token value from the .env file
guild = os.getenv('SOUPER_DISCORD_GUILD')	#Load the guild name from the .env file

client = discord.Client()

@client.event
async def on_ready():	#The following scripts in on_ready() will only run everytime the bot comes online
	for guild in client.guilds:
			if guild.name == guild:
				break

	#GUILD = discord.utils.get(client.guilds, name=guild)
	print("All systems go!! \n(Press CTRL + C to terminate script at any time. There will be a delay before bot logs off.")
	print("{client.user} is online in {guild.name} (id: {guild.id}) at system time " + str(datetime.now()) + ".")
	#print(GUILD)
	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')

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
		url = 'https://hikarinoakari.com/'

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

	elif message.content == ("ayy"):
		await message.channel.send("lmao")

	elif message.content == ("lmao"):
		await message.channel.send("ayy")

	elif message.content == ("!soup eat"):
		await message.channel.send("Bye bye! じゃあまたね~")
		await asyncio.sleep(1)
		await message.channel.send("> **Shutting down...**")
		await asyncio.sleep(3)
		await client.close()

	elif message.content == ("!soup spill"):
		await message.channel.send("> **Emergency shutdown**")
		await client.close()

#	elif message.content == ("!soup refill"):
#		await message.channel.send("> **Rebooting...**")
#		await asyncio.sleep(3)
#		await client.clear()

	elif message.content == ("!soup help"):
		await message.author.send(
		"> **List of Commands**\n"
		"```\n"
		"!soup news-ny			- Receiving the first 15 headlines in NYTimes\n"
		"!soup news-tom		   - Receiving the first 15 headlines in Toms Hardware\n"
		"!soup news-hna		   - Get the first 15 headlines from Hikari no Akari OST\n"
		"!soup news-slash	     - Get the first 15 headlines from SlashDot news\n"
		"!soup hello			  - Talk with a robot\n"
		"!soup eat				- Delay shutdown\n"
		"!soup spill			  - Emergency shutdown (immediate shutdown)\n"
		"```"
		)
'''
	elif message.content == ("!soup newsapi"):
		url = ('https://newsapi.org/v2/top-headlines?'
        'country=us&'
        'apiKey=7f2826a87e5a4061af386613e358c664')
		response = requests.get(url)
		print(response.json())
'''

client.run(token)
