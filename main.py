#"kill 1" in shell if rando errors with curly brackets
#"python3 -m pip install --upgrade pytube" in shell if download doesnt work

import os
import discord
from discord.ext import commands
import id
import random
import json
import functions
import asyncio
import time
import math as maf
import glob
import pytube
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.environ.get('TOKEN')
deleted = []
sender = []
edited = []
esender = []

intents = discord.Intents.default()
intents.members = True  # Subscribe to the Members intent
# intents.presences = True
# bot = commands.Bot(command_prefix='!', case_insensitive=True,activity=discord.Game(name = "☝️ #1 girlboss!!"))
bot = commands.Bot(command_prefix='!', case_insensitive=True, intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):

    #gec
    #gec
    if await functions.del_check(message):
        await message.delete()
    """
  #censorship
    if message.author.id == id.Zayd_id:
  
      censored = False
      with open("censored.txt", "r") as file:
        words = file.read().split("\n")
  
        for word in words:
          if word in ctx:
            censored = True
  
      if censored == True: 
        with open("deleted.txt","a") as file:
          file.write(str(message.content + '\n'))
        await message.delete()
        print("censored")
 """
    #get fucked

    if "get fucked" in message.content.lower():
        await message.channel.send("loser")
    """if "get fucked" in message.content.lower() and message.author.id == id.Zayd_id:
    await message.channel.send("imagine copying ashton what a bozo")"""

    #uwu
    if ("uwu" in message.content.lower() and message.author.id != id.Ashton_id
        ) and message.content != "I am an egirl uwu :pensive:":
        if message.author == bot.user:
            await message.channel.send("I am an egirl uwu :pensive:")
        else:
            await message.channel.send("are you an egirl?")

    await bot.process_commands(message)


@bot.event
async def on_message_delete(message):
    if await functions.del_check(message):
        return

    global deleted
    global sender
    deleted.insert(0, message.content)
    sender.insert(0, message.author.display_name)


@bot.command()
async def snipe(message, position=1):
    global deleted
    global sender
    pos = int(position) - 1
    try:
        await message.channel.send(f'{sender[pos]} sent "{deleted[pos]}"')
    except:
        await message.channel.send("no one has deleted anything bozo")


@bot.command(hidden=True)
async def status(message, *, status):
    if message.author.id == id.Nolan_id:
        if status.lower() != "none":
            await bot.change_presence(activity=discord.Game(name=status))
        else:
            await bot.change_presence(activity=discord.Game(name=""))


@bot.event
async def on_message_edit(message_before, message_after):
    global esender
    global edited
    edited.insert(0, message_before.content)
    esender.insert(0, message_before.author)


@bot.command(hidden=True)
async def esnipe(message, position=1):
    if message.author.id != id.Nolan_id and message.author.id != id.Emma_id and message.author.id != id.Ryan_id and message.author.id != id.Eva_id:
        await message.channel.send("you don't have access to this")
        return
    global esender, edited
    pos = int(position) - 1
    try:
        await message.channel.send(
            f'{esender[pos]} edited their message saying "{edited[pos]}"')
    except:
        await message.channel.send("no one has edited anything")


@bot.command(hidden=True)
async def sclear(message):
    if message.author.id == id.Nolan_id:
        global deleted, sender
        deleted = None
        sender = None


@bot.command(hidden=True)
async def eclear(message):
    if message.author.id == id.Nolan_id:
        global esender, edited
        esender = None
        edited = None


@bot.command(hidden=True)
async def bozo(message, delta=0):
    await message.channel.send("this feature has been removed")


"""  file = open("bozo.txt", 'r')
  counter = int(file.read())
  if message.author.id in id.bozo_permitted or message.author == bot.user:
    counter += delta
    file.close()
    file = open("bozo.txt", 'w')
    file.write(str(counter))
  else:
    if delta != 0:
      await message.channel.send("you don't have perms to add bozo")
  await message.channel.send("Zayd's bozo counter: " + str(counter))
"""


@bot.command()
async def quote(message, *, search=None):
    if message.author.id == id.Owen_id:
        return
    if message.channel.id != 940070876345434144:
        return
    response = ""
    if search != None:
        search = search.lower()
    with open("quotes.txt", "r") as file:
        quote_list = file.read().split("\n")
        quote_list.pop()
    if search == None:
        response = random.choice(quote_list)

    elif search == 'latest' or search == "l":
        response = (quote_list[-2])

    elif search.isdigit():
        amount = int(search)
        response = (quote_list[amount - 1])

    else:
        for i in quote_list:

            if search in i.lower():
                response += i + '\n'
        if response == "":
            response = ("no results")
    if len(response) < 2000:
        await message.channel.send(response)
    else:
        with open('response.txt', 'w') as file:
            file.write(response)
        with open("response.txt", "r") as file:
            await message.send(file=discord.File(file, "response.txt"))


@bot.command()
async def quote_list(ctx):
    if ctx.channel.id != 940070876345434144:
        return
    with open("quotes.txt", "rb") as file:
        await ctx.send(file=discord.File(file, "quotes.txt"))


@bot.command()
async def add_quote(message, *, quote):
    if message.channel.id != 940070876345434144:
        return
    with open("quotes.txt", "a") as file:
        file.write('"' +
                   quote.replace('“', '"').replace('”', '"').strip("\"") +
                   '"' + "\n")
        await message.message.add_reaction('✅')


@bot.command(aliases=['rad'])
async def radical(message):
    quote = random.choice(id.radical_quotes)
    await message.channel.send(quote)


@bot.command()
async def vibe(message):
    vibes = random.choice(id.vibes)
    await message.channel.send(vibes)


@bot.command()
@commands.has_role('gecpilled')
async def gec(message, amount=363):

    if amount <= 500:
        await message.channel.send("gec " * amount)
    else:
        a_messages = maf.floor(amount / 500)
        for i in range(a_messages):
            await message.channel.send("gec " * 500)
        new_amount = amount % 500
        await message.channel.send("gec " * new_amount)


@bot.command()
@commands.has_role('gay >:(')
async def gay(message, amount=69):

    if amount == 'slur':
        with open("quotes.txt", "r") as file:
            quote_list = file.read().split("\n")
        gay_quotes = []

    if amount <= 500:
        await message.channel.send("gay " * amount)
    else:
        a_messages = maf.floor(amount / 500)
        for i in range(a_messages):
            await message.channel.send("gay " * 500)
        new_amount = amount % 500
        await message.channel.send("gay " * new_amount)


@bot.command()
async def who(message, asked):
    if asked == "asked":
        await message.channel.send("not me bozo")


@bot.command()
async def math(message, c='but', type=None):
    if type == None:
        x = random.randint(1, 99)
        y = random.randint(1, 99)
        ans = str(x + y)
        await message.channel.send(f'whats {x} + {y}?')
    elif type == "hard":
        x = random.randint(1, 99)
        y = random.randint(1, 99)
        ans = str(x * y)
        await message.channel.send(f'whats {x} * {y}?')
    elif type == "harder":
        x = random.randint(99, 200)
        y = random.randint(99, 200)
        ans = str(x * y)
        await message.channel.send(f'whats {x} * {y}?')
    elif type == "hardest":
        x = random.randint(498, 964)
        y = random.randint(500, 1000)
        ans = str(x * y)
        await message.channel.send(f'whats {x} * {y}?')
    elif type == "eva":
        x = random.randint(0, 10)
        y = random.randint(0, 10)
        ans = str(x * y)
        await message.channel.send(f'whats {x} * {y}?')
    elif type == "69":
        x = random.randint(1, 68)
        y = 69 - x
        ans = str(x + y)
        await message.channel.send(f'whats {x} + {y}?')
    else:
        message.channel.send("nah thats not the right type")
        return

    def check(m):
        return m.channel == message.channel and message.author == m.author and m.content.isnumeric(
        )

    msg = await bot.wait_for("message", check=check)
    await functions.open_account(message.author)
    users = await functions.get_bank_data()

    if msg.content == ans:
        await message.channel.send("noice")
        if type == None:
            users[str(message.author.id)]["Correct"] += 1
        elif type == "hard":
            users[str(message.author.id)]["Correct"] += 2
        elif type == "harder":
            users[str(message.author.id)]["Correct"] += 5
        elif type == "hardest":
            users[str(message.author.id)]["Correct"] += 12
    else:
        await message.channel.send(f"nah it was {ans}")
        users[str(message.author.id)]["Wrong"] += 1
    with open("data_file.json", 'w') as f:
        json.dump(users, f)


@bot.command(aliases=['bal'])
async def balance(ctx, member: discord.Member = None):
    if member == None:
        member = ctx.author

    await functions.open_account(member)
    user = member

    users = await functions.get_bank_data()

    amt = users[str(user.id)]["Correct"]

    em = discord.Embed(title=f'{member.display_name} Balance',
                       color=discord.Color.red())
    em.add_field(name="Wallet Balance", value=amt)
    await ctx.send(embed=em)


@bot.command(aliases=['lb', 'top'])
async def leaderboard(message, x=5):
    users = await functions.get_bank_data()
    leader_board = {}
    total = []
    for user in users:
        name = int(user)
        total_amount = users[user]["Correct"]
        leader_board[total_amount] = name
        total.append(total_amount)

    total = sorted(total, reverse=True)

    em = discord.Embed(
        title=f"Top {x} Richest People",
        description="This is decided on the basis of correct questions",
        color=discord.Color(0xfa43ee))
    index = 1
    for amt in total:
        id_ = leader_board[amt]
        member = await bot.fetch_user(id_)
        name = member.name
        em.add_field(name=f"{index}. {name}", value=f"{amt}", inline=False)
        if index == x:
            break
        else:
            index += 1

    await message.channel.send(embed=em)


@bot.command(hidden=True)
async def bless(message, member: discord.Member, amount=None):
    amount = int(amount)
    if message.author.id != id.Emma_id:
        await message.channel.send("smh get outta here non-Emma")
        return
    await functions.open_account(member)
    await functions.update_bank(member, amount, 'Correct')
    await message.channel.send(f"you gave {member} {amount} points")


@bot.command(aliases=['pay'])
async def send(message, member: discord.Member, amount=None):
    await functions.open_account(message.author)
    await functions.open_account(member)
    if amount is None:
        await message.send("Please enter the amount")
        return
    bal = await functions.update_bank(message.author)
    amount = int(amount)
    if amount > bal:
        await message.send('You do not have sufficient balance')
        return
    if amount < 0:
        await message.send('Amount must be positive!')
        return

    await functions.update_bank(message.author, -1 * amount, 'Correct')
    await functions.update_bank(member, amount, 'Correct')
    await message.send(
        f'{message.author.mention} You gave {member} {amount} points')


@bot.command()
async def wordle(ctx):
    response = ""
    timeout = time.time() + 60 * 10

    def check(m):
        return m.channel == ctx.channel and ctx.author == m.author

    with open('answers.txt') as file:
        contents = file.read().splitlines()
    answer = random.choice(contents)
    with open('guesses.txt') as file:
        contents += file.read().splitlines()
    print(answer)
    await ctx.channel.send("yall are bozos, your wordle started")
    guess = 0
    while guess < 6:
        if time.time() > timeout:
            await ctx.channel.send(
                f"{ctx.author.mention}, your wordle timed out, the asnwer was {answer}"
            )
            return
        try:
            msg = await asyncio.wait_for(bot.wait_for("message", check=check),
                                         timeout=2.0)
            if msg.content.lower() == "cancel":
                await ctx.channel.send(f"canceling, the word was {answer}")
                return
            if len(msg.content) != 5:
                continue
            if msg.content.lower() in contents:
                response_ = ''
                for i in range(0, 5):
                    if msg.content.lower()[i] == answer[i]:
                        response_ += '🟩'
                    elif msg.content.lower()[i] in answer:
                        response_ += '🟨'
                    else:
                        response_ += '⬛'
                response += ('\n')
                response += msg.content.lower() + '\n' + response_
                await ctx.channel.send(response)
                if msg.content.lower() == answer:
                    await ctx.channel.send("you got it!")
                    break
                guess += 1

        except:
            continue

    else:
        await ctx.channel.send(
            f"Sorry you ran out of guesses, the word was {answer}")


@bot.command(hidden=True)
async def opclear(message):
    if message.author_id not in [
            id.Eva_id, id.Emma_id, id.Nolan_id, id.Ryan_id
    ]:
        return

    file = open("opp_list.txt", "r+")
    file.truncate()
    file.close()
    file = open("people_list.txt", "r+")
    file.truncate()
    file.close()
    file = open("side_list.txt", "r+")
    file.truncate()
    file.close()


@bot.command(aliases=['op'])
async def opp(message, opo, side):
    ctx = opo.lower()
    file = open("opp_list.txt", "r")
    file_lines = file.read()
    op_list = file_lines.split("\n")  # sets op_list as a list of opp_list.txt

    file2 = open("people_list.txt", "r")
    file_lines2 = file2.read()
    peep_list = file_lines2.split(
        "\n")  # opens people_list and sets peep_list = to it

    file3 = open("side_list.txt", "r")
    file_lines3 = file3.read()
    side_list = file_lines3.split("\n")
    if not (side.lower() == "aff" or side.lower() == "neg"):
        await message.channel.send("send better sides")
        return

    if ctx in op_list:
        for i in range(len(op_list)):
            if op_list[i] == ctx and side_list[i] == side.lower():
                await message.channel.send(
                    f"{peep_list[i]} faced them on the same side")
            if op_list[i] == ctx and side_list[i] != side.lower():
                await message.channel.send(
                    f"{peep_list[i]} faced them on the opposite side")

    else:
        await message.message.add_reaction('❌')
    file1 = open("opp_list.txt", "a")
    file2 = open("people_list.txt", "a")
    file3 = open("side_list.txt", "a")
    file1.write(ctx + "\n")
    file2.write(message.author.display_name + "\n")
    file3.write(side.lower() + "\n")


@bot.command(aliases=['gamb'])
async def gamble(ctx, amount=None):
    dice_a = random.randint(1, 6)
    dice_b = random.randint(1, 6)
    dice_c = random.randint(1, 6)
    total = dice_a + dice_b + dice_c
    await functions.open_account(ctx.author)
    users = await functions.get_bank_data()
    user = ctx.author
    temp_bal = 0
    real_id = 0
    for u in users:
        name = int(u)
        if users[u]["Correct"] >= temp_bal:
            temp_bal = users[u]["Correct"]
            real_id = name
    if amount is None:
        await ctx.send("Please enter the amount after the command")
        return
    amount = int(amount)
    if amount > users[str(user.id)]["Correct"]:
        await ctx.send('You do not have sufficient balance')
        return
    if amount < 0:
        await ctx.send('Amount must be positive!')
        return
    if total >= 11:
        await ctx.send(
            f"You rolled {total} \n {ctx.author.mention}Congrats you won")
        users[str(user.id)]["Correct"] += amount
        users[str(real_id)]["Correct"] -= amount

    else:
        await ctx.send(f"You rolled {total} \n rip you lost")
        users[str(real_id)]["Correct"] += amount
        users[str(user.id)]["Correct"] -= amount
    with open("data_file.json", 'w') as f:
        json.dump(users, f)


@bot.command()
async def play(context, *, song="random"):
    # voice_channel_ = bot.get_channel(context.channel.id)
    channel_ = context.channel
    words = song

    def check(m):
        return m.guild == context.guild

    if song == "continue":
        song = "random"

    # grab the user who sent the command
    try:
        voice_channel = context.author.voice.channel
    except:
        await channel_.send("get in a channel bozo")
        return
    # only play music if user is in a voice channel'
    list_ = glob.glob(r"songs/*.mp3")
    if song == "random":
        song = random.choice(list_)[:-len(".mp3")]
    else:
        song = "songs/" + song
    if song + ".mp3" not in list_ and words != "continue":
        await channel_.send("type better bozo")
        return

    if voice_channel == None:
        await context.channel.send('get in a channel bozo')
        return

    # grab user's voice channel
    channel = voice_channel.name

    # create StreamPlayer
    vc = await voice_channel.connect()

    vc.play(discord.FFmpegPCMAudio(song + '.mp3'),
            after=lambda e: print('done', e))
    await channel_.send(f'joining {channel}, playing {song[len("songs/"):]}')
    while vc.is_playing():
        try:
            msg = await asyncio.wait_for(bot.wait_for("message", check=check),
                                         timeout=1.0)
            if (msg.content.lower() == "!skip"
                    or msg.content.lower() == "skip"):
                break
        except:
            continue

    if words == "continue":
        # voice_channel_ = bot.get_channel(919315563157803098)
        # while len(voice_channel.members) > 1:
        # while len(voice_channel_.members) > 1:
        while True:
            vc.stop()
            song = random.choice(list_)[:-len(".mp3")]
            vc.play(discord.FFmpegPCMAudio(song + '.mp3'),
                    after=lambda e: print('done', e))
            await channel_.send(f'playing {song[len("songs/"):]}')
            while vc.is_playing():
                try:
                    msg = await asyncio.wait_for(bot.wait_for("message",
                                                              check=check),
                                                 timeout=1.0)
                    if msg.content.lower() == "skip" or msg.content.lower(
                    ) == "!skip":

                        break
                except:
                    continue
            # voice_channel_ = bot.get_channel(context.channel.id)

    await vc.disconnect()


@bot.command()
async def skip(message):
    print("skipped")


@bot.command(aliases=["dc", "disconnect", "shutup"])
async def stop_play(message):
    role = discord.utils.get(message.guild.roles, name="DJ")
    if role in message.author.roles:
        if message.author.voice.channel == None:
            await message.channel.send('ur not listenin to anything smh')
            return

        await message.voice_client.disconnect()
        await message.channel.send(">:(")

    else:
        await message.channel.send('get outta here lmao')


@bot.command()
async def ok(message, member: discord.Member = None):
    if member == None:
        await message.channel.send(
            f"{message.author.mention}, it is going to be ok")
    else:
        await message.channel.send(f"it is going to be ok, {member.mention}")


@bot.command()
async def night(message):
    await message.channel.send("go to sleep bozo")


@bot.command()
async def gn(message):
    await message.channel.send(
        "good night, but youre still a couple hours late")


@bot.command()
async def serotonin(message):
    embed = discord.Embed(title="SEROTONIN!")
    list = [
        "https://c.tenor.com/GCjdDuPUgHEAAAAC/ejemplo-tony-montana.gif",
        "https://c.tenor.com/ujcdnknWUuAAAAAC/wows-wolf.gif",
        "https://c.tenor.com/hLM1tPprsJAAAAAC/alice-shook.gif",
        "https://c.tenor.com/ed1A-0F-SVEAAAAC/drug-breakingbad.gif"
    ]
    embed.set_image(url=random.choice(list))
    await message.channel.send(embed=embed)


@bot.command()
async def arnie(message):
    embed = discord.Embed(title="get over here")
    embed.set_image(
        url=
        "https://media.discordapp.net/attachments/894696179747668089/942037405773463663/IMG_4641.jpg"
    )
    await message.channel.send(embed=embed)


@bot.command()
async def italian(message):
    embed = discord.Embed(title="Ashtolini")
    embed.set_image(
        url=
        "https://media.discordapp.net/attachments/746433515725520949/981959538230050897/image0.gif"
    )
    await message.channel.send(embed=embed)


@bot.command()
async def meme(message):
    a = random.randint(0, (len(id.names) - 1))
    embed = discord.Embed(title=id.names[a])
    embed.set_image(url=id.meme[a])
    await message.channel.send(embed=embed)


@bot.command()
async def bop(message, *, x=None):
    if x == None:
        await message.channel.send("bop")
    else:
        await message.channel.send(f"bop {x}")


@bot.command(hidden=True)
async def say(message, channel, *, words=""):
    if message.author.id != id.Nolan_id:
        return
    try:
        channel = bot.get_channel(int(channel))
    except:
        try:
            channel = bot.get_channel(
                int(
                    channel.replace("#", "").replace("<", "").replace('>',
                                                                      "")))
        except:
            words = channel + " " + words
            channel = message.channel

    await channel.send(words)


@bot.command(hidden=True)
async def react(ctx, channel: discord.TextChannel, mid: int,
                emoji: discord.Emoji):
    if ctx.author.id == id.Nolan_id:
        msg = discord.utils.get(await channel.history(limit=100).flatten(),
                                id=mid)
        # this gets the most recent message from a specified member in the past 100 messages
        # in a certain text channel - just an idea of how to use its versatility
        await msg.add_reaction(emoji)
    else:
        await ctx.channel.send("you don't have permission for this")


@bot.command(hidden=True)
async def levi(ctx):
    if ctx.author.id != id.Eva_id:
        await ctx.channel.send("smh get outta here")
        return
    embed = discord.Embed(title="LEVI!")
    list = [
        "https://c.tenor.com/3HAncAYO8DwAAAAC/levi-ackerman-anime.gif",
        "https://c.tenor.com/AXTSXVbBdOIAAAAC/leviackerman-attackontitan.gif",
        "https://c.tenor.com/hpx_Mxq9xt4AAAAC/levi-anime.gif",
        "https://c.tenor.com/uKtpA6aBurMAAAAd/anime-attack-on-titan.gif",
        "https://c.tenor.com/BRGzOn9GntcAAAAC/levi-funnylevi.gif",
        "https://c.tenor.com/PSn71OtIk3YAAAAC/levi-levi-ackerman.gif",
        "https://c.tenor.com/S2hu5vLcVQQAAAAd/levi-ackerman-aot.gif",
        "https://c.tenor.com/DngCJOAFzTcAAAAS/levi-ackerman-attack-on-titan.gif"
    ]
    url = random.choice(list)
    if random.randint(0, 100) == 100:
        url = "https://cdn.discordapp.com/attachments/746433515725520949/946531604849889290/levi_ackerman.jpg"
    embed.set_image(url=url)
    await ctx.channel.send(embed=embed)


@bot.command(hidden=True)
async def uwu(ctx):
    if ctx.author.id != id.Ashton_id:
        await ctx.channel.send("what are you? an egirl?")
        return
    embed = discord.Embed(title="uwu")

    embed.set_image(url=random.choice([
        "https://cdn.discordapp.com/attachments/913148557341622322/945532187556577350/images.png",
        "https://cdn.discordapp.com/attachments/946955538162405477/966535321498030090/unknown.png",
        "https://cdn.discordapp.com/attachments/939549218572501062/1014676530460377179/5DD35623-3441-4ACA-B548-4E1029497636.jpg",
      "https://cdn.discordapp.com/attachments/679850755993370625/1021889657174241392/IMG_8358.jpg"
    ]))
    await ctx.channel.send(embed=embed)


@bot.command()
async def song_list(ctx):
    response = ""
    list_ = glob.glob(r"songs/*.mp3")
    for x in range(len(list_)):
        list_[x] = list_[x][:-len(".mp3")][len("songs/"):]
        response += f"{list_[x]}, "
    await ctx.channel.send(response)


@bot.command()
async def download(ctx, link, *, name):
    try:
        yt = pytube.YouTube(link)
        if (yt.length > 600 and ctx.author.id != id.Nolan_id
                and ctx.author.id != id.Pranay_id):
            await ctx.channel.send(
                "you better not be trying to download something 10 hours long,(or a break from the ads) if not then just ask nolan to download it"
            )
            return
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download(output_path="songs/")
        base, ext = os.path.splitext(out_file)
        os.rename(out_file, f"songs/{name}.mp3")

        await ctx.channel.send(
            f"{yt.title} has been successfully downloaded as {name}")

    except pytube.exceptions.RegexMatchError:
        await ctx.channel.send("download is broken for now sadly")
        msg = await ctx.channel.send(
            "<@380902364711878659> fix download you bozo")
        await msg.delete()


@bot.command()
async def prints(ctx, *, words):
    print(words)


@bot.command()
async def link(ctx):
    await ctx.channel.send("""meaning of life
http://gg.gg/xuwgu""")


@bot.command()
async def rules(ctx):
    await ctx.channel.send(id.rules)


@bot.command()
async def breaks_calc(ctx, amount_of_players, rounds):
    amount_of_players = int(amount_of_players)
    rounds = int(rounds)
    player_list = []
    for i in range(amount_of_players):
        player_list.append(0)

    player_list = functions.simulate_wins(player_list, rounds)
    wins_list = []
    for player in player_list:
        wins_list.append(player)

    response = ""
    for i in range(rounds, -1, -1):
        count = wins_list.count(i)
        response += (f"{i} wins = {count} \n")
    await ctx.channel.send(response)


@bot.command(aliases=['8ball'])
async def EightBall(ctx, *, message=""):
    await ctx.channel.send(
        random.choice([
            "It is certain.", "It is decidedly so.", "Without a doubt.",
            " Yes definitely.", "You may rely on it.", "As I see it, yes.",
            "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.",
            "Reply hazy, try again.", "Ask again later.",
            "Better not tell you now", "Cannot predict now.",
            "Concentrate and ask again.", "Don't count on it.",
            "My reply is no.", "My sources say no.", " Outlook not so good.",
            "Very doubtful."
        ]))

try:
    bot.run(TOKEN)  # does stuff
except Exception as err:
    if "429" in str(err).split():  # if its a rate limit
        print("Rate-limit detected. Restarting repl")
        os.system("kill 1")  # reset bot
    print(err)  # I took this code of the internet so it might not work
'''
blackjack
LUNCH
breaks calculator
hyperop only random
'''
