from discord.ext import commands

import discord


def sqrt(number) -> float:
  square_root = number / 2
  temp = 0
  while square_root!=temp:
    temp = square_root
    square_root = (number / temp + temp) / 2

  return square_root


def floor(integer) -> float:  # remove decimals
  decimals = integer % 1
  print(decimals)
  if decimals > 0:
    return integer - decimals
  return integer


def abv(integer) -> float:  # absolute value
  if integer < 0:
    return -integer
  return integer


def pythagorean_c(a, b) -> float:
  c = sqrt(pow(a, 2) + pow(b, 2))
  return c


def pythonagorean_ab(c, o) -> float:
  other = sqrt(pow(c, 2) - pow(o, 2))
  return other


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
  async def slope(self, ctx, *, points):
    dict_points = points_lister(points)
    x = dict_points.get("X")
    y = dict_points.get("Y")

    if len(x) + len(y)==4:  # This check that they each are 2 ints long
      slope = float((y[1] - y[0]) / (x[1] - x[0]))
      await ctx.send(f"The slope of yor line is {slope}")
    else:
      await ctx.send("Insert as such: x2 y2 x1 y1")
      return

  @commands.command(aliases=["lol", "line_length"])
  async def length_of_line(self, ctx, *, inputted):

    returned_dic = points_lister(inputted)  # get the x and y into lists
    x = returned_dic.get("X")
    y = returned_dic.get("Y")  # objects into lists

    x2 = x[0]
    x1 = x[1]
    y2 = y[0]
    y1 = y[1]  # makes the equation a lot more dynamic and simple to read

    # this replicates the formula of (y2-y1)**2 + (x2-x1)**2 square rooted.
    # It gets the  of a line using their x and y coordinates
    length = sqrt(pow((y2 - y1), 2) + pow((x2 - x1), 2))
    await ctx.send("The distance of the line {0}/{1} to {2}/{3} is {4} units".format(x2, y2, x1, y1, length))

  @commands.command(aliases=["si"])
  async def slope_intercept(self, ctx, slope):
    slope_intercept = -pow(float(slope), -1)
    await ctx.send(slope_intercept)

  @commands.command(aliases=["point_line", "pl", "p_l"])
  async def dpoint_line(self, ctx, *, equation):
    equation = equation.split()

    A = float(equation[0])
    B = float(equation[2])
    C = float(equation[4])
    h = float(equation[1])
    k = float(equation[3])

    final_distance = abv(
      (A * h) + (B * k) + C
    ) / sqrt(pow(A, 2) + pow(B, 2))

    await ctx.send(final_distance)


def setup(client):
  client.add_cog(Math(client))
