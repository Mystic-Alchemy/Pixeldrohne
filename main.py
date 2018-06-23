# Um den gesamten Bot auszuführen muss nur noch die Datei genutzt werden

import asyncio
import aiohttp
import io
import discord
import safygiphy
from discord.ext import commands
import sys
from server_specifics import *
from helps import Help
from moderation import *
from custom_commands import *
from music import Voice
import keys
import random

giphy = safygiphy.Giphy()
bot = commands.Bot(command_prefix=keys.prefix, case_insensitive=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Bot-Info:\nName: " + bot.user.name + "\nId: " + str(bot.user.id))
    await bot.change_presence(activity=discord.Game(f"mit {bot.command_prefix}help"))


@bot.command(no_pm=True)
async def say(ctx, *, arg):
    await ctx.message.delete()
    time = 0.2 * len(arg.split(' '))
    async with ctx.channel.typing():
        await asyncio.sleep(time)
        await ctx.channel.send(arg)

@say.error
async def say_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.message.delete()
        await ctx.channel.send("Du musst mir schon etwas geben, dass ich sagen kann.", delete_after=3)


@bot.command(no_pm=True)
async def avatar(ctx, user: discord.Member):
    async with aiohttp.ClientSession() as session:
        async with session.get(user.avatar_url) as resp:
            img = await resp.read()
            await ctx.send(file=discord.File(img, 'avatar.gif'))


@avatar.error
async def avatar_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Sorry, den Avatar dieses Nutzers kann ich nicht abrufen")
    if isinstance(error, commands.MissingRequiredArgument):
        async with aiohttp.ClientSession() as session:
            async with session.get(ctx.message.author.avatar_url) as resp:
                img = await resp.read()
                await ctx.send(file=discord.File(img, 'avatar.gif'))


@bot.command(no_pm=True)
async def gif(ctx, *, arg):
    async with ctx.channel.typing():
        rgif = giphy.random(tag=arg)
        async with aiohttp.ClientSession() as session:
            async with session.get(str(rgif.get("data", {}).get('image_original_url'))) as resp:
                rgif = await resp.read()
                await ctx.send(file=discord.File(rgif, 'gif.gif'))


@gif.error
async def gif_error(ctx, error):
    if isinstance(error, commands.CommandInvokeError):
        await ctx.send("Irgendetwas ist schiefgegangen. Bitte versuche es nochmal")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Bitte gib einen Suchbegriff ein.")
    else:
        await ctx.send(str(error))


@bot.command(no_pm=True)
async def zahl(ctx, z_min: int, z_max: int):
    await ctx.send(f"Deine Zahl ist: {random.randint(z_min, z_max)}")


@zahl.error
async def zahl_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Du musst mir zwei Zahlen geben, die erste das Minimum, die zweite das Maximum.")


bot.add_cog(Help(bot))
bot.add_cog(Voice(bot))
bot.add_cog(Mods(bot))
bot.add_cog(CustomCommands(bot))
bot.run(keys.dev)
