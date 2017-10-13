import discord
import asyncio

client = discord.Client()

players = {}


@client.event
async def on_ready():
    print(client.user.name)
    print("--------------------")

@client.event
async def on_message(message):
    if message.content.startswith('?troll '):
        yt_url = message.content[7:]
        try:
            channel = client.get_channel('289783480575852557')
            voice = await client.join_voice_channel(channel)
            player = await voice.create_ytdl_player(yt_url, before_options=" -reconnect 1 -reconnect_streamed 1"
                                                                           " -reconnect_delay_max 5")
            await client.delete_message(message)
            players[message.server.id] = player
            player.volume = 0.08
            player.start()
            await asyncio.sleep(5)
            await voice_client.disconnect()
        except Exception as error:
            await client.send_message(message.channel,
                                      "Ein Error ist aufgetreten:\n ```{error}```".format(error=error))

    if message.content.startswith('?loop'):
        await client.send_message(message.channel, "Jetzt wird es lustig")
        await asyncio.sleep(1)
        await client.send_message(message.channel, "?loop")

    if message.content.lower().startswith('?scroll'):
        await client.change_presence(game=discord.Game(name='1234321', type=0))
        await asyncio.sleep(0.5)
        await client.change_presence(game=discord.Game(name='2343212', type=0))
        await asyncio.sleep(0.5)
        await client.change_presence(game=discord.Game(name='3432123', type=0))
        await asyncio.sleep(0.5)
        await client.change_presence(game=discord.Game(name='4321234', type=0))
        await asyncio.sleep(0.5)
        await client.change_presence(game=discord.Game(name='3212343', type=0))
        await asyncio.sleep(0.5)
        await client.change_presence(game=discord.Game(name='2123432', type=0))
        await asyncio.sleep(0.5)





client.run('MzQ2OTk3MTY5MDcwMjc2NjA4.DHR94g.It1hLi-Tk-tEAKln3VWg5MSQVAk')