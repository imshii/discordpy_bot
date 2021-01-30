from discord.ext import commands
from random import choice
from random import randint

import discord


class Extras(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  async def eight(self, ctx):
    await ctx.send(choice(Storage.eight_list))

  @commands.command(aliases=["pp"])
  async def penis(self, ctx):
    await ctx.send('```' + str(randint(0, 10) * '=' + '>' + '```'))

  @commands.command()
  async def say(self, ctx, *, message):
    await ctx.send(f'As per the great {ctx.author.display_name} has said, "{message}".')

  @commands.command()
  async def ping(self, ctx):
    await ctx.send('Pong! :ping_pong:')

  @commands.command()
  async def pong(self, ctx):
    await ctx.send('Ping! :ping_pong:')

  @commands.command(aliases=["coin"])
  async def toss(self, ctx):
    await ctx.send(choice(Storage.coins))

  @commands.command()
  async def kiera(self, ctx):
    if ctx.author.id!="648700779003117578":
      await ctx.send(f"{str(ctx.author)[:-5]} {choice(Storage.equilizers)} kiera")
    else:
      await ctx.send("You are not worthy of that command! <:thor_hammer:804921376166641714>")

  @commands.command(aliases=["yip", "Yip"])
  async def workout(self, ctx):
    await ctx.send(Storage.twerking_stickmen)

  @commands.command(aliases=["poggers", "Pog"])
  async def pog(self, ctx):
    await ctx.send(Storage.poggers_kiss)

  @commands.command(aliases=["happyness", "happiness"])
  async def felicita(self, ctx):
    await ctx.send(Storage.felicita_lyrics)


def setup(client):
  client.add_cog(Extras(client))


class Storage:
  eight_list = ['https://media.discordapp.net/attachments/732740996990894171/785330053730664458/4.png',
                'https://media.discordapp.net/attachments/732740996990894171/785330084148019210/19.png',
                'https://media.discordapp.net/attachments/732740996990894171/785330369578139658/7.png',
                'https://media.discordapp.net/attachments/732740996990894171/785330548439646219/6.png',
                'https://media.discordapp.net/attachments/732740996990894171/785330562340487268/12.png',
                'https://media.discordapp.net/attachments/732740996990894171/785330698827333642/18.png',
                'https://media.discordapp.net/attachments/732740996990894171/785330698827333642/18.png',
                'https://media.discordapp.net/attachments/732740996990894171/785330844747300944/13.png',
                'https://media.discordapp.net/attachments/732740996990894171/785330916838342676/3.png',
                'https://media.discordapp.net/attachments/732740996990894171/785331034023526430/10.png',
                'https://media.discordapp.net/attachments/732740996990894171/785331249409032212/4.png',
                'https://media.discordapp.net/attachments/732740996990894171/785331358036656188/12.png']

  coins = ['https://user-images.githubusercontent.com/75594425/101301574-3e88a080-3807-11eb-867b-d70868125ff8.png',
           'https://user-images.githubusercontent.com/75594425/101301529-1c8f1e00-3807-11eb-962a-e76f2f81415d.png'
           ]

  poggers_kiss = "https://tenor.com/view/poggers-anime-girls-kissing-pog-gif-18050577"

  equilizers = ["<", ">"]

  twerking_stickmen = "https://tenor.com/view/butts-booty-pop-booty-bump-twerk-ass-shake-gif-5592141"

  felicita_lyrics = """Felicità
È tenersi per mano andare lontano, la felicità
È il tuo sguardo innocente in mezzo alla gente, la felicità
È restare vicini come bambini, la felicità
Felicità
Felicità
È un cuscino di piume, l'acqua del fiume che passa che va
È la pioggia che scende dietro alle tende, la felicità
È abbassare la luce per fare pace, la felicità
Felicità
Felicità
È un bicchiere di vino con un panino, la felicità
È lasciarti un biglietto dentro al cassetto, la felicità
È cantare a due voci quanto mi piaci, la felicità
Felicità
Senti nell'aria c'è già
La nostra canzone d'amore che va
Come un pensiero che sa di felicità
Senti nell'aria c'è già
Un raggio di sole più caldo che va
Come un sorriso che sa di felicità
Felicità
È una sera a sorpresa la luna accesa e la radio che va
È… """
