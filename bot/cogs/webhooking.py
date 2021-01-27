import discord
from discord.ext import commands
from urllib.request import Request, urlopen
from json import dumps


def webbhook(webhook, message, username, avatar):
    headers = {
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 '
                      'Safari/537.11 '
    }
    payload = dumps({'content': message, 'username': username, 'avatar_url': avatar})
    req = Request(webhook, data=payload.encode(), headers=headers)
    urlopen(req)


# def correct_webhook(channel_id):
#     if input == '759424516052615209':
#         webbhook(
#             webhook='https://discord.com/api/webhooks/762019327620546580/'
#                     'aQdYJADploKiupCrUte8ckPrXnIzehhiqWZxyCUZJZO2U0fyNg_5ND5c5foGtaIdtHuP',
#             message='Sup dude',
#             username='John f Kennedy',
#             avatar='https://images.fineartamerica.com/images/artworkimages/'
#                    'mediumlarge/1/canada-maple-leaf-deer-devil-designs.jpg'
#         )


# webbhook(message='',
#             username="", avatar="",
#             webhook='')


class WebTest(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        pass

    @commands.command()
    async def hyperlink(self, ctx, message='', link=''):
        embedVar = discord.Embed() # title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Link", value=f"[{message}]({link})", inline=True)
        await ctx.send(embed=embedVar)

    @commands.command()
    async def mimic(self, ctx, *, stuff=''):
        await webbhook(
            webhook='https://discord.com/api/webhooks/790977831085539348/'
                    'P7DphtHNxuExg88ZyaQJzFD9GJHbVnWd7VE0Sti30PhqxC91eFonXcfL3iFhAb9RnpUP',
            message=f'Hi {ctx.author.display_name}! It looks like we have the same name :)' if stuff == '' else f'[{stuff}](https://youtube.com)',
            username=str(ctx.author.display_name),
            avatar=str(ctx.author.avatar_url)
        )


def setup(client):
    client.add_cog(WebTest(client))
