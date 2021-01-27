import discord
from discord.ext import commands
from discord.ext.commands import has_permissions


class Purge(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    @has_permissions(manage_messages=True)
    async def purge(self, ctx, number=0):
        try:
            await ctx.channel.purge(limit=number + 1)
        except discord.ext.commands.errors.MissingPermissions:
            await ctx.send('You don\'t have perms to do that')


def setup(client):
    client.add_cog(Purge(client))
