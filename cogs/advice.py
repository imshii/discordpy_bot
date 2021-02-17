import discord
from discord.ext import commands
from random import randint, choice

people_list = ['648700779003117578', '763779299354083369', '309463352885641227', '216966910770806787',
               '758894038006104085', '326446495098470420', '607392053848047691', '769007607809572886',
               '770768826072825867', '761698072345968661', '755218923959615489', '713758706516361296',
               '581251765937373184', '766424599088594965', '766424599088594965', '511962658937765888',
               '511962658937765888', '447808369483448330', '403668557331955712', '763779537267458068',
               '453653348315430944', '670782523462385666', '785184215263346699', '342738876760195072',
               '769017813956296735', '801900716557205565']

with open('ext/pickup lines.txt') as f:
    pickup_line = [str(line.rstrip()) for line in f]

with open('ext/facts.txt') as fact:
    fact_list = [str(lines.rstrip()) for lines in fact]


class Advice(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def pickup(self, ctx, *, pinged=''):
        await ctx.send(pinged + ' ' + choice(pickup_line))

    @commands.command()
    async def fact(self, ctx):
        await ctx.send(choice(fact_list))


def setup(client):
    client.add_cog(Advice(client))
