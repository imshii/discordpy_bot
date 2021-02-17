from discord.ext import commands
from subprocess import check_output
from cogs.encrypt import decrypt
from cogs.maths import ciel

import asyncio

import discord


def splitter(string):
  if len(string) < 2000:
    return string
  length = len(string)
  num_messages = round(ciel(length / 1900))
  s = []
  i, f = 0, 0
  for n in range(num_messages):
    i += 1900
    s += [string[f:i]]
    f += 1900

  return s


class Confidential(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  # Just a heads up that these commands for security reasons will be very static as I will be personally using it for
  # fixing minor issues or just to get some data I store on my server
  @commands.command()
  async def file(self, ctx, password, *, file):
    if str(ctx.author.id)!="607392053848047691" \
        or str(ctx.author)!="imshy#1619" \
        or str(password)!=decrypt("04124YA1E1WLE1WLFLDCJ8P5GO9LJ8P5GO9L"):
      await ctx.send("Currently only the owner can use this tool")
      return

    await ctx.send(file=discord.File(file))

  @commands.command()
  async def system(self, ctx, password, *, command):
    if str(ctx.author.id)!="607392053848047691" \
        or str(ctx.author)!="imshy#1619" \
        or str(password)!=decrypt("04124YA1E1WLE1WLFLDCJ8P5GO9LJ8P5GO9L"):
      await ctx.send("**PASSWORD INCORRECT**")
      return

    output = check_output(command.split(" ")).decode("utf-8")

    try:
      new_output = splitter(output)
      await ctx.send("{}\n{}\n{}".format("```", new_output, "```")) if type(new_output) is str else [
        await ctx.send("{}\n{}\n{}".format("```", i, "```")) for i in new_output]
    except Exception as error:
      await ctx.send(error)


def setup(client):
  client.add_cog(Confidential(client))
