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