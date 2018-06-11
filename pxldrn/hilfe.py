# Hier werden die einzelnen 'p.help'-Argumente gehandled.

import discord
import asyncio
import keys
from pxldrn.adv.embed_data import help_embeds

client = discord.Client()
mlist = open("pxldrn/adv/config/mods.txt", "r", encoding='utf-8')
mods = mlist.readlines()


def hilfe(message, length, client):
    if length <= 7:
        embed = help_embeds.intro(client)
        return embed
    elif length > 7:
        arg = message
        if arg == "musik":
            embed = help_embeds.music(client)
            return embed
        elif arg == "allgemein":
            embed = help_embeds.primary(client)
            return embed
        elif arg == "spiele":
            embed = help_embeds.minigames(client)
            return embed
        else:
            embed = help_embeds.intro(client)
            return embed
