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
	member = message.author
	user = client.get_user(member.id)
	if message.content == "cookie":
		await message.channel.send(":cookie:")
	elif message.content == "hari":
		await message.channel.send("<:hari:505608378656096256>")
	elif message.content == "frown":
		await message.channel.send(":frowning:")
	elif message.content == "love":
		await message.channel.send(":cold_sweat:")
	elif message.content.startswith("!say "):
		args = message.content.split(" ")
		await message.channel.send(" ".join(args[1:]))



client.run(os.getenv('TOKEN'))







