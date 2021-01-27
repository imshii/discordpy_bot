import discord
from discord.ext import commands
import string
from random import sample


def random_string(string_length=11):
    letters = string.ascii_letters + string.digits
    return ''.join(sample(letters, string_length))


class Tokens(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def gift(self, ctx):
        await ctx.send('https://discord.gift/' + str(random_string()))


def setup(client):
    client.add_cog(Tokens(client))
