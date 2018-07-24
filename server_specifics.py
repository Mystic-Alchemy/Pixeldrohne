import discord
from discord.ext import commands
# Alle weiteren benötigten Imports einfach zwischen diesem und dem nächsten Kommentar hinzufügen

# Ende der Imports


def is_in_guild(guild_id):
    async def predicate(ctx):
        return ctx.guild and ctx.guild.id == guild_id
    return commands.check(is_in_guild)


"""
Pro Server unter hier einfach eine Klasse aufbauen. Eine Vorlage wie die Klasse aufgebuat sein sollte folgt hierauf.
Ausfühlichere Beispiele und sowie bessere Vorlagen werden noch den Docs hinzugefügt.

class Name:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='name')
    async def name(self, ctx):
        Befehl
"""