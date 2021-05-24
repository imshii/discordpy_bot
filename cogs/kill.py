import discord
from discord.ext import commands


class Avatar(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  async def kill(self, ctx):
    guild = self.client.get_guild(782099194222477353)
    l = guild.members
    await ctx.send(l)

def setup(client):
  client.add_cog(Avatar(client))
