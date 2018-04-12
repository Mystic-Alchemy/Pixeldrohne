# Hier werden die einzelnen 'p.help'-Argumente gehandled.

import discord
import asyncio
import keys
from pxldrn.adv.embed_data import help_embeds

client = discord.Client()
mlist = open("pxldrn/adv/config/mods.txt", "r", encoding='utf-8')
mods = mlist.readlines()


def hilfe(message, length):
    if length <= 7:
        embed = help_embeds.intro()
        return embed
    elif length > 7:
        arg = message
        if arg == "musik":
            embed = help_embeds.music()
            return embed
        elif arg == "allgemein":
            embed = help_embeds.primary()
            return embed
        elif arg == "spiele":
            embed = help_embeds.minigames()
            return embed
        else:
            embed = help_embeds.intro()
            return embed
