import discord
from discord.ext import commands
from random import randint


def coin_tossing():
    x = randint(0, 1)
    coin = 'https://user-images.githubusercontent.com/75594425/101301529-1c8f1e00-3807-11eb-962a-e76f2f81415d.png' \
        if x == 1 else \
        'https://user-images.githubusercontent.com/75594425/101301574-3e88a080-3807-11eb-867b-d70868125ff8.png'
    return coin


class CoinFlip(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def toss(self, ctx):
        await ctx.send(coin_tossing())


def setup(client):
    client.add_cog(CoinFlip(client))
