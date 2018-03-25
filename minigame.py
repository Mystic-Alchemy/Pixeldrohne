# Hier werden alle Minigames ausgeführt.

import discord
import random
import sys
import asyncio
import keys
from pxldrn.adv import minigames

client = discord.Client()
mods = open("config/mods.txt", "r", encoding='utf-8')

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    # Schere Stein Papier
    if message.content.lower().startswith("p.ssp"):
        spieler = message.content[6:]
        await client.send_message(message.channel, embed=minigames.ssp(spieler))

    #Roulette
    # TODO: Einsatz adden!
    if message.content.lower().startswith("p.roulette"):
        spieler = message.content.strip().split(" ")[1]
        await client.send_message(message.channel, embed=minigames.roulette(spieler))

    # Botstop
    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        await client.logout()
        await asyncio.sleep(1)
        sys.exit(1)


client.run(keys.token)
