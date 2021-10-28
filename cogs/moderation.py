from discord.ext import commands
from discord.commands import slash_command
import discord
from discord.ext import commands
from discord.ext.commands import *
from discord.abc import *
import os, sys, sqlite3

guild_id = 893947040869019708



class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("\nModeration Cog is ready!")


    @slash_command(guild_ids=[guild_id], description="Shows the rules of this server")
    async def rules(self, ctx):
        embed = discord.Embed(title="Rules", description="""
        1.) Einladen fremder Personen ist nicht erlaubt und nicht erwünscht - habt ihr Freunde, die gerne mitmachen wollen - schreibt mir (<@895767818165956628>)!

    2.) Abmeldungen - falls ihr für eine bestimmte Zeit weg seid (Krank etc.) soll man sich melden.

    3.) Streit, Konflikte werden zusammen gelöst! Niemand wird beleidigt falls er etwas falsch macht usw. Jeder zählt gleich viel und als Team muss man deswegen immer zusammenhalten.

    4.) Leaks vom Projekt u.a Chats, Source (außer Open Source Repository) sind strengstens untersagt, unsere harte Arbeit also haltet es euch privat unter uns.

    5.) Ausnutzen von Bugs um an Admin Rechte zu kommen ist nicht gerne gesehen, bleibt Fair und meldet diese (und jegliche anderen Bugs/Fehler) umgehend im Chat oder bei mir!

    6.) Vertrauen ist wichtig, auf jeden soll Verlass sein. Einfaches verlassen / gehen wird nicht gerne gesehen - dies hier ist freiwillig und dient zum Lernen, geht auf eure Freizeit / Hobby Zeit also könnt ihr entscheiden wann ihr arbeiten möchtet. Gerne gesehen aber nicht immer verpflichtend.

    7.) Bei Abstimmungen teilnehmen. Diese sind unter anderem Abstimmungen über neue Features (abstimmung) und vieles mehr. 

    8.) Inaktivität ist nicht gerne gesehen, wie gesagt => abmelden auf eine bestimmte Zeit ist natürlich erlaubt und wünschenswert. Einfaches "nicht melden" ist kontraproduktiv.

    9.) Gegenseitiges helfen! Wir haben auch welche dabei die noch nie mit Technologien die wir nutzen, gearbeitet haben. Helft denen bitte falls diese eure beanspruchen und oder euch/uns fragen.
    Jeder hat seine Stärken / Schwächen und zählt damit überall gleich viel. 
    Falls möglich, Documentations / Guides zu Lösungen dazu senden um davon zu lernen!

    10.) Unangenehmes Verhalten innerhalb und außerhalb des Servers via Beleidigungen, Verspottung, Spam und mehr. Ich achte auf das Verhalten von jeden und will jeden mit einem netten Umgang sehen.

    Freude, Spaß und Lernen ist das Ziel unseres Projektes **Xaytex**.""", color=discord.Color.fuchsia())
        await ctx.respond(embed=embed)

    @slash_command(guild_ids=[guild_id], description="This Command warns member", default_permission=False)
    @commands.has_role("Core")
    async def warn(self, ctx, member: discord.Member, member_id, reason):
        role_2 = discord.utils.get(ctx.guild.roles, id=895760763556356156)
        role = discord.utils.get(ctx.guild.roles, name="Core")

        if role in ctx.author.roles or role_2 in ctx.author.roles:
            embed = discord.Embed(title="User warned",
                                  description=f'✅ User was warned with the ID {member_id} ✅ ',
                                  color=discord.Color.red())
            await ctx.respond(embed=embed)

            sql = "UPDATE warn_members SET warn_counter = +1" \
                  "WHERE id = member_id"
            cursor.execute(sql)
            connection.commit()

            embed_member = discord.Embed(title=":warning: Warn",
                                         description=f"{ctx.author.name} just warned you on **Xaytex**",
                                         color=discord.Color.dark_red())
            embed_member.add_field(name="Reason", value=f"```{reason}```")
            embed_member.add_field(name="Channel", value=f"{ctx.channel}", inline=False)
            await member.send(embed=embed_member)

        elif role not in ctx.author.roles or role_2 in ctx.author.roles:
            embed = discord.Embed(title="Warned",
                                  description="You don't have permissions to do that. The Incident will be reported.",
                                  colour=discord.Color.red())
            await ctx.respond(embed=embed)

    @slash_command(guild_ids=[guild_id], description="This Command clears the messages in a channel")
    async def clear(self, ctx, amount: int):
        await ctx.channel.purge(limit=amount)
        embed = discord.Embed(title=f"{amount} messages were deleted",
                              description=f"Warnung: **{amount} were deleted**. :warning: ",
                              color=discord.Color.blue())
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Moderation(bot))
