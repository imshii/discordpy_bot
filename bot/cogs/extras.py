from discord.ext import commands
from random import choice
from random import randint
from time import strftime
from time import perf_counter

import discord
import requests


class Extras(commands.Cog):

  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  async def ping(self, ctx):
    start = perf_counter()
    await ctx.message.delete()
    stop = perf_counter()
    ping = round((stop - start) * 1000, None)
    embed = discord.Embed(colour=discord.Colour.red())
    embed.add_field(name="Pong! :ping_pong:", value=str(ping) + " ms", inline=True)
    embed.set_footer(text=f"Requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def pong(self, ctx):
    await ctx.send('Ping! :ping_pong:')

  @commands.command()
  async def eight(self, ctx):
    await ctx.send(choice(Storage.eight_list))

  @commands.command(aliases=["pp", "penis"])
  async def size(self, ctx):
    await ctx.send('```' + str(randint(0, 10) * '=' + '>' + '```'))

  @commands.command()
  async def time(self, ctx):
    embed = discord.Embed(colour=discord.Color.dark_blue())
    embed.add_field(name=strftime("%A %h %d, %Y"), value=strftime("%l:%M:%I %p"))
    embed.set_footer(text=f"Time requested by {ctx.author.name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

  @commands.command()
  async def say(self, ctx, *, message):
    await ctx.send(f'As per the great {ctx.author.display_name} has said, "{message}".')

  @commands.command(aliases=["coin"])
  async def toss(self, ctx):
    await ctx.send(choice(Storage.coins))

  @commands.command(aliases=["drip"])
  async def vas(self, ctx):
    await ctx.send(choice(Storage.vas_list))

  @commands.command(aliases=["creator"])
  async def author(self, ctx):
    await ctx.send(Storage.author_ascii)

  @commands.command()
  async def bibre(self, ctx):
    await ctx.send(requests.get(Storage.bibre_link).text)

  @commands.command()
  async def vroom(self, ctx):
    await ctx.send(Storage.mustang_brrr)

  @commands.command()
  async def kiera(self, ctx):
    if ctx.author.id!="648700779003117578":
      await ctx.send(f"{ctx.author.name} {choice(Storage.equilizers)} kiera")
    else:
      await ctx.send("You are not worthy of that command! <:thor_hammer:804921376166641714>")

  @commands.command(aliases=["yip", "Yip"])
  async def workout(self, ctx):
    await ctx.send(Storage.twerking_stickmen)

  @commands.command(aliases=["poggers", "Pog"])
  async def pog(self, ctx):
    await ctx.send(Storage.poggers_kiss)

  @commands.command(aliases=["...", "dog", ".."])
  async def quokka(self, ctx):
    await ctx.send(choice(Storage.quokka))

  @commands.command()
  async def fbi(self, ctx):
    await ctx.message.delete()
    await ctx.send("Fbi tracking that btw ^")

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

  quokka = ["https://media.discordapp.net/attachments/763837055163170856/806175155285131264/badass.png", "https://media.discordapp.net/attachments/763837055163170856/806175166706745414/65165a16d5a1dad.png", "https://media.discordapp.net/attachments/763837055163170856/806175174898089994/someone-is-ready-for-winter.png", "https://media.discordapp.net/attachments/763837055163170856/806175414325870642/image1.png", "https://media.discordapp.net/attachments/763837055163170856/806175426405466182/quokka-smiling-for-the-camera-at-sunset.png", "https://media.discordapp.net/attachments/763837055163170856/806175438262108180/12aff3d9d27de3663568eecfd8b778f0.png", "https://media.discordapp.net/attachments/763837055163170856/806175446583476254/quokka-leaf-smile-cute.png"]

  poggers_kiss = "https://tenor.com/view/poggers-anime-girls-kissing-pog-gif-18050577"

  equilizers = ["<", ">"]

  mustang_brrr = "https://images-ext-1.discordapp.net/external/JqMrmxPfMjAVO8D0t2O17EBJMcIuxHj1V3kw5N3zHvk/https/" \
                 "media.discordapp.net/attachments/782103157546287124/803321887161319504/voinea.gif"

  twerking_stickmen = "https://tenor.com/view/butts-booty-pop-booty-bump-twerk-ass-shake-gif-5592141"

  bibre_link = "https://pastebin.com/raw/zX6zjTb5"

  vas_list = ["https://media.discordapp.net/attachments/782103157546287124/806746845690593290/image0.jpg", "https://media.discordapp.net/attachments/782103157546287124/806744561899798528/unknown.png", "https://media.discordapp.net/attachments/782103157546287124/806743460626825226/unknown.png", "https://media.discordapp.net/attachments/782103157546287124/806740948465745951/unknown.png", "https://media.discordapp.net/attachments/782103157546287124/806739794411520000/unknown.png", "https://media.discordapp.net/attachments/782103157546287124/806736829621207090/unknown.png", "https://media.discordapp.net/attachments/782103157546287124/806731652452974602/146879139_735015937154224_9012277692766871897_n.png"]

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
  author_ascii = """Kinda broken atm lol discord is annoying
  """