import string

from discord.ext import commands
from discord.commands import slash_command
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *
import buttons.button
from buttons.button import Confirm


guild_id = 893947040869019708


class Settings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\nSettings Cog is ready!")

    @slash_command(guild_ids=[guild_id], description="Change the  prefix of the Bot", name="chprefix")
    async def change_prefix(self, ctx, prefix: str):
        if not 0 < len(prefix) <= 16:
            laenge = discord.Embed(title=" :x: Error", description="Prefix is too long", color=discord.Color.dark_red())
            await ctx.respond(embed=laenge)

        valid_chars = set(string.ascii_letters + string.digits + string.punctuation) - {"`"}
        if prefix not in valid_chars:
            valid = discord.Embed(title=" :x: Error", description="Prefix has no valid ascii letters!", color=discord.Color.dark_red())
            await ctx.respond(embed=valid)

        embed = discord.Embed(title="Prefix", description=f"Prefix has been changed successful. New Prefix = {prefix}")
        await ctx.respond(embed=embed)
        changelog = discord.Embed(title="New Prefix", description=f"{ctx.author.mention} changed the bot prefix to {prefix}")
        channel = self.bot.get_channel(895761460033110047)
        await channel.send(embed=changelog)




def setup(bot):
    bot.add_cog(Settings(bot))