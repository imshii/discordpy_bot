import discord
from discord.ext import commands
from string import ascii_uppercase


class Talk(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(f'As per the great {ctx.author.display_name} has said, "{message}".')

    @commands.command()
    async def alphabet(self, ctx):
        x = list(ascii_uppercase)
        for i in range(len(x)):
            await ctx.send(x[i])


def setup(client):
    client.add_cog(Talk(client))
