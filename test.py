# Diese Datei ist für den Schwesterbot der Pixeldrohne, PixelDev gedacht.

import discord
import sys
import asyncio
import keys
import random
import urllib.request
import pxldrn

client = discord.Client()
players = {}
p_volume = {}

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')
    await client.change_presence(game=discord.Game(name='mit dev.help', type=1, url="https://twitch.tv/pilleniusmc"))


@client.event
async def on_message(message):
    try:
        mu = message.author.name + ": "
        ms = message.content
        print(mu + ms)
    except Exception:
        pass
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
    if message.content.lower().startswith('dev.p'):
        await client.send_message(message.channel, embed=pxldrn.adv.embed_data.help_embeds.intro(client))
    if message.content.lower().startswith('dev.perms'):
        member = message.author
        perms = member.server_permissions
        await client.send_message(message.channel, str(perms.value))
    if message.content.lower().startswith('dev.radio'):
        radio = "".join(message.content.split(' ')[1:]).lower()
        radio_msg = pxldrn.adv.capword(message.content.split(' ')[1:])
        radio_url = pxldrn.adv.radio(radio)
        if radio_url == "XTAB":
            await client.send_message(message.channel, 'Sorry, den Radiosender kenne ich nicht. Für eine Liste der Sender nutze "dev.radio liste".')
        elif radio_url == "RSL":
            await client.send_message(message.channel, embed=pxldrn.adv.embed_data.radio_list())
        elif radio_url == "NoStation":
            await client.send_message(message.channel, 'Wähle bitte einen Radio-Sender aus. Für eine Liste der Sender nutze "dev.radio liste".')
        else:
            if client.is_voice_connected(message.server):
                voice = client.voice_client_in(message.server)
                if players[message.server.id].is_playing():
                    players[message.server.id].stop()
                    player = voice.create_ffmpeg_player(radio_url, before_options=' -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 ')
                    players[message.server.id] = player
                    player.volume = p_volume[message.server.id]
                    player.start()
                    await client.send_message(message.channel, "Kanal auf {} gewechselt.".format(radio_msg))
                else:
                    player = voice.create_ffmpeg_player(radio_url, before_options=' -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 ')
                    players[message.server.id] = player
                    player.volume = 0.03
                    p_volume[message.server.id] = 0.03
                    player.start()
                    await client.send_message(message.channel, "Du hörst jetzt {}".format(radio_msg))
            elif not client.is_voice_connected(message.server):
                channel = message.author.voice.voice_channel
                voice = await client.join_voice_channel(channel)
                player = voice.create_ffmpeg_player(radio_url, before_options=' -reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5 ')
                players[message.server.id] = player
                player.volume = 0.03
                p_volume[message.server.id] = 0.03
                player.start()
                await client.send_message(message.channel, "Du hörst jetzt {}".format(radio_msg))
    if message.content.startswith('dev.volume'):
        volume = int(message.content.split(" ")[1])
        if volume <= 100:
            players[message.server.id].volume = volume / 100
            p_volume[message.server.id] = volume / 100
            await client.send_message(message.channel, "Lautstärke erfolgreich "
                                                       "auf {0} % eingestellt.".format(volume))
        elif volume > 100:
            await client.send_message(message.channel, "Diese Lautstärke ist eindeutig **zu hoch**!")
    if message.content.lower().startswith('dev.mute'):
        if players[message.server.id].volume == 0:
            players[message.server.id].volume = p_volume[message.server.id]
        else:
            players[message.server.id].volume = 0
    if message.content.startswith('p.leave'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "Ich bin doch in keinem Kanal, was willst du von mir?")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error is aufgetreten:\n ```{error}```".format(error=error))
    if message.content.lower().startswith('p.8ball'):
        msg = message.content.split(' ')[1:]
        length = len(message.content[8:])
        await client.send_message(message.channel, pxldrn.adv.eightball(msg, length))

    if message.author.id == keys.pmcid and message.content.lower().startswith('dev.halt'):
        await client.close()
        sys.exit(1)


client.run(keys.dev)
# client.run(keys.eng)
# client.run(keys.token)
