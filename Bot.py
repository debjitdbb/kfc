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



# @client.event
# async def on_member_join(member):
#     if member.dm_channel is None:
#         await member.create_dm()
#     dmchannel = member.dm_channel
#     await dmchannel.send("https://cdn.discordapp.com/attachments/467741161910435852/513031345329405973/IMG-20181116-WA0019.jpg")
#     await dmchannel.send("Please go through the first PINNED message on match-info channel and post any doubts(if you have any) on that channel itself.")



@client.event
async def on_message(message):
	tppsquad = [340029411145416707, 430425824118833162, 466270095497363496, 488707015921893377, 444780058888896527]
	fppsquad = [466270095497363496, 428543156242481152, 455039811791749130, 463002393617891338, 430425824118833162, 483990246825132053]
	member = message.author
	user = client.get_user(member.id)
	if message.content.startswith("!say "):
		args = message.content.split(" ")
		await message.channel.send(" ".join(args[1:]))
	elif message.content == "!calltpp":
		st = callSquad(member,tppsquad)
		await message.channel.send(st)
	elif message.content == "!callfpp":
		st = callSquad(member,fppsquad)
		await message.channel.send(st)
	elif message.content == "!allmembers":
		x = message.guild.members
		s = "\n"
		for m in x:
			if m.bot:
				continue
			s = s + "\n" + m.name
		await message.channel.send(s)
	elif message.content == "!allbots":
		x = message.guild.members
		s = "\n"
		for m in x:
			if m.bot:
				s = s + "\n" + m.name
		await message.channel.send(s)

	elif message.content == "!memberstats":
		x = message.guild.members
		a = 0
		b = 0
		for m in x:
			if m.bot:
				b = b + 1
			else:
				a = a + 1
		s = "\n"
		s = s + "Total strength " + str(a+b) + "\n" + "Members " + str(a) + "\n" + "Bots " + str(b)
		await message.channel.send(s)

	elif message.content == "!send":
		servers = client.guilds
		for i in servers:
			await message.channel.send(i.id + " " + i.name)



def randomize():
	st = ["Let's have chicken dinner...", "Let's go...", "The opportunity of defeating the enemy is provided by the enemy himself...", "Gather around...", "Stay alert...", "Charge...", "There can only be one WINNER...", "Enemies ahead..."]
	n = random.randint(0,len(st)-1)
	return st[n]



def callSquad(member, squad):
	s = ""
	flag = False
	# squad = [466270095497363496,428543156242481152,455039811791749130,463002393617891338,430425824118833162]
	for i in squad:
		# print(i)
		if member.id == i:
			flag = True
			continue
		s = s + "<@" + str(i) + "> "
	if flag == False:
		return "You are not authorised to execute this command..."
	s = s + " come, " "<@" + str(member.id) + "> is calling you... "
	s = s + randomize()
	return s

client.run("NTA0Mzg2MDY4MDUzODg0OTMw.DrrKkg.vJ5I6l4fuDLjNguOveQzN3f6sdc")
# client.run(os.getenv('TOKEN'))







