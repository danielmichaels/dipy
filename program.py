import asyncio
from datetime import datetime
import requests
import discord
from discord.ext import commands
import logging

logging.basicConfig(level=logging.INFO)


TOKEN = 'NDI2NjE1MDI1NzM0NjQ3ODE2.DZYnbw.3Rk99ugEcmCdm7gpsonj3ukJBco'

bot = commands.Bot(command_prefix='$', description='A simple tutbot')

@bot.event
async def on_ready():
    print('logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')

@bot.command()
async def hello():
    await bot.say('World!')

@bot.command()
async def add(a: int, b: int):
    await bot.say(a + b)

@bot.command()
async def time():
    now = datetime.ctime(datetime.now())
    await bot.say(now)

@bot.command()
async def btc():
    btc_now = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    js = requests.get(btc_now).json()
    usd_price = js['bpi']['USD']['rate']
    await bot.say(f'BTC rate in USD now: {usd_price}')

bot.run(TOKEN)

