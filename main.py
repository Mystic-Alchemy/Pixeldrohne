# Die 'main.py' function des Bots.

import asyncio
import io
import discord
import requests
import sys
import keys
import pxldrn


client = discord.Client()
mods = open("config/mods.txt", "r", encoding='utf-8')


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    await client.change_presence(game=discord.Game(name='mit p.help', url="http://twitch.tv/pixeldrohne",
                                                   type=1))


@client.event
async def on_message(message):
    # Spielstatus
    if message.content.startswith('p.game') and message.author.id == keys.pmcid:
        game = message.content[7:]
        await client.change_presence(game=discord.Game(name=game, url="http://twitch.tv/pixeldrohne", type=1))
        await client.send_message(message.channel, "Status erfolgreich zu {0} geändert".format(game))

    # Pixels Liebling
    if message.content.startswith('p.pixels_liebling'):
        response = requests.get('https://media.giphy.com/media/3xz2BIXYagz5STg0xi/giphy.gif', stream=True)
        await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="kaffee.gif", content="Jeder muss Pixel's Liebling kennen")

    # Uptime abrufen
    if message.content.startswith('p.uptime'):
        await client.send_message(message.channel, "Ich laufe seit {0} Stunden und {1} Minuten im Testbetrieb".format(pxldrn.hour, pxldrn.minutes))

    # Hilfe
    if message.content.lower().startswith('p.help'):
        await client.send_message(message.author, embed=pxldrn.hilfe.hilfe(message.content[7:].lower(), len(message.content)))

    # Sysinfo
    if message.content.lower().startswith('p.sysinfo'):
        await client.send_message(message.channel, embed=pxldrn.adv.embed_data.system_info())

    # Python help
    if message.content.lower().startswith('p.python'):
        await client.send_message(message.channel, embed=pxldrn.adv.embed_data.py_help())

    # Avatar abrufen
    if message.content.startswith('p.avatar'):
        if len(message.content) == 8:
            user = message.author
            response = requests.get(user.avatar_url, stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()),
                                   filename="avatar.jpg", content=message.author.name)
        if len(message.content) > 8:
            user = message.mentions[0]
            response = requests.get(user.avatar_url, stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()),
                                   filename="avatar.jpg", content=user.display_name)

    # Bot Remote
    if message.content.startswith('p.say') and message.channel == client.get_channel('347000675093315584'):
        msg = message.content[5:]
        await client.delete_message(message)
        await client.send_typing(discord.Object(id='269432704360120321'))
        await asyncio.sleep(2)
        await client.send_message(discord.Object(id='269432704360120321'), msg)

    # Bot Remote Embed
    if message.content.startswith('p.esay') and message.channel == client.get_channel('347000675093315584'):
        emsg = message.content[7:]
        embedmsg = discord.Embed(color=0x1213a6, description=emsg)
        await client.delete_message(message)
        await client.send_typing(discord.Object(id='269432704360120321'))
        await asyncio.sleep(2)
        await client.send_message(discord.Object(id='269432704360120321'), embed=embedmsg)

    # eine "Über" Sektion
    if message.content.startswith('p.about'):
        await client.send_message(message.channel, embed=pxldrn.adv.embed_data.about())

    # Invite zur Heimat
    if message.content.lower().startswith('p.test'):
        await client.send_message(message.channel, embed=pxldrn.adv.embed_data.server_invite())

    # Bot Invite
    if message.content.lower().startswith('p.invite'):
        await client.send_message(message.channel, embed=pxldrn.adv.embed_data.bot_invite())

    # Schere Stein Papier
    if message.content.lower().startswith("p.ssp"):
        spieler = message.content[6:]
        await client.send_message(message.channel, embed=pxldrn.adv.minigames.ssp(spieler))

    # Roulette
    # TODO: Einsatz adden!
    if message.content.lower().startswith("p.roulette"):
        spieler = message.content.strip().split(" ")[1]
        await client.send_message(message.channel, embed=pxldrn.adv.minigames.roulette(spieler))

    # Botstop
    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        await client.logout()
        await pxldrn.hilfe.halt()
        await asyncio.sleep(1)
        sys.exit(1)


client.loop.create_task(pxldrn.uptime())
client.run(keys.token)
