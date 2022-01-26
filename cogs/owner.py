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

def setup(bot):
    bot.add_cog(Owner(bot))
    print("Owner cog is Loaded\n------")