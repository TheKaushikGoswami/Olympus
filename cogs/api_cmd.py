import discord
from discord.ext import commands
import io
from logging import error
from discord import Option, slash_command
from discord.ext import commands
import aiohttp
import requests

class Api(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

# Dog

    @slash_command()
    async def dog(self, ctx):
        """🐶 Sends a random Doggo picture"""
        try:
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://dog.ceo/api/breeds/image/random") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Woof", color=ctx.author.color)
                    embed.set_image(url=data['message'])
                    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

                    await ctx.respond(embed=embed)
        except error:
            print(error)

# Cat

    @slash_command()
    async def cat(self, ctx):
        """🐱 Sends a random Catto picture"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("http://aws.random.cat/meow") as r:
                data = await r.json()

                embed = discord.Embed(title="Meow", color=ctx.author.color)
                embed.set_image(url=data['file'])
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.respond(embed=embed)

# Panda

    @slash_command()
    async def panda(self, ctx):
        """🐼 Sends a random Panda picture"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/panda") as r:
                data = await r.json()

                embed = discord.Embed(title="Pandasound :P", color=ctx.author.color)
                embed.set_image(url=data['link'])
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

                await ctx.respond(embed=embed)

# Panda

    @slash_command()
    async def koala(self, ctx):
        """🐨 Sends a random Koala picture"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/img/koala") as r:
                data = await r.json()
                embed = discord.Embed(title="Koala sound :P", color=ctx.author.color)
                embed.set_image(url=data['link'])
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.respond(embed=embed)

# DogFact

    @slash_command()
    async def dogfact(self, ctx):
        """🐕 Sends a random doggo fact"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/dog") as r:
                data= await r.json()

                embed = discord.Embed(title="Dog fact :D", description=data['fact'], color=ctx.author.color)
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

                await ctx.respond(embed=embed)

# CatFact

    @slash_command()
    async def catfact(self, ctx):
        """🐈 Sends a random catto fact"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/cat") as r:
                data= await r.json()

                embed = discord.Embed(title="Cat fact :D", description=data['fact'], color=ctx.author.color)
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.respond(embed=embed)

# PandaFact

    @slash_command()
    async def pandafact(self, ctx):
        """🐼 Sends a random panda fact"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/facts/panda") as r:
                data = await r.json()

                embed = discord.Embed(title="Panda fact", description=data['fact'], color=ctx.author.color)
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)

                await ctx.edit(embed=embed)

# YearFact

    @slash_command()
    async def yearfact(self, ctx):
        """📅 Sends a random Year fact"""
        await ctx.defer()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"http://numbersapi.com/random/year?json") as r:
                data = await r.json()
                embed = discord.Embed(title= data['number'], description=data['text'], color=ctx.author.color)
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.edit(embed=embed)

# NumberFact

    @slash_command()
    async def numberfact(self, ctx):
        """🔢 Sends a random Number fact"""
        await ctx.defer()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"http://numbersapi.com/random?json") as r:
                data = await r.json()
                embed = discord.Embed(title=data['number'], description=data ['text'],color=ctx.author.color)
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.edit(embed=embed)

# Clyde

    @slash_command()
    async def clyde(self, ctx, text: Option(str, "Enter the message you want Clyde to say")):
        """🤖 Makes Clyde say something for You"""
        await ctx.defer()
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=clyde&text={text}") as r:
                res = await r.json()
                embed = discord.Embed(color=ctx.author.color)
                embed.set_image(url=res['message'])
                embed.set_footer(text=f'Requested by {ctx.author.name}', icon_url=ctx.author.avatar.url)
                await ctx.edit(embed=embed)

# Advice

    @slash_command()
    async def advice(self, ctx):
        """💭 Gives a random but wise advice"""
        await ctx.defer()
        r = requests.get("https://api.adviceslip.com/advice").json()
        advice= r["slip"]["advice"]
        embed = discord.Embed(title=advice, color=ctx.author.color)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.edit(embed=embed)

# Headpat

    @slash_command()
    async def headpat(self, ctx):
        """😃 Pats your head for you :)"""
        await ctx.defer()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/pat") as r:
                data = await r.json()

                embed = discord.Embed(title="There there everything will be better" ,color=ctx.author.color)
                embed.set_image(url=data['link'])
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.edit(embed=embed)

# Wink

    @slash_command()
    async def wink(self, ctx):
        """😉 Winks at you ;)"""
        await ctx.defer()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/wink") as r:
                data = await r.json()

                embed = discord.Embed(title=";)" ,color=ctx.author.color)
                embed.set_image(url=data['link'])
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.edit(embed=embed)

# Hug

    @slash_command()
    async def hug(self, ctx):
        """🫂 Get some free Hugs!!!"""
        await ctx.defer()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/hug") as r:
                data = await r.json()

                embed = discord.Embed(title="Hug!!!!!" ,color=ctx.author.color)
                embed.set_image(url=data['link'])
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.edit(embed=embed)

# Facepalm

    @slash_command()
    async def facepalm(self, ctx):
        """🤦 Delivers a facepalm!"""
        await ctx.defer()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://some-random-api.ml/animu/face-palm") as r:
                data = await r.json()

                embed = discord.Embed(title="Palm to the face" ,color=ctx.author.color)
                embed.set_image(url=data['link'])
                embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
                await ctx.edit(embed=embed)

# Triggered

    @slash_command()
    async def triggered(self, ctx, member: Option(discord.Member, "Select the user you want to trigger", required=False)):
        """😤 Trigger someone (atleast in their pfp) ;)"""
        await ctx.defer()
        if member == None:
            member = ctx.author

        if member.avatar.is_animated():
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.display_avatar.with_static_format("gif").url}') as af:
                    if 300 > af.status >= 200:
                        fp = io.BytesIO (await af.read())
                        fileee = discord.File(fp, "triggered.gif")
                        em = discord.Embed(title="", color=ctx.author.color)
                        em.set_image(url="attachment://triggered.gif")
                        await ctx.edit(embed=em, files=[fileee])
        else:
            async with aiohttp.ClientSession() as session:
                async with session.get(f'https://some-random-api.ml/canvas/triggered?avatar={member.display_avatar.with_static_format("png").url}') as af:
                    if 300 > af.status >= 200:
                        fp = io.BytesIO (await af.read())
                        fileee = discord.File(fp, "triggered.png")
                        em = discord.Embed(title="", color=ctx.author.color)
                        em.set_image(url="attachment://triggered.png")
                        await ctx.edit(embed=em, files=[fileee])
        
# Weather

    @slash_command()
    async def weather(self, ctx, location: Option(str, "Enter the name of the location", required=True)):
        """⛅ Gets the Weather information for a location"""
        embed = discord.Embed(color=123456,
                            timestamp=discord.utils.utcnow(),
                            title=f"Weather in {location}")
        embed.set_image(
            url=
            f"https://api.cool-img-api.ml/weather-card?location={location}&background=https://cdn.discordapp.com/attachments/820496743211728937/829268642801647636/2021-04-07-15-17-17.jpg"
        )
        await ctx.respond(embed=embed)

# Achievement

    @slash_command()
    async def achievement(self, ctx, text: Option(str,"Enter the text for achievement", required=True)):
        """🏆 Rewards you with some achievement (whatever you want to)"""
        final = text.replace(" ", "+")
        image = f"https://api.cool-img-api.ml/achievement?text={final}"

        await ctx.respond(image)

def setup(bot):
    bot.add_cog(Api(bot))
    print("API Cog is Loaded\n------")