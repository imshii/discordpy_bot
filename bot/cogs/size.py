import discord
from discord.ext import commands
from random import randint


# def size_matters():
#     return randint(0, 10) * '=' + '>'
#
#
class Thingy(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def penis(self, ctx):
        await ctx.send('```' + str(randint(0, 10) * '=' + '>' + '```'))

    @commands.command()
    async def pp(self, ctx):
        await ctx.send('```' + str(randint(0, 10) * '=' + '>' + '```'))


def setup(client):
    client.add_cog(Thingy(client))
