import discord
from discord.ext import commands
from discord.ext.commands import has_permissions
from discord.ext.commands import MissingPermissions


class Purge(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  @has_permissions(manage_messages=True)
  async def purge(self, ctx, number=0):
    await ctx.channel.purge(limit=number + 1)


def setup(client):
  client.add_cog(Purge(client))
