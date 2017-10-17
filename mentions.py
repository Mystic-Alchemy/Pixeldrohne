import asyncio
import io
import random
import sqlite3
import discord
import requests
import keys


client = discord.Client()
pmcid = "216529627034812416"
pxlid = "269431915725979648"

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    try:
        if message.mentions[0]:
            user = message.mentions[0]
            id = user.id
            if id == pmcid:
                await client.delete_message(message)
                await client.send_message(message.channel, "Bitte PilleniusMC nicht taggen!")
            if id == pxlid:
                await client.delete_message(message)
                await client.send_message(message.channel, "Bitte Pixelwerfer nicht taggen!")
    except Exception as error:
        print("Erwarteter Error: {error}".format(error=error))

client.run(keys.token)
