import discord

from api_secrets import BOT_TOKEN
from datetime import datetime
from discord.ext import commands
from weather import Weather
import logging
import requests

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='?', description='A simple tutbot')


@bot.event
async def on_ready():
    print('{0}:{1} starting...'.format(bot.user.name, bot.user.id))
    print('Ready to serve, my Lord.')
    print('--------------')


@bot.command()
async def hello(ctx):
    await ctx.send('World!')


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a + b)


# @bot.command(description="Prints servers system time")
# async def time():
#    now = datetime.ctime(datetime.now())
#    await bot.say(now)
#
#
# @bot.command(description="Prints out current CoinDesk USD value of BTC")
# async def btc():
#    btc_now = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
#    js = requests.get(btc_now).json()
#    usd_price = js['bpi']['USD']['rate']
#    await bot.say('BTC rate in USD now: {}'.format(usd_price))
#
#
# @bot.command(
#    description="Get weather from user entered location: requires {city} {country code}"
#                "\n\n If city is hyphenated please use underscores: alice_springs")
# async def weather(city='perth', cc='au'):
#    city = city.replace("_", " ")
#    query = Weather(city, cc)
#    data = query.get_data()
#    results = query.format(data)
#    await bot.say(results)


bot.run(BOT_TOKEN)
