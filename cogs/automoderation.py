import asyncio
import sys
import json
from discord.ext import commands
from discord.commands import slash_command
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *
from dotenv import load_dotenv
import os

guild_id = 893947040869019708


def get_config(name):
    with open("invites.json", "r") as f:
        json_file = json.load(f)
        return json_file[name]


class Automod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """Checks allowed Discord server"""
        invite = 'https://discord.gg/'
        if invite in message.content:
            await message.delete()


    @commands.Cog.listener()
    async def on_message(self, message):
        load_dotenv()

        token = os.getenv("discord_token")

        if token in message.content:
            await message.delete()



def setup(bot):
    bot.add_cog(Automod(bot))