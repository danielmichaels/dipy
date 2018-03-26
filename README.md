## Dipy

A simple toy discord bot that doesn't do much.

- Can get current BTC price from coindesk in USD
- Return servers current time
- Print out the current weather at any OpenWeatherMap location in the world.

Exists to show the ninjas at local CoderDojo that python can do stuff on your phone in an app most of them have, or have heard of.

### Commands

```bash
?weather {city} {country code} # if hyphenated city must be seperated by underscore
>>> ?weather london gb
>>> ?weather new_york us

?btc
>>> "Current price: <price>"

?time
>>> time.ctime()

?add {int} {int}
>>> sum{int + int}

?hello
>>> "World!"

```

### Requirements

- requests
- discord.py
