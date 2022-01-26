import discord
from discord.ext import commands
import traceback

intents = discord.Intents.all()
prefix = ['o!', 'O!']
bot = commands.Bot(command_prefix=prefix, case_insensitive=True, intents=intents)
OWNERID = 737903565313409095

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"/help | Made with ❤️ by KAUSHIK"))
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")

# Hello

@bot.command(guild_ids=[830504002905964586])
async def hello(ctx):
    """👋 Waves A Hand to Olympus"""
    await ctx.respond(f"Hello {ctx.author.mention}, I am Olympus. How are you doin' ?")

# Guild Join

@bot.event
async def on_guild_join(guild):
    em = discord.Embed(title=f"Guild Joined", description=f"**Name**: {guild.name}\n" ,color=0x3498DB, timestamp=guild.created_at)
    em.add_field(name=f"Guild ID:", value=f"`{guild.id}`", inline=False)
    em.add_field(name="Member Count:", value=f"{guild.member_count}", inline=False)
    em.add_field(name=f"Owner:", value=f"{guild.owner} (`{guild.owner_id}`)", inline=False)
    try:
        em.set_thumbnail(url=f"{guild.icon.url}")
    except:
        em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/902555662964359228/a8db71b81cbaed7567d996551bd0f56f.png")
    em.set_footer(text=f"Guild Created At")
    await bot.get_channel(912006221182152725).send(embed=em)
    
# Guild Leave

@bot.event
async def on_guild_remove(guild):
    em = discord.Embed(title=f"Guild Removed", description=f"**Name**: {guild.name}\n" ,color=0xE74C3C, timestamp=guild.created_at)
    em.add_field(name=f"Guild ID:", value=f"`{guild.id}`", inline=False)
    em.add_field(name="Member Count:", value=f"{guild.member_count}", inline=False)
    em.add_field(name=f"Owner:", value=f"{guild.owner} (`{guild.owner_id}`)", inline=False)
    try:
        em.set_thumbnail(url=f"{guild.icon.url}")
    except:
        em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/902555662964359228/a8db71b81cbaed7567d996551bd0f56f.png")
    em.set_footer(text=f"Guild Created At")
    await bot.get_channel(912006221182152725).send(embed=em)

# Welcome Message

@bot.event
async def on_member_join(member):
    if member.guild.id == 931474769797316638: #Check for Joins in a specific Guild
        guild = bot.get_guild(931474769797316638)
        botrole = discord.utils.get(guild.roles, name="Automation") # Auto-assign a role from Guild mentioned above.
        humanrole = discord.utils.get(guild.roles, name="Insighters")
        embed = discord.Embed(title="Welcome to `_TheKaushikG_` 🎴", description=f"Hey {member.mention}, Welcome to `_TheKaushikG_` 🎴.\n Enjoy your stay here. If you have any queries, feel free to contact our Management & Staff Team.\n We hope you will have a good time here. To Get started, check out these channels:")
        embed.add_field(name='‎‎‎‏‏‎ ‎', value=f"╭・Brief information about the Rules:\n ╰・<#931474769797316641>", inline=False)
        embed.add_field(name='‎‎‎‏‏‎ ‎', value=f"╭・Spice up your profile with some Self-Assignable Roles:\n ╰・<#931560761409548328>", inline=False)
        embed.add_field(name='‎‎‎‏‏‎ ‎', value=f"╭・Stay tuned with our Official Server Updates:\n ╰・<#931516407747846164>", inline=False)
        embed.add_field(name='‎‎‎‏‏‎ ‎', value=f"╭・Hangout with your friends :\n ╰・<#931474769797316643>", inline=False)
        embed.set_thumbnail(url=guild.icon.url)
        embed.set_image(url=f"https://cdn.discordapp.com/attachments/912569804483858434/931586826207109190/Welcome_Banner.png")
        embed.set_footer(icon_url=guild.icon.url, text="Thanks For Joining <3")
        await bot.get_channel(931474769797316640).send(content=f"{member.mention}", embed=embed)

        if member.bot == True:
            await member.add_roles(botrole)
        else:
            await member.add_roles(humanrole)

#Cogs Setup

extensions=[
              'cogs.mod',
              'cogs.api_cmd',
              'cogs.fun',
              'cogs.utility',
              'cogs.owner',
              'cogs.olympus',
              'cogs.help'
]
if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(e)
            traceback.print_exc()

bot.run("Your-Token-Here")