import discord
from discord.ext import commands
from random import choice


class Among(commands.Cog):

  def __init__(self, client):
    self.client = client
    self.sus_list = ["is very sus",
                     "is only a tad sus",
                     "is doing his tasks",
                     "just vented",
                     "probably imposter tbh",
                     "is running from red"]

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  async def sus(self, ctx, member: discord.Member):
    await ctx.send(str(member.display_name) + " " + choice(self.sus_list))


def setup(client):
  client.add_cog(Among(client))
