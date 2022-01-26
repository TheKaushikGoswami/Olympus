import discord
from discord import Option
from discord.commands.errors import ApplicationCommandInvokeError
from discord.errors import NotFound
from discord.ext import commands
from discord.commands import slash_command
from discord.ext.commands.errors import MissingPermissions
import asyncio

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Nickname

    @slash_command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: Option(discord.Member, "Select the user", required=True), nickname: Option(str, "Write the new nickname of the user", required=False, default=None)):
        """✒️ Change the nickname of a user"""
        if nickname == None:
            nick_msg = f"```{member}\'s nickname was reset by {ctx.author}```"
        else:
            nick_msg = f"```{member}\'s nickname was changed to {nickname} by {ctx.author}```"
        if ctx.user.id == ctx.guild.owner_id:
            await member.edit(nick=nickname)
            await ctx.respond(nick_msg)
            return
        elif ctx.user.top_role.position > member.top_role.position:
            await member.edit(nick=nickname)
            await ctx.respond(nick_msg)
            return
        else:
            await ctx.respond(f"**<:Cross:902943066724388926> You can't change the nickname of that person**", ephemeral=True)

    @nick.error
    async def nick_error(self, ctx, error):
        print(type(error), "--- Nickname Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Nicknames` permission to be able to use this command.**")
        if isinstance(error, ApplicationCommandInvokeError):
            await ctx.respond(f"**<:Cross:902943066724388926> The user is having a higher role than me...**")

# Purge

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: Option(int, "Enter the number of messages to be purged(Default = 3)", required=False)):
        """🧹 Clears a certain amount of messages from the channel"""
        if amount == None:
            amount = 3
        else:
            amount = int(amount)
        if amount <= 200:
            await ctx.channel.purge(limit=amount)
            await ctx.respond(f"**<a:exclaim:905693082857639937> The higher-ups have purged some messages.**", delete_after=5)

        else:
            await ctx.respond(f"**<:Cross:902943066724388926> Please input a number smaller than 200**", ephemeral=True)

    @purge.error
    async def purge_error(self, ctx, error):
        print(type(error), "--- Purge Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Messages` permission to be able to use this command.**")

# PurgeUser

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def purgeuser(self, ctx, member: Option(discord.Member, "Select the Member", required=True), amount: Option(int, "Enter the number of messages to be purged(Default = 5)", required=False)):
        """🧹 Clears a certain amount of messages by a specific user"""
        if amount == None:
            amount = 5
        else:
            amount = int(amount)
        channel = ctx.channel

        def check(ctx):
            return ctx.author.id == member.id

        if ctx.user.id == ctx.guild.owner_id:
            await channel.purge(limit=amount, check=check, before=None)
            await ctx.respond(f"**<a:exclaim:905693082857639937> The higher-ups have purged someone\'s messsages.**", delete_after=5)
        elif ctx.user.top_role.position > member.top_role.position:
            await channel.purge(limit=amount, check=check, before=None)
            await ctx.respond(f"**<a:exclaim:905693082857639937> The higher-ups have purged someone\'s messsages.**", delete_after=5)
        else:
            await ctx.respond(f"**<:Cross:902943066724388926> You are not cool enough to delete that person\'s messages.**", ephemeral=True)

    @purgeuser.error
    async def purgeuser_error(self, ctx, error):
        print(type(error), "--- Purge User Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Messages` permission to be able to use this command.**")
        if isinstance(error, ApplicationCommandInvokeError):
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to delete this user\'s messages.**")

# Nuke Channel

    @slash_command()
    @commands.has_permissions(manage_channels=True)
    async def nukechannel(self, ctx):
        """💥 Nukes a channel and re-create another clone of it"""
        await ctx.defer()
        channel = ctx.channel
        positions = ctx.channel.position
        n = await channel.clone()
        await n.edit(position=positions)
        await channel.delete()
        await n.send(" :ok_hand: Successfully Nuked this channel")
        await n.send("https://giphy.com/gifs/animation-explosion-bomb-FnatKdwxRxpVC?utm_source=media-link&utm_medium=landing&utm_campaign=Media%20Links&utm_term=")

    @nukechannel.error
    async def nukechannel_error(self, ctx, error):
        print(type(error), "--- Nuke Channel Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Channels` permission to be able to use this command.**")
        if isinstance(error, ApplicationCommandInvokeError):
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to nuke this channel.**")

# Role

    @slash_command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: Option(discord.Member, "Select the member", required=True), role: Option(discord.Role, "Select the role", required=True)):
        """🍥 Add or Remove a role from a User"""
        if ctx.user.id == ctx.guild.owner_id:
            if role not in member.roles:
                await member.add_roles(role)
                await ctx.respond(f"`{member}` was given role `{role.name}`.")
            else:
                await member.remove_roles(role)
                await ctx.respond(f"`{member}` was removed from the role `{role.name}`.")
        elif ctx.user.top_role.position > role.position:
            if role not in member.roles:
                await member.add_roles(role)
                await ctx.respond(f"`{member}` was given role `{role.name}`.")
            else:
                await member.remove_roles(role)
                await ctx.respond(f"`{member}` was removed from the role `{role.name}`.")
        else:
            await ctx.respond(f"**<:Cross:902943066724388926> That role is higher than or same as your top-most role!**", ephemeral=True)

    @role.error
    async def role_error(self, ctx, error):
        print(type(error), "--- Role Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Roles` permission to be able to use this command.**")
        if isinstance(error, ApplicationCommandInvokeError):
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to manage this role.**")

# Slowmode

    @slash_command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, time: Option(str, "Enter the time (in seconds)", required=False)):
        """🕐 Adds or Removes the slowmode from the channel"""
        if time == None:
            await ctx.channel.edit(slowmode_delay=0)
            await ctx.respond(f"Slowmode removed.")
        else:
            await ctx.channel.edit(slowmode_delay=int(time))
            await ctx.respond(f"`{time}s` of slowmode was set on the current channel.")
    
    @slowmode.error
    async def slowmode_error(self, ctx, error):
        print(type(error), "--- Slowmode Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Channels` permission to be able to use this command.**")
        if isinstance(error, ApplicationCommandInvokeError):
            await ctx.respond(f"**<:Cross:902943066724388926> Invalid Duration! The slowmode duration must be less than or equal to 21600 seconds.**")

# Channel Lock

    @slash_command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        """🔒 Locks the channel for the server members"""
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond("**🔒 Channel locked down. Only staff members may speak. Do not bring the topic to other channels or risk disciplinary actions.**")
    
    @lock.error
    async def lock_error(self, ctx, error):
        print(type(error), "--- Lock Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Channels` permission to be able to use this command.**")

# Channel Unlock

    @slash_command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        """🔓 Unlocks the locked channel for the server members"""
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
        await ctx.respond("**🔓 Channel unlocked.**")

    @unlock.error
    async def unlock_error(self, ctx, error):
        print(type(error), "--- Unlock Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Channels` permission to be able to use this command.**")

# Mute

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def mute(self, ctx, member: Option(discord.Member, "Select the user", required=True), time: Option(str, "Mention the mute duration(s: seconds, m: minutes, h: hours, d: days)", required=True), reason: Option(str, "Write the reason for mute", required=False, default="Reason Not Mentioned")):
        """🤐 Mutes a member for a specific duration of time"""
        guild = ctx.guild
        Muted = discord.utils.get(guild.roles, name="Muted")
        # Gets the numbers from the time argument, start to -1
        seconds = int(time[:-1])
        duration = time[-1]  # Gets the timed maniulation, s, m, h, d
        if duration == "s":
            seconds = seconds * 1
        elif duration == "m":
            seconds = seconds * 60
        elif duration == "h":
            seconds = seconds * 60 * 60
        elif duration == "d":
            seconds = seconds * 86400
        else:
            await ctx.respond("Invalid time input", ephemeral=True)
            return

        if not Muted:
            Muted = await guild.create_role(name="Muted")

            for channel in guild.channels:
                await channel.set_permissions(Muted, speak=False, send_messages=False, read_message_history=True, read_messages=False)

        if ctx.user.id == ctx.guild.owner_id:
            await member.add_roles(Muted, reason=reason)
            await ctx.respond(f":ok_hand: {member.mention} was successfully muted!")
            await asyncio.sleep(seconds)
            await member.remove_roles(Muted, reason="Mute Period Over")
            return
        elif ctx.user.top_role.position > member.top_role.position:
            await member.add_roles(Muted, reason=reason)
            await ctx.respond(f":ok_hand: {member.mention} was successfully muted!")
            await asyncio.sleep(seconds)
            await member.remove_roles(Muted, reason="Mute Period Over")
        elif ctx.user.id == 737903565313409095:
            await member.add_roles(Muted, reason=reason)
            await ctx.respond(f":ok_hand: {member.mention} was successfully muted!")
            await asyncio.sleep(seconds)
            await member.remove_roles(Muted, reason="Mute Period Over")
        else:
            await ctx.respond(f"**<:Cross:902943066724388926> You are not cool enough to mute that person.**", ephemeral=True)

    @mute.error
    async def mute_error(self, ctx, error):
        print(type(error), "--- Mute Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Messages` permission to be able to use this command.**")

# Unmute

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: Option(discord.Member, "Select the user", required=True)):
        """🗣️ Unmute a member"""
        role = discord.utils.get(ctx.guild.roles, name="Muted")
        if role in member.roles:
            await member.remove_roles(role)
            await ctx.respond(f"**:ok_hand: Successfully unmuted {member.mention}.**")
        else:
            await ctx.respond(f"**Is That Person even muted?** <:hmm:905680733597736980>")

    @unmute.error
    async def unmute_error(self, ctx, error):
        print(type(error), "--- Unmute Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Messages` permission to be able to use this command.**")

# Kick

    @slash_command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: Option(discord.Member, "Select the user", required=True), reason: Option(str, "Write the reason", required=False, default="Reason Not Mentioned")):
        """🦶 Kicks a user from the server."""
        kick_embed = discord.Embed(
            description=f"**<:Tick:902943008096391299>  `{member}` was successfully kicked!**", color=0x3498DB)
        if ctx.user.id == ctx.guild.owner_id:
            await member.kick(reason=reason)
            await ctx.respond(embed=kick_embed)
            return
        elif ctx.user.top_role.position > member.top_role.position:
            await member.kick(reason=reason)
            await ctx.respond(embed=kick_embed)
        else:
            await ctx.respond(f"**<:Cross:902943066724388926> You are not cool enough to kick that person.**", ephemeral=True)

    @kick.error
    async def kick_error(self, ctx, error):
        print(type(error), "--- Kick Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Kick Members` permission to be able to use this command.**")
        if isinstance(error, ApplicationCommandInvokeError):
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to kick this member!**")


# Ban

    @slash_command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: Option(discord.Member, "Select the user", required=True), reason: Option(str, "Write the reason", required=False, default="Reason Not Mentioned")):
        """✈️ Bans a Member from the server"""
        ban_embed = discord.Embed(
            description=f"**<:Tick:902943008096391299> `{member}` was successfully banned!**", color=0x3498DB)
        if ctx.user.id == ctx.guild.owner_id:
            await member.ban(reason=reason)
            await ctx.respond(embed=ban_embed)
            return
        elif ctx.user.top_role.position > member.top_role.position:
            await member.ban(reason=reason)
            await ctx.respond(embed=ban_embed)
        else:
            await ctx.respond(f"**<:Cross:902943066724388926> You are not cool enough to ban that person.**", ephemeral=True)

    @ban.error
    async def ban_error(self, ctx, error):
        print(type(error), "--- Ban Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Ban Members` permission to be able to use this command.**")
        if isinstance(error, ApplicationCommandInvokeError):
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to ban this member!**")

    @ban.error
    async def ban_error(self, ctx, error):
        print(type(error), "--- Ban Command")
        if isinstance(error, MissingPermissions):
            await ctx.send(f"**<:Cross:902943066724388926> You need `Ban Members` permission to be able to use this command.**")
        if isinstance(error, ApplicationCommandInvokeError):
            await ctx.send(f"**<:Cross:902943066724388926> I don\'t have enough permissions to ban this member!**")
# Unban

    @slash_command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: Option(str, "Enter the user ID"), reason: Option(str, "Write the reason", required=False, default="Reason Not Mentioned")):
        """🛬 Unbans a Member from the server"""
        guild = ctx.guild
        unban_user = await self.bot.fetch_user(int(user))
        unban_embed = discord.Embed(
            description=f"**<:Tick:902943008096391299>  `{unban_user.name}` was unbanned!**", color=0x3498DB)
        await guild.unban(unban_user)
        await ctx.respond(embed=unban_embed)

    @unban.error
    async def unban_error(self, ctx, error):
        print(type(error), "--- Role Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Ban Members` permission to be able to use this command.**")
        if isinstance(error, NotFound):
            await ctx.respond(f"**<:Cross:902943066724388926> Are You sure this user is banned? Coz Am Not.**")


def setup(bot):
    bot.add_cog(Mod(bot))
    print("------\nModeration Cog is Loaded\n------")
