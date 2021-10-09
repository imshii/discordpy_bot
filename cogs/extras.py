from discord.ext import commands
from random import choice, randint
from time import strftime, perf_counter

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
  async def invite(self, ctx):
    await ctx.send('```Administrator invite: https://discord.com/api/oauth2/'
                   'authorize?client_id=785192185796231188&permissions=8&scope=bot'
                   '\n'
                   'No permissions invite: https://discord.com/api/oauth2/'
                   'authorize?client_id=785192185796231188&permissions=0&scope=bot```')

  @commands.command()
  async def strati(self, ctx):
    await ctx.send(
      'https://media.discordapp.net/attachments/782103157546287124/'
      '785596636269117535/egg3.PNG?width=1090&height=683')

  @commands.command()
  async def stef(self, ctx):
    await ctx.send('https://media.discordapp.net/attachments/782103157546287124/'
                   '785171862761373696/image0.jpg?width=263&height=468')

  @commands.command()
  async def clean(self, ctx):
    await ctx.send(
      'https://media.discordapp.net/attachments/760678854334611461/'
      '771198231219666954/Mr.Clean.PNG?width=400&height=193')

  @commands.command()
  async def damato(self, ctx):
    await ctx.send(choice(Storage.damato_list))

  @commands.command()
  async def kien(self, ctx):
    await ctx.send(
      'https://media.discordapp.net/attachments/760678854334611461/'
      '778794093223870504/ahmad-customer-service_-_Discord_2020-11-18_8_22_51_PM_2.png')

  @commands.command()
  async def rockets(self, ctx):
    await ctx.send('https://media.discordapp.net/attachments/760678854334611461/765707585781104672/imageh0.png')

  @commands.command()
  async def nasa(self, ctx):
    await ctx.send(
      'https://media.discordapp.net/attachments/760678854334611461/'
      '778451995798274048/unknown.png?width=1010&height=701')

  @commands.command()
  async def gang(self, ctx):
    await ctx.send('https://media.discordapp.net/attachments/760678854334611461/778722611629654026/unknown.png')

  @commands.command()
  async def obama(self, ctx):
    await ctx.send(
      'https://images-ext-2.discordapp.net/external/vvBzIMXepxOCrsRm_DxdiC_RrUnPXIwo3JM2ppSQhSA/'
      'https/media.discordapp.net/attachments/473658772099694612/783903546520371250/bomabomb.gif')

  @commands.command()
  async def teacher(self, ctx):
    await ctx.send('<@453653348315430944> or <@769007607809572886> **WE NEED HELP OMG PLEASE HELP**')

  @commands.command()
  async def damiano(self, ctx):
    await ctx.send('https://tenor.com/view/persongee-morphs-morphing-melting-faces-gif-8217558')

  @commands.command()
  async def pong(self, ctx):
    await ctx.send('Ping! :ping_pong:')

  @commands.command(aliases=[".."])
  async def vic(self, ctx):
    await ctx.send(choice(Storage.vic_list))

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
    if str(ctx.author.id)!="648700779003117578":
      await ctx.send(f"{ctx.author.name} {choice(Storage.equilizers)} kiera")
      return
    await ctx.send("You are not worthy of that command! <:thor_hammer:804921376166641714>")

  @commands.command(aliases=["yip", "Yip"])
  async def workout(self, ctx):
    await ctx.send(Storage.twerking_stickmen)

  @commands.command(aliases=["poggers", "Pog"])
  async def pog(self, ctx):
    await ctx.send(Storage.poggers_kiss)

  @commands.command(aliases=["play", "pause", "skip", "fs", "join", "clear", "queue"])
  async def ignoreMusic(self, ctx):
    pass


  @commands.command(aliases=["dog", "...", "."])
  async def quokka(self, ctx):
    await ctx.send(choice(Storage.quokka))

  @commands.command()
  async def fbi(self, ctx):
    await ctx.message.delete()
    await ctx.send("Fbi tracking that btw ^")

  @commands.command(aliases=["happyness", "happiness"])
  async def felicita(self, ctx):
    await ctx.send(Storage.felicita_lyrics)

  @commands.command()
  async def yellow(self, ctx):
    await ctx.send("Lol bad colour")

  @commands.command(aliases=["nerds"])
  async def nerd(self, ctx):
    await ctx.send(choice(Storage.blizzard_list))

  @commands.command()
  async def toilet(self, ctx):
    await ctx.send("wtf were you expecting???")


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
  blizzard_list = [
    "https://media.discordapp.net/attachments/763837055163170856/833703230890180668/Nerds_blizzard.jpg?width=455&height=666",
    "go study ||nerd||"
  ]

  coins = [
           'https://user-images.githubusercontent.com/75594425/101301574-3e88a080-3807-11eb-867b-d70868125ff8.png',
           'https://user-images.githubusercontent.com/75594425/101301529-1c8f1e00-3807-11eb-962a-e76f2f81415d.png'
           ]

  quokka = ["https://media.discordapp.net/attachments/763837055163170856/806175155285131264/badass.png",
            "https://media.discordapp.net/attachments/763837055163170856/806175166706745414/65165a16d5a1dad.png",
            "https://media.discordapp.net/attachments/763837055163170856/806175174898089994/someone-is-ready-for-winter.png",
            "https://media.discordapp.net/attachments/763837055163170856/806175414325870642/image1.png",
            "https://media.discordapp.net/attachments/763837055163170856/806175426405466182/quokka-smiling-for-the-camera-at-sunset.png",
            "https://media.discordapp.net/attachments/763837055163170856/806175438262108180/12aff3d9d27de3663568eecfd8b778f0.png",
            "https://media.discordapp.net/attachments/763837055163170856/806175446583476254/quokka-leaf-smile-cute.png"]

  vic_list = [
    "https://cdn.discordapp.com/attachments/782103157546287124/814139025278500904/2011_ford_crown_victoria-pic-1139495547192806221-1024x768.png",
    "https://cdn.discordapp.com/attachments/782103157546287124/814138928075374592/424x-.png",
    "https://cdn.discordapp.com/attachments/782103157546287124/814138823046725652/8c9ba8e56e852b4029b873f3912e79f6.png",
    "https://cdn.discordapp.com/attachments/782103157546287124/814138712249597993/1955-ford-fairlane-crown-victoria-front.png",
    "https://cdn.discordapp.com/attachments/782103157546287124/814138667391385601/1955_Ford_Crown_Victoria_2.png",
    "https://cdn.discordapp.com/attachments/782103157546287124/814138302981472264/unknown.png",
    "https://cdn.discordapp.com/attachments/782103157546287124/814138253384613918/unknown.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138706918768650/images.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138637360431164/images.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138611674120252/images.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138551196581898/images.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138551196581898/images.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138528673169468/images.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138515230687272/2Q.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138476353552454/9k.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138449074061371/Z.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138433790279730/2Q.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138411547361341/Z.png",
    "https://cdn.discordapp.com/attachments/805111959724490782/814138382472970260/Ford_Crown_Victoria_LX.png"]

  poggers_kiss = "https://tenor.com/view/poggers-anime-girls-kissing-pog-gif-18050577"

  equilizers = ["<", ">"]

  mustang_brrr = "https://images-ext-1.discordapp.net/external/JqMrmxPfMjAVO8D0t2O17EBJMcIuxHj1V3kw5N3zHvk/https/" \
                 "media.discordapp.net/attachments/782103157546287124/803321887161319504/voinea.gif"

  twerking_stickmen = "https://tenor.com/view/butts-booty-pop-booty-bump-twerk-ass-shake-gif-5592141"

  bibre_link = "https://pastebin.com/raw/zX6zjTb5"

  vas_list = ["https://media.discordapp.net/attachments/782103157546287124/806746845690593290/image0.jpg",
              "https://media.discordapp.net/attachments/782103157546287124/806744561899798528/unknown.png",
              "https://media.discordapp.net/attachments/782103157546287124/806743460626825226/unknown.png",
              "https://media.discordapp.net/attachments/782103157546287124/806740948465745951/unknown.png",
              "https://media.discordapp.net/attachments/782103157546287124/806739794411520000/unknown.png",
              "https://media.discordapp.net/attachments/782103157546287124/806736829621207090/unknown.png",
              "https://media.discordapp.net/attachments/782103157546287124/806731652452974602/146879139_735015937154224_9012277692766871897_n.png"]

  damato_list = [
    'https://media.discordapp.net/attachments/763837055163170856/'
    '786247443213582396/20201120_230436.jpg?width=177&height=383',
    'https://media.discordapp.net/attachments/760678854334611461/778721257713303612/unknown.png'
  ]

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
