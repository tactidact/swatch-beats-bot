# bot.py
import os

import beats
from math import floor
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if (message.content == '$beats') or (message.content == '$swatch') or (message.content == '$internet') or (message.content == '$time'):
        await message.channel.send(f'@{floor(beats.itime())}')

    if message.content == '$beatd':
        await message.channel.send(f'@{"{:.3f}".format(beats.itime())}')

    if message.content == '$what':
        await message.channel.send(f'https://en.wikipedia.org/wiki/Swatch_Internet_Time')

client.run(TOKEN)
