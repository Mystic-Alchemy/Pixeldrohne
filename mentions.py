# Hier wird das taggen von gewissen Personen verhindert.

import discord
import keys


client = discord.Client()

@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    try:
        if message.mentions[0]:
            user = message.mentions[0]
            id = user.id
            if id == keys.pmcid:
                await client.delete_message(message)
                await client.send_message(message.channel, "Bitte PilleniusMC nicht taggen!")
            if id == keys.pxlid:
                await client.delete_message(message)
                await client.send_message(message.channel, "Bitte Pixelwerfer nicht taggen!")
    except Exception as error:
        print("Erwarteter Error: {error}".format(error=error))
    if message.content.lower().startswith('p.halt') and message.author.id == keys.pmcid:
        await client.close()
        sys.exit(1)

client.run(keys.token)
