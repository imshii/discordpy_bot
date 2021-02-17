import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import requests


def world():
    site_data = requests.get("https://www.worldometers.info/coronavirus/")  # data from site
    soup = BeautifulSoup(site_data.text, "lxml")  # string to html
    info = soup.findAll("div", class_="maincounter-number")  # finds all and outputs to a list

    try:
        info_list = [info[0].text, info[1].text, info[2].text]
    except IndexError:
        pass
    return info_list


def country(location):
    site_data = requests.get(f"https://www.worldometers.info/coronavirus/country/{location}/")  # data from site
    soup = BeautifulSoup(site_data.text, "lxml")  # string to html
    info = soup.findAll("div", class_="maincounter-number")  # finds all and outputs to a list
    print(info, site_data, location)

    try:
        info_list = [info[0].text, info[1].text, info[2].text]
    except IndexError:
        return "Error"

    return info_list


class Covid(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def covid(self, ctx, location=''):
        if location == '':
            temp = world()
            name = "globally"
        else:
            temp = country(location)
            name = f"in {location}"
        print(temp)
        if temp != "Error":
            total_cases, deaths, recoveries = temp[0], temp[1], temp[2]
            print(total_cases)
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.add_field(name=f"Total cases {name}", value=total_cases)
            embed.add_field(name="Deaths :frowning:", value=deaths)
            embed.add_field(name="Recoveries :slight_smile:", value=recoveries)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.blue())
            embed.add_field(name="Index Error", value="Country could not be found")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Covid(client))
