import discord, datetime, time
from discord.commands.commands import command, slash_command
from discord.ext import commands
import sys
import datetime
import random
import platform
import time
from discord.ext.commands import bot
import discord.utils

start_time = time.time()

class Olympus(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

# Ping

    @slash_command()
    async def ping(self, ctx):
        """🏓 Displays the Latency of the Bot"""
        msg = await ctx.respond("Pinging bot\'s latency...")
        times = []
        counter=0
        embed = discord.Embed(title="More information:", description="Pinged 3 times and calculated the average.", color = ctx.author.color)

        for _ in range(3):
            counter += 1
            start = time.perf_counter()
            await ctx.edit(content=f"Pinging... {counter}/3")
            end = time.perf_counter()
            speed = round((end - start) * 1000)
            times.append(speed)
            embed.add_field(name=f"Ping {counter}:", value=f"{speed}ms", inline=True)

        embed.set_author(name="Pong!", icon_url= ctx.author.avatar.url)
        embed.add_field(name="Bot latency", value=f"{round(self.bot.latency * 1000)}ms", inline=True)
        embed.add_field(name="Average speed", value=f"{round((round(sum(times)) + round(self.bot.latency * 1000))/4)}ms")  
        embed.set_thumbnail(url=f'{ctx.me.avatar.url}')
        embed.set_footer(text=f"Estimated total time elapsed: {round(sum(times))}ms")
        await ctx.edit(content=f":ping_pong: {round((round(sum(times)) + round(self.bot.latency * 1000))/4)}ms", embed=embed)

# Invite

    @slash_command()
    async def invite(self, ctx):
        """😃 Invite me to Your Server"""
        await ctx.respond(f"**{ctx.author.mention}, Invite Me by Clicking this link** ❯\n https://discord.com/api/oauth2/authorize?client_id=902555662964359228&permissions=8&scope=bot%20applications.commands")

# Support

    @slash_command()
    async def support(self, ctx):
        """❔ Get Support related to me here."""
        await ctx.respond(f"https://discord.gg/VYDq5AheEU")
        await ctx.send(f"👆 Join The Above Server for all support related to **Olympus**")

# Uptime

    @slash_command()
    async def uptime(self, ctx):
        """📈 The time I have been up from"""
        current_time = time.time()
        difference = int(round(current_time - start_time))
        text = str(datetime.timedelta(seconds=difference))
        embed = discord.Embed(colour=ctx.author.top_role.colour)
        embed.add_field(name="Uptime", value=f"I am online from\n `{text}`")
        try:
            await ctx.respond(embed=embed)
        except discord.HTTPException:
            await ctx.respond("Current uptime: " + text)
        

# About

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime #global variable to be used later in cog
        startTime = time.time()# snapshot of time when listener sends on_ready

    @slash_command()
    async def about(self, ctx):
        """🤝 Know more about me here."""
        pythonVersion = platform.python_version()
        pycVersion = discord.__version__
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
        embed=discord.Embed(title="About SPIKE", description=f"**Olympus** is an advanced discord bot, written in `Python` using the library named, `py-cord`.\n\n <:slash:910783011035963452> This bot is totally based on **Application Commands** AKA `/Slash commands` supporting other new discord features with it.\n\n <:badge:910783553694994453> The major features of the bot are `Moderation`, `Fun`, `Utility`, `Games`, etc. -based commands.\n\n <:users:910783496937668638> The bot is `user-friendly` too, to make it comfortable for everyone to get familiar with discord bots and stuff.", color=0x5de5c9)
        embed.set_thumbnail(url=f'{ctx.me.avatar.url}')
        embed.add_field(name=f"__General Details__", value=f"**❯ Bot:** Olympus#5983 (902555662964359228)\n **❯ Created On:** 3rd November 2020, 1:41:38 PM IST\n **❯ Uptime:** `{uptime}`\n **❯ Developer:** `_TheKauchikG_#5300` (<@737903565313409095>)", inline=False)
        embed.add_field(name=f"__Front-end Stats__", value=f"**❯ Servers:** {len(self.bot.guilds)}\n **❯ Channels:** {len(set(self.bot.get_all_channels()))}\n **❯ Users:** {len(set(self.bot.get_all_members()))}", inline=True)
        embed.add_field(name=f"__Back-end Stats__", value=f"**❯ Version:** [v1](https://github.com/TheKaushikGoswami/Olympus)\n **❯ Python version:** [v{pythonVersion}](https://python.org)\n **❯ py-cord version:** [v{pycVersion}](https://pycord.dev/)\n **❯ Modules:** Total 15 modules", inline=False)
        embed.add_field(name="__Check Out:__", value=f'[Invite](https://discord.com/api/oauth2/authorize?client_id=902555662964359228&permissions=8&scope=bot%20applications.commands) • [Support](https://discord.gg/VYDq5AheEU) • [Github(Bot)](https://github.com/TheKaushikGoswami/Olympus) • [Github(Me)](https://github.com/TheKaushikGoswami)')
        embed.set_image(url=f"https://i.imgur.com/yPCP0qr.png")
        embed.set_footer(icon_url=f'{ctx.me.avatar.url}', text=f"Olympus is made with ❤️ |  _TheKauchikG_#5300")
        await ctx.respond(embed=embed)

#setup COMMAND

def setup(bot):
    bot.add_cog(Olympus(bot))
    print("Olympus Cog is Loaded\n------")