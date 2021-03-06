from discord.ext import commands
from random import choice
import math

"""
# SQUARE ROOT
This is the coolest trick ever, let me explain.
Create an object that is equal to the half the number's value, here I named it square_root
Then a temporary number equivalent to zero.
Now while both numbers are not the same:
  The temp number is equal to the temp number,
  The square_root is equal to the original number divided by the temp number plus the temp number, all divided by 2.
The loop ends when the temporary number is equivalent to the square_root, making it the square root
Feel free to try this out on a calculator

Example:
number = 9
###FIRST LOOP
square_root = temp = 4.5
  square_root = (9 / 4.5 + 4.5) / 2
  square_root = 3.25
###SECOND LOOP
square_root = temp = 3.25
  square_root = (9 / 3.25 + 3.25) / 2
  square_root = 3.009

### THIS IS REPEATED UNTIL EVERY NUMBER BEFORE THE NINTH DECIMAL IS THE SAME
"""

funny_sentences = [
  "Thy shall not judge my answer of {}",
  "You think your smart, but need me to give you this answer: {}",
  "Never have I ever gotten this answer in my life: {}",
  "Yea pretty sure you got it wrong, but i'll give you the number anyways: {}",
  "Just take it and stop bothering me. {}",
  "This number is sus: {}",
  "I think the number {} just vented"
]


def getRandomFunnySentence() -> str:
  return choice(funny_sentences)


def sqrt(number) -> float:
  square_root = number / 2
  temp = 0
  while square_root!=temp:
    temp = square_root
    square_root = (number / temp + temp) / 2

  return square_root


# round the number down, no matter the decimal
def floor(integer) -> int:
  return int(integer - (integer % 1))


# rounds up the number, no matter the decimal
def ciel(integer):
  return integer + (1 - integer % 1)


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


def hero_area_formula(a: float, b: float, c: float) -> float:
  semi_peremeter: float = (a + b + c) / 2
  area: float = sqrt(semi_peremeter * (semi_peremeter - a) * (semi_peremeter - b) * (semi_peremeter - c))
  return area


def cosine_line_formula(a: float, b: float, angle: float) -> float:
  print(pow(a, 2))
  print(pow(b, 2))
  print(math.cos(angle))
  like: float = sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b * math.cos(angle))
  print(like)
  return sqrt(pow(a, 2) + pow(b, 2) - 2 * a * b * math.cos(math.radians(angle)))


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

  @commands.command()
  async def hero(self, ctx, a=None, b=None, c=None):
    if a is None or b is None or c is None:
      await ctx.send("input: .hero a b c")
      return
    await ctx.send("The area of the triangle is {0}".format(hero_area_formula(float(a), float(b), float(c))))

  # not broken anymore
  @commands.command()
  async def coslaw(self, ctx, a=None, b=None, angle=None):
    if a is None or b is None or angle is None:
      await ctx.send("input: .coslaw a b angle")
      return
    await ctx.send(getRandomFunnySentence().format(cosine_line_formula(float(a), float(b), float(angle))))

  @commands.command(aliases=["si"])
  async def slope_intercept(self, ctx, slope):
    slope_intercept = -pow(float(slope), -1)
    await ctx.send(slope_intercept)

  @commands.command()
  async def cos(self, ctx, number):
    await ctx.send(getRandomFunnySentence().format(math.cos(math.radians(float(number)))))

  @commands.command()
  async def sin(self, ctx, number):
    await ctx.send(getRandomFunnySentence().format(math.sin(math.radians(float(number)))))

  @commands.command()
  async def tan(self, ctx, number):
    await ctx.send(getRandomFunnySentence().format(math.tan(math.radians(float(number)))))

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
