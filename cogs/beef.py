from discord.ext import commands
from random import randint, choice


with open('beef.txt') as menacing_messages:
  beef_list = [line.rstrip() for line in menacing_messages]


class Beef(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  async def beef(self, ctx):
    await ctx.send(choice(beef_list))


def setup(client):
  client.add_cog(Beef(client))
