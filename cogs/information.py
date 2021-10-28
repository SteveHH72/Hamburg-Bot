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
import time


guild_id = 893947040869019708


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\nInformation Cog is ready!")

    @slash_command(guild_ids=[guild_id], description="Sows the Version of the Bot")
    async def announcement(self, ctx, headline, message, channel: discord.TextChannel):
        announcement_channel = channel
        embed = discord.Embed(title=f"{headline}", description=f"{message}", color=discord.Color.blue())
        await ctx.respond(f"Your announcement has been send in the {announcement_channel.mention} Channel")
        await announcement_channel.send("@everyone", embed=embed)

    @commands.command()
    async def yn(self, ctx):
        await ctx.message.add_reaction('👍')
        await ctx.message.add_reaction('👎')

    @slash_command(guild_ids=[guild_id], description="With this Command you can Google some things")
    async def google(self, ctx: commands.Context, *, suche: str):
        """Returns a google link for a query"""
        embed = discord.Embed(title="Google Result", description=f"Google Result for: ```{suche}```",
                              color=discord.Color.fuchsia())
        embed.set_footer(text=f"{ctx.author.name} | {ctx.author.nick} ({ctx.author.id})")
        await ctx.respond(embed=embed, view=Google(suche))



    @slash_command(guild_ids=[guild_id], description="Shows the Link of the Code from the Bot")
    async def github(self, ctx):
        embed = discord.Embed(title="Github", url='https://github.com/Xaytex/Xaytex-Discord-Bot',
                              description="Bot for the Xaytex Development Team Server",
                              color=discord.Color.nitro_pink())
        await ctx.respond(embed=embed)




    @slash_command(guild_ids=[guild_id], description="Shows the Ping of the Bot")
    async def ping(self, ctx: commands.Context):
        """Get the bot's current websocket and API latency."""
        end_time = time.time()
        start_time = time.time()
        embed = discord.Embed(title="Pong!", color=discord.Color.brand_green())
        embed.add_field(name='Bot ping', value=f"⌛ {round(self.bot.latency * 1000)}ms")
        embed.add_field(name="API ping", value=f"⌛ {round((end_time - start_time) * 1000)}ms")
        await ctx.respond(embed=embed)




    @slash_command(guild_ids=[guild_id], description="Shows more Information about the Server")
    async def server(self, ctx):
        embed = discord.Embed(title=f"{ctx.guild.name}", description="Serverstats",
                              timestamp=datetime.datetime.utcnow(),
                              color=discord.Color.fuchsia())
        embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}", inline=True)
        embed.add_field(name="Server Owner", value="<@578678204890349594>", inline=False)
        embed.add_field(name="Server Region", value=f"{ctx.guild.region}", inline=False)
        embed.add_field(name="Server ID", value=f"{ctx.guild.id}  ", inline=True)
        await ctx.respond(embed=embed)




    @slash_command(guild_ids=[guild_id], description="Sows the Version of the Bot")
    async def version(self, ctx):
        embed = discord.Embed(title=f"`{self.bot.user}` v.2.0.0", color=discord.Color.blue())
        await ctx.respond(embed=embed)



    @slash_command(guild_ids=[guild_id], description="This is a poll Command")
    async def poll(self, ctx, arg,
                   option1: str,
                   option2: str,
                   option3: str,
                   option4: str,
                   option5: str):
        if option3 is None:
            embed = discord.Embed(title="Poll",
                                  description=f"**{arg}**\n\n\n **Option 1** {option1}\n\n\n **Option 2** {option2}")
            embed.set_footer(text=f"Created by {ctx.author.name} ({ctx.author.id})")
            await ctx.respond(embed=embed, view=Poll())

        elif option4 is None:
            embed = discord.Embed(title="Poll",
                                  description=f"**{arg}**\n\n\n **Option 1** {option1}\n\n\n **Option 2** {option2}\n\n\n **Option 3** {option3}")
            embed.set_footer(text=f"Created by {ctx.author.name} ({ctx.author.id})")
            await ctx.respond(embed=embed, view=Poll())

        elif option5 is None:
            embed = discord.Embed(title="Poll",
                                  description=f"**{arg}**\n\n\n **Option 1** {option1}\n\n\n **Option 2** {option2}\n\n\n **Option 3** {option3}\n\n\n **Option 4** {option4}")
            embed.set_footer(text=f"Created by {ctx.author.name} ({ctx.author.id})")
            await ctx.respond(embed=embed, view=Poll())

        else:
            embed = discord.Embed(title="Poll",
                                  description=f"**{arg}**\n\n\n **Option 1** {option1}\n\n\n **Option 2** {option2}\n\n\n **Option 3** {option3}\n\n\n **Option 4** {option4}\n\n\n **Option5** {option5}")
            embed.set_footer(text=f"Created by {ctx.author.name} ({ctx.author.id})")
            await ctx.respond(embed=embed, view=Poll())


def setup(bot):
    bot.add_cog(Information(bot))