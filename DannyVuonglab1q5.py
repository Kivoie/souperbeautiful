import re				#import the regular expressions library
import math				#import math methods
from bs4 import BeautifulSoup	#import string parser
import requests			#import string parser
import discord


def soupny():

	article = 1		#start counter at 1
	url = 'https://www.nytimes.com/'
	#https://www.nytimes.com/2019/09/23/us/politics/trump-un-biden-ukraine.html?action=click&module=Top%20Stories&pgtype=Homepage
	#https://www.bloomberg.com/news/articles/2019-08-16/cybersecurity-tips-from-a-master-of-deception-turned-consultant

	r = requests.get(url)	#get method to get url
	r_html = r.text		#convert html into text

	soup = BeautifulSoup(r_html)	#parser to parse all the text

	for title in soup.find_all('article'):		#print out all the strings starting with the h2 tag
		try:
			print(article, title.find('p').text)	#print the article count number followed by the name of the headline
		except AttributeError:
			break
		article += 1		#increment counter by 1 for every loop

soupny()