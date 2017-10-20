import discord
import he
import asyncio
import keys

client = discord.Client()


@asyncio.coroutine
async def hilfe(message, user, length):
    await client.login(keys.token)
    if length <= 7:
        embed = he.hilfe
        await client.send_message(user, embed=embed)
    elif length > 7:
        arg = message
        print(arg)

