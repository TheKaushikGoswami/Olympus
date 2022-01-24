from discord import slash_command, Option
from discord.ext import commands
from discord.ext.commands.errors import MissingPermissions, BotMissingPermissions

class Activities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @commands.has_permissions(start_embedded_activities=True)
    async def activity(self, ctx, activity: Option(str, "Choose the Activity You wanna play in the Voice Channel", choices=["Watch Together", "Poker Night", "Chess in the Park", "Betrayal.io", "Fishington.io", "Letter Tile", "Word Snack", "Doodle Crew", "SpellCast", "Awkword", "Checkers in the Park"], required=True)):
        """🚀 Let's Have Some Fun Activities Together"""

        try:
            activities = {"Watch Together":'youtube', "Poker Night":'poker', "Chess in the Park":'chess', "Betrayal.io":'betrayal', "Fishington.io":'fishington', "Letter Tile":'letter-tile', "Word Snack": 'word-snack', "Doodle Crew":'doodle-crew', "SpellCast":'spellcast', "Awkword":'awkword', "Checkers in the Park":'checkers'}

            final_activity = activities.get(activity)
            if ctx.author.voice == None:
                await ctx.respond(f"**<:Cross:902943066724388926> You Need To Join a Voice Channel in order to Start An Activity!**", ephemeral=True)
            else:
                link = await self.bot.togetherControl.create_link(ctx.author.voice.channel.id, final_activity)
                await ctx.respond(f"Click the Blue Link!\n{link}")
        except Exception as e:
            print(e)
    
    @activity.error
    async def activity_error(self, ctx, error):
        if isinstance(error, ConnectionError):
            await ctx.respond(f"**<:Cross:902943066724388926> Oops! There was an issue connecting to Discord API!**")
        elif isinstance(error, MissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> You need `Start Activities` permission to be able to use this command.**")
        elif isinstance(error, BotMissingPermissions):
            await ctx.respond(f"**<:Cross:902943066724388926> I don't have enough permissions to Launch the Activity**")

def setup(bot):
    bot.add_cog(Activities(bot))
    print("Activities Cog is Loaded\n------")