import discord
import os
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os
import random

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
		await message.channel.send("<:hari:506923677225320468>")
	elif message.content == "frown":
		await message.channel.send(":frowning:")
	elif message.content == "love":
		await message.channel.send(":cold_sweat:")
	elif message.content.startswith("!say "):
		args = message.content.split(" ")
		await message.channel.send(" ".join(args[1:]))
	elif message.content == "!call":
		st = callSquad(member)
		await message.channel.send(st)
	elif message.content == "!allmembers":
		x = message.guild.members
		for m in x:
			if m.bot:
				continue
			await message.channel.send(m.name)
	elif message.content == "!allbots":
		x = message.guild.members
		for m in x:
			if m.bot:
				await message.channel.send(m.name)
	elif message.content == "!memberstats":
		x = message.guild.members
		a = 0
		b = 0
		for m in x:
			if m.bot:
				b = b + 1
			else:
				a = a + 1
		await message.channel.send("Total strength "+ str(a+b))
		await message.channel.send("Members "+ str(a))
		await message.channel.send("Bots "+ str(b))

def randomize():
	st = ["Let's have chicken dinner...", "Let's go...", "The opportunity of defeating the enemy is provided by the enemy himself...", "Gather around...", "Stay alert..."]
	n = random.randint(0,len(st)-1)
	return st[n]



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
	s = s + "<@" + str(member.id) + "> is calling you... "
	s = s + randomize()
	return s


client.run(os.getenv('TOKEN'))







