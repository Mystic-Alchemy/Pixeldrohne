import discord
import asyncio
import io
import random
import requests

client = discord.Client()
pmcid = "216529627034812416"
rpyid = "207899976796209152"
mods = open("config/mods.txt", "r", encoding='utf-8')

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    await client.change_presence(game=discord.Game(name='In der Entwicklung',type=0))

@client.event
async def on_message(message):
    #Schere Stein Papier
    if message.content.lower().startswith("p.ssp"):
        ssp = ['schere', 'stein', 'papier']
        wahl = random.choice(ssp)
        spieler = message.content[6:]
        if not spieler.lower() in ssp:
            await client.send_message(message.channel, "Du musst Schere, Stein oder Papier wählen!")
        elif wahl == spieler.lower():
            ergemb = discord.Embed(color=0xecde13, title="Unentschieden", description="Wir haben das gleiche gewählt."
                                                                                      "\n\n Du hast {sp} gewählt, ich "
                                                    "habe {bot} gewählt.".format(sp=spieler.capitalize()
                                                                                 ,bot=wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)
        elif (spieler.lower() == "schere" and wahl.lower() == "stein") or\
                (spieler.lower() == "stein" and wahl.lower() == "papier") or\
                (spieler.lower() == "papier" and wahl.lower() == "schere"):
            ergemb = discord.Embed(color=0xb21512, title="Verloren", description="Yay! Ich habe gewonnen.\n\n"
                                                                                 " Du hast {sp} gewählt, ich"
                                                                                 " habe {bot}"
                                                                                 " gewählt.".format(
                                                                                    sp=spieler.capitalize(),
                                                                                    bot=wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)
        elif (wahl.lower() == "schere" and spieler.lower() == "stein") or\
                (wahl.lower() == "stein" and spieler.lower() == "papier") or\
                (wahl.lower() == "papier" and spieler.lower() == "schere"):
            ergemb = discord.Embed(color=0x71cc39, title="Gewonnen", description="Du hast gegen mich gewonnen."
                                                                                 " Jetzt bin ich traurig."
                                                                                      "\n\n Du hast {sp} gewählt, ich "
                                        "habe {bot} gewählt.".format(sp=spieler.capitalize(), bot=wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)
    # Botstop
    if message.content.lower().startswith('p.halt') and message.author.id == pmcid:
        await client.close()
        sys.exit(0)


client.run('MzQ2OTk3MTY5MDcwMjc2NjA4.DHR94g.It1hLi-Tk-tEAKln3VWg5MSQVAk')
