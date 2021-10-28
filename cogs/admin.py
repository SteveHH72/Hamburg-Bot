import asyncio
import sys

from discord.ext import commands
from discord.commands import slash_command
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *

guild_id = 893947040869019708


class Sudo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\nAdmin Cog is ready!")


    @slash_command(guild_ids=[guild_id], description="Sudeoer Kill Command")
    async def kill(self, ctx):
        await asyncio.sleep(3)
        print("Bot is offline")
        sys.exit(1)


def setup(bot):
    bot.add_cog(Sudo(bot))
