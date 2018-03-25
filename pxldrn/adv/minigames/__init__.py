import discord
import random


def ssp(spieler):
    ssp = ['schere', 'stein', 'papier']
    wahl = random.choice(ssp)
    if not spieler.lower() in ssp:
        message = discord.Embed(description="Du musst Schere, Stein oder Papier wählen!", title="[SSP] Fehler")
        return message
    elif wahl == spieler.lower():
        ergemb = discord.Embed(color=0xecde13,
                               title="Unentschieden!",
                               description="Wir haben das gleiche gewählt.\n\nDu hast {sp} gewählt, ich habe {bot} gewählt.".format(sp=spieler.capitalize(), bot=wahl.capitalize()))
        return ergemb
    elif (spieler.lower() == "schere" and wahl.lower() == "stein") or \
            (spieler.lower() == "stein" and wahl.lower() == "papier") or \
            (spieler.lower() == "papier" and wahl.lower() == "schere"):
        ergemb = discord.Embed(color=0xb21512,
                               title="Verloren!",
                               description="Yay! Ich habe gewonnen.\n\nDu hast {sp} gewählt, ich habe {bot} gewählt.".format(sp=spieler.capitalize(), bot=wahl.capitalize()))
        return ergemb
    elif (wahl.lower() == "schere" and spieler.lower() == "stein") or \
            (wahl.lower() == "stein" and spieler.lower() == "papier") or \
            (wahl.lower() == "papier" and spieler.lower() == "schere"):
        ergemb = discord.Embed(color=0x71cc39,
                               title="Gewonnen!",
                               description="Du hast gegen mich gewonnen. Jetzt bin ich traurig.\n\n Du hast {sp} gewählt, ich habe {bot} gewählt.".format(sp=spieler.capitalize(), bot=wahl.capitalize()))
        return ergemb


def roulette(spieler):
    farbe = ['schwarz', 'rot']
    wahl = random.choice(farbe)
    if not spieler.lower() in farbe:
        message = discord.Embed(title="[Roulette] Fehler", description="Du musst schon Rot oder Schwarz wählen!")
        return message
    elif wahl != spieler.lower():
        ergemb = discord.Embed(color=0xb21512,
                               title="Verloren!",
                               description="Die Kugel ist auf {} gelandet. Schade eigentlich!".format(
                                   wahl.capitalize()))
        return ergemb
    elif wahl == spieler.lower():
        ergemb = discord.Embed(color=0x71cc39,
                               title="Gewonnen!",
                               description="Juhu! Die Kugel ist auf {} gelandet. Herzlichen Glückwunsch!".format(
                                   wahl.capitalize()))
        return ergemb
