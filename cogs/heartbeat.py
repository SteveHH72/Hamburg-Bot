import asyncio
import datetime

from discord.ext import commands
from discord.commands import slash_command
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *
import buttons.button
from buttons.button import Poll
from buttons.button import Google
from buttons.button import TicTacToeButton
from buttons.button import TicTacToe

guild_id = 893947040869019708


class Heartbeat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.loop.create_task(heartbeat(self))
        print("\nHeartbeat Cog is ready")


def setup(bot):
    bot.add_cog(Heartbeat(bot))


async def heartbeat(self):
    while True:
        try:
            channel = self.bot.get_channel(901425113172418570)

            message = discord.Embed(title=" :heartbeat: Heartbeat",
                                    description=f"Bot is online, {datetime.datetime.now()}",
                                    color=discord.Color.blue())

            await channel.send(embed=message)
            await asyncio.sleep(20)
            await channel.purge()

        except discord.HTTPException:
            return
