# bot.py
import os

import beats
from math import floor
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN is None:
    raise RuntimeError("DISCORD token not set (set DISCORD_TOKEN env var)")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content in {".beat", ".beats", ".time", "$beat", "$beats", "$time"}:
        await message.channel.send(f"@{floor(beats.itime())}")

    if message.content in {".beatd", "$beatd"}:
        await message.channel.send(f"@{'{:.3f}'.format(beats.itime())}")

    if message.content in {".what", "$what"}:
        await message.channel.send("https://en.wikipedia.org/wiki/Swatch_Internet_Time")


client.run(TOKEN)
