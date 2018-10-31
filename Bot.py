import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")



@client.event
async def on_message(message):
	if message.content == "cookie":
		await client.send_message(message.channel, ":cookie:")
	elif message.content == "frown":
		await client.send_message(message.channel, ":frowning:")
	elif message.content == "love":
		await client.send_message(message.channel, ":cold_sweat:")
	elif message.content.startswith("!say "):
		args = message.content.split(" ")
		await client.send_message(message.channel, " ".join(args[1:]))



client.run(os.getenv('TOKEN'))







