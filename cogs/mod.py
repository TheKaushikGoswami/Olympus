import datetime
import discord
from discord import Option
from discord.commands.errors import ApplicationCommandInvokeError
from discord.errors import NotFound
from discord.ext import commands
from discord.commands import slash_command
from discord.ext.commands.errors import MissingPermissions

class Mod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

# Nickname

    @slash_command()
    @commands.has_permissions(manage_nicknames=True)
    async def nick(self, ctx, member: Option(discord.Member, "Select the user", required=True), nickname: Option(str, "Write the new nickname of the user", required=False, default=None)):
        """✒️ Change the nickname of a user"""
        try:
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
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don't have enough permissions to change their nickname!**")
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Nicknames` permission to be able to use this command.**")

# Purge

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, amount: Option(int, "Enter the number of messages to be purged(Default = 3)", required=False)):
        """🧹 Clears a certain amount of messages from the channel"""
        try:
            if amount == None:
                amount = 3
            else:
                amount = int(amount)
            if amount <= 200:
                await ctx.channel.purge(limit=amount)
                await ctx.respond(f"**<a:exclaim:905693082857639937> The higher-ups have purged some messages.**", delete_after=5)
            else:
                await ctx.respond(f"**<:Cross:902943066724388926> Please input a number smaller than 200**", ephemeral=True)
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Messages` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don't have enough permissions to delete the messages!**")

# PurgeUser

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def purgeuser(self, ctx, member: Option(discord.Member, "Select the Member", required=True), amount: Option(int, "Enter the number of messages to be purged(Default = 5)", required=False)):
        """🧹 Clears a certain amount of messages by a specific user"""
        try:
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
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Messages` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don't have enough permissions to delete the messages!**")

# Nuke Channel

    @slash_command()
    @commands.has_permissions(manage_channels=True)
    async def nukechannel(self, ctx):
        """💥 Nukes a channel and re-create another clone of it"""
        try:
            await ctx.defer()
            channel = ctx.channel
            positions = ctx.channel.position
            n = await channel.clone()
            await n.edit(position=positions)
            await channel.delete()
            await n.send(" :ok_hand: Successfully Nuked this channel")
            await n.send("https://giphy.com/gifs/animation-explosion-bomb-FnatKdwxRxpVC?utm_source=media-link&utm_medium=landing&utm_campaign=Media%20Links&utm_term=")
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Channels` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to nuke this channel.**")

# Role

    @slash_command()
    @commands.has_permissions(manage_roles=True)
    async def role(self, ctx, member: Option(discord.Member, "Select the member to change role of", required=True), role: Option(discord.Role, "Select the role", required=True)):
        """🍥 Add or Remove a role from a User"""
        try:
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
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Roles` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to manage that role.**")

# Slowmode

    @slash_command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, time: Option(str, "Enter the time (in seconds)", required=False)):
        """🕐 Adds or Removes the slowmode from the channel"""
        try:
            if time == None:
                await ctx.channel.edit(slowmode_delay=0)
                await ctx.respond(f"Slowmode removed.")
            else:
                await ctx.channel.edit(slowmode_delay=int(time))
                await ctx.respond(f"`{time}s` of slowmode was set on the current channel.")
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Channels` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to edit this channel\'s settings.**")
        except discord.HTTPException:
            await ctx.respond(f"**<:Cross:902943066724388926> Invalid Duration! The slowmode duration must be less than or equal to 21600 seconds.**")

# Channel Lock

    @slash_command()
    @commands.has_permissions(manage_channels=True)
    async def lock(self, ctx):
        """🔒 Locks the channel for the server members"""
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = False
        try:
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.respond("**🔒 Channel locked down. Only staff members may speak. Do not bring the topic to other channels or risk disciplinary actions.**")
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Channels` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to edit this channel\'s settings.**")

# Channel Unlock

    @slash_command()
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        """🔓 Unlocks the locked channel for the server members"""
        overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
        overwrite.send_messages = True
        try:
            await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
            await ctx.respond("**🔓 Channel unlocked.**")
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Channels` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to edit this channel\'s settings.**")

# Mute

    @slash_command()
    @commands.has_permissions(moderate_members=True)
    async def mute(self, ctx, member: Option(discord.Member, "Select the User to be Muted", required=True), time: Option(str, "Mention the mute duration(s:seconds, m:minutes, h:hours, d:days)", required=True), reason:Option(str, "Write the reason for mute", required=False)):
        """🤐 Mutes a member for a specific duration of time"""
        if reason == None:
            reason = f"Muted by {ctx.author} - No Reason Mentioned"
        else:
            reason = f"Muted by {ctx.author} - {reason}"
        prefix = int(time[:-1])
        suffix = time[-1]  # Gets the timed maniulation, s, m, h, d
        if suffix == "s":
            duration = datetime.timedelta(seconds=prefix)
        elif suffix == "m":
            duration = datetime.timedelta(minutes=prefix)
        elif suffix == "h":
            duration = datetime.timedelta(hours=prefix)
        elif suffix == "d":
            duration = datetime.timedelta(days=prefix)
        else:
            await ctx.respond("Invalid time input (Guide:- s:seconds, m:minutes, h:hours, d:days)", ephemeral=True)
            return

        try:
            if ctx.user.id == ctx.guild.owner_id:
                await member.timeout_for(duration=duration, reason=reason)
                await ctx.respond(f":ok_hand: {member.mention} was successfully muted!")
            elif ctx.user.top_role.position > member.top_role.position:
                await member.timeout_for(duration=duration, reason=reason)
                await ctx.respond(f":ok_hand: {member.mention} was successfully muted!")
            else:
                await ctx.respond(f"**<:Cross:902943066724388926> You are not cool enough to mute that person.**", ephemeral=True)
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don't have enough permissions to mute this person!**")
        except discord.HTTPException:
            await ctx.respond(f"**<:Cross:902943066724388926> You can mute a member for maximum `28 days(28d)` due to Discord API limitations**")
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Moderate Members` permission to be able to use this command.**")

# Unmute

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def unmute(self, ctx, member: Option(discord.Member, "Select the user to unmute", required=True)):
        """🗣️ Unmute a member"""
        try:
            if member.communication_disabled_until != None:
                await member.remove_timeout()
                await ctx.respond(f"**:ok_hand: Successfully unmuted {member.mention}.**")
            else:
                await ctx.respond(f"**Is That Person even muted?** <:hmm:905680733597736980>")
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Moderate Members` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to mute/unmute this member.**")

# Kick

    @slash_command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: Option(discord.Member, "Select the user", required=True), reason: Option(str, "Write the reason for kick", required=False)):
        """🦶 Kicks a user from the server."""
        if reason == None:
            reason = f"Kicked by {ctx.author} - No Reason Mentioned"
        else:
            reason = f"Kicked by {ctx.author} - {reason}"
        kick_embed = discord.Embed(
            description=f"**<:Tick:902943008096391299>  `{member}` was successfully kicked!**", color=0x3498DB)
        try:
            if ctx.user.id == ctx.guild.owner_id:
                await member.kick(reason=reason)
                await ctx.respond(embed=kick_embed)
                return
            elif ctx.user.top_role.position > member.top_role.position:
                await member.kick(reason=reason)
                await ctx.respond(embed=kick_embed)
            else:
                await ctx.respond(f"**<:Cross:902943066724388926> You are not cool enough to kick that person.**", ephemeral=True)
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Kick Members` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to kick that person.**")

# Ban

    @slash_command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: Option(discord.Member, "Select the user", required=True), reason: Option(str, "Write the reason for ban", required=False)):
        """✈️ Bans a Member from the server"""
        if reason == None:
            reason = f"Banned by {ctx.author} - No Reason Mentioned"
        else:
            reason = f"Banned by {ctx.author} - {reason}"
        ban_embed = discord.Embed(
            description=f"**<:Tick:902943008096391299> `{member}` was successfully banned!**", color=0x3498DB)
        try:
            if ctx.user.id == ctx.guild.owner_id:
                await member.ban(reason=reason)
                await ctx.respond(embed=ban_embed)
                return
            elif ctx.user.top_role.position > member.top_role.position:
                await member.ban(reason=reason)
                await ctx.respond(embed=ban_embed)
            else:
                await ctx.respond(f"**<:Cross:902943066724388926> You are not cool enough to ban that person.**", ephemeral=True)
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Ban Members` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to ban that person.**")

# Unban

    @slash_command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, user: Option(str, "Enter the user ID"), reason: Option(str, "Write the reason for unban", required=False)):
        """🛬 Unbans a Member from the server"""
        if reason == None:
            reason = f"Unbanned by {ctx.author} - No Reason Mentioned"
        else:
            reason = f"Unbanned by {ctx.author} - {reason}"
        guild = ctx.guild
        unban_user = await self.bot.fetch_user(int(user))
        unban_embed = discord.Embed(
            description=f"**<:Tick:902943008096391299>  `{unban_user.name}` was unbanned!**", color=0x3498DB)
        try:
            await guild.unban(unban_user, reason=reason)
            await ctx.respond(embed=unban_embed)
        except commands.MissingPermissions:
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Ban Members` permission to be able to use this command.**")
        except discord.Forbidden:
            await ctx.respond(f"**<:Cross:902943066724388926> I don\'t have enough permissions to ban that person.**")
        except discord.NotFound:
            await ctx.respond(f"**<:Cross:902943066724388926> Are You sure this user is banned? Coz Am Pretty sure He/She Isn't banned.**")

def setup(bot):
    bot.add_cog(Mod(bot))
    print("------\nModeration Cog is Loaded\n------")
