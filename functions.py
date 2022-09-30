import json
import discord
import id
import random

async def open_account(user):
    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["Correct"] = 0
        users[str(user.id)]["Wrong"] = 0

    with open("data_file.json", "w") as f:
        json.dump(users, f)
    return True


async def get_bank_data():
    with open("data_file.json", "r") as f:
        users = json.load(f)

    return users


async def update_bank(user, change=0, mode='Correct'):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open('data_file.json', 'w') as f:
        json.dump(users, f)
    bal = users[str(user.id)]['Correct']
    return bal

async def del_check(ctx):
  if not isinstance(ctx.channel, discord.channel.DMChannel):
    role = discord.utils.get(ctx.guild.roles, name="gecpilled")
  msg = ctx.content.replace(" ", "").lower()
  for x in id.gec_block:
    if msg.count(x) >= 4 and (role not in ctx.author.roles or isinstance(ctx.channel, discord.channel.DMChannel)):
      return True
  if "!say" in msg and ctx.author.id == id.Nolan_id:
    return True
  return False

def simulate_wins(player_list, rounds):
    for i in range(0,rounds):
        for t in range(0, len(player_list), 2):
            player_list[t] += 1  
        player_list.sort()
        if i == 0:
          random.shuffle(player_list)
    return player_list