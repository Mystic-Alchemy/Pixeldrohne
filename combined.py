# Diese Datei nur ausführen wenn ihr den gesamten Bot ausführen wollt ohne verschiedene Dateien zu verwenden.
# Der Einfachheit halber wird diese Datei auch ein vollständiges UI kriegen.

import asyncio
import io
import random
import discord
import requests
import sys
import keys
from pxldrn import embeds

client = discord.Client()
mods = open("config/mods.txt", "r", encoding='utf-8')
players = {}

minutes = 0
hour = 0


@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    await client.change_presence(game=discord.Game(name='mit p.help', url="https://twitch.tv/pixelwerfer",
                                                   type=1))


@client.event
async def on_message(message):
    # Spielstatus
    if message.content.startswith('p.game') and message.author.id == keys.pmcid:
        game = message.content[7:]
        await client.change_presence(game=discord.Game(name=game, url="https://twitch.tv/pixelwerfer", type=1))
        await client.send_message(message.channel, "Status erfolgreich zu {0} geändert".format(game))

    # Nickname ändern
    # if message.content.startswith('p.nick') and message.author.id == keys.pmcid:
    #     nick = message.content[7:]
    #     await client.change_nickname(message.author, nick)

    # Pixels Liebling
    if message.content.startswith('p.pixels_liebling'):
        response = requests.get('https://media.giphy.com/media/3xz2BIXYagz5STg0xi/giphy.gif', stream=True)
        await  client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="kaffee.gif", content="Jeder muss Pixel's Liebling kennen")

    # Uptime abrufen
    if message.content.startswith('p.uptime'):
        await client.send_message(message.channel, "Ich laufe seit {0} Stunden und {1} Minuten im Testbetrieb".format(hour, minutes))

    # Python Hilfe
    if message.content.lower().startswith('p.python'):
        await client.send_message(message.channel, embed=embeds.py_help())

    # Hilfe
    if message.content.lower().startswith('p.help'):
        user = message.author
        await embeds.hilfe(message.content[7:].lower(), user, len(message.content))

    # Sysinfo
    if message.content.lower().startswith('p.sysinfo'):
        await client.send_message(message.channel, embed=embeds.system_info())

    # Bot Invite
    if message.content.lower().startswith('p.invite'):
        iembed = discord.Embed(
            title="Einfach dem Link folgen um den Bot einzuladen.",
            description="http://pixeldrohne.mystic-alchemy.com",
            color=0x8a2be2
        )
        await client.send_message(message.channel, embed=iembed)

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
        abemb = discord.Embed(
            color=0xad1457,
            title="Über",
            description="Sorry, hier gibt es noch nichts zu sehen.")
        await client.send_message(message.channel, embed=abemb)

    # Invite zur Heimat
    if message.content.lower().startswith('p.test'):
        embed = discord.Embed(
            title="Invite zum Heimat-/Testserver",
            description="http://discord.gg/sgDQjeH",
            color=0x8a2be2
        )
        await client.send_message(message.channel, embed=embed)

# Zufälliges "falsches" Zitat
    if message.content.lower().startswith('p.zitat'):
        öffnen = open("config/zitate.txt", "r", encoding='utf-8')
        auswahl = öffnen.readlines()
        zitat = random.choice(auswahl)
        await client.send_message(message.channel, zitat)
        öffnen.close()

    # Zitat hinzufügen
    if message.content.lower().startswith('p.schreiben'):
        datei = open("config/zitate.txt", "a", encoding='utf-8')
        zitat = message.content[12:]
        datei.write("\n" + zitat)
        await client.send_message(message.channel, "Dein Zitat `{0}` wurde der Liste hinzugefügt.".format(zitat))
        datei.close()

    # Coinflip
    if message.content.lower().startswith('p.coin'):
        choice = random.randint(1, 2)
        if choice == 1:
            await client.add_reaction(message, '🌑')
        if choice == 2:
            await client.add_reaction(message, '🌕')

    # Test, dass Bot reagieren kann
    if message.content.lower().startswith('p.response'):
        botmsg = await client.send_message(message.channel, "Akzeptierst du mich? 👍 oder 👎")

        await client.add_reaction(botmsg, "👍")
        await client.add_reaction(botmsg, "👎")

        global messageid
        messageid = botmsg.id

        global messageuserid
        messageuserid = message.author

        # Schere Stein Papier
        if message.content.lower().startswith("p.ssp"):
            ssp = ['schere', 'stein', 'papier']
            wahl = random.choice(ssp)
            spieler = message.content.strip().split(" ")[1]
            if not spieler.lower() in ssp:
                await client.send_message(message.channel, "[SSP] Du musst Schere, Stein oder Papier wählen!")
            elif wahl == spieler.lower():
                ergemb = discord.Embed(color=0xecde13, title="Unentschieden!",
                                       description="Wir haben das gleiche gewählt."
                                                   "\n\n Du hast {sp} gewählt, ich "
                                                   "habe {bot} gewählt.".format(sp=spieler.capitalize()
                                                                                , bot=wahl.capitalize()))
                await client.send_message(message.channel, embed=ergemb)
            elif (spieler.lower() == "schere" and wahl.lower() == "stein") or \
                    (spieler.lower() == "stein" and wahl.lower() == "papier") or \
                    (spieler.lower() == "papier" and wahl.lower() == "schere"):
                ergemb = discord.Embed(color=0xb21512, title="Verloren!", description="Yay! Ich habe gewonnen.\n\n"
                                                                                      " Du hast {sp} gewählt, ich"
                                                                                      " habe {bot}"
                                                                                      " gewählt.".format(
                    sp=spieler.capitalize(),
                    bot=wahl.capitalize()))
                await client.send_message(message.channel, embed=ergemb)
            elif (wahl.lower() == "schere" and spieler.lower() == "stein") or \
                    (wahl.lower() == "stein" and spieler.lower() == "papier") or \
                    (wahl.lower() == "papier" and spieler.lower() == "schere"):
                ergemb = discord.Embed(color=0x71cc39, title="Gewonnen!", description="Du hast gegen mich gewonnen."
                                                                                      " Jetzt bin ich traurig."
                                                                                      "\n\n Du hast {sp} gewählt, ich "
                                                                                      "habe {bot} gewählt.".format(
                    sp=spieler.capitalize(), bot=wahl.capitalize()))
                await client.send_message(message.channel, embed=ergemb)

    #Roulette
    # TODO: Einsatz adden!
    if message.content.lower().startswith("p.roulette"):
        roulette = ['schwarz', 'rot']
        wahl = random.choice(roulette)
        spieler = message.content.strip().split(" ")[1]
        if not spieler.lower() in roulette:
            await client.send_message(message.channel, "[Roulette] Du musst schon Rot oder Schwarz wählen!")
        elif wahl != spieler.lower():
            ergemb = discord.Embed(color=0xb21512,
                                title="Verloren!",
                                description="Die Kugel ist auf {} gelandet. Schade eigentlich!".format(wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)
        elif wahl == spieler.lower():
            ergemb = discord.Embed(color=0x71cc39,
                                title="Gewonnen!",
                                description="Juhu! Die Kugel ist auf {} gelandet. Herzlichen Glückwunsch!".format(wahl.capitalize()))
            await client.send_message(message.channel, embed=ergemb)

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

        # Dieses Blockkommentar ist für eine spätere Funktion gedacht.
        """if not players[message.server.id].is_playing():
            if client.is_voice_connected(message.server):
                voice = client.voice_client_in(message.server)
                player = await voice.create_ytdl_player(yt_url,
                                                        before_options=' -reconnect 1 -reconnect_streamed 1 '
                                                                       '-reconnect_delay_max 5 ')
                player.volume = 0.03
                player.start()
            elif not client.is_voice_connected(message.server):
                channel = message.author.voice.voice_channel
                voice = await client.join_voice_channel(channel)
                player = await voice.create_ytdl_player(yt_url,
                                                        before_options=' -reconnect 1 -reconnect_streamed 1 '
                                                                       '-reconnect_delay_max 5 ', )
                player.volume = 0.03
                player.start()
        else:
            if client.is_voice_connected(message.server):
                voice = client.voice_client_in(message.server)
                player = await voice.create_ytdl_player(yt_url,
                                                        before_options=' -reconnect 1 -reconnect_streamed 1 '
                                                                       '-reconnect_delay_max 5 ')
                player.volume = 0.03
                player.start()
            elif not client.is_voice_connected(message.server):
                channel = message.author.voice.voice_channel
                voice = await client.join_voice_channel(channel)
                player = await voice.create_ytdl_player(yt_url,
                                                        before_options=' -reconnect 1 -reconnect_streamed 1 '
                                                                       '-reconnect_delay_max 5 ', )
                player.volume = 0.08
                player.start()"""

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

    # Massenlöschung
    try:
        if message.content.lower().startswith('p.purge') and ((message.author.id in mods) or keys.pmcid or keys.pxlid):
            lim = int(message.content[8:]) + 1
            await client.purge_from(message.channel, limit=lim)
            await client.send_message(message.channel, "Erfolgreich gelöscht.")
    except Exception as e:
        await client.send_message(message.channel, "Es ist ein Fehler aufgetreten: {e}".format(e=e))

    # Mod hinzufügen
    if message.author.id == (keys.pmcid or keys.pxlid) and message.content.lower().startswith('p.madd'):
        user = message.mentions[0]
        mod = user.id
        madd = open("config/mods.txt", "a", encoding='utf-8')
        madd.write('"{0}"'.format(mod) + "\n")
        await client.send_message(message.channel, "{0} wurde erfolgreich den Mods hinzugefügt".format(user.name))
        madd.close()

    # Anti invite
    if ('discord'.lower() in message.content.lower()) and (message.author.id not in keys.exceptions):
        if 'discord.me'.lower() in message.content.lower():
            user = message.author
            aif = open("config/invite.txt", "r", encoding='utf-8')
            ainv = aif.readlines()
            anti = random.choice(ainv)
            await client.delete_message(message)
            await client.send_message(message.channel, anti + " " + user.mention)
        if 'discord.gg'.lower() in message.content.lower():
            user = message.author
            aif = open("config/invite.txt", "r", encoding='utf-8')
            ainv = aif.readlines()
            anti = random.choice(ainv)
            await client.delete_message(message)
            await client.send_message(message.channel, anti + " " + user.mention)

    # Ab hier muss umgebaut werden
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

    if 'porg' in message.content.lower():
        response = requests.get('https://media.giphy.com/media/3ohhwqOVlEbBxEbss0/giphy.gif', stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename="porg.gif")

    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        await client.logout()
        await asyncio.sleep(1)
        sys.exit(1)

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
# client.run(keys.token)
client.run(keys.eng)
