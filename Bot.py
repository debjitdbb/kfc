import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
	game = discord.Game(name = "in Erangel")
	await client.change_presence(status=discord.Status.idle, activity=game)



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
	elif message.content == "!call":
		str = callSquad(member)
		await message.channel.send(str)


def callSquad(member):
	s = ""
	flag = False
	squad = [466270095497363496,428543156242481152,455039811791749130,463002393617891338,430425824118833162]
	for i in squad:
		# print(i)
		if member.id == i:
			flag = True
			continue
		s = s + "<@" + str(i) + "> "
	if flag == False:
		return "You are not authorised to execute this command..."
	s = s + "Let's have chicken dinner..."
	return s


client.run(os.getenv('TOKEN'))







