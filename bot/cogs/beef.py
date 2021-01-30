import discord
from discord.ext import commands
from random import randint, choice

# beef_list = ['let\'s go, back of school :boom: :punch:.', 'dude fuck no you\'re scary.', 'your a hoe.',
#              'I can do this all day.',
#              'you think you\'re all the shit? 1v1 me Maxi.', 'child.', 'bench warmer.',
#              'my dick thicker than you\'re skinny ass arms.', 'better start running kid.']

with open('beef.txt') as menacing_messages:
  beef_list = [line.rstrip() for line in menacing_messages]


class Beef(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  # @commands.command()
  # async def beef(self, ctx, *, recipient=''):
  #     await ctx.send(
  #         str(ctx.author.display_name) + ' ' + choice(menacing_messages) if len(recipient) == 0 else str(
  #             recipient) + ' ' + choice(menacing_messages))

  @commands.command()
  async def beef(self, ctx, *, recipient=''):
    await ctx.send(choice(beef_list))


def setup(client):
  client.add_cog(Beef(client))
