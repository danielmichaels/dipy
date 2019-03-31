import logging
from datetime import datetime

import discord
import requests
from discord.ext import commands

from api_secrets import BOT_TOKEN
from weather import Weather

logging.basicConfig(level=logging.INFO)

bot = commands.Bot(command_prefix='?', description='A simple bot')
bot.remove_command('help')


@bot.event
async def on_ready():
    print('{0}:{1} starting...'.format(bot.user.name, bot.user.id))
    print('Ready to serve, my Lord.')
    print('--------------')


@bot.command()
async def help(ctx):
    author = ctx.message.author
    embed = discord.Embed(title="My Helper Bot",
                          description="A useful helper - list of available commands: ",
                          color=discord.Color.dark_gold())
    embed.set_author(name="Help")
    embed.add_field(name="?hello", value="echo replies 'world'", inline=False)
    embed.add_field(name="?add",
                    value="Gives the sum of two integers **A** and **B**",
                    inline=False)
    embed.add_field(name="?cat", value="Provide comic cat relief gif.",
                    inline=False)
    embed.add_field(name="?weather [city] [country_code]",
                    value="Returns weather for user entered location"
                          "\n**Requires {city} {country_code}**"
                          "\nIf city is hyphenated or multi-word such as "
                          "Alice Springs it must be underscored, see example."
                          "\n`?weather alice_springs au`",
                    inline=False)
    embed.add_field(name="?btc",
                    value="Return current BTC price in USD from CoinDesk",
                    inline=False)
    embed.add_field(name="?time", value="return current server time.",
                    inline=False)

    await ctx.send(author, embed=embed)


@bot.command()
async def hello(ctx):
    await ctx.send('World!')


@bot.command()
async def add(ctx, int1: int, int2: int):
    await ctx.send(int1 + int2)


@bot.command()
async def cat(ctx):
    await ctx.send("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif")


@bot.command()
async def time(ctx):
    now = datetime.ctime(datetime.now())
    await ctx.send(now)


@bot.command()
async def btc(ctx):
    btc_now = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
    js = requests.get(btc_now).json()
    usd_price = js['bpi']['USD']['rate']
    await ctx.send('BTC rate in USD now: {}'.format(usd_price))


@bot.command()
async def weather(ctx, city='newcastle', cc='au'):
    city = city.replace("_", " ")
    query = Weather(city, cc)
    data = query.get_data()
    results = query.format(data)
    await ctx.send(results)


bot.run(BOT_TOKEN)
