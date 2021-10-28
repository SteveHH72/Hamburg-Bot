from discord.ext import commands
from discord.commands import slash_command
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *

guild_id = 893947040869019708


class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\nServer Management Cog is ready!")


    @slash_command(guild_ids=[guild_id],
                   description="Makes an Emoji Clone from a existing Emote from another server", name="clonee")
    async def emojy_clone(ctx, emoji, name, reason):
        embed = discord.Embed(title="New Emoji", description=f"{emoji}")
        await ctx.respond(emoji, embed=embed)
        await ctx.guild.create_custom_emoji(name=name, image=emoji, reason=reason)

    @slash_command(guild_ids=[guild_id], description="Makes an Role Clone from a existing Emote", name="cloner")
    async def cloner(ctx, role: discord.Role,
                     name,
                     mentionable,
                     display_role_seperately,
                     reason):
        role_per = discord.utils.get(ctx.guild.roles, name="Core")
        if role_per not in ctx.author.roles:
            embed_warn = discord.Embed(title="warning!", description="You don't have permssions to to that!",
                                       color=discord.Color.dark_red())
            await ctx.respond(embed=embed_warn)

        else:
            role = await ctx.guild.create_role(name=name, mentionable=mentionable, hoist=display_role_seperately,
                                               reason=reason)
            embed = discord.Embed(title="Role", description=f"Role {role.mention} has been Created.",
                                  color=discord.Color.brand_green())
            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Server(bot))
