import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


async def on_ready():
	print("Bot starts")

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



bot.run(os.getenv('TOKEN'))







