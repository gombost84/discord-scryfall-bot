import discord
import re
import scryfall_request

pattern = r'\[\[(\w+|\w+.*\w+)\]\]'

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if re.findall(pattern, message.content):
        await message.channel.send(scryfall_request.card_data(re.search(pattern, message.content).group(1)))

client.run('')
