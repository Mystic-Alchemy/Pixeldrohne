# Um den gesamten Bot auszuführen muss nur noch die Datei genutzt werden

import asyncio
import io
import discord
import requests
import sys
import keys
import random
import pxldrn
import safygiphy


client = discord.Client()
mods = open("pxldrn/adv/config/mods.txt", "r", encoding='utf-8')
players = {}
gif = safygiphy.Giphy()


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
        await client.send_message(message.channel, "Ich laufe seit {0} Stunden und {1} Minuten ununterbrochen".format(hour, minutes))

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

    # 8-Ball
    if message.content.lower().startswith('p.8ball'):
        msg = message.content.split(' ')[1:]
        length = len(message.content[8:])
        await client.send_message(message.channel, pxldrn.eightball(msg, length))

    # Gif Reaction
    if message.content.lower().startswith('p.gif'):
        try:
            tag = message.content.lower().split(" ")[1:]
            tag = " ".join(tag)
            rgif = gif.random(tag=tag)
            response = requests.get(str(rgif.get("data", {}).get('image_original_url')), stream=True)
            await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='gif.gif')
        except AttributeError:
            await client.send_message(message.channel, "Es schaut fast so aus als gäbe es dazu kein Gif")

    # Schere Stein Papier
    if message.content.lower().startswith("p.ssp"):
        spieler = message.content[6:]
        await client.send_message(message.channel, embed=pxldrn.adv.minigames.ssp(spieler))

    # Zufälliges "falsches" Zitat
    if message.content.lower().startswith('p.zitat'):
        await client.send_message(message.channel, pxldrn.adv.zitate())

    # Zitat hinzufügen
    if message.content.lower().startswith('p.schreiben'):
        zitat = message.content[12:]
        await client.send_message(message.channel, pxldrn.adv.schreiben(zitat))

    # Zufällige Zahl
    if message.content.lower().startswith('p.zahl'):
        zahl = message.content.split(" ")
        try:
            b1 = int(zahl[1])
            b2 = int(zahl[2])
            zahl = random.randint(b1, b2)
            await client.send_message(message.channel, "Deine Zahl ist {}".format(zahl))
        except IndexError:
            await client.send_message(message.channel, "Du musst mir zwei Zahlen geben [p.zahl <min> <max>]")

    # Coinflip
    if message.content.lower().startswith('p.coin'):
        await client.add_reaction(message, pxldrn.adv.coin())

    # Roulette
    # TODO: Einsatz adden!
    if message.content.lower().startswith("p.roulette"):
        spieler = message.content.strip().split(" ")[1]
        await client.send_message(message.channel, embed=pxldrn.adv.minigames.roulette(spieler))

    # Massenlöschung
    try:
        if message.content.lower().startswith('p.purge') and (keys.pmcid or keys.pxlid):
            lim = int(message.content[8:]) + 1
            await client.purge_from(message.channel, limit=lim)
            await client.send_message(message.channel, "Erfolgreich gelöscht.")
    except Exception as e:
        await client.send_message(message.channel, "Es ist ein Fehler aufgetreten: {e}".format(e=e))

    # Botstop
    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        await client.logout()
        await asyncio.sleep(1)
        sys.exit(1)

# Ab hier beginnt der Musik-Bot
    if message.content.startswith('p.join'):
        try:
            if client.is_voice_connected(message.server):
                try:
                    voice_client = client.voice_client_in(message.server)
                    await voice_client.disconnect()
                except AttributeError:
                    await client.send_message(message.channel, "Ich bin doch in keinem Kanal, was willst du von mir?")
                except Exception as error:
                    await client.send_message(message.channel,
                                              "Ein Error is aufgetreten:\n ```{error}```".format(error=error))
            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    await client.join_voice_channel(channel)
                except Exception as error:
                    await client.send_message(message.channel, "Ein Error ist aufgetreten:\n"
                                                               "```{error}```".format(error=error))
        except Exception as error:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n"
                                                       "```{error}```".format(error=error))

    if message.content.startswith('p.leave'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "Ich bin doch in keinem Kanal, was willst du von mir?")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error is aufgetreten:\n ```{error}```".format(error=error))

    if message.content.startswith('p.play'):
        yt_url = message.content[7:]
        if client.is_voice_connected(message.server):
            voice = client.voice_client_in(message.server)
            player = await voice.create_ytdl_player(yt_url,
                                                    before_options=' -reconnect 1 -reconnect_streamed 1 '
                                                                   '-reconnect_delay_max 5 ')
            players[message.server.id] = player
            player.volume = 0.03
            player.start()
        elif not client.is_voice_connected(message.server):
            channel = message.author.voice.voice_channel
            voice = await client.join_voice_channel(channel)
            player = await voice.create_ytdl_player(yt_url,
                                                    before_options=' -reconnect 1 -reconnect_streamed 1 '
                                                                   '-reconnect_delay_max 5 ', )
            players[message.server.id] = player
            player.volume = 0.03
            player.start()

    if message.content.startswith('p.pause'):
        try:
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n ```{error}```".format(error=error))

    if message.content.startswith('p.resume'):
        try:
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n ```{error}```".format(error=error))

    if message.content.startswith('p.volume'):
        volume = int(message.content[9:])
        if volume <= 100:
            players[message.server.id].volume = volume / 100
            await client.send_message(message.channel, "Lautstärke erfolgreich "
                                                       "auf {0} % eingestellt.".format(volume))
        elif volume > 100:
            await client.send_message(message.channel, "Diese Lautstärke ist eindeutig **zu hoch**!")

    if message.content.startswith('p.stop'):
        try:
            players[message.server.id].stop()
        except Exception as error:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n ```{error}```".format(error=error))


async def uptime():
    await client.wait_until_ready()
    global minutes
    minutes = 0
    global hour
    hour = 0
    while not client.is_closed:
        await asyncio.sleep(60)
        minutes += 1
        if minutes == 60:
            minutes = 0
            hour += 1

client.loop.create_task(uptime())
client.run(keys.token)
