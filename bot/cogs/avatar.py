import discord
from discord.ext import commands


class Avatar(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def av(self, ctx):
        await ctx.send(ctx.author.avatar_url)

    @commands.command()
    async def who(self, ctx, member: discord.Member):
        embed = discord.Embed(colour=discord.Colour.blue(), title=member.display_name)
        embed.set_thumbnail(url=member.avatar_url)
        embed.add_field(name="ID", value=member.id, inline=True)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f'Requested by {ctx.author.display_name}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Avatar(client))
