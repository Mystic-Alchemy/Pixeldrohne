# Diese Datei ist für den Schwesterbot der Pixeldrohne, PixelDev gedacht.

import discord
import sys
import asyncio
import keys
import random
import urllib.request

client = discord.Client()


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    await client.change_presence(game=discord.Game(name='mit dev.help', type=1, url="https://twitch.tv/pilleniusmc"))


@client.event
async def on_message(message):
    # Hilfe für Dev-Branch und Cutting Edge
    if message.content.lower().startswith('dev.help'):
        user = message.author
        embed = discord.Embed(
            title="Kategorie: Test",
            description="Alle Befehle, die hier aufgeführt sind noch in der Testphase, heißt sie können komplett "
                        "verbuggt sein.\n[Beta]: Sollte soweit stabil sein.\n[Alpha]: Könnte zu Abstürzen führen."
        )
        embed.add_field(name="Error 404", value="There seems to be nothing.")
        await client.send_message(user, embed=embed)
    if message.content.lower().startswith('dev.lsd') and message.author.id == keys.pmcid:
        # öffnen = open("config/zitate.txt", "r", encoding='utf-8')
        öffnen = urllib.request.urlopen("https://sherlock-holm.es/stories/plain-text/cano.txt")
        for line in öffnen:
            line = line.strip()
            line = str(line)
            if not line == "b''":
                line = line[2:]
                line = line.rstrip('\'')
                await client.send_message(message.channel, line)
                await asyncio.sleep(1)
    try:
        if message.content.lower().startswith('p.purge') and keys.pmcid:
            lim = int(message.content[8:]) + 1
            await client.purge_from(message.channel, limit=lim)
            await client.send_message(message.channel, "Erfolgreich gelöscht.")
    except discord.Forbidden:
        await client.change_presence(game=discord.Game(name='Du kannst mich doch nicht einfach muten.', type=1))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='ENTMUTE MICH JETZT!!!', type=1))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='Ok, ich gebe auf.', type=1))
        await sys.exit(1)
    except Exception as e:
        await client.send_message(message.channel, "Es ist ein Fehler aufgetreten: {e}".format(e=e))

    if message.author.id == keys.pmcid and message.content.lower().startswith('dev.halt'):
        await client.close()
        sys.exit(1)


@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    chat = reaction.message.channel

    if reaction.emoji == "👎" and msg.id == messageid and not user.id == client.user.id:
        lol_msg = await client.send_message(chat, "Hey {0}! Du sollst dem bitte nicht auch noch den Daumen geben.".format(user.mention))
        await client.remove_reaction(msg, "👎", user)
        await asyncio.sleep(3)
        await client.delete_message(lol_msg)

# client.start(keys.dev)
client.run(keys.dev)
