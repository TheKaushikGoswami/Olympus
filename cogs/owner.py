import discord
from discord.ext import commands
from discord import Option, slash_command
import platform

from discord.ext.commands.errors import NotOwner

class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Stats

    @slash_command(guild_ids=[830504002905964586, 820621306797359124])
    @commands.is_owner()
    async def stats(self, ctx):
        """📊 Shows the Statistics of the Bot"""
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.bot.guilds)
        memberCount = len(set(self.bot.get_all_members()))

        embed = discord.Embed(title=f'{self.bot.user.name} Stats', description='\uFEFF', colour=ctx.author.colour)
        embed.set_thumbnail(url=f"{ctx.me.avatar.url}")
        embed.add_field(name='Python Version:', value=pythonVersion, inline=False)
        embed.add_field(name='Discord.Py Version', value=dpyVersion, inline=False)
        embed.add_field(name='Total Guilds:', value=serverCount, inline=False)
        embed.add_field(name='Total Users:', value=memberCount, inline=False)
        embed.add_field(name='Bot Developers:', value="<@737903565313409095>", inline=False)

        embed.set_footer(text=ctx.author, icon_url=ctx.author.avatar.url)
        embed.set_author(name=self.bot.user, icon_url=ctx.me.avatar.url)

        await ctx.respond(embed=embed)

    @stats.error
    async def stats_error(self, ctx, error):
        print(type(error), "--- Stats Command")
        if isinstance(error, NotOwner):
            await ctx.respond(f"**<:Cross:902943066724388926> Hey! You lack permission to use this command as you don't own me!**")

# Server list

    @slash_command()
    @commands.is_owner()
    async def serverlist(self, ctx):
        """🎴 Shows the name of the guilds the bot is in"""
        await ctx.defer()
        msg = ""
        async for cached_guild in self.bot.fetch_guilds():
            guild = await self.bot.fetch_guild(cached_guild.id)
            msg += "".join(f"{guild.name} ({guild.id}) - ({guild.owner_id})\n")
            f = open("servers.txt", "w+", encoding="utf-8")
            f.write(msg)
            f.close()
        print(msg)
        upload_file = discord.File('./servers.txt')
        await ctx.edit(file=upload_file)

    @serverlist.error
    async def serverlist_error(self, ctx, error):
        print(type(error), "--- Serverlist Command")
        if isinstance(error, NotOwner):
            await ctx.respond(f"**<:Cross:902943066724388926> Hey! You lack permission to use this command as you don't own me!**")

# Create Invite

    @slash_command()
    @commands.is_owner()
    async def createinvite(self, ctx, guild_id: Option(str, "Enter the Guild ID", required=True)):
        """🎴 Creates invite for the Guild ID passed"""
        try:
            guild = self.bot.get_guild(int(guild_id))
            invitelink = ""
            i = 0
            while invitelink == "":
                channel = guild.text_channels[i]
                link = await channel.create_invite(max_uses=0)
                invitelink = str(link)
                i += 1
            await ctx.respond(invitelink)
        except Exception:
            print(Exception)
            await ctx.respond("Something went wrong")

    @createinvite.error
    async def createinvite_error(self, ctx, error):
        print(type(error), "--- CreateInvite Command")
        if isinstance(error, NotOwner):
            await ctx.respond(f"**<:Cross:902943066724388926> Hey! You lack permission to use this command as you don't own me!**")

# Leave

    @slash_command()
    @commands.is_owner()
    async def leave(self, ctx):
        """🎴 Leaves the Guild"""
        await ctx.respond(f"<:Tick:902943008096391299> **Leaving this Server**", ephemeral=True)
        await ctx.guild.leave()
    
    @leave.error
    async def leave_error(self, ctx, error):
        print(type(error), "--- Leave Command")
        if isinstance(error, NotOwner):
            await ctx.respond(f"**<:Cross:902943066724388926> Hey! You lack permission to use this command as you don't own me!**")

# Say

    @slash_command()
    @commands.is_owner()
    async def say(self, ctx, message: Option(str, "Enter the message You want me to say", required=True)):
        """💬 Makes Me speak Something For You"""
        say_embed = discord.Embed(
            description=f'**<:Tick:902943008096391299> Your message was sent successfully!**', color=0x3498DB)
        await ctx.respond(embed=say_embed, ephemeral=True)
        await ctx.send(message)

    @say.error
    async def say_error(self, ctx, error):
        print(type(error), "--- Say Command")
        if isinstance(error, NotOwner):
            await ctx.respond(f"**<:Cross:902943066724388926> Hey! You lack permission to use this command as you don't own me!**")

# Change Presence

    @slash_command()
    @commands.is_owner()
    async def change_presence(self, ctx, status: Option(str, "Status of the Bot", choices=["Online", "Idle", "Do Not Disturb", "Invisible"], required=False), activity: Option(str, "The Activity of the Bot", choices=["Playing", "Watching", "Listening", "Streaming"], required=False), activity_name = Option(str, "Name of the Activity", required=False, default="/help | Made with ❤️ by _TheKauchikG_#5300")):
        """🚀 Change the Activity of the Bot"""
        statuses = {"Online" : discord.Status.online, "Idle" : discord.Status.idle, "Do Not Disturb" : discord.Status.do_not_disturb, "Invisible" : discord.Status.invisible}
        final_status = statuses.get(status)

        activities = {"Playing" : discord.ActivityType.playing, "Watching" : discord.ActivityType.watching, "Listening" : discord.ActivityType.listening, "Streaming" : discord.ActivityType.streaming}
        final_activity = activities.get(activity)

        presence_embed = discord.Embed(description=f'**<:Tick:902943008096391299> The Presence was updated successfully!**', color=0x3498DB)
        try:
            if final_activity == discord.ActivityType.streaming:
                link = "https://www.twitch.tv/thekaushikgoswami"
                await self.bot.change_presence(status=discord.Status.streaming, activity=discord.Activity(type=final_activity,name=activity_name, url=link))
                await ctx.respond(embed=presence_embed)
            elif final_activity == discord.ActivityType.playing:
                game=discord.Game(activity_name)
                await self.bot.change_presence(status=final_status, activity=game)
                await ctx.respond(embed=presence_embed)
            else:
                await self.bot.change_presence(status=final_status, activity=discord.Activity(type=final_activity, name=activity_name))
                await ctx.respond(embed=presence_embed)
        except discord.InvalidArgument:
            await ctx.respond(f"**<:Cross:902943066724388926> There was an issue in setting up that activity. Please Try Again**", ephemeral=True)
        except NotOwner:
            await ctx.respond(f"**<:Cross:902943066724388926> Hey! You lack permission to use this command as you don't own me!**")

# Rules

    @slash_command(guild_ids=[931474769797316638])
    @commands.is_owner()
    async def rules(self, ctx):
        """The Rules command for my Private Server"""
        color = 0xa100f2
        embed = discord.Embed(color=color)

        embed.add_field(name='<:badge:910783553694994453> Rules! <:badge:910783553694994453>', value='**1.** Do not be racist, homophobic, or sexist, it can be overlooked if the other party is fine with it.\n\n'
                        '**2.** You are allowed to curse on someone as long as they do not mind. There are no barred curse words. If there are complaints on one\'s behavior then it may result in certain actions taken from the moderators.\n\n'
                        '**3.** You should not offend or antagonize other parties. You never know who the other party may be.\n\n'
                        '**4.** Spamming of texts, emojis, images, etc is strictly prohibited, if found out it may result in a permanent ban from the server.\n\n'
                        '**5.** The server does allow anything under the [Discord ToS](https://discord.com/terms) but it doesn\'t means that we won\'t take actions if the situation is necessary.\n\n', inline=False)
        embed.add_field(name='‎‎‎‏‏‎ ‎', value='**6.** Posts related to the information of another party, private messages, or pictures without their permission will be removed. This is a rigorous  policy, may result in a permanent ban.\n\n'
                        '**7.** Moderators have final judgment on everything, if they ask you to stop doing something then stop. Do not complain if you have been kicked or banned from the server.\n\n'
                        '**8.** You are free to debate about anything, just don\'t force your beliefs on others.\n\n'
                        '**9.** There shouldn\'t be any bullying or bad behavior to new members.\n\n'
                        '**10.** There should not be any sharing of graphical or image posts related to violence, gore, and things that are against Discord ToS \n\n'
                        '**11.** All NSFW content under ToS  are allowed, as long as they are NOT in Non-NSFW channels. This includes gifs, profile pictures, status,etc.\n\n'
                        '**12.** Self-advertising on main channels won\'t be tolerated, asking for roles, permissions, custom commands will result in warns from the moderators.', inline=False)
        embed.set_footer(icon_url=ctx.author.avatar.url, text="React with Tick below If You read everything!")
        await ctx.respond(embed=embed)

    @rules.error
    async def rule_error(self, ctx, error):
        print(type(error), "--- Rule Command")
        if isinstance(error, NotOwner):
            await ctx.respond(f"**<:Cross:902943066724388926> Hey! You lack permission to use this command as you don't own me!**", ephemeral=True)

def setup(bot):
    bot.add_cog(Owner(bot))
    print("Owner cog is Loaded\n------")