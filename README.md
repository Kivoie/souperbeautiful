# souperbeautiful
### A Discord bot for parsing HTML strings/tags and outputs them as messages in discord text chat.

As the title suggests, a Discord bot written in Python that uses the BeautifulSoup4 module to parse and display strings from webpages. This is a discord bot that will hopefully be capable of performing many more tasks in the near future.  

If you wish to automate this bot, write a simple Windows batch script (2 or 3 lines) that runs as a background service upon system startup.  

## To Do
- Along with the headlines, respond with the URLs of their respective headlines (url may or may not be embeded)
- Add parsing for other websites
	- hikarinoakariost
	- Tom's Hardware
	- Bloomberg
	- ArsTechnica
	- WIRED
	- IGN
- Automate parsing/message procedure instead of always being prompted by a user
- Add debugging and activity logging in the python script
- Containerize (Docker) and integrate with GitHub as a package
- Bot status (Online/Offline/Malfunction) logging with timestamps to ASCII file (DOES NOT INCLUDE BOT ACTIVITY)  

## Changelog
### 12/7/2019
- Bot can parse HTML strings and send HTML strings as messages to Discord text chat
- Basic bot status logging in the main python script
- `.env` is now ignored
- Git repository initialized