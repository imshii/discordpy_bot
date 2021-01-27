import discord
from discord.ext import commands
from random import randint


def rocky():
    rock_list = ['I got paper :roll_of_paper:,yYou lost :)', 'I got scissors :scissors:, you win :C',
                 'Damn we both got rock :rock:, reroll?']
    return rock_list[randint(0, 2)]


def papery():
    paper_list = ['I got rock :rock:, you win :C', 'I got scissors :scissors:, you lost :)',
                  'Damn we both got paper :roll_of_paper:, reroll?']
    return paper_list[randint(0, 2)]


def scissors():
    scissors_list = ['I got paper :roll_of_paper:, you win :C', 'I got rock :rock: you lost :)',
                     'Damn we both got scissors :scissors:, reroll?']
    return scissors_list[randint(0, 2)]


class Rock(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def rock(self, ctx):
        await ctx.send(rocky())

    @commands.command()
    async def paper(self, ctx):
        await ctx.send(papery())

    @commands.command()
    async def scissors(self, ctx):
        await ctx.send(scissors())


def setup(client):
    client.add_cog(Rock(client))
