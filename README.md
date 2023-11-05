# souperbeautiful
### A Discord bot for parsing HTML strings/tags and outputs them as messages in discord text chat. Intended to be hosted on a small SoC (Pi, Jetson, etc).

As the title suggests, a Discord bot written in Python that uses the BeautifulSoup4 module to parse and display strings from webpages. This is a discord bot that will hopefully be capable of performing many more tasks in the near future.  

## To Do
- Along with the headlines, reply with the URIs of their respective headlines (uri may not be embeded)
- Add parsing for other websites
	- hikarinoakariost (guarded by cloudflare)
	- Tom's Hardware
	- Bloomberg
	- ArsTechnica
	- WIRED
	- IGN
- Automate parsing/message procedure instead of always being prompted by a user
- Add debugging and activity logging in the python script
- Bot status (Online/Offline/Malfunction) logging with timestamps to ASCII file on the filesystem  

## Changelog
### 11/5/2023
- Added more commands
- Added command scheduling (hard coded)

### 12/7/2019
- Bot can parse HTML strings and send HTML strings as messages to Discord text chat
- Basic bot status logging in the main python script
- `.env` is now ignored
- Git repository initialized
