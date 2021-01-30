from string import ascii_lowercase
from discord.ext import commands

import requests
import json
import discord


element_api = "http://10.0.0.46:88/elements"


def requester(element):
    all_info = requests.get(element_api)
    dumped_info = json.loads(all_info.text)
    res = [i for i in dumped_info if i.get("name") == element]

    try:
        dump = json.dumps(res[0], indent=4)
    except IndexError:
        dump = "Element not found"
    return dump


def calculator(Element):

    try:
        all_info = requests.get(element_api)
        dumped_info = json.loads(all_info.text)
        res = []
        mm = float()
        # checks first if there is a first number
        # and multiplies the string by
        # that number
        try:
            if isinstance(int(Element[0]), int):
                num = int(Element[0])
                Element = Element[Element.startswith(str(num)) and 1:]
                Element *= num
        except:
            pass

        element_list = list(Element)
        lenner = 0

        for item in element_list:

            if ascii_lowercase.__contains__(item):
                element_list[lenner - 1] += item
                del element_list[lenner]

            try:
                print(element_list)
                if isinstance(int(item), int):
                    del element_list[lenner]
                    for i in range(int(item) - 1):
                        element_list += element_list[lenner - 1]
                lenner += 1
            except:
                lenner += 1
                pass

        print(element_list)
        # get's the dic using the symbol to validate
        for atom in element_list:
            print(atom)
            res += [i for i in dumped_info if i.get("symbol") == atom]
        for i in range(len(res)):
            mm += float(res[i].get("atomicMass"))
        print(mm)
        return mm
    except:
        return "Something went wrong"


class Elements(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def element(self, ctx, element):
        element = element.title()
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name=element, value=requester(element))
        await ctx.send(embed=embed)

    @commands.command()
    async def mm(self, ctx, elements):
        embed = discord.Embed(color=discord.Colour.blue())
        embed.add_field(name=f'{elements}\'s molar mass', value=calculator(elements))
        embed.set_footer(text=f'Requested by {ctx.author.display_name}', icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Elements(client))
