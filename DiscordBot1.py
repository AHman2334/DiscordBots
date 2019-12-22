import discord
import urllib.request
import urllib.parse
import re
import asyncio
import pafy
import time
from threading import Thread
client = discord.Client()

def return_url(video_url):
	video = pafy.new(video_url)
	best = video.getbest()
	playurl = best.url
	req = urllib.request.Request(video_url)
	resp = urllib.request.urlopen(req)
	respData = resp.read()
	video_name = re.findall(r'<meta name="title" content="(.*?)">',str(respData))
	return(playurl,video_name)

@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")
    game = discord.Game("Watching over UEE Medical Corps")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_member_join(member):
	guild = client.get_guild(515344221989765120)
	verify_channel = guild.get_channel(536336140215648266)
	user_hash = int(member.id)
	user_hash = user_hash * 2
	user = guild.get_member(member.id)
	await user.send(f"Hello there fellow citizen please navigate to https://robertsspaceindustries.com/account/profile and go to your bio and put this code at the end of your bio on a new line `{user_hash}` then please hed over to {verify_channel.mention} and put your star citizen handle there, if you need any assistance please feel free to contact a senior medical officer.")

@client.event
async def on_raw_reaction_add(payload):
	guild = client.get_guild(515344221989765120)
	if payload.message_id == 539927202800599074 and str(payload.emoji) == '👍':
		role = discord.utils.get(client.get_guild(payload.guild_id).roles, name="General")
		await guild.get_member(payload.user_id).add_roles(role)
		await guild.get_member(payload.user_id).send("You have accepted the rules this means that you will now be able to chat and talk in UEE medical discord discord server, dont forget ***FOLLOW THE RULES***")

@client.event
async def on_message(message):
	global vc
	guild = client.get_guild(515344221989765120)
	print(f"{message.channel}:{message.content}:{message.author}:{message.author.name}")

	if message.content == "!logout" and message.author.id == 285494159203368960 :
		await client.close()

	elif "!delete" in message.content and discord.utils.get(message.guild.roles, name= "✨Officer") in message.author.roles or "!delete" in message.content and discord.utils.get(message.guild.roles, name= "✨Corpsman") in message.author.roles or "!delete" in message.content and  discord.utils.get(message.guild.roles, name= "✨Medical Officer") in message.author.roles or "!delete" in message.content and  discord.utils.get(message.guild.roles, name= "🌟 Senior Medical Officer") in message.author.roles :
		messages_to_delete = int(message.content.split(" ")[1]) + 1
		messages = message.channel.history(limit= messages_to_delete)
		async for i in messages:
			message = i
			await message.delete()

	elif "SearchUserDetails" in message.content :
		user_message = str(message.content).split(" ")
		user_RSI_id = user_message[1]
		print(user_RSI_id)
		url = 'https://robertsspaceindustries.com/citizens/'+user_RSI_id
		try:
			req = urllib.request.Request(url)
			resp = urllib.request.urlopen(req)
			respData = resp.read()
			user_data = re.findall(r'<strong class="value">(.*?)</strong>',str(respData))
			user_data2 = re.findall(r'<meta property="og:site_name" content="(.*?)- Roberts Space Industries',str(respData))
			user_data2 = user_data2[0].split("|")
			citizen_ID = user_data[0]
			citizen_name = user_data[2]
			citizen_handle = user_data[1]
			citizen_joindate = user_data[3]
			try:
				citizen_org = user_data2[1].split("-")
			except:
				citizen_org = "NO ORGANIZATION LISTED"

			try:
				citizen_org = citizen_org[1]
			except:
				citizen_org = citizen_org[0]

			print(user_data,user_data2)


			try:
				citizen_org_role = user_data2[2]
				print(citizen_org_role)
				citizen_org_role = citizen_org_role.split("(")
				citizen_org_id = citizen_org_role[0]
				citizen_org_role = citizen_org_role[1]
				try:
					citizen_org_role = citizen_org_role.split(")")
					citizen_org_role = citizen_org_role[0]
				except:
					print("no brakcets present")
				print(citizen_org_role)
			except:
				citizen_org_role = "UNKNOWN"
				citizen_org_id = "UNKNOWN"

			try:
				citizen_language = ""
				citizen_language_test = user_data[5].split(" ")
				for i in citizen_language_test :
					if i != "":
						citizen_language = citizen_language+i

			except:
				citizen_language = ""
				citizen_language_test = user_data[4].split(" ")
				print(citizen_language_test)
				for i in citizen_language_test :
					if i != "":
						citizen_language = citizen_language+i
			await message.channel.send(f"Citizen `{citizen_ID}`\nHandle: `{citizen_name}`\nMoniker: `{citizen_handle}`\nJoined: `{citizen_joindate}`\nLanguage: `{citizen_language}`\nMain organization: `{citizen_org}`\nRole: `{citizen_org_role}`\nMain org ID:`{citizen_org_id}`")
		except Exception as error :
			print(error)
			await message.channel.send("***Sorry but that user was not found.***")


	elif message.channel.id == 536336140215648266:
		if message.author.id != 539548228157308931:
			try:
				user_verify = False
				guild = client.get_guild(515344221989765120)
				url = "https://robertsspaceindustries.com/citizens/" + message.content
				req = urllib.request.Request(url)
				resp = urllib.request.urlopen(req)
				respData = resp.read()
				citizen_name = str(message.content)
				print(citizen_name)
				user_bio = re.findall(r'<div class="value">(.*?)</div>',str(respData))
				print(user_bio)
				user_bio = str(user_bio[0])
				user_bio = user_bio.split(" ")
				print(user_bio)
				print(str(message.author.id))
				user_id = int(message.author.id)
				user_id = user_id * 2
				user_data2 = re.findall(r'<meta property="og:site_name" content="(.*?)- Roberts Space Industries',str(respData))
				user_data2 = user_data2[0].split("|")
				print(user_data2)
				try:
					citizen_org_role = user_data2[2]
					print(citizen_org_role)
					citizen_org_role = citizen_org_role.split("(")
					citizen_org_id = citizen_org_role[0]
				except Exception as error :
					print(error)
					citizen_org_id = "UNKNOWN"


				for i in user_bio:
					try:
						i = re.findall(r"\d+",i)
					except Exception as error:
						print(error)
					print(i)
					i = "".join(i)
					print(i)
					if i == str(user_id):
						if citizen_org_id == " HOSPITAL ":
							member = guild.get_member(message.author.id)
							await member.edit(nick = citizen_name)
							role = discord.utils.get(message.guild.roles, name="Verified")
							await message.author.add_roles(role)
							user_verify = True
							await message.channel.send("yay your in medical and you are verified!!!")
						else:
							print("Match!")
							print(citizen_org_id)
							member = guild.get_member(message.author.id)
							await member.edit(nick = citizen_name)
							role = discord.utils.get(message.guild.roles, name="Verified")
							await message.author.add_roles(role)
							user_verify = True
							await message.channel.send("yay you got an match but your not in medical :(, but i did you the favour of verifying you anyway, happy trails!")
				if user_verify == False :
					await message.channel.send("Gosh darn something went wrong my tricorder is picking up no signs of your verification code anywhere in your bio are you sure you put one there?")
			except Exception as error:
				print(error)
				await message.channel.send("Sorry something went wrong this could be because you typed your name wrong or you do not exist we hope it was the former of the 2 please ask a senior medical officer for help.")

	elif message.content == "!verify":
		guild = client.get_guild(515344221989765120)
		verify_channel = guild.get_channel(536336140215648266)
		user_hash = int(message.author.id)
		user_hash = user_hash * 2
		await message.channel.send(f"Hello there fellow citizen please navigate to https://robertsspaceindustries.com/account/profile and go to your bio and put this code at the end of your bio on a new line `{user_hash}` then please hed over to {verify_channel.mention} and put your star citizen handle there, if you need help please feel free to contact a senior medical officer.")

	elif message.content == "join chat":
		member = guild.get_member(message.author.id)
		try:
			vc = await member.voice.channel.connect()
			await message.channel.send(f"🔊 ok i am in {member.voice.channel} 🔊")
		except Exception as error:
			print(error)
			await message.channel.send("**YOU NEED TO BE IN A VOICE CHANNEL TO USE THAT COMMAND**")

	elif message.content.startswith("play") :
		member = guild.get_member(message.author.id)
		if "https://" in message.content :
			try:
				url = str(message.content.split(" ")[1])
				print(url)
			except Exception as error :
				print(error)
				await message.channel.send("**please try again and put a URL.**")
				return

			video_url = url
			playurl = return_url(video_url)[0]
			video_name = return_url(video_url)[1]
			try:
				print("line 216")
				vc.play(discord.FFmpegPCMAudio(playurl))
				print("LINE 218")
			except Exception as error:
				print(error)
				try:
					print("line 221")
					vc = await member.voice.channel.connect()
					print("line 223")
					vc.play(discord.FFmpegPCMAudio(playurl))
				except Exception as error:
					print(error)
					await message.channel.send("**YOU NEED TO BE IN A VOICE CHANNEL TO USE THAT COMMAND**")
					return
			await message.channel.send(f"**OK, PLAYING `{video_name[0]}`** 🎵")
		else:
			song_url = "https://www.youtube.com/results?search_query="
			song_name = message.content.split(" ")
			for i in song_name:
				if i != "play":
					song_url = song_url + i + "+"
			print(song_url)
			req = urllib.request.Request(song_url)
			resp = urllib.request.urlopen(req)
			respData = resp.read()
			video_results = re.findall(r'<h3 class="yt-lockup-title "><a href="(.*?)" class="yt-uix-tile-link',str(respData))
			print(video_results)
			try:

				video_url = "https://youtube.com" + video_results[0]
				playurl = return_url(video_url)[0]
				video_name = return_url(video_url)[1]

				try:
					vc.play(discord.FFmpegPCMAudio(playurl))
				except Exception as error:
					print(error)
					try:
						vc = await member.voice.channel.connect()
						vc.play(discord.FFmpegPCMAudio(playurl))
					except Exception as error:
						print(error)
						await message.channel.send("**YOU NEED TO BE IN A VOICE CHANNEL TO USE THAT COMMAND**")
						return
				await message.channel.send(f"**OK, PLAYING `{video_name[0]}`** 🎵")

			except Exception as error:
				print(error)
				await message.channel.send("**SORRY NO RESULTS FOUND**")


	elif message.content == "pause" :
		try:
			vc.pause()
			await message.channel.send("**OK,** ⏸")
		except:
			await message.channel.send("**THE BOT IS NOT IN A VOICE CHAT**")

	elif message.content == "resume" :
		try:
			vc.resume()
			await message.channel.send("**OK,** ▶")
		except:
			await message.channel.send("**THE BOT IS NOT IN A VOICE CHAT**")
	elif message.content == "stop" :
		try:
			vc.stop()
			await message.channel.send("**OK,** ⏹")
		except:
			await message.channel.send("**THE BOT IS NOT IN A VOICE CHAT**")
	elif message.content == "disconnect":
		try:
			await vc.disconnect()
			await message.channel.send("**OK, DISCONNECTED**")
		except:
			await message.channel.send("**THE BOT IS NOT IN A VOICE CHAT**")

	elif message.content.startswith("SearchShip"):
		ship_name = []
		for i in message.content.split(" "):
			if i !="SearchShip":
				ship_name.append(i)
				ship_name.append("%20")
		print(ship_name)
		ship_name.pop(len(ship_name)-1)
		print(ship_name)
		ship_name_str = ""
		for i in ship_name:
			ship_name_str = ship_name_str + i
		base_url_PT1 = "https://robertsspaceindustries.com/pledge/ships?sort=store&search="
		base_url_PT2 = "&itemType=ships&storefront=pledge&type=&mass=&length=&max_crew=&msrp=&"
		ship_search_url = base_url_PT1 + ship_name_str + base_url_PT2
		req = urllib.request.Request(ship_search_url)
		resp = urllib.request.urlopen(req)
		respData = resp.read()
		f = open("RespData.txt","w")
		f.write(str(respData))
		f.close()
		ship_page_url = re.findall(r'<a class="gradient trans-02s" href="(.*?)"></a>',str(respData))
		print(ship_page_url)

client.run("NTM5NTQ4MjI4MTU3MzA4OTMx.Xf5Vgw.RYv66Ap2ouSaMiUR4dwQVllklMQ")