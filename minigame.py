# Hier werden alle Minigames ausgeführt.

import discord
import random
import sys
import asyncio
import keys

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
    #Schere Stein Papier
    if message.content.lower().startswith("dev.ssp"):
        ssp = ['schere', 'stein', 'papier']
        wahl = random.choice(ssp)
        spieler = message.content.strip().split(" ")[1]
        if not spieler.lower() in ssp:
            await client.send_message(message.channel, "[SSP] Du musst Schere, Stein oder Papier wählen!")
        elif wahl == spieler.lower():
            ergemb = discord.Embed(color=0xecde13, title="Unentschieden!", description="Wir haben das gleiche gewählt."
                                                                                      "\n\n Du hast {sp} gewählt, ich "
                                                    "habe {bot} gewählt.".format(sp=spieler.capitalize(), bot=wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)
        elif (spieler.lower() == "schere" and wahl.lower() == "stein") or\
                (spieler.lower() == "stein" and wahl.lower() == "papier") or\
                (spieler.lower() == "papier" and wahl.lower() == "schere"):
            ergemb = discord.Embed(color=0xb21512, title="Verloren!", description="Yay! Ich habe gewonnen.\n\n"
                                                                                 " Du hast {sp} gewählt, ich"
                                                                                 " habe {bot}"
                                                                                 " gewählt.".format(
                                                                                    sp=spieler.capitalize(),
                                                                                    bot=wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)
        elif (wahl.lower() == "schere" and spieler.lower() == "stein") or\
                (wahl.lower() == "stein" and spieler.lower() == "papier") or\
                (wahl.lower() == "papier" and spieler.lower() == "schere"):
            ergemb = discord.Embed(color=0x71cc39, title="Gewonnen!", description="Du hast gegen mich gewonnen."
                                                                                 " Jetzt bin ich traurig."
                                                                                      "\n\n Du hast {sp} gewählt, ich "
                                        "habe {bot} gewählt.".format(sp=spieler.capitalize(), bot=wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)
    #Roulette
    # TODO: Einsatz adden!
    if message.content.lower().startswith("p.roulette"):
        roulette = ['schwarz', 'rot']
        wahl = random.choice(roulette)
        spieler = message.content.strip().split(" ")[1]
        if not spieler.lower() in roulette:
            await client.send_message(message.channel, "[Roulette] Du musst schon Rot oder Schwarz wählen!")
        elif wahl != spieler.lower():
            ergemb = discord.Embed(color=0xb21512,
                                title="Verloren!",
                                description="Die Kugel ist auf {} gelandet. Schade eigentlich!".format(wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)
        elif wahl == spieler.lower():
            ergemb = discord.Embed(color=0x71cc39,
                                title="Gewonnen!",
                                description="Juhu! Die Kugel ist auf {} gelandet. Herzlichen Glückwunsch!".format(wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)

    # Botstop
    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        await client.logout()
        await asyncio.sleep(1)
        sys.exit(1)


client.run(keys.token)
