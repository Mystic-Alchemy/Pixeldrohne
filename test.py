# Diese Datei ist für den Schwesterbot der Pixeldrohne, PixelDev gedacht.

import discord
import sys
import asyncio
import keys
import dataset
import data
from collections import OrderedDict


db = dataset.connect('sqlite:///bot.db')
userdb = db['daten']
client = discord.Client()


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    await client.change_presence(game=discord.Game(name='mit dev.help', type=1))


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
        embed.add_field(name="[Beta] dev.inspect", value="Statistik Befehl")
        await client.send_message(user, embed=embed)

    elif message.content.lower().startswith('dev.inspect'):
        if userdb.find_one(userid=message.author.id) is None:
            db.begin()
            userdb.upsert(dict(userid=message.author.id, lvl=0, xp=0, nachrichten=0), ['userid'])
        ohgod = userdb.find_one(userid=message.author.id)
        lvlemb = discord.Embed(
            title="Deine Statistik",
            color=0xf12b6e,
            description='Hier siehst du alle deine Statistiken auf einen Blick'
        )
        lvlemb.add_field(name='Level:', value=ohgod['lvl'])
        lvlemb.add_field(name='XP:', value=ohgod['xp'])
        lvlemb.add_field(name='Nachrichten:', value=ohgod['nachrichten'])
        await client.send_message(message.channel, embed=lvlemb)

    elif message.content.lower().startswith('dev.halt') and (message.author.id == keys.pmcid or message.author.id == keys.m3lid):
        await client.logout()
        await asyncio.sleep(1)
        await sys.exit(1)

    elif message.content.lower().startswith('dev.'):
        client.send_message(message.channel, "Sorry, den Befehl kenne ich nicht.")
    else:
        user = message.author
        name = user.name
        mid = message.author.id
        data.nachrichten(message.author.id)
        data.xp(message.author.id, len(message.content))
        db.begin()
        xp = 250
        nutzer = userdb.find_one(userid=mid)
        if nutzer['lvl'] == 0:
            level = dict(userid=mid, lvl=1)
            userdb.upsert(level, ['userid'])
            embed = discord.Embed(
                title="Levelaufstieg:",
                color=0xF0FA4A,
                description="{0}, du bist jetzt Level 1.".format(name)
            )
            db.commit()
            await client.send_message(message.channel, embed=embed)
        elif nutzer['lvl'] == 1:
            lvl = nutzer['lvl'] + 1
            if nutzer['xp'] >= xp:
                level = dict(userid=mid, lvl=lvl)
                userdb.upsert(level, ['userid'])
                embed = discord.Embed(
                    title="Levelaufstieg:",
                    color=0xF0FA4A,
                    description="{0}, du bist jetzt Level {1}.".format(name, str(lvl))
                )
                db.commit()
                await client.send_message(message.channel, embed=embed)
            else:
                xp = xp + (xp * (nutzer['lvl'] * 1.5))
                if nutzer['xp'] > xp:
                    lvl = nutzer['lvl'] + 1
                    level = dict(userid=mid, lvl=lvl)
                    userdb.upsert(level, ['userid'])
                    embed = discord.Embed(
                        title="Levelaufstieg:",
                        color=0xF0FA4A,
                        description="{0}, du bist jetzt Level {1}.".format(name, str(lvl))
                    )
                    db.commit()
                    await client.send_message(message.channel, embed=embed)

# client.start(keys.dev)
client.run(keys.dev)
