import discord
import asyncio
import pxldrn.adv
from pxldrn.adv import *
import pxldrn.hilfe

client = discord.Client()
minutes = 0
hour = 0


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
