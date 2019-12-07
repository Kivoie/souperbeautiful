# bot.py
import os
from datetime import datetime
import discord
from dotenv import load_dotenv
#import DannyVuonglab1q5
import re				#import the regular expressions library
import math				#import math methods
from bs4 import BeautifulSoup	#import string parser
import requests			#import string parser

#parserny = DannyVuonglab1q5.soupny()

load_dotenv()
token = os.getenv('SOUPER_DISCORD_TOKEN')	#Load the discord token value from the .env file
guild = os.getenv('SOUPER_DISCORD_GUILD')	#Load the guild name from the .env file

client = discord.Client()

@client.event
async def on_ready():
	for guild in client.guilds:
			if guild.name == guild:
				break
				
	#GUILD = discord.utils.get(client.guilds, name=guild)
	print("All systems go!! \n(Press CTRL + C to terminate script at any time. There will be a delay before bot logs off.")
	print(f"{client.user} is online in {guild.name} (id: {guild.id}) at system time " + str(datetime.now()) + ".")
	#print(GUILD)
	members = '\n - '.join([member.name for member in guild.members])
	print(f'Guild Members:\n - {members}')

@client.event
async def on_message(message):
	if message.author == client.user:
		return
	elif message.content == "!soup news":	
		#await message.channel.send(parserny)

		article = 1		#start counter at 1
		url = 'https://www.nytimes.com/'
		#https://www.nytimes.com/2019/09/23/us/politics/trump-un-biden-ukraine.html?action=click&module=Top%20Stories&pgtype=Homepage
		#https://www.bloomberg.com/news/articles/2019-08-16/cybersecurity-tips-from-a-master-of-deception-turned-consultant

		r = requests.get(url)	#get method to get url
		r_html = r.text		#convert html into text

		soup = BeautifulSoup(r_html)	#parser to parse all the text

		for title in soup.find_all('article'):		#print out all the strings starting with the h2 tag
			try:
				print(await message.channel.send(title.find('p').text))	#print the article count number followed by the name of the headline
			except AttributeError:
				break
			article += 1		#increment counter by 1 for every loop

	elif message.content == ("!soup hello"):
		await message.channel.send("Hello, souper!")
	elif message.content == ("ya"):
		await message.channel.send("yeet!")
	elif message.content == ("ayy"):
		await message.channel.send("lmao")
	elif message.content == ("lmao"):
		await message.channel.send("ayy")

client.run(token)