from discord.ext import commands
from discord.commands import slash_command
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *

guild_id = 893947040869019708


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\nHelp Cog is ready!")

    @slash_command(guild_ids=[guild_id],
                   description="A short about the Server and the Bot")
    async def help(self, ctx):
        embedVar = discord.Embed(title="Hilfe", description='''
    Prefix: `/`
        Version: `1.2.5`
        Please write every time you need the Bot the prefix ( `/` ) at the beginning''', color=discord.Color.orange())
        embedVar.add_field(name="Slash-Command",
                           value="You always can see, what for Arguments you need.", inline=False)
        embedVar.add_field(name="Bot",
                           value="The Bot will **NEVER** ask you after your password or your Discord-Bot Token",
                           inline=False)
        embedVar.add_field(name="Information general to Discord Server invites",
                           value="Discord Invite Links Are not allowed. Please ask <@821453379779035227> for Permissions",
                           inline=False)
        embedVar.add_field(name="Moderation",
                           value="Please no insults (insults will be detected) and also please no spam (penalty is a mute)",
                           inline=False)
        await ctx.respond(embed=embedVar)


def setup(bot):
    bot.add_cog(Help(bot))
