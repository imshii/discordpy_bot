import discord
import requests
import concurrent.futures

from time import sleep
from discord.ext import commands


def uuid_to_name(uuid):
  response = requests.get("https://api.mojang.com/user/profiles/{}/names".format(uuid))
  print(response.json()[0].get("name"))
  name_list.append(response.json()[0].get("name"))


def mystic_api(mystics: list):
  switcher = {"not_gladiator": "less_damage_nearby_players",
              "mirror": "immune_true_damage",
              "instaboom": "instaboom_tnt",
              "gold_bump": "gold_per_kill",
              "gold_bump": "gold_strictly_kills",
              "executioner": "melee_execute",
              "eggs": "eggs",
              "paparazzi": "paparazzi",
              "trash_panda": "trash_panda",
              "gold_boost": "gold_boost",
              "golden_hearts": "absorption_on_kill",
              "self_checkout": "max_bounty_self_claim",
              "double_jump": "double_jump",
              "lodbrok": "increase_armor_drops",
              "beat_the_spammers": "melee_damage_vs_bows",
              "streaker": "streak_xp",
              "lifesteal": "melee_heal_on_hit",
              "xp_boost": "xp_boost",
              "sierra": "gold_per_diamond_piece",
              "pickpocket": "pickpocket",
              "somber": "somber",
              "venom": "venom",
              "misery": "misery",
              "spite": "spite",
              "combo_heal": "melee_combo_heal",
              "combo_speed": "melee_combo_speed",
              "critically_rich": "gold_per_crit"}

  for mystic in mystics:
    mystic_there = switcher.get(mystic)
    if mystic_there:
      mystics[mystics.index(mystic)] = mystic_there
    else:
      del mystics[mystics.index(mystic)]

  mystic1 = mystic2 = mystic3 = ""

  if len(mystics)==1:
    mystic1 = mystics[0] + "0+"
  if len(mystics)==2:
    mystic2 = "," + mystics[1] + "0+"
  if len(mystics)==3:
    mystic3 = "," + mystics[2] + "0+"

  url = "https://pitpanda.rocks/api/itemsearch/{}{}{}".format(mystic1, mystic2, mystic3)
  print(url)
  response = requests.get(url)
  print(response.json())
  return response.json()


class MysticSearch(commands.Cog):
  def __init__(self, client):
    self.client = client

  @commands.Cog.listener()
  async def on_ready(self):
    pass

  @commands.command()
  async def mystic(self, ctx, *, mystics):
    mystic_list = [mystic for mystic in mystics.split(" ")]
    uuid_list = []
    global name_list
    name_list = []
    for item in mystic_api(mystic_list).get("items"):
      uuid_list.append(item.get("owner"))

    print(uuid_list)

    for uuid in uuid_list:
      concurrent.futures.ThreadPoolExecutor().submit(uuid_to_name, uuid, deamon=True)
    n, i = 1, 0
    while n > i:
      n = i = len(name_list)
      sleep(0.3)
      n = len(name_list)
    print(name_list)
    await ctx.send(str(name_list))


def setup(client):
  client.add_cog(MysticSearch(client))
