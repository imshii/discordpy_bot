import discord
from discord.ext import commands
import os


class Ping(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong! :ping_pong:')

    @commands.command()
    async def pong(self, ctx):
        await ctx.send('Ping! :ping_pong:')


def setup(client):
    client.add_cog(Ping(client))
