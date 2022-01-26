import discord
from discord.ext import commands
from discord import slash_command
from disputils import BotEmbedPaginator

color = 0x1ABC9C
ban = 'https://cdn.discordapp.com/attachments/912569804483858434/912570890686988318/Kick_Ban_Unban.gif'
slowmode = 'https://cdn.discordapp.com/attachments/912569804483858434/912576188055175188/Slowmode.gif'
role = 'https://cdn.discordapp.com/attachments/912569804483858434/912574118048710656/Role.gif'
purge = 'https://cdn.discordapp.com/attachments/912569804483858434/912578349342277652/Purge_Purgeuser.gif'

class Help(commands.Cog):
    def __init__(self, Bot):
        self.bot = Bot
        self.cmds_per_page = 10

    @slash_command()
    async def help(self, ctx):
        """🍁 Need Help? Feel Free"""
        embed1 = discord.Embed(
            color=color, description=f"These are the commands which are executable in the **Olympus**. For additional info on a command, use `/<command>`, There will be a guide about how to use the command right below the command itself. For More Info on Moderation Commands, use `/helpmod`.")
        embed1.set_author(name="Help Interface",
                            icon_url=f'{ctx.me.avatar.url}')
        embed1.set_thumbnail(
            url=f"https://media2.giphy.com/media/401pPJe8AtsC55e1y8/source.gif")
        embed1.add_field(
            name="🛡️ Moderation", value=f'`nick` `purge` `purgeuser` `mute` `unmute` `kick` `ban` `nuke` `role` `slowmode` `lock` `unlock` `name_role`', inline=False)
        embed1.add_field(
            name="⚽ Fun & Games", value=f'`8ball` `activity` `lovemeter` `rps` `sad/happy/angry` `hello` `lenny` `flip` `f` `calculator` `diceroll` `meme` `joke` `password` `slots` `cheers` `simp` `iq` `roast` `kill`',  inline=False)
        embed1.add_field(
            name="🖼️ Images", value=f'`cat` `dog` `panda` `koala` `clyde` `facepalm` `wink` `headpat` `triggered` `hug` `snap`', inline=False)
        embed1.add_field(
            name="🛠️ Utility", value=f'`userinfo` `serverinfo` `avatar` `membercount` `roleinfo` `channelstats` `say` `mentions` `timer`',  inline=False)
        embed1.add_field(
            name="💭 Facts & Advices", value=f'`dogfact` `catfact` `pandafact` `numberfact` `yearfact` `advice`',   inline=False)
        embed1.add_field(
            name="🤖 Olympus", value=f'`about` `ping` `invite` `support` `help` `uptime`', inline=False)
        embed1.add_field(
            name=f"👑 Owner Only", value=f'`stats` `serverlist` `createinvite` `leave`', inline=False)

        embed1.set_footer(
            text=f"Olympus is made with ❤️ | _TheKauchikG_#5300", icon_url=f'{ctx.author.avatar.url}')

        await ctx.respond(embed=embed1)

# Help Mod

    @slash_command()
    async def helpmod(self, ctx):
        """🛡️ Detailed Info about Moderation Commands"""
        await ctx.defer()
        embed1 = discord.Embed(color=color)
        embed1.set_author(name="Mod Commands", icon_url=f'{ctx.me.avatar.url}')

        embed1.add_field(name="Nick", value=f"**Permission** : Manage Nicknames \n"
                         "**Usage :\n** ```/nick <user> <nickname>```\n", inline=False)
        embed1.set_footer(text=f"Invoked by {ctx.author}", icon_url=ctx.author.avatar.url)

        embed2 = discord.Embed(color=color)
        embed2.add_field(name="Purge", value="**Limit** : 200 \n"
                         "**Default value** : 3 \n"
                         "**Permission** : Manage Messages \n"
                         "**Usage :\n** ```/purge <no-of-messages>```\n\n", inline=False)
        embed2.add_field(name="\nPurge User", value="**Default value** : 5\n"
                         "**Permission** : Manage Messages\n"
                         "**Usage :\n** ```/purgeuser <user> <no-of-messages>```\n" 
                         "**Example :** \n\n", inline=False)
        embed2.set_image(url=f'{purge}')
        embed2.set_footer(text=f"Invoked by {ctx.author}", icon_url=ctx.author.avatar.url)

        embed3 = discord.Embed(color=color)
        embed3.add_field(name="Kick", value=f"**Permission** : Kick Members\n"
                         "**Usage :\n** ```/kick <user> <reason>```\n", inline=False)
        embed3.add_field(name="Ban", value=f"**Permission** : Ban Members\n"
                         "**Usage :\n** ```/ban <user> <reason>```\n", inline=False)
        embed3.add_field(name="Unban", value=f"**Permission** : Ban Members\n"
                         "**Usage :\n** ```/unban <user-id>```\n"
                         "**Example :** \n\n", inline=False)
        embed3.set_image(url=f'{ban}')
        embed3.set_footer(text=f"Invoked by {ctx.author}", icon_url=ctx.author.avatar.url)

        embed4 = discord.Embed(color=color)
        embed4.add_field(name='Role', value=f"**Permission** : Manage Roles\n"
                         "**Usage :\n** ```/role <user> <role>```\n"
                         "**Example :** \n\n", inline=False)
        embed4.set_image(url=f'{role}')
        embed4.set_footer(text=f"Invoked by {ctx.author}", icon_url=ctx.author.avatar.url)

        embed5 = discord.Embed(color=color)
        embed5.add_field(name='Slowmode', value=f"**Permission** : Manage Channels\n"
                                                "**Usage :\n** ```/slowmode <time (in seconds)>```\n"
                                                "**Example **:\n\n")
        embed5.set_image(url=f'{slowmode}')
        embed5.set_footer(text=f"Invoked by {ctx.author}", icon_url=ctx.author.avatar.url)

        embed6 = discord.Embed(color=color)
        embed6.add_field(name='Lock', value=f'**Permission :** Manage Channels\n'
                         '**Usage :** ```/lock```', inline=False)
        embed6.add_field(name='Unlock', value=f'**Permission :** Manage Channels\n'
                         '**Usage :** ```/unlock```\n')
        embed6.set_footer(text=f"Invoked by {ctx.author}", icon_url=ctx.author.avatar.url)
        embeds = [embed1, embed2, embed3, embed4, embed5, embed6]
        paginator = BotEmbedPaginator(ctx, embeds)
        await ctx.respond(f"**Moderation Commands are Listed Here:**")
        await paginator.run()


def setup(Bot):
    Bot.add_cog(Help(Bot))
    print("Help cog is Loaded\n------")
