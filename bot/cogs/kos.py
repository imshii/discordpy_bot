import discord
from discord.ext import commands
import requests
import json
from discord_bot_pit.bot.bot import reload

list_players = []
online_players = []
skeleton = []

with open('players.txt'.rstrip()) as document:
    list_players += [str(line) for line in document]


def online_status():
    embed = discord.Embed(colour=discord.Colour.dark_red())
    embed_list = ''

    for person in list_players:
        print(person)
        response = requests.get(f'https://pitpanda.rocks/api/players/{str(person)}')
        json_response = json.loads(response.text)
        # print(json_response)

        success_status = json_response.get('success')

        if success_status:
            print('sucess_status')
            if json_response.get("data").get("online"):
                print("json_response")
                online_players.append(person)

    if online_players == skeleton:
        embed.add_field(name="Online Players:", value='None online')
        return embed

    for player in online_players:
        print(player)
        embed_list += f'[{player}](https://pitpanda.rocks/players/{player})'

    embed.add_field(name="Online Players:", value=str(embed_list))
    print(online_players)

    return embed


def checker(ign):
    response = requests.get(f'https://pitpanda.rocks/api/players/{ign}')
    x = json.loads(response.text)

    try:
        status = 'online :white_check_mark:' if x.get('data').get('online') else 'offline :no_entry_sign:'
    except AttributeError:
        embedd = discord.Embed()
        embedd.add_field(name="Error", value=f'{ign} never played pit')
        return embedd

    embed_var = discord.Embed(colour=discord.Colour.dark_red())  # title="Title", description="Desc", color=0x00ff00)
    embed_var.add_field(name="Checker", value=f'[{ign}](https://pitpanda.rocks/players/{ign}) is {status}', inline=True)

    return embed_var


def list_manager(objective, player_name):
    if objective == 'add':
        with open('players.txt', 'a') as adder:
            adder.write('\n' + player_name)
            reload(extension='kos')
    elif objective == 'remove':
        reader = open('players.txt', 'rt')
        writer = open('players.txt', 'wt')
        for line in reader:
            writer.write(line.replace('', str(player_name)))
        reader.close()
        writer.close()
        reload(extension='kos')
    return f'{objective} of {player_name} has finished successfully'


def list_players():
    list_kos = ''
    with open('players.txt') as lister:
        for line in lister:
            list_kos += f'[{str(line)}](https://pitpanda.rocks/players/{str(line)}) '
    embed = discord.Embed()
    embed.add_field(name="Kos list", value=list_kos)
    return embed


class Kos(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def check(self, ctx, user=''):
        await ctx.send(embed=checker(ign=user))

    @commands.command(aliases=['mhgx', 'imshy', 'diet', 'badlist'])
    async def kos(self, ctx):
        await ctx.send(embed=online_status())

    @commands.command(aliases=['a'])
    @commands.has_permissions(kick_members=True)
    async def add(self, ctx, player):
        await ctx.send(list_manager(objective='add', player_name=player))

    @commands.command(aliases=['delete', 'rm', 'r'])
    @commands.has_permissions(kick_members=True)
    async def remove(self, ctx, player):
        await ctx.send(list_manager(objective='remove', player_name=player))

    @commands.command()
    async def list(self, ctx):
        await ctx.send(embed=list_players())


def setup(client):
    client.add_cog(Kos(client))
