import discord
import os
from discord.ext import commands

TOKEN = 'MTA1MzA1NTU3NDI4NTIyMTk2OQ.GP6asU.lDMCjoKrRpboG8ezqgp6zkf3lPYdmal0vBcSn0'

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

client.run(TOKEN)