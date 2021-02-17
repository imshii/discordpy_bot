from discord.ext import commands

import discord
import json


class Tests(commands.Cog):
  def __init__(self, client):
    client.self = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command(aliases=["Test", "tests", "quiz"])
  async def test(self, ctx, solution="", test="", *, time="Unspecified"):
    file = open("tests.json", "r")

    try:
      json_file = json.loads(file.read())
    except json.decoder.JSONDecodeError:
      json_file = {}
    if solution=="" or solution=="list":

      if json_file=={}:
        await ctx.send("There are no tests!! :partying_face:")
        return
      key_list = json_file.keys()
      values = ""
      for key in key_list:
        values += f"{key} : {json_file.get(key)}\n"
      embed = discord.Embed(colour=discord.Colour.random())
      embed.add_field(name="Tests:", value=values)
      await ctx.send(embed=embed)
      return

    elif solution=="add":
      await ctx.send(f"{test} successfully added, get to studying :book:")
      new_test = {test: time}  # puts The test and time in a json format
      json_file.update(new_test)  # adds it to the existing json list

    elif solution=="del" or solution=="remove":
      try:
        del (json_file[test])
        print(json_file)
      except KeyError:
        await ctx.send(f"{test} is not in the library of tests")
        return
      await ctx.send(f"{test} has gone bye bye, I hope you passed :fingers_crossed:")
    else:
      await ctx.send(".test list/add/remove **test** **date**")
      return

    file.close()
    json_dumped = json.dumps(json_file, indent=2)  # turning it into a string to write to the file
    print(json_dumped)
    writable_file = open("tests.json", "w")
    writable_file.write(json_dumped)  # overwriting current data in the file with new json list
    writable_file.close()


def setup(client):
  client.add_cog(Tests(client))
