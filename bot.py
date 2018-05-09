import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import os



bot = commands.Bot(command_prefix="a.")



@bot.event
async def on_ready():
  print(bot.user.name)

  
  
@bot.command(pass_context=True)
async def hi(ctx):
  await bot.say("Hello there"+" "+ctx.message.author.name)
  
  
  
  
bot.run(os.environ['BOT_TOKEN'])

language: python
python:
  - "3.5.2"
install:
  - pip install -r requirements.txt
script:
  - python -m compileall ./red.py
  - python -m compileall ./cogs
  - python ./red.py --no-prompt --no-cogs --dry-run
cache: pip
notifications:
  email: false
