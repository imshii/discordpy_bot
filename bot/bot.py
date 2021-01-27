from discord.ext import commands
from discord.ext.commands import has_permissions
from tokens import school_boy, ignis

# CheckFailure
from os import system, name, listdir

from time import sleep


client = commands.Bot(command_prefix='.')


# , help_command=None


@client.event
async def on_ready():
    print(f'\n{client.user.display_name} is now online\n')
    # while True:
    #     online_status()
    #     sleep(5)


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
    system('cls') if name == 'nt' else system('clear')


for filename in listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
        print(f'{filename} loaded')

# ignis or school_boy
client.run(ignis())
