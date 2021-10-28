import asyncio
import os
import random
import typing
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *
import time
import datetime
# import buttons
#from discord.app import Option
from urllib.parse import quote_plus
import json
from typing import List
import os
from dotenv import load_dotenv
import sqlite3


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\nMember Cog is ready!")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        channel = bot.get_channel(895761785846636574)
        embed = discord.Embed(title=f"Willkommen",
                              description=f":wave: Willkommen auf diesem Server {member.mention}. :wave: ",
                              color=discord.Color.gold())
        embed.add_field(name="Regeln",
                        value=":exclamation: Bitte lese dir die <#895395790426603530> durch, um ein paar Fragen schon geklärt zu haben :exclamation: ",
                        inline=False)
        embed.add_field(name="Bot",
                        value=":interrobang: Wenn du fragen zu dem Bot hast, oder wenn du Fehler findest, oder generell wenn du ein Feature willst, schreibe eine Issue oder schreibe mich (<@821453379779035227>) __privat__ an. :interrobang:",
                        inline=False)
        embed.add_field(name="Bestrafungen",
                        value=":warning: Du kannst bestraft werden. Ein Member mit der Rolle 'Member' kann dich reporten. Ein Team Mitglied kann dich warnen und Muten. Und nur ein Administrator kann dich bannen (wir hoffen das das niemals Vorkommen wird) :warning:",
                        inline=False)
        embed.add_field(name="Spaß",
                        value=":stuck_out_tongue_winking_eye: Hab Spaß auf diesem Server :stuck_out_tongue_winking_eye:",
                        inline=False)
        embed.set_footer(text=f"{member.name} ({member.id})")
        await channel.send(embed=embed)



def setup(bot):
    bot.add_cog(Greetings(bot))