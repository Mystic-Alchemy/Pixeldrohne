# Hier werden die einzelnen 'p.help'-Argumente gehandled.

import discord
import asyncio
import keys
import sysinfo
from pxldrn.adv import he

client = discord.Client()
mlist = open("config/mods.txt", "r", encoding='utf-8')
mods = mlist.readlines()


def system_info():
    sysembed = discord.Embed(
        title="System Info",
        description="Hier siehst du alle System-Infos",
        color=0x128f24
    )
    sysembed.add_field(
        name="CPU Temperatur",
        value=sysinfo.getCPUtemp()
    )
    sysembed.add_field(
        name="CPU Nutzung",
        value=sysinfo.getCPUuse()
    )
    sysembed.add_field(
        name="RAM Auslastung",
        value="Belegt: {0} KB\nFrei: {1} KB\nGesamt: {2} KB".format(sysinfo.getRAMinfo()[1], sysinfo.getRAMinfo()[2], sysinfo.getRAMinfo()[0])
    )
    return(sysembed)


def py_help():
    pyemb = discord.Embed(
        title="Python lernen.",
        color=0xf8dc2e,
        description="Es scheint so, dass jemand hier zu viele Fragen über Python und vielleicht"
                    " auch discord.py stellt."
    )
    pyemb.set_author(name="Pixeldrohne")
    pyemb.set_footer(text='"Intelligenz ist die Fähigkeit, sich dem Wandel anzupassen." - Stephen Hawking')
    pyemb.set_thumbnail(url="https://www.python.org/static/opengraph-icon-200x200.png")
    pyemb.add_field(name="Tutorials:", value="https://www.python-kurs.eu/index.php\n"
                                             "http://py-tutorial-de.readthedocs.io/de/python-3.3/\n"
                                             "http://praxistipps.chip.de/python-tutorial-auf-deu"
                                             "tsch-fuer-einsteiger_93386")
    pyemb.add_field(name="Bücher:", value="https://www.rheinwerk-verlag.de/einstieg-in-python_4374/\n"
                                          "https://www.rheinwerk-verlag.de/programmieren-lernen-mit-python_3674/\n")
    pyemb.add_field(name="Videos:", value="https://www.youtube.com/watch?v=bt_Wcp3qemM\n"
                                          "https://www.youtube.com/watch?v=dG0kxa0XoXc\n"
                                          "https://www.youtube.com/watch?v=ikuyDZNsbNk")
    pyemb.add_field(name="discord.py", value="https://www.youtube.com/channel/UCisqgTzV--rB_WByK-wuY6g\n"
                                             "https://discordpy.readthedocs.io/en/latest/api.html#client")
    return(pyemb)


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
