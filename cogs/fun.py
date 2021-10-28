from discord.ext import commands
from discord.commands import slash_command
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *
import buttons.button
from buttons.button import Confirm


guild_id = 893947040869019708


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\nFun Cog is ready!")

    @slash_command(guild_ids=[guild_id], description="TikTakToe")
    async def tic(self, ctx: commands.Context):
        await ctx.respond("Tic Tac Toe: X goes first", view=TicTacToe())

    @slash_command(guild_ids=[guild_id], description="Ask")
    async def ask(self, ctx: commands.Context):
        """Asks the user a question to confirm something."""
        # We create the view and assign it to a variable so we can wait for it later.
        view = Confirm()
        await ctx.send("Do you want to continue?", view=view)
        # Wait for the View to stop listening for input...
        await view.wait()
        if view.value is None:
            print("Timed out...")
        elif view.value:
            print("Confirmed...")
        else:
            print("Cancelled...")


def setup(bot):
    bot.add_cog(Fun(bot))