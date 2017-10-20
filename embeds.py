# Hier werden die einzelnen 'p.help'-Argumente gehandled.

import discord
import he
import asyncio
import keys

client = discord.Client()
mlist = open("config/mods.txt", "r", encoding='utf-8')
mods = mlist.readlines()


@asyncio.coroutine
async def hilfe(message, user, length):
    await client.login(keys.token)
    if length <= 7:
        embed = he.hilfe
        await client.send_message(user, embed=embed)
    elif length > 7:
        arg = message
        if arg == "musik":
            embed = he.musik
            await client.send_message(user, embed=embed)
        elif arg == "allgemein":
            embed = he.allgemein
            await client.send_message(user, embed=embed)
        elif arg == "mod" and user.id in mods:
            embed = he.mods
            await client.send_message(user, embed=embed)
        elif arg == "spiele":
            embed = he.minigames
            await client.send_message(user, embed=embed)
        elif arg == "test":
            pass
        elif arg == "komplett":
            if user.id in mods:
                allgemein = he.allgemein
                musik = he.musik
                spiele = he.minigames
                mem = he.mods
                await client.send_message(user, embed=allgemein)
                await client.send_message(user, embed=musik)
                await client.send_message(user, embed=spiele)
                await client.send_message(user, embed=mem)
            else:
                allgemein = he.allgemein
                musik = he.musik
                spiele = he.minigames
                await client.send_message(user, embed=allgemein)
                await client.send_message(user, embed=musik)
                await client.send_message(user, embed=spiele)
        else:
            embed = he.hilfe
            await client.send_message(user, embed=embed)


async def halt():
    await client.logout()
