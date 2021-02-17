from discord.ext import commands
from urllib import parse
from random import choice
from math import floor

import requests
import json
import discord
from datetime import datetime

names = {
  "TESLA": "TSLA",
  "APPLE": "AAPL",
  "BITCOIN": "BTCUSD"
}


class Stock(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  async def stock(self, ctx, stock):
    switch = names.get(stock.upper())
    if switch:
      stock = switch

    time = "60min"
    key = ["YSU6PW16SX0Y6HK3", "K7819OLJ7MU1LHSC", "P1GNUT6Q03LYY6S4"]
    url = "https://www.alphavantage.co/query"
    values = {"function": "TIME_SERIES_INTRADAY",
              "symbol": stock,
              "interval": time,
              "apikey": choice(key),
              "outputsize": "compact"}

    parsed = parse.urlparse(url)
    query = parsed.query
    dic = dict(parse.parse_qsl(query))
    dic.update(values)
    parsed = parsed._replace(query=parse.urlencode(dic))
    print(parse.urlunparse(parsed))

    response = requests.request(url=parse.urlunparse(parsed), method="get")
    jsonified_response = response.json()

    if jsonified_response.get("Error Message"):
      await ctx.send(f"The stock {stock} was not found anywhere ")
      return

    last_refresh = jsonified_response.get("Meta Data").get("3. Last Refreshed")
    times = jsonified_response.get(f"Time Series ({time})")

    last_open = times.get(last_refresh).get("1. open")
    high = times.get(last_refresh).get("2. high")
    low = times.get(last_refresh).get("3. low")
    close = times.get(last_refresh).get("4. close")
    volume = times.get(last_refresh).get("5. volume")

    dic_info = {
      "Current": last_open,
      "Close": close,
      "High": high,
      "Low": low,
      "Volume": volume
    }

    paste_ee_query = "http://paste.ee/api"
    paste_ee_values = {
      "key": "aIIjsnVxrqdsP9YmkKPXSWxMFjSCXQcvuBIt3FHAL",
      "description": "none",
      "paste": "HEllo Worlds"
    }

    # paste_ee_response = requests.post(paste_ee_query, data=paste_ee_values)
    # print(paste_ee_response)
    # paste_link = paste_ee_response.json().get("paste").get("raw")

    embed = discord.Embed(colour=discord.Colour.teal(), description="**{}, NASQAD**".format(stock.upper()))
    embed.add_field(name="** **", value=
    f"**Current:** $ {moniezer(last_open)}\n \
      **Close:** $ {moniezer(close)}\n \
      **High:** $ {moniezer(high)}\n \
      **Low:** $ {moniezer(low)}\n \
      **Volume:** {moniezer(volume)}"
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    # embed.add_field(name="** **", value="All json info can be found here: {}".format(paste_link), inline=False)
    # working on it xD
    await ctx.channel.send(embed=embed)


def setup(client):
  client.add_cog(Stock(client))


def moniezer(money):
  return (round(float(money) * 100)) / 100


"""    pastebin_query = "https://pastebin.com/api/api_post.php"
    pastebin_api_key = "FUcM5aRRjL1rrXgNdr8nu42m4T8xjJns"
    values = {
      "api_dev_key": pastebin_api_key,
      "api_option": "paste",
      "api_paste_code": json.dumps(jsonified_response, indent=4),
      "api_paste_format": "json",
      "api_paste_name": f"{ctx.author.name} {datetime.now()}",
      "api_paste_private": 0  # makes the post public
    }

    pastebin_response = requests.post(url=pastebin_query, data=values).text

    # new_url = response.text.replace("https://pastebin.com/", "https://pastebin.com/raw/")
    # makes it raw"""
