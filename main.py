# Um den gesamten Bot auszuführen muss nur noch die Datei genutzt werden

import asyncio
import io
import discord
from discord.ext import commands
import requests
import sys
from server_specifics import *
from helps import Help
from moderation import *
from custom_commands import *
from music import Voice
import keys
import random

bot = commands.Bot(command_prefix=keys.prefix, case_insensitive=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Bot-Info:\nName: " + bot.user.name + "\nId: " + str(bot.user.id))


bot.add_cog(Help(bot))
bot.add_cog(Voice(bot))
bot.add_cog(Mods(bot))
bot.add_cog(CustomCommands(bot))
bot.run(keys.dev)
