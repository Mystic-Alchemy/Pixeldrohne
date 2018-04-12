# Diese Datei ist für den Schwesterbot der Pixeldrohne, PixelDev gedacht.

import discord
import sys
import asyncio
import keys
import random
import urllib.request

client = discord.Client()
players = {}

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
    if message.content.lower().startswith('dev.lsd'):
        # öffnen = open("config/zitate.txt", "r", encoding='utf-8')
        öffnen = urllib.request.urlopen("https://sherlock-holm.es/stories/plain-text/cano.txt")
        for line in öffnen:
            line = line.strip()
            line = str(line)
            if not line == "b''":
                line = line[2:]
                line = line.rstrip('\'')
                await client.send_message(message.author, line)
                await asyncio.sleep(1)

    if message.content.lower().startswith('dev.tt'):
        ttemb = discord.Embed(
            title="PilleniusMC",
            description="So könnte ein Twitch Chat Embed aussehen.",
            color=0x6441a4
        )
        await client.send_message(message.channel, embed=ttemb)

    if message.author.id == keys.pmcid and message.content.lower().startswith('dev.halt'):
        await client.close()
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

    if message.content.startswith('m.leave'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "Ich bin doch in keinem Kanal, was willst du von mir?")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error is aufgetreten:\n ```{error}```".format(error=error))

    if message.content.startswith('m.play'):
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

    if message.content.startswith('m.pause'):
        try:
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n ```{error}```".format(error=error))

    if message.content.startswith('m.resume'):
        try:
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n ```{error}```".format(error=error))

    if message.content.startswith('m.volume'):
        volume = int(message.content[9:])
        if volume <= 100:
            players[message.server.id].volume = volume / 100
            await client.send_message(message.channel, "Lautstärke erfolgreich "
                                                       "auf {0} % eingestellt.".format(volume))
        elif volume > 100:
            await client.send_message(message.channel, "Diese Lautstärke ist eindeutig **zu hoch**!")

    if message.content.startswith('m.stop'):
        try:
            players[message.server.id].stop()
        except Exception as error:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n ```{error}```".format(error=error))


# client.start(keys.dev)
# client.run(keys.dev)
# client.run(keys.eng)
client.run(keys.token)