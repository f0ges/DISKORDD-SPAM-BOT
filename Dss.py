import discord
import os
from discord.ext import commands

TOKEN = "MTA1MzA1NTU3NDI4NTIyMTk2OQ.Gg3pgI.FcvBv8e5qmu8vR3b3OyDoFaoP1cCXT-DvPvT3A"

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        while True:
            await    message.channel.send('@everyone')
    elif message.content.startswith('$stop'):
        await    message.channel.send('Ok!')
        exit()

client.run(TOKEN)