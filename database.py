import asyncio
import sqlite3
import discord
import sys

client = discord.Client()
pmcid = "216529627034812416"
pxlid = "269431915725979648"
rpyid = "207899976796209152"
connection = sqlite3.connect("bot.db")
cursor = connection.cursor()
mods = open("mods.txt", "r", encoding='utf-8')


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    if message.content.startswith('p.enter'):
        try:
            user = message.author.id
            cursor.execute("INSERT INTO daten (userid, nachrichten, xp, lvl, pixel) VALUES (?,?,?,?,?)", (user, 0, 0, 0, 0))
            connection.commit()
            await client.send_message(message.channel,"Du wurdest erfolgreich in die Datenbank eingetragen.")
        except Exception as error:
            await client.send_message(message.channel,"Du konntest nicht in die Datenbank eingetragen werden "
                                                      "oder bist schon eingetragen.\n"
                                                      "Error: ```{error}```".format(error=error))

    if message.content.lower().startswith('p.halt') and message.author.id == pmcid:
        await client.close()
        sys.exit(0)

@client.event
async def on_member_join(member):
    try:
        sc = member.server.default_channel
        user = member.id
        await client.send_message(sc, "Willkommen auf dem Server {user}".format(user=member.mention))
        if member.server.id == "269432704360120321":
            role = discord.utils.find(lambda r: r.name == "Pixelwerfer", discord.Server.roles)
            await client.add_roles(member, role)
        elif member.server.id == "228906870839050243":
            role = discord.utils.find(lambda r: r.name == "User", discord.Server.roles)
            await client.add_roles(member, role)
        cursor.execute("INSERT INTO daten (userid, nachrichten, xp, lvl, pixel) VALUES (?,?,?,?,?)", (user, 0, 0, 0, 0))
        connection.commit()
    except Exception as error:
        print(error)

@client.event
async def on_member_remove(member):
    serverchannel = member.server.default_channel
    msg = "Leider hat {0} den Server verlassen".format(member.mention)
    await client.send_message(serverchannel, msg)

client.run('MzQ2OTk3MTY5MDcwMjc2NjA4.DHR94g.It1hLi-Tk-tEAKln3VWg5MSQVAk')
