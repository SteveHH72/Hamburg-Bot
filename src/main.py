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
# from discord.app import Option
from urllib.parse import quote_plus
import json
from typing import List
import os
from dotenv import load_dotenv
import sqlite3
import buttons.button
from buttons.button import Message_Logging
from cogs.heartbeat import Heartbeat




guild_id = 893947040869019708

# --------------------------------------------------------


intents = discord.Intents.all()
intents.members = True

bot = commands.Bot(command_prefix=commands.when_mentioned_or("."), case_insensitive=True, help_command=None,
                   description="Das ist ein Moderations Bot", invoke_without_command=False, intents=intents,
                   command_attrs=dict(hidden=True))

guild = discord.Guild


# json


# def get_config(name):
# with open("word.json", "r") as f:
# json_file = json.load(f)
# return json_file[name]


# -----------------------------------------------------------------------------


@bot.user_command(guild_ids=[893947040869019708])  # create a user command for the supplied guilds
async def mention(ctx, member: discord.Member):  # user commands return the member
    await ctx.respond(f"{ctx.author.name} just mentioned {member.mention}!")


@bot.user_command(guild_ids=[893947040869019708], name="Ban Author")
async def ban(ctx, member: discord.Member):
    await member.ban(delete_message_days=1)
    await ctx.respond("Member wurde erfolgreich gebannt")


@bot.user_command(guild_ids=[893947040869019708], name="Kick Author")
async def kick(ctx, member: discord.Member):
    await member.kick()
    await ctx.respond("Member wurde erfolgreich kickt")


@bot.message_command(guild_ids=[guild_id]) # message_command, don't pass in guild_ids if you want to make your context menu global.
async def test(ctx, message: discord.Message): # discord.Message for message commands
    await ctx.respond("Testing")


# ----------------------------------------------------------------------------------------------


@bot.event
async def on_message_edit(message_before, message_after):
    try:
        # view = Message()
        embed = discord.Embed(title="Message Edited",
                            description="", color=discord.Color.yellow())
        embed.add_field(name="Message Author", value=f"{message_before.author.mention}", inline=True)
        embed.add_field(name="Message Channel", value=f"{message_before.channel.mention}", inline=True)
        embed.add_field(name="Author ID", value=f"{message_before.author.id}", inline=True)
        embed.add_field(name="Message ID", value=f"{message_before.id}")
        embed.add_field(name="Message Link", value=f"{message_before.jump_url}", inline=False)
        embed.add_field(name="Message before", value=f"{message_before.content}",
                        inline=False)
        embed.add_field(name="Message after", value=f"{message_after.content}",
                        inline=False)
        channel = bot.get_channel(895761431474098206)
        await channel.send(embed=embed)

    except discord.HTTPException:
        await channel.send("Can't send a Bot embed")



@bot.event
async def on_message_delete(message):
    channel = bot.get_channel(895761406341832764)
    try:
        deleted = discord.Embed(title="Deleted Message", color=discord.Color.red(),
                                timestamp=datetime.datetime.utcnow())
        deleted.add_field(name="Author", value=f"{message.author.mention}", inline=True)
        deleted.add_field(name="Channel", value=f"{message.channel.mention}", inline=True)
        deleted.add_field(name="Author ID", value=f"{message.author.id}", inline=True)
        deleted.add_field(name="Message ID", value=f"{message.id}")
        deleted.add_field(name="Message", value=message.content, inline=False)
        deleted.set_footer(text=f"{message.author.nick}")
        deleted.timestamp = message.created_at
        await channel.send(embed=deleted, view=Message_Logging())

    except discord.HTTPException:
        pass



# -----------------------------------------------------------------------------------------------------


@bot.event
async def on_ready():
    print(f"                ------------------------------------ Bot -----------------------------------------\n"
          f"                Logged in as: {bot.user.name} \n"
          f"                Id: {bot.user.id}\n"
          f"                {datetime.datetime.now()}\n"
          f"                ------------------------------- Bot ist online ------------------------------------")

    print(f"Information Cog successfully registered ({datetime.datetime.now()})")
    print(f"Server Management Cog successfully registered ({datetime.datetime.now()})")
    print(f"Moderation Cog successfully registered ({datetime.datetime.now()})")
    print(f"Member Cog successfully registered ({datetime.datetime.now()})")
    print(f"Fun Cog successfully registered ({datetime.datetime.now()})")
    print(f"Help Cog successfully registered ({datetime.datetime.now()})")
    print(f"Notification Cog successfully registered ({datetime.datetime.now()})")
    print(f"Admin Cog successfully registered ({datetime.datetime.now()})\n\n")


    print(f"tic (TicTacToe) Command successfully registered ({datetime.datetime.now()}) from fun Cog")
    print(f"ask Command successfully registered ({datetime.datetime.now()}) from Fun Cog")
    print(f"clear Command successfully registered ({datetime.datetime.now()}) from Moderation Cog")
    print(f"help Command successfully registered ({datetime.datetime.now()}) from Help Cog")
    print(f"announcement Command successfully registered ({datetime.datetime.now()}) from Information Cog")
    print(f"google announcement Command successfully registered ({datetime.datetime.now()}) from Information Cog")
    print(f"github Command successfully registered ({datetime.datetime.now()}) from Information Cog")
    print(f"ping Command successfully registered ({datetime.datetime.now()}) from Information Cog")
    print(f"server Command successfully registered ({datetime.datetime.now()}) from Information Cog")
    print(f"version Command successfully registered ({datetime.datetime.now()}) from Information Cog")
    print(f"poll Command successfully registered ({datetime.datetime.now()}) from Information Cog")
    print(f"rules Command successfully registered ({datetime.datetime.now()}) from Moderation Cog")
    print(f"warn Command successfully registered ({datetime.datetime.now()}) from Moderation Cog")
    print(f"clear Command successfully registered ({datetime.datetime.now()}) from Moderation Cog")
    print(f"emoji_clone Command successfully registered ({datetime.datetime.now()}) from Server_management Cog")
    print(f"role_cloner Command successfully registered ({datetime.datetime.now()}) from Server_management Cog")
    print(f"kill Command successfully registered ({datetime.datetime.now()}) from Admin Cog")
    print(f"reaction Command successfully registered ({datetime.datetime.now()}) from Notification Cog")
    print(f"reaction_add Command successfully registered ({datetime.datetime.now()}) from Notification Cog")
    print(f"reactions Command successfully registered ({datetime.datetime.now()}) from Notification Cog")
    print(f"reaction_remove Command successfully registered ({datetime.datetime.now()}) from Notification Cog")

    bot.loop.create_task(change_status())
    # bot.loop.create_task(rules())

    # add_view(PersistentView())
    # persistent_views_added = True


for filename in os.listdir("C:\\Users\\mathi\\Documents\\\Phyton\\Bot\\cogs"):
    if filename.endswith(".py"):
        bot.load_extension(f"cogs.{filename[:-3]}")





async def change_status():
    while True:
        try:
            await bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.playing, name="/help", state=discord.Status.online))
            await asyncio.sleep(5)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Xaytex",
                                                                state=discord.Status.online))
            await asyncio.sleep(5)
            await bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.playing, name="Developed by Lynix152#9707"))
            await asyncio.sleep(5)
        except:
            pass


print(discord.__version__)
print("""
 #     #                                  
  #   #    ##   #   # ##### ###### #    # 
   # #    #  #   # #    #   #       #  #  
    #    #    #   #     #   #####    ##   
   # #   ######   #     #   #        ##   
  #   #  #    #   #     #   #       #  #  
 #     # #    #   #     #   ###### #    #                                                                              
""")

load_dotenv()

token = os.getenv("discord_token")

bot.run(str(token))
