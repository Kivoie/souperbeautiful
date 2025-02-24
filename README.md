# souperbeautiful
### A Discord bot for parsing HTML strings/tags and outputs them as messages in discord text chat. Intended to be hosted on a small SBC (Pi, Jetson, etc), or a cloud server.

As the title suggests, a Discord bot written in Python that uses the BeautifulSoup4 module to parse and display strings from webpages. This is a discord bot that will hopefully be capable of performing many more tasks in the near future.  

## Changelog

### 02/24/2025
- Fixed an issue where the output was not displaying debugs correctly
- Removed Kernel banners to reduce the number of characters in the embed (max 4096)

### 02/17/2025
- Fixed 'ak_chars' automated message
- Added `!soup crash-mc` to print first few lines of latest crash log

### 02/10/2025
- Cleaned up code base
- Added Arknights banner function
- Removed HNA and other news functions
- Added embeds
- Added Minecraft functions

### 11/5/2023
- Added more commands
- Added command scheduling (hard coded)

### 12/7/2019
- Bot can parse HTML strings and send HTML strings as messages to Discord text chat
- Basic bot status logging in the main python script
- `.env` is now ignored
- Git repository initialized
