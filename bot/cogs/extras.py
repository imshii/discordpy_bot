import discord
from discord.ext import commands
from random import choice

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


class Extras(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def eight(self, ctx):
        await ctx.send(choice(eight_list))


def setup(client):
    client.add_cog(Extras(client))
