# Diese Datei ist für den Schwesterbot der Pixeldrohne, PixelDev gedacht.

import discord
import sys
import asyncio
import keys

client = discord.Client


@client.event
async def on_message(message):
    # Hilfe für Dev-Branch und Cutting Edge
    if message.content.lower().startswith('p.help test'):
        user = message.author
        embed = discord.Embed(
            title="Kategorie: Test",
            description="Alle Befehle in dieser Kategorie müssen noch getestet werden und können auch nur auf dem Heimat-/"
                        "Testserver genutzt werden. Um viele dieser Befehle nutzen zu können, ist der Schwesterbot PixelDev"
                        "nötig. Die Befehle habe Tags:\n[Alpha] Cuttin Edge\n[Beta] Early Access"
                        "verwendet werden."
        )
        await client.send_message(user, embed=embed)

client.run(keys.dev)
