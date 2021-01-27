import discord
from discord.ext import commands
from string import ascii_lowercase, ascii_uppercase, digits
import json


def custom(message):
    message_list = list(message.replace(" ", "*"))
    allowed = ''.join(ascii_uppercase + ascii_lowercase + digits + ",.?!*")
    file = open("encrypt", "r")
    file_data = file.read()
    dumped_data = json.loads(file_data)
    for char in message_list:
        for ascii in allowed:
            if char == ascii:
                message_list[message_list.index(char)] = dumped_data.get(char)

    encrypted = "".join(message_list[n] for n in range(len(message_list)))
    return encrypted


class Encrypt(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def encrypt(self, ctx, *, message):
        try:
            await ctx.channel.purge(limit=1)
        except AttributeError:
            pass
        await ctx.author.send("```fix\n" + custom(message) + "\n```")


def setup(client):
    client.add_cog(Encrypt(client))
