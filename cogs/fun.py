import discord
from discord import Option, slash_command
from discord.errors import Forbidden
from discord.ext import commands
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from datetime import datetime
import asyncio
import os

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# 8ball

    @slash_command(name="8ball")
    async def _8ball(self, ctx, *, question: Option(str, "Write Your Question", required=True)):
        """The Ultimate 8-ball game is now on Discord 🎱"""
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes – definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     "Don't count on it.",
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.']
        e = discord.Embed(title=f"MAGIC 8-BALL", color=ctx.author.color)
        e.set_thumbnail(
            url=f'https://media.tenor.com/images/47ceded02690a48da88d02bb7c1f5f46/tenor.gif')
        e.add_field(name=f"**🔮Question by `{ctx.author}`:**", value=f"`{question}`", inline=False)
        e.add_field(name=f"**My Magic Foretells me:**", value = f"`{random.choice(responses)}`", inline=False)
        await ctx.respond(embed=e)

# Lovemeter

    @slash_command()
    async def lovemeter(self, ctx, name1: Option(str, "Enter the name of 1st lovebird", required=True), name2: Option(str, "Enter the name of 2nd lovebird", required=True)):
        """How Much Do You Love Me~ Senpai? 💖"""
        percentage = random.randint(0, 100)

        if 0 <= percentage <= 10:
            result = ['Friendzone',
                      'You sure it was love-meter not friend-meter ',
                      'Dude that is insultingly low.]',
                      'Ahh the classic, "one sided love"',
                      'Just friends?',
                      'Is my meter off today? Can not pick any numbers']

        elif 10 <= percentage <= 30:
            result = ['Huh, just started dating?',
                      'I guess friendzone never ends',
                      'Best-friend zone?',
                      'My meter picked something up']

        elif 30 <= percentage <= 50:
            result = ['Still one sided, next time bud',
                      'There is still alot room for love',
                      'I mean it is a good start',
                      'There is potential']

        elif 50 <= percentage <= 70:
            result = ['I sense love here',
                      'Oh... love birds?',
                      'Love is in the air',
                      'My meter picked something big',
                      'There is still a long road ahead, stay strong :D',
                      'I mean acceptable']

        elif 70 <= percentage <= 90:
            result = ['Just got wed?',
                      'Very good relationship',
                      'I do not talk much with love birds',
                      'My meter says it is looking good ',
                      'Just steps below the perfect match']

        elif 90 <= percentage <= 100:
            result = ['Yoo dude that iss real love',
                      'Romeo and Juliet?',
                      'My meter nearly exploded',
                      'Adam and Eve?',
                      'Match made in heavens']

        if percentage <= 33:
            shipColor = 0x000000
        elif 33 < percentage < 66:
            shipColor = 0xe3ff00
        else:
            shipColor = 0xee66ee

        if percentage <= 10:
            gif = "https://media.tenor.com/images/8eb3ea6f8b8e05115a37df84ba03144a/tenor.gif"
        if 10 < percentage <= 30:
            gif = "https://media.tenor.com/images/d9f4ebad1365272d2605a1a5151d501a/tenor.gif"
        if 30 < percentage <= 50:
            gif = "https://media.tenor.com/images/12414d69b8a99bd6dc19275363e17554/tenor.gif"
        if 50 < percentage <= 70:
            gif = "https://64.media.tumblr.com/09efd576d1e31d6dbf2a66eaa07ef6af/tumblr_n52l5bmodz1tt23n5o1_500.gif"
        if 70 < percentage <= 100:
            gif = "https://media.tenor.com/images/d85ef0ba33daf46de0838eba3efe8d08/tenor.gif"

        final_result = random.choice(result)

        embed = discord.Embed(color=shipColor,
                              title=f"Love meter of `{name1}` and `{name2}`")
        embed.set_thumbnail(url=f'{gif}')
        embed.add_field(name="Results:", value=f'{percentage}% ', inline=True)

        embed.add_field(name="Personal opinion :",
                        value=f'{final_result}', inline=False)

        embed.set_author(name="❤ Love Meter ❤", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

# Hi

    @slash_command()
    async def hi(self, ctx):
        '''Nothing special just some greetings 🙋‍♂️'''
        greetings = ['Hello', 'Hiya', 'nĭ hăo', 'Namaste', 'Konichiwa', 'Zdravstvuyte', 'Bonjour', 'Guten tag',
                     'Anyoung haseyo', 'Asalaam alaikum', 'Goddag', 'Selamat siang', 'hola', 'marhabaan  ', 'hyālō',
                     'Sata srī akāla', 'Nggoleki', 'Vandanalu', '   Xin chào', 'Namaskār', 'Vaṇakkam', 'Salām', 'Merhaba', 'Ciao', 'Sà-wàt-dii', 'Kaixo', 'Cześć’', 'Namaskāra', 'Prannam', 'Kamusta', 'Hallo', 'Yasou', 'Hej', 'oi', 'Wazza', 'kem cho',
                     'Hai', 'doki-doki', 'meow meow ', 'Lí-hó', 'Vitaju', 'Bok', 'Hej', 'Moi', 'Sveika /Sveiks ', 'God dag',
                     'Moïen ', 'Vitayu ', 'Aloha ', 'Wassup', 'Howdy!']
        reply = random.choice(greetings)
        await ctx.respond(f'**{reply}**, {ctx.author.mention}. How is it going for you? No need to ask me, but I am mostly good.')

# Lenny

    @slash_command()
    async def lenny(self, ctx):
        """Sends a random lenny from my collection 👓"""
        lennys = ['( ͡° ͜ʖ ͡°)', 'ಠ_ಠ', '( ͡ʘ ͜ʖ ͡ʘ)', '(▀̿Ĺ̯▀̿ ̿)', '( ͡°( ͡° ͜ʖ( ͡° ͜ʖ ͡°)ʖ ͡°) ͡°)', '( ͡ᵔ ͜ʖ ͡ᵔ )',
                  '(╯ ͠° ͟ʖ ͡°)╯┻━┻', 'ᕙ(▀̿̿Ĺ̯̿̿▀̿ ̿) ᕗ', '(✿╹◡╹)', 'щ（ﾟДﾟщ） < "Dear god why‽ )', '(人◕ω◕)', '(*бωб)', 'ヽ(͡◕ ͜ʖ ͡◕)ﾉ',
                  '(⌐▀͡ ̯ʖ▀)︻̷┻̿═━一-', 'ᕕ(╯°□°)ᕗ']
        await ctx.respond(random.choice(lennys))

# Coinflip

    @slash_command()
    async def coinflip(self, ctx):
        """Flips the coin - Heads or Tails 🪙"""
        value = [f"<:Heads:907238222785036319>",
                 f"<:Tails:907238251398578186>"]

        fliping = await ctx.respond(f"https://i.pinimg.com/originals/52/91/f5/5291f56897d748b1ca0a10c90023588d.gif")

        await asyncio.sleep(10)

        flip = random.choice(value)

        if flip == f"<:Tails:907238251398578186>":

            await ctx.edit(content=f'{flip}')
            await ctx.send(f"**The coin flipped and gave u a `Tails`**")

        else:
            await ctx.edit(content=f'{flip}')
            await ctx.send(f"**The coin flipped and gave u a `Heads`**")

# Happy

    @slash_command()
    async def happy(self, ctx):
        """I am so Happy :D"""
        await ctx.respond(f'https://media1.tenor.com/images/3419ea3da202cf42d6c7ab37a7fcd44e/tenor.gif')

# Sad

    @slash_command()
    async def sad(self, ctx):
        """I am Sad :("""
        await ctx.respond(f'https://media1.tenor.com/images/09b085a6b0b33a9a9c8529a3d2ee1914/tenor.gif')

# Angry

    @slash_command()
    async def angry(self, ctx):
        """I am so Angry >ω<"""
        await ctx.respond(f'https://tenor.com/view/anime-angry-evil-plan-gif-14086662')

# F for Respect

    @slash_command()
    async def f(self, ctx):
        """F in the chats bois 🙃"""
        await ctx.respond(f'`{ctx.author.display_name}` paid their respects.')

# Calculate

    @slash_command()
    async def calc(self, ctx, query: Option(str, "Your Question Here", required=True)):
        """Solve the DMAS questions right here 🧮"""
        allowed = set('0123456789+-*/()')
        clean = ''.join(char for char in query if char in allowed)
        try:
            await ctx.respond(f'``{query}`` ``=`` ``{eval(clean)}\n``')
        except Exception:
            await ctx.respond('Please a write valid equation.')

# Dice roll

    @slash_command()
    async def diceroll(self, ctx):
        """Rolls the Dice for You 🎲"""
        responses = ['<:dice_1:907244741014482944>',
                     '<:dice_2:907244762917142558>',
                     '<:dice_3:907244779606253609>',
                     '<:dice_4:907244799835406376>',
                     '<:dice_5:907244819691237376>'
                     '<:dice_6:907244837126959125>']

        msg_1 = await ctx.respond(f"** The Dice is Rolling Now**")
        msg_2 = await ctx.send(f"<a:dice_roll:907244864490590209>")

        await asyncio.sleep(8)

        await ctx.edit(content=f"**The Dice has Roled on:**")
        await msg_2.edit(content=random.choice(responses))

# Rock, Paper, Scissors

    @slash_command()
    async def rps(self, ctx, msg: Option(str, "Choose between Rock, Paper or Scissors", required=True)):
        """Rock, Paper or Scissors? Uhm? ✂️"""
        tie_data = ['Tie for this time but I am sure I will win the next time.', 'We have tied, a good battle.',
                    'It was a good battle, learned alot from you but a tie is a tie', 'Good battle, you didn\'t disappoint me.']

        win_data = ['Sorry but I will be taking the crown for today.', 'Hehe, no victory for you today, friend. ',
                    'A good match but you lost.', 'I have seen better from you.', 'Weakness disgusts me.', 'I see no god up here, other than me!']

        data = ['I have lost this time but it does not mean that this is over', 'I have lost, good battle.',
                'Never felt a defeat in so long.', 'Ah the smell of defeat, finally!', 'I have lost to a meer human',
                'Hey kid, you won but not for long.', 'I have lost this time but next time I will crush you!']

        t = ["rock", "paper", "scissors"]
        result = None
        tcolor = None
        computer = t[random.randint(0, 2)]
        player = msg.lower()

        if player == computer:
            result = tie_data

        elif player == "scissors":

            if computer == "rock":
                result = win_data
            else:
                result = data

        elif player == "rock":
            if computer == "paper":
                result = win_data
            else:
                result = data

        elif player == "paper":
            if computer == "scissors":
                result = win_data

            else:
                result = data
        else:
            await ctx.respond("Do I have to teach you rock, scissors and paper now? Choose between **`rock/paper/scissors`**")

        if result == win_data:
            tcolor = 0x2eff5d
        if result == data:
            tcolor = 0xff0003
        if result == tie_data:
            tcolor = 0x529dff

        final_result = random.choice(result)
        embed = discord.Embed(color=tcolor,
                              title=f"Rock Paper Scissors")
        embed.set_thumbnail(
            url=f'https://media.tenor.com/images/5969d2658a51ef93de54a0049fffac9e/tenor.gif')
        embed.add_field(name="I choose:", value=f'**{computer}**', inline=True)

        embed.add_field(name=f"Olympus' words:",
                        value=f'"**{final_result}**"', inline=False)

        embed.set_footer(
            text=f'Played with {ctx.author}', icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

# Password

    @slash_command()
    async def password(self, ctx, amt: Option(int, "Number of characters you want in your password", required=False, default=8)):
        """ Get random password in DM 🔒"""
        try:
            nwpss = []
            lst = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '@',
                    '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '{', ",", '}', ']',
                    '[', ';', ':', '<', '>', '?', '/', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '`', '~',
                    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                    'U', 'V', 'W', 'X', 'Y', 'Z']
            for x in range(amt):
                newpass = random.choice(lst)
                nwpss.append(newpass)
            fnpss = ''.join(nwpss)
            await ctx.respond(f'`{ctx.author}`, attempting to send you the generated password in dms.')
            await ctx.author.send(f':white_check_mark: Password Generated: ```{fnpss}```')
        except Forbidden:
            await ctx.send(f"**<:Cross:902943066724388926> Your DMs are turned off or You might have blocked me, I wasn\'t able to DM you.**")

# Slots

    @slash_command()
    async def slot(self, ctx):
        """Slots!!! 🍎🍊🍐🍋🍉🍇🍓🍒"""
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} | {b} | {c} ]\n{ctx.author.name}**,"

        if a == b == c:
            await ctx.respond(embed=discord.Embed(title='Slot Machine:',
                                                  description=slotmachine + ' has gotten 3/3 he wins!!! :tada:',
                                                  colour=discord.Colour.red()))
        elif (a == b) or (a == c) or (b == c):
            await ctx.respond(embed=discord.Embed(title='Slot Machine:',
                                                  description=slotmachine + ' has gotten 2/3 he wins!!! :tada:',
                                                  colour=discord.Colour.red()))
        else:
            await ctx.respond(embed=discord.Embed(title='Slot Machine:',
                                                  description=slotmachine + ' has gotten 0/3 he looses. :pensive:',
                                                  colour=discord.Colour.red()))

# Cheers

    @slash_command()
    async def cheers(self, ctx, user: Option(discord.Member, "Choose Your Partner to say Cheers with!", required=True), reason: Option(str, "Tell the reason for your celebration!", required=False)):
        """Say Cheeeeeers!!! 🍺"""
        if user.bot:
            return await ctx.respond(f"You that lonely? Give an actual person not a bot.")
        beer_offer = f"**{user.mention}**, You have a 🍺 offered from **{ctx.author.mention}**"
        beer_offer = beer_offer + \
            f"\n\n**Reason:** {reason}" if reason else beer_offer
        await ctx.respond(f"<a:cheeers:907996199951409242> Say Cheeeeeeeers!!!")
        msg = await ctx.send(beer_offer)

        def reaction_check(m):
            if m.message_id == msg.id and m.user_id == user.id and str(m.emoji) == "🍻":
                return True
            return False

        try:
            await msg.add_reaction("🍻")
            await self.bot.wait_for('raw_reaction_add', timeout=10.0, check=reaction_check)
            if reason == None:
                await msg.edit(content=f"**{user.mention}** and **{ctx.author.mention}** Are enjoying a lovely 🍻")
                await msg.clear_reactions()
            else:
                await msg.edit(content=f"**{user.mention}** and **{ctx.author.mention}** Are enjoying a lovely 🍻 coz\n\n `{reason}`")
                await msg.clear_reactions()
        except asyncio.TimeoutError:
            await msg.delete()
            await ctx.send(f"Well, it seems **{user.name}** didn't wanted to say 'cheers' with **`{ctx.author.name}`** ;-;")
        except discord.Forbidden:
            beer_offer = f"{user.mention} and {ctx.author.mention} are enjoying a 🍻."
            beer_offer = beer_offer + f"\n\n**reason:** {reason}" if reason else beer_offer
            await msg.edit(content=beer_offer)

# Simp

    @slash_command()
    async def simp(self, ctx, user: Option(discord.Member, "Choose The User", required=False)):
        """Ayo Man! You are a Simp!!! 😳"""
        user = user or ctx.author
        embed = discord.Embed(
            color=discord.Color.red(),
            description=f'`{user.display_name}` is {random.randint(0, 101)}% simp'
        )
        await ctx.respond(embed=embed)

# IQ

    @slash_command()
    async def iq(self, ctx, user: Option(discord.Member, "Choose the User", required=False)):
        """I wonder what is your IQ? 🤔"""
        user = user or ctx.author
        iq = ['130 and above (Very Superior)',
              '120–129 (Superior)',
              '110–119 (High Average)',
              '90–109 (Average)',
              '80–89 (Low Average)',
              '70–79 (Borderline)',
              '69 and below	(Extremely Low)']
        e = discord.Embed(
            color=discord.Colour.red(),
            description=f'`{user.display_name}`\'s IQ is {random.choice(iq)}'
        )
        await ctx.respond(embed=e)

# Roast

    @slash_command()
    async def roast(self, ctx, user: Option(discord.Member, "Choose the User", required=False)):
        """Hehe Boi! Roast Time! 😏"""
        if not user:
            user = ctx.author
        A = ['You’re the reason God created the middle finger.',
             'You’re a grey sprinkle on a rainbow cupcake.',
             'If your brain was dynamite, there wouldn’t be enough to blow your hat off.',
             'You are more disappointing than an unsalted pretzel.',
             'Light travels faster than sound which is why you seemed bright until you spoke.',
             'We were happily married for one month, but unfortunately we’ve been married for 10 years.',
             'Your kid is so annoying, he makes his Happy Meal cry.',
             'You have so many gaps in your teeth it looks like your tongue is in jail.',
             'Your secrets are always safe with me. I never even listen when you tell me them.',
             'I’ll never forget the first time we met. But I’ll keep trying.',
             'I forgot the world revolves around you. My apologies, how silly of me.',
             'I only take you everywhere I go just so I don’t have to kiss you goodbye.',
             'Hold still. I’m trying to imagine you with personality.',
             'Our kid must have gotten his brain from you! I still have mine.',
             'Your face makes onions cry.',
             'The only way my husband would ever get hurt during an activity is if the TV exploded.',
             'You look so pretty. Not at all gross, today.',
             'Her teeth were so bad she could eat an apple through a fence.',
             'I’m not insulting you, I’m describing you.',
             'I’m not a nerd, I’m just smarter than you.',
             'Keep rolling your eyes, you might eventually find a brain.',
             'Your face is just fine but we’ll have to put a bag over that personality.',
             'You bring everyone so much joy, when you leave the room.',
             'I thought of you today. It reminded me to take out the trash.',
             'Don’t worry about me. Worry about your eyebrows.',
             'there is approximately 1,010,030 words in the language english, but i cannot string enough words together to express how much i want to hit you with a chair']
        await ctx.respond(embed=discord.Embed(
            colour=discord.Colour.red(),
            description=f'`{user.display_name}`,\n {random.choice(A)}'
        ).set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url))

# Kill

    @slash_command()
    async def kill(self, ctx, user: Option(discord.Member, "Choose The User", required=False)):
        """Got 'Em! Stab 'Em 🔪"""
        user = user or ctx.author
        died = ['rolling out of the bed and the demon under the bed ate them.',
                'getting impaled on the bill of a swordfish.',
                'falling off a ladder and landing head first in a water bucket.',
                'his own explosive while trying to steal from a condom dispenser.',
                'a coconut falling off a tree and smashing there skull in.',
                'taking a selfie with a loaded handgun shot himself in the throat.',
                'shooting himself to death with gun carried in his breast pocket.',
                'getting crushed while moving a fridge freezer.',
                'getting crushed by his own coffins.',
                'getting crushed by your partner.',
                'laughing so hard at The Goodies Ecky Thump episode that he died of heart failure.',
                'getting run over by his own vehicle.',
                'car engine bonnet shutting on there head.',
                'tried to brake check a train.',
                'dressing up as a cookie and cookie monster ate them.',
                'trying to re-act Indiana Jones, died from a snake bite.',
                'tried to short circuit me, not that easy retard',
                'tried to fight a bear with their hands',
                'getting Billy Heartied in the ball sacks'
                ]
        await ctx.respond(embed=discord.Embed(
            colour=discord.Colour.red(),
            description='`{}` was killed by {}'.format(
                user.display_name, random.choice(died))
        ).set_author(name=self.bot.user.display_name, icon_url=self.bot.user.avatar.url))


# Snap

    @slash_command()
    async def snap(self, ctx, member: Option(discord.Member, "Choose the Member", required=True), message: Option(str, "What do you want the user to say?", required=True)):
        """Lemme snap some messages for You 📸"""
        await ctx.defer()
        colour = {
            "time": (114, 118, 125),
            "content": (220, 221, 222)
        }

        size = {
            "title": 20,
            "time": 13
        }

        font = 'fonts/Whitney-Medium.ttf'

        if not member:
            member = ctx.author

        img = Image.new('RGB', (500, 115), color=(54, 57, 63))
        titlefnt = ImageFont.truetype(font, size["title"])
        timefnt = ImageFont.truetype(font, size["time"])
        d = ImageDraw.Draw(img)
        if member.nick is None:
            txt = member.name
        else:
            txt = member.nick
        color = member.color.to_rgb()
        if color == (0, 0, 0):
            color = (255, 255, 255)
        d.text((90, 20), txt, font=titlefnt, fill=color)
        h, w = d.textsize(txt, font=titlefnt)
        time = datetime.utcnow().strftime("Today at %I:%M %p")
        d.text((90+h+10, 25), time, font=timefnt, fill=colour["time"])
        d.text((90, 25+w), message, font=titlefnt, fill=colour["content"])

        img.save('img.png')
        await member.display_avatar.with_format("png").save("pfp.png")
        f2 = Image.open("pfp.png")
        f1 = Image.open("img.png")
        f2.thumbnail((50, 55))
        f2.save("pfp.png")

        f2 = Image.open("pfp.png").convert("RGB")

        mask = Image.new("L", f2.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, f2.size[0], f2.size[1]), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(0))

        result = f2.copy()
        result.putalpha(mask)

        result.save('pfp.png')

        f2 = Image.open("pfp.png")

        f3 = f1.copy()
        f3.paste(f2, (20, 20), f2)
        f3.save("img.png")

        file = discord.File("img.png")
        await ctx.edit(file=file)

        try:
            os.remove("pfp.gif")
            os.remove("pfp.png")
            os.remove("img.png")
            await ctx.message.delete()
        except:
            pass

# setup COMMAND


def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun Cog is Loaded\n------")
