from discord.ext import commands

import discord
import matplotlib.pyplot as plt
import os


def points_lister(points):
  values = points.split()
  x, y = [], []
  for n in range(len(values)):
    if n % 2==0:
      x.append(float(values[n]))
    else:
      y.append(float(values[n]))
  return {"X": x, "Y": y}


class Math(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  async def graph(self, ctx, *, points):
    dict_points = points_lister(points)
    x = dict_points.get("X")
    y = dict_points.get("Y")

    file_name = f"{ctx.author.name}.png"

    plt.plot(x, y)
    plt.savefig(file_name)
    plt.figure()

    await ctx.send(file=discord.File(file_name))
    os.remove(file_name)

  @commands.command()
  async def slope(self, ctx, *, points):
    dict_points = points_lister(points)
    x = dict_points.get("X")
    y = dict_points.get("Y")

    if len(x) + len(y)==4:  # This check that they each are 2 ints long
      slope = float((x[1] - x[0]) / (y[1] - y[0]))
      await ctx.send(f"The slope of yor line is {slope}")
    else:
      await ctx.send("Insert as such: x1 y1 x2 y2")
      return


def setup(client):
  client.add_cog(Math(client))
