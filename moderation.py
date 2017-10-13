import asyncio
import io
import random
import sqlite3
import discord
import requests
import sys

client = discord.Client()
pmcid = "216529627034812416"
pxlid = "269431915725979648"
rpyid = "207899976796209152"
connection = sqlite3.connect("bot.db")
cursor = connection.cursor()
mlist = open("config/mods.txt", "r", encoding='utf-8')
mods = mlist.readlines()

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    # Massenlöschung
    try:
        if message.content.lower().startswith('p.purge') and ((message.author.id in mods) or pmcid or pxlid):
            await client.purge_from(message.channel, limit=int(message.content[8:]))
            await client.send_message(message.channel, "Erfolgreich gelöscht.")
    except Exception as e:
        await client.send_message(message.channel, "Es ist ein Fehler aufgetreten: {e}".format(e=e))

    # Mod hinzufügen
    if message.author.id == (pmcid or pxlid or rpyid) and message.content.lower().startswith('p.madd'):
        user = message.mentions[0]
        mod = user.id
        madd = open("mods.txt", "a", encoding='utf-8')
        madd.write('"{0]"'.format(mod) + "\n")
        await client.send_message(message.channel, "{0} wurde erfolgreich den Mods hinzugefügt".format(user.name))
        madd.close()

    # Botstop
    if message.content.lower().startswith('p.halt') and message.author.id == pmcid:
        mlist.close()
        await client.close()
        sys.exit(0)


client.run('MzQ2OTk3MTY5MDcwMjc2NjA4.DHR94g.It1hLi-Tk-tEAKln3VWg5MSQVAk')
