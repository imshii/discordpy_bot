from discord.ext import commands


class Purge(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  @commands.has_permissions(administrator=True)
  async def purge(self, ctx, number=0):
    await ctx.channel.purge(limit=number + 1)


def setup(client):
  client.add_cog(Purge(client))
