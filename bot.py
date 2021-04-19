from discord.ext import commands
from discord.ext.commands import has_permissions

# Clear terminal with ".cls"
from os import system, name, listdir
from requests import get as getreq
import threading
import concurrent.futures

import discord


client = commands.Bot(command_prefix='.', description="Felicità!")


@client.event
async def on_ready():
  await client.change_presence(activity=discord.Activity(
    type=discord.ActivityType.listening, name="Felicità"))
  print(f'\n{client.user.display_name} is now online\n')


@client.command()
@has_permissions(administrator=True)
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'{extension} was loaded') and print(f'{extension} was loaded')


@client.command()
@has_permissions(administrator=True)
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  await ctx.send(f'{extension} was unloaded') and print(f'{extension} was unloaded')


@client.command()
@has_permissions(administrator=True)
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')
  await ctx.send(f'{extension} was reloaded') and print(f'{extension} was reloaded')


@client.command()
@has_permissions(administrator=True)
async def cls():
  system('cls') if name=='nt' else system('clear')


for filename in listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
    print(f'{filename} loaded')


def missing_import(ctx, imported):
  ctx.send("Sorry, this command will not work because the host is missing the import: \n {}".format(imported))


 # Suppresses errors related to those mentioned, and informing the user what went wrong
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send("Command not found")
  elif isinstance(error, commands.MissingPermissions):
    await ctx.send("Nope, not happening.")
  elif isinstance(error, commands.MissingRequiredArgument):
    await ctx.send("ugh, be more specific")
  else:
    print(error)


# You can add your token as a string, just replace the current function
# school_boy || ignis
json_tokens = getreq("http://10.0.0.32/discord").json()  # gets my tokens off a local server
client.run(json_tokens.get("school_boy"))
