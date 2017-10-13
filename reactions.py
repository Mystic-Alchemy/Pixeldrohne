import discord
import requests
import random
import io
import sys
import os
import codecs

client = discord.Client()
messageid = None
messageuserid = None
botid = "346997169070276608"
pmcid = "216529627034812416"
rpyid = "207899976796209152"
mods = open("mods.txt", "r", encoding='utf-8')

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    if message.content.lower().startswith('p.zitat'):
        öffnen = open("zitate.txt", "r", encoding='utf-8')
        auswahl = öffnen.readlines()
        zitat = random.choice(auswahl)
        await client.send_message(message.channel, zitat)
        öffnen.close()

    if message.content.lower().startswith('p.schreiben'):
        datei = open("zitate.txt", "a", encoding='utf-8')
        zitat = message.content[12:]
        datei.write("\n" + zitat)
        await client.send_message(message.channel, "Dein Zitat `{0}` wurde der Liste hinzugefügt.".format(zitat))
        datei.close()

    if message.content.lower().startswith('p.response'):
        botmsg = await client.send_message(message.channel, "Akzeptierst du mich? 👍 oder 👎")

        await client.add_reaction(botmsg, "👍")
        await client.add_reaction(botmsg, "👎")

        global messageid
        messageid = botmsg.id

        global messageuserid
        messageuserid = message.author

    if message.content.lower().startswith('p.ja'):
        choice = random.randint(1, 4)
        if choice == 1:
            response = requests.get('https://media.giphy.com/media/A3dD2XWfJ7tV6/giphy.gif', stream=True)
            await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="ja.gif")
        if choice == 2:
            response = requests.get('https://media.giphy.com/media/XMBJ0l20sNWEM/giphy.gif', stream=True)
            await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="ja.gif")
        if choice == 3:
            response = requests.get('https://media.giphy.com/media/BlVVi6LGpZZ7O/giphy.gif', stream=True)
            await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="ja.gif")
        if choice == 4:
            response = requests.get('https://media.giphy.com/media/dZWJ0MdlA6W9W/giphy.gif', stream=True)
            await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="ja.gif")

    if message.content.lower().startswith('p.nein'):
        response = requests.get('https://media.giphy.com/media/eXQPwwE8DFTZS/200w_d.gif', stream=True)
        await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="nein.gif")

    if message.content.lower().startswith('p.tableflip'):
        response = requests.get('https://media.giphy.com/media/uKT0MWezNGewE/giphy.gif', stream=True)
        await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="pixie.gif")

    if ('porg' or 'porgs') in message.content.lower():
        response = requests.get('https://media.giphy.com/media/3ohhwqOVlEbBxEbss0/giphy.gif', stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="porg.gif")

    if message.content.lower().startswith('p.halt') and message.author.id == pmcid:
        await client.close()
        sys.exit(0)

@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    chat = reaction.message.channel

    if reaction.emoji == "👍" and msg.id == messageid and user == messageuserid:
        await client.send_message(chat, "Yay! Du akzeptierst mich!")
        await client.delete_message(msg)

    if reaction.emoji == "👎" and msg.id == messageid and user == messageuserid:
        await client.send_message(chat, "Jetzt bin ich traurig!")
        await client.delete_message(msg)

client.run('MzQ2OTk3MTY5MDcwMjc2NjA4.DHR94g.It1hLi-Tk-tEAKln3VWg5MSQVAk')
