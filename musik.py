# Dieses Skript steuert die Musikfunktion des Bots.

import discord
import sys
import keys
import asyncio

client = discord.Client()
players = {}
schlange = []
mods = open("config/mods.txt", "r", encoding='utf-8')


@client.event
async def on_ready():
    print(client.user.name)
    print("--------------------")


@client.event
async def on_message(message):
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
        if not players[message.server.id].is_playing():
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
                player.start()
        else:
            await client.send_message(message.channel, "Sorry diese Anfrage kann ich zur Zeit nicht verarbeiten.")
            schlange.append(yt_url)

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
        try:
            volume = int(message.content[9:])
            if volume <= 100:
                players[message.server.id].volume = volume / 100
                await client.send_message(message.channel, "Lautstärke erfolgreich "
                                                           "auf {0} % eingestellt.".format(volume))
            elif volume > 100:
                await client.send_message(message.channel, "Diese Lautstärke ist eindeutig **zu hoch**!")
        except Exception as e:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n ```{error}```".format(error=e))

    if message.content.startswith('p.stop'):
        try:
            players[message.server.id].stop()
        except Exception as error:
            await client.send_message(message.channel, "Ein Error ist aufgetreten:\n ```{error}```".format(error=error))

    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        await client.logout()
        await asyncio.sleep(1)
        sys.exit(1)

client.run(keys.token)
