import os
import re				#import the regular expressions library
from datetime import datetime
import requests			#import string parser
import asyncio		#asynchronous concurrency
import discord          #import discord lib
from dotenv import load_dotenv
import DannyVuonglab1q5 #import from my custom lib
from bs4 import BeautifulSoup	#import string parser
import subprocess
import ak_operators, ak_operators_new
import xmlrpc.client
import tabulate

load_dotenv()
token = os.getenv('SOUPER_DISCORD_TOKEN')	#Load the discord token value from the .env file
guild = os.getenv('SOUPER_DISCORD_GUILD')	#Load the guild name from the .env file
admin_id = int(os.getenv('ADMIN_USER_ID'))
guest_id = int(os.getenv('GUEST_USER_ID'))
guest_id2 = int(os.getenv('GUEST_USER_ID2'))
mc_host = str(os.getenv('MC_HOST'))
mc_dport = os.getenv('MC_DPORT')
mc_pw = str(os.getenv('MC_PW'))
mc_command1 = str(os.getenv('MC_COMMAND1'))
server_ip = os.getenv('RPC_HOST')
server_port = os.getenv('RPC_PORT')
server_url = "http://" + str(server_ip) + ":" + str(server_port)

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
				await channel.send("> Fetching data...")
				ak_operators_new.get_data()		# Fetches, scrapes, and parses the data from an online blog
				
				timestamp = str(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
				ak_chars_embed_auto = discord.Embed(title="Upcoming Arknights Banners", description="Every Monday at 10:00 EST!", color=0xffd34f)
				ak_chars_embed_auto.set_thumbnail(url="https://i.imgur.com/ypKd7gp.png")
				ak_chars_embed_auto.add_field(name="", value=f"{ak_text}", inline=False)
				ak_chars_embed_auto.set_footer(text=f"Danny's ak_operators script, retrieved {timestamp}")
				await message.channel.send(embed=ak_chars_embed_auto)
				
				#await channel.send(file=discord.File(r'/home/ubuntu/Documents/souperbeautiful/ak.txt'))
				#await channel.send("Upload complete! Click Expand to see more. Mobile version below.")
	
				# send the mobile version and clear the files
				#with open('/home/ubuntu/Documents/souperbeautiful/ak-simple.txt', "r+") as tempfile:
					#await channel.send("```\n" + str(tempfile.read()) + "\n```")
					#tempfile.write('')

				#with open('/home/ubuntu/Documents/souperbeautiful/ak.txt', 'w+') as tempfile:
					#tempfile.write('')
			await asyncio.sleep(60)
	except Exception as e:
		try:
			await channel.send(f"**Exception caught in `schedule_ak_chars()`**\n```{e}```")
		finally:
			print(f"Exception caught in schedule_ak_chars()\n{e}")


#async def news_hna(channel):
#	await client.wait_until_ready()
#	await channel.send("Hikari no Akari OST 音楽 [HNA Updates]")
#	article = 1		#start counter at 1
#	url = 'https://hikarinoakari.com/'      #domain https://hikarinoakariost.info deprecated? Anyways, using new domain
#
#	r = requests.get(url)	#get method to get url
#	r_html = r.text		    #convert html into text
#
#	soup = BeautifulSoup(r_html)	#parser to parse all the text
#
#	for title in soup.find_all('h3'):		#print out all the strings starting with the h3 tag
#		try:
#			await channel.send(str(article) + ") [song] " + "**" + title.find('a').text + "**")	#print the article count number followed by the name of the headline
#			#print(article)
#		except AttributeError:
#			print("ERROR: AttributeError")
#			break
#		article += 1		#increment counter by 1 for every loop
#		if article == 16:
#			article = 1
#			break
#	await channel.send("Those are the top releases for today! Find more at " + "<" + url + ">")
#
#async def schedule_news_hna():
#	await client.wait_until_ready()
#
#	channel = client.get_channel(652711785023143936)
#	try:
#		while not client.is_closed():
#			current_time = datetime.now()
#			if (current_time.weekday() == 0 and current_time.hour == 10 and current_time.minute == 1) \
#			or (current_time.weekday() == 2 and current_time.hour == 10 and current_time.minute == 1) \
#			or (current_time.weekday() == 4 and current_time.hour == 13 and current_time.minute == 11):
#				try:
#					await news_hna(channel)
#				except Exception as e:
#					print(f"Exception caught within news_hna()\n{e}")
#					channel.send("Exception caught within news_hna()\n```" + str(e) + "```")
#			await asyncio.sleep(60)
#	except Exception as e:
#		print(f"Exception caught in schedule_news_hna()\n{e}")
#		await channel.send("Exception caught in schedule_news_hna()\n```" + str(e) + "```")



@client.event
async def on_ready():	#The following scripts in on_ready() will only run everytime the bot comes online
	for guild in client.guilds:
			if guild.name == guild:
				break

	#GUILD = discord.utils.get(client.guilds, name=guild)
	print("[debug] Souperbeautiful started at system time " + (str(datetime.now().strftime("%Y%m%d-%H:%M:%S")) + ". All systems go!!"))
	#print("{client.user} is online in {guild.name} (id: {guild.id}) at system time " + str(datetime.now()) + ".")
	#print(GUILD)
	#members = '\n - '.join([member.name for member in guild.members])
	#print(f'Guild Members:\n - {members}')

	client.loop.create_task(schedule_ak_chars())	#init ak loop task

	print("[debug] Updating activity name...")
	await client.change_presence(activity=discord.Game(name='instead of working'))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	#elif message.content == ("!soup news-ny"):
	#	await message.channel.send("News Articles ニュース記事 [New York Times]")
	#	article = 1		#start counter at 1
	#	url = 'https://www.nytimes.com/ca/'
    #
	#	r = requests.get(url)	#get method to get url
	#	r_html = r.text		    #convert html into text
    #
	#	soup = BeautifulSoup(r_html)	#parser to parse all the text
    #
	#	for title in soup.find_all('article'):		#print out all the strings starting with the h2 tag
	#		try:
	#			await message.channel.send(str(article) + "........[article] " + "**" + title.find('h1').text + "**")	#print the article count number followed by the name of the headline
	#			#print(article)
	#		except AttributeError:
	#			print("ERROR: AttributeError")
	#			break
	#		article += 1		#increment counter by 1 for every loop
	#		if article == 16:
	#			article = 1
	#			break
	#	await message.channel.send("These are the top headlines for today! Find them at "+ "<" + url + ">")
    #
	#elif message.content == ("!soup news-tom"):
	#	await message.channel.send("News Articles ニュース記事 [Tom's Hardware")
	#	article = 1		#start counter at 1
	#	url = 'https://www.tomshardware.com/'
    #
	#	r = requests.get(url)	#get method to get url
	#	r_html = r.text		    #convert html into text
    #
	#	soup = BeautifulSoup(r_html)	#parser to parse all the text
    #
	#	for title in soup.find_all('figcaption'):		#print out all the strings referenced by article-name class
	#		try:
	#			await message.channel.send(str(article) + "........[article] "  + "**" + title.find(class_="article-name").text + "**" )	#print the article count number followed by the name of the headline
	#			#print(article)
	#		except AttributeError:
	#			print("ERROR: AttributeError")
	#			break
	#		article += 1		#increment counter by 1 for every loop
	#		if article == 16:
	#			article = 1
	#			break
	#	await message.channel.send("Those are the top headlines for today! Find more at " + "<" + url + ">")

    elif message.content == ("!soup hello"):
		await message.channel.send("Hello, souper!")

	elif message.content == ("!soup eat") and message.author.id == admin_id:
		await message.channel.send("Bye bye! じゃあまたね~")
		await asyncio.sleep(1)
		await message.channel.send("> **Shutting down...**")
		await asyncio.sleep(3)
		await client.close()

	elif message.content == ("!soup spill") and message.author.id == admin_id:
		await message.channel.send("> **Emergency shutdown**")
		await client.close()

#	elif message.content == ("!soup headpat"):
#		await message.channel.send("> Uploading...")
#		await message.channel.send(file=discord.File(r'/home/ubuntu/Documents/PixivUtil2/Gree_N (83399472)/103079168_p0.jpg'))
#		
#		fs = subprocess.Popen('df | head -1 && df -hV | grep -i blk', stdout=subprocess.PIPE, shell=True)
#		await message.channel.send(f"> Uploading finished\n```df | head -1 && df -hV | grep -i blk\n{fs}```")

	elif message.content == ("!soup ak-chars"):
		await message.channel.send("> Fetching data...")
		try:
			ak_text = ak_operators_new.get_data()
		except Exception as e:
			message.channel.send(f"Exception caught in ak_operators_new\n```{e}```")
		else:
			timestamp = str(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
			ak_chars_embed = discord.Embed(title="Upcoming Arknights Banners", description="", color=0xffd34f)
			ak_chars_embed.set_thumbnail(url="https://i.imgur.com/ypKd7gp.png")
			ak_chars_embed.add_field(name="", value=f"{ak_text}", inline=False)
			ak_chars_embed.set_footer(text=f"Danny's ak_operators script, retrieved {timestamp}")
			await message.channel.send(embed=ak_chars_embed)
			
			#await message.channel.send(file=discord.File(r'/home/ubuntu/Documents/souperbeautiful/ak.txt'))
			#await message.channel.send("Upload complete! Click Expand to see more. Mobile version below.")


		#with open('/home/ubuntu/Documents/souperbeautiful/ak-simple.txt', "r+") as tempfile:
		#	await message.channel.send("```\n" + str(tempfile.read()) + "\n```")
		#	tempfile.write('')
		#	
		#with open('/home/ubuntu/Documents/souperbeautiful/ak.txt', 'w+') as tempfile:
		#	tempfile.write('')


	elif message.content == ("!soup bc"):
		await message.channel.send("Have fun in BC!")

	elif message.content == ("!soup mc") and message.channel.id == 979855384443502642:

		raw_ping = subprocess.Popen([f'fping -t2000 -r 0 {mc_host}'], stdout=subprocess.PIPE, shell=True)
		raw_ping.wait()

		if 'alive' in str(raw_ping.communicate()[0]):

			await message.channel.send("> Fetching data...")


			try:
				result = subprocess.Popen([f'mcrcon -H {mc_host} -P {mc_dport} -p {mc_pw} {mc_command1}'], stdout=subprocess.PIPE, shell=True)
			except Exception as e:
				result = "mcrcon encountered an error:" + str(e)
			else:
				result = re.sub(r"\\n", '\n', str(result.communicate()[0]).strip())
				result = str(re.sub(r"b\'", '', str(result))).rstrip("'")
				result = str(re.sub(r'\\x1b\[0m', '', str(result)))

			try:
				call_peer = xmlrpc.client.ServerProxy(server_url)

			except Exception as e:
				result = result + str(e)
				mcstatus = discord.Embed(title="Minecraft Server Status", description="There was an error.", color=0x870000)
			else:
				try:
					result = result + str(call_peer.listen_system_stats())
				except Exception as e:
					result = result + str(e)
					mcstatus = discord.Embed(title="Minecraft Server Status", description="There was an error.", color=0x870000)
				else:
					mcstatus = discord.Embed(title="Minecraft Server Status", description="", color=0xffd34f)

			timestamp = str(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
			mcstatus.set_thumbnail(url="https://i.imgur.com/vdB3U0w.png")
			mcstatus.add_field(name="", value=f"```{result}```", inline=False)
			mcstatus.set_footer(text=f"Danny's mcrpc script, retrieved {timestamp}")
			await message.channel.send(embed=mcstatus)

		else:
			timestamp = str(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
			mcstatus = discord.Embed(title="Minecraft Server Status", description="", color=0x870000)
			mcstatus.set_thumbnail(url="https://i.imgur.com/vdB3U0w.png")
			mcstatus.add_field(name="There was an error.", value="Minecraft server unreachable!", inline=False)
			mcstatus.set_footer(text=f"Danny's mcrpc script, retrieved {timestamp}")
			await message.channel.send(embed=mcstatus)

	elif message.content == ("!soup restart-mc") and message.channel.id == 979855384443502642 and (message.author.id == admin_id or message.author.id == guest_id or message.author.id == guest_id2):

		raw_ping = subprocess.Popen([f'fping -t2000 -r 0 {mc_host}'], stdout=subprocess.PIPE, shell=True)
		raw_ping.wait()

		if 'alive' in str(raw_ping.communicate()[0]):

			await message.channel.send("> Sending restart signal...")
			try:
				call_peer = xmlrpc.client.ServerProxy(server_url)
			except Exception as e:
				output = str(e)
				await message.channel.send(f'```{output}```')
			else:
				try:
					output = call_peer.listen_mc_reboot()
				except Exception as e:
					output = str(e)
					await message.channel.send(f'```{output}```')
				else:
					timestamp = str(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
					restartmc = discord.Embed(title="Minecraft Server Restart", description="", color=0xffd34f)
					restartmc.set_thumbnail(url="https://i.imgur.com/vdB3U0w.png")
					restartmc.add_field(name="Restart signal has been sent.", value="Server is restarting in 10 seconds...", inline=False)
					restartmc.set_footer(text=f"Danny's restartmc script, retrieved {timestamp}")
					await message.channel.send(embed=restartmc)
		else:
			timestamp = str(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
			restartmc = discord.Embed(title="Minecraft Server Restart", description="There was an error.", color=0x870000)
			restartmc.set_thumbnail(url="https://i.imgur.com/vdB3U0w.png")
			restartmc.add_field(name="Minecraft server unreachable!", value="", inline=False)
			restartmc.set_footer(text=f"Danny's restartmc script, retrieved {timestamp}")
			await message.channel.send(embed=restartmc)


	elif message.content == ("!soup help"):

		help_headers = ['Command', 'Description', 'Protected']
		help_data = [
				['!soup hello', 'Talk with a robot', 'No'],
				['!soup ak-chars', 'List upcoming Arknights banners and operators (CN)', 'No'],
				['!soup mc', 'Get Minecraft server status', 'No'],
				['!soup restart-mc', 'Restart the Minecraft server immediately', 'Yes'],
				['!soup <eat|spill>', 'Shutdown the bot', 'Yes'],
				['!soup bc', 'Specifically for David', 'No'],
				['!soup help', 'Display this help tool', 'No']
			]

		helpmessage = tabulate(help_data, headers=help_headers, tablefmt='simple')

		timestamp = str(datetime.now().strftime("%m-%d-%Y %H:%M:%S"))
		helptext = discord.Embed(title="Souperbeautiful Discord Bot", description="Help", color=0xffd34f)
		helptext.set_thumbnail(url="https://i.imgur.com/7NehTAD.png")
		helptext.add_field(name="", value=f"```{helpmessage}```", inline=False)
		helptext.set_footer(text=f"Retrieved {timestamp}")
		await message.author.send(embed=helptext)


		#await message.author.send(
		#"> **List of Commands**\n"
		#"```\n"
		#"!soup news-ny			- Receiving the first 15 headlines in NYTimes\n"
		#"!soup news-tom		   - Receiving the first 15 headlines in Toms Hardware\n"
		#"!soup news-slash	     - Get the first 15 headlines from SlashDot news\n"
		#"!soup ak-chars		   - List upcoming Arknights operators (NA)\n"
		#"!soup hello			  - Talk with a robot\n"
		#"!soup eat				- Normal shutdown\n"
		#"!soup spill			  - Emergency shutdown (immediate shutdown)\n"
		#"```"
		#)


client.run(token)
