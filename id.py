import random
import asyncio

Nolan_id = 380902364711878659
Arnav_id = 671428552326905881
Eva_id = 692897486657945620
Ryan_id = 340153637525389313
Emma_id = 767540979074859018
Destynn_id = 412244299623956486
Pranay_id = 642920418382053392
Zayd_id = 420358189268336640
Ashton_id = 810634852356456478
Owen_id = 687692161616969885
subject = 0
t_amount = 0
bozo_permitted = [Pranay_id, Nolan_id, Emma_id, Ashton_id]

ans = 0
gec_id = [
    Nolan_id, Arnav_id, Eva_id, Emma_id, 810634852356456478, Ryan_id,
    898975664189866035
]
gec_block = ["gec", " ge(", "&ec", "gex", "🇬📧🇨", "🇬🇪🇨", "🇬 📧 🇨"]
rules = ("""
Golden Rule - "Do unto others as you would have them do unto you."(Jesus)

Silver Rule - "one should not treat other people in the manner in which one would not want to be treated."(Confucius)
                         
Platinum Rule - "we should do unto others the way they want us to do unto them."(Bennett)

Diamond Rule - "Do Unto Others As Someone Special Did Unto You."(Kerpen)

Iron Rule - "Might makes right."(Habakkuk 1:11)

Titanium Rule - "do unto others according to their druthers."(Raines and Ewing)

Double Platinum Rule - "treat others the way they don't even know they want to be treated."(Williams)

Bronze Rule - "Do unto others as they have done unto you."(Sisney)
                         
Leaden Rule - "Do unto others what you most fear having done unto you."(Riso and Hudson)

Plutonium Rule - "Treat others as you would in the knowledge that you will one day be them."(Chappell)
""")

vibes = [
    "https://tenor.com/view/cat-vibe-153bpm-gif-18260767",
    "https://tenor.com/view/vibe-dance-rainbow-lol-gif-18210034",
    "https://tenor.com/view/happy-dance-party-positive-vibes-vibe-gif-12376906",
    "https://tenor.com/view/girl-music-head-shaking-eyes-close-chill-gif-17828830",
    "https://tenor.com/view/dance-weekend-vibe-mood-gif-14019019",
    "https://tenor.com/view/woona-vibin-catto-vibe-cat-mlem-gif-18638749",
    "https://tenor.com/view/vibing-st6-cute-dog-dance-gif-16459631",
    "https://tenor.com/view/aethestic-anime-just-woke-up-stretching-stretch-gif-16042656",
    "https://tenor.com/view/dance-happy-dog-reaction-dogs-gif-19659302",
    "https://tenor.com/view/monke-monkey-discord-pfp-pfp-monkeys-gif-21010625",
    "https://tenor.com/view/sasha-gif-19376100",
    "https://tenor.com/view/no-bad-vibes-good-vibes-only-avoid-slide-roy-purdy-gif-10840468"
]
names = ["tis da new feature"]
meme = [
    "https://cdn.discordapp.com/attachments/894696179747668089/942121001179807744/IMG_5502.png"
]

radical_quotes = [
    "I hate Nazis", "racism is bad", "I don't like homophobia",
    "I will not allow you to oppress black people",
    "I am in fact not a racist",
    "yeah sleep is ocasionally good for your body", "im a big fan of fascism",
    "emma got into stanford",
    "I would go as far to say the holocaust is bad *loud chinese music plays*"
]


async def oppress_react(reaction, payload):
    b = random.randint(1, 5)
    if b == 3:
        a = random.randint(18, 48)
        await asyncio.sleep(a)
        await reaction.remove(payload.member)


async def oppress(message):
    b = random.randint(1, 5)
    if b == 3:
        a = random.randint(18, 48)
        await asyncio.sleep(a)
        await message.delete()
