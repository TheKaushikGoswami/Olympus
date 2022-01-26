import discord
from discord.ext import commands
from discord.commands import slash_command
from discord.ext.commands.errors import MissingPermissions 
from discord import slash_command, Option
from ago import human
import collections
import discord.utils
import asyncio

class Utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.times = dict()

# userinfo

    @slash_command()
    async def userinfo(self, ctx, member: Option(discord.Member, "Choose The Member", required=False)):
        """👤 Gets Information about a User"""
        await ctx.defer()
        if not member:
            member = ctx.author
        uroles = []
        for role in member.roles[1:]:
            if role.is_default():
                continue
            uroles.append(role.mention)

            uroles.reverse()
        timestamp = 'ㅤ'
        time = member.created_at
        time1 = member.joined_at
        if member.status == discord.Status.online:
            status = '<:online:909452628763750400>'
        elif member.status == discord.Status.idle:
            status = '<:idle:909452697999118337>'
        elif member.status == discord.Status.dnd:
            status = '<:dnd:909452665224822826>'
        else:
            status = '<:offline:909452732719570974>'
        if member.activity == None:
            activity = 'None'
        else:
            activity = member.activities[-1].name
            if member.activities[0].details != None:
                timestamp = member.activities[0].details
            else:
                timestamp = ' '
        embed = discord.Embed(color=ctx.author.color, type="rich")
        embed.set_thumbnail(url=f"{member.avatar.url}")
        embed.set_author(name=f"{member.name}'s information",
                        icon_url=f'{ctx.me.avatar.url}')
        embed.add_field(name="__General information__", value=f'**Nickname :** `{member.display_name}`\n'
                        f'**ID :** {member.id}\n'
                        f'**Account created :** `{member.created_at.strftime("%A, %B %d %Y %H:%M:%S %p")}`\n{human(time, 4)}\n'
                        f'**Server Joined :** `{member.created_at.strftime("%A, %B %d %Y %H:%M:%S %p")}`\n{human(time1, 4)}\n', inline=False)

        embed.add_field(name="__Role info__", value=f'**Highest role :** {member.top_role.mention}\n'
                        f'**Color** : `{member.color}`\n' f'**Role(s) :** {", ".join(uroles)}\n', inline=False)

        embed.add_field(name="__Presence__", value=f'**Status : ** {status}\n'
                        f'**Activity : ** ```{activity}\nㅤ{timestamp}```')
        embed.set_footer(
            text=f"Requested by {ctx.author.name}",  icon_url=ctx.author.avatar.url)
        await ctx.edit(embed=embed)
        return

# avatar

    @slash_command()
    async def avatar(self, ctx, user: Option(discord.Member, "Choose the Member", required=False)):
        """🖼️ Gets the avatar of a User"""
        if not user:
            user = ctx.author
        embed = discord.Embed(
            title=f"`{user.name}`'s avatar", color=ctx.author.color)
        embed.description = f'[PNG]({user.display_avatar.with_static_format("png")}) | [JPEG]({user.display_avatar.with_static_format("jpeg")}) | [WEBP]({user.display_avatar.with_static_format("webp")})'
        embed.set_image(url=str(user.display_avatar.with_static_format("png")))
        embed.set_footer(
            text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar.url)
        if user.avatar.is_animated():
            embed.description += f' | [GIF]({user.display_avatar.with_static_format("gif")})'
            embed.set_image(url=str(user.display_avatar.with_static_format("gif")))

        await ctx.respond(embed=embed)

# membercount

    @slash_command()
    async def membercount(self, ctx):
        """🧑🏼‍🤝‍🧑🏼 Fetches the number of members in the server"""
        embed = discord.Embed(color=0x529dff)
        embed.add_field(name="Members",
                        value=f"{ctx.guild.member_count}", inline=False)
        embed.set_footer(text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

# Serverinfo

    @slash_command()
    async def serverinfo(self, ctx):
        """ℹ️ Gets You information about the server"""
        guild = ctx.guild
        emojis = str(len(guild.emojis))

        channels = str(len(guild.channels))
        roles = str(len(guild.roles))
        time = ctx.guild.created_at.strftime("%a, %#d %B %Y, %I:%M %p ")
        voice = str(len(guild.voice_channels))
        text = str(len(guild.text_channels))
        verification_level = str(guild.verification_level).capitalize()
        statuses = collections.Counter(
            [member.status for member in guild.members])

        online = statuses[discord.Status.online]
        idle = statuses[discord.Status.idle]
        dnd = statuses[discord.Status.dnd]
        offline = statuses[discord.Status.offline]

        embed = discord.Embed(
            color=ctx.author.color)
        try:
            embed.set_thumbnail(url=f"{ctx.guild.icon.url}")
        except:
            embed.set_thumbnail(url=f"{self.me.avatar.url}")
        embed.set_author(name=f"Information for  {ctx.guild.name}")
        embed.add_field(name="__General information__\n", value=f'**Server name : ** `{guild.name}`\n'
                        f'**Server ID : ** `{guild.id}`\n'
                        f'**Created at : ** `{time}`\n'
                        f'**Verification level : ** `{verification_level}`\n'
                        f'**Server owner : ** <@{ctx.guild.owner_id}> \n', inline=False)

        embed.add_field(name="\n\n\n__Statistics__", value=f'**Member count : ** {ctx.guild.member_count}\n'
                        f'**Roles count : ** {roles} \n'
                        f'**Channel count : ** {channels}\n'
                        f'**Text channels :** {text}\n'
                        f'**Voice channels :** {voice}\n'
                        f'**Emoji count : ** {emojis}\n'
                                                 f'**Server boosts : ** {guild.premium_subscription_count}\n')

        embed.add_field(name="__Activity__", value=f'<:online:909452628763750400>{online}\n'
                        f'<:idle:909452697999118337>{idle}\n'
                        f'<:dnd:909452665224822826>{dnd}\n'
                        f'<:offline:909452732719570974>{offline}')

        embed.set_footer(
            text=f"Requested by {ctx.author}",  icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

# Role Info

    @slash_command()
    async def roleinfo(self, ctx, role: Option(discord.Role, "Choose the Role or Enter the Role ID", required=True)):
        """🍥 Gets the information about the role mentioned"""
        allowed = []
        try:
            permissions = role.permissions

            for name, value in permissions:
                if value:
                    name = name.replace('_', ' ').replace(
                        'guild', 'server').title()
                    allowed.append(name)
        except:
            return await ctx.respond(f"Couldn't find the role")
        time = role.created_at
        em = discord.Embed(description=f'', color=ctx.author.color, timestamp=time)
        em.set_author(name=f'{role}', icon_url=f'{ctx.author.avatar.url}')
        try:
            em.set_thumbnail(url=f"{ctx.guild.icon.url}")
        except:
            em.set_thumbnail(url=f"{self.me.avatar.url}")
        em.add_field(name='__Info__', value=f'**ID :** {str(role.id)} \n'
                                            f'**Color :** {role.color}\n'
                                            f'**Hoisted :** {str(role.hoist)}\n'
                                            f'**Position :** {str(role.position)}\n'
                                            f'**Is mentionable :** {str(role.mentionable)}\n'
                                            f'**Members in role :** {str(len(role.members))}\n')
        em.add_field(name='__Role Permissions__', value=f', '.join(allowed) or 'No Valid Perms Enabled on this role!', inline=False)
        em.set_footer(text="Role created on")
        await ctx.respond(embed=em)

# Channel Stats

    @slash_command()
    async def channelstats(self, ctx):
        """🔗 Fetches information about the channel where the cmd is envoked at"""
        channel = ctx.channel
        thumbnail = ctx.guild.icon.url or ctx.me.avatar.url
        tmembers = str(len(channel.members))
        nsfw = (ctx.channel.is_nsfw())
        news = (ctx.channel.is_news())
        embed = discord.Embed(color=ctx.author.color)
        embed.set_thumbnail(url=f'{thumbnail}')
        embed.add_field(name="__Information__", value=f'**Server name: ** `{ctx.guild.name}`\n'
                        f'**Channel name :** `{channel.name}`\n'
                        f'**Channel ID : ** `{channel.id}`\n'
                        f'**Channel type : ** `{channel.type}`\n'
                        f'**Channel category : ** `{channel.category}`\n'
                        f'**Topic : ** `{channel.topic}`\n'
                        f'**Channel position :** `{channel.position}`\n'
                        f'**Created at :** `{channel.created_at.strftime("%a, %#d %B %Y, %I:%M %p ")}`\n'
                        f'**Slowmode :** `{channel.slowmode_delay}`\n'
                        f'**Channel Permissions :** `{channel.permissions_synced}`\n'
                        f'**Channel members :** `{tmembers}`\n'
                        f'**Is nsfw : ** `{nsfw}`\n'
                        f'**Is news : ** `{news}`', inline=False)

        embed.set_author(name="Channel Stats", icon_url=f'{ctx.me.avatar.url}')
        embed.set_footer(
            text=f" Requested by {ctx.author}", icon_url=ctx.author.avatar.url)
        await ctx.respond(embed=embed)

# Timer

    @slash_command()
    async def timer(self, ctx, time: Option(str, "Enter the time you want to set the Timer for!", required=True)):
        """⏱️ Sets a timer for You (in Minutes)"""
        try:
            is_there = self.times[ctx.author.id]
            now = time.time()
            gap = now - is_there['time']
            del self.times[ctx.author.id]
            return await ctx.respond(embed=discord.Embed(
                description='⌚ | Timer was set for {}'.format(await self.convert(int(gap))),
                colour=discord.Colour.red()
            ))
        except KeyError:
            if not time:
                self.times[ctx.author.id] = {
                    'time': time.time()
                }
                await ctx.respond(embed=discord.Embed(
                    description='⌚ | The timer has been set...',
                    colour=discord.Colour.red()
                ))
            else:
                try:
                    time = int(time)
                except ValueError:
                    ctx.command.reset_cooldown(ctx)
                    return await ctx.respond(embed=discord.Embed(
                        description='<a:RedTick:796628786102927390> Time to set must a number (counted with minutes)',
                        colour=discord.Color.red()
                        ))
                await ctx.respond(embed=discord.Embed(
                    description='⌚ | Will remind you in **{}** minute(s).'.format(time),
                    colour=discord.Colour.green()
                ))
                await asyncio.sleep(time*60)
                return await ctx.send(embed=discord.Embed(
                    description='⏰ | Times Up!',
                    colour=discord.Color.red()
                    ), content=ctx.author.mention)

# Mentions

    @slash_command()
    async def mentions(self, ctx, limit: Option(str, "Number of messages to be checked for mentions (10 by Default)", default=10, required=False), user: Option(discord.Member, "Select the User whose mentions You want to check for", required=False)):
        """🔴 Counts the amount of mentions You got in last certain amount of messages"""
        user = ctx.author if not user else user
        try:
            limit = int(limit)
        except ValueError:
            return await ctx.respond('The limit for the searching must be a number.')
        if limit > 100:
            return await ctx.respond('Max limit is 100 messages. This is to keep the command consistent.')
        counter = 0
        async for message in ctx.channel.history(limit=limit):
            if user.mentioned_in(message):
                counter += 1
        await ctx.respond('You have been pinged {} times in the last {} messages.'.format(counter, limit))

# Say

    @slash_command()
    @commands.has_permissions(manage_messages=True)
    async def say(self, ctx, message: Option(str, "Enter the message You want me to say", required=True)):
        """💬 Makes Me speak Something For You"""
        say_embed = discord.Embed(
            description=f'**<:Tick:902943008096391299> Your message was sent successfully!**', color=0x3498DB)
        await ctx.respond(embed=say_embed, ephemeral=True)
        await ctx.send(message)

    @say.error
    async def say_error(self, ctx, error):
        print(type(error), "--- Say Command")
        if isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Manage Messages` permission to be able to use this command.**")

def setup(bot):
    bot.add_cog(Utility(bot))
    print("Utility Cog is Loaded\n------")