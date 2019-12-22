# id   502184905606955009
# token NTAyMTg0OTA1NjA2OTU1MDA5.DqkP2Q._xZqE70ewswRhK5sTFPK_ABpY8k
# permission int 8

# url https://discordapp.com/oauth2/authorize?client_id=502184905606955009&scope=bot&permissions=8
import random
import discord
import os ,os.path
import urllib.request
import urllib.parse
import re
import socket
import time

client = discord.Client()

global message


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")

@client.event
async def on_member_join(member):
    channel = client.get_channel(409652681851011083)
    await member.send(f"Hello there {member.mention} Welcome to Harv & Kapps please go to #rules and upvote them to get access to the server also please upvote your continent that is listed below")
    await channel.send(f"Welcome to Harv & Kapps !!!{member.mention}")

@client.event
async def on_member_remove(member):
    channel = client.get_channel(409652681851011083)
    await channel.send(f"Goodbye {member.mention}.")
    
@client.event
async def on_raw_reaction_remove(payload):
    print(payload.message_id)
    print(payload.emoji.name)
    guild = client.get_guild(315139594771234816)
    user_id = payload.user_id
    user = client.get_user(user_id)
    user2 = str(user).split('#')
    user2 = user2[0]
    if payload.message_id == 504570124821331968 and str(payload.emoji) == '👍':
        role = discord.utils.get(client.get_guild(payload.guild_id).roles, name="people")
        await guild.get_member(payload.user_id).remove_roles(role)
        await guild.get_member(payload.user_id).send("You have un accepted the rules this means you will not be able to chat on Harv & Kapps Discord server.")

@client.event
async def on_raw_reaction_add(payload):
    print(payload.message_id)
    print(payload.emoji.name)
    guild = client.get_guild(315139594771234816)
    user_id = payload.user_id
    user = client.get_user(user_id)
    user2 = str(user).split('#')
    user2 = user2[0]
    member = guild.get_member(user_id)
    if payload.message_id == 504570124821331968 and str(payload.emoji) == '👍':
        role = discord.utils.get(client.get_guild(payload.guild_id).roles, name="people")
        await guild.get_member(payload.user_id).add_roles(role)
        await guild.get_member(payload.user_id).send("You have accepted the rules this means that you will now be able to chat and talk in Harv & Kapps discord server, dont forget ***FOLLOW THE RULES***")
    if payload.message_id == 504570124821331968 and str(payload.emoji) == '👎':
        role = discord.utils.get(client.get_guild(payload.guild_id).roles, name="temp ban")
        role2 = discord.utils.get(client.get_guild(payload.guild_id).roles, name="people")
        await guild.get_member(payload.user_id).add_roles(role)
        author = guild.get_member(payload.user_id)
        await guild.get_member(payload.user_id).send("""You have denied the rules this means that you have been added the temp ban if you would like to accept the rules accept them then tell an admin to remove your temp ban role.""")
        if  discord.utils.get(client.get_guild(payload.guild_id).roles, name="people") in author.roles :
            await guild.get_member(payload.user_id).remove_roles(role2)

    if payload.message_id == 505376001715601409 :
        try:
            await member.edit(nick = '[EU] '+user2)
        except:
            print("Permission denied")
    if payload.message_id == 505374346722803713 :
        try:
            await member.edit(nick = '[NAM] '+user2)
        except:
            print("Permission denied")
    if payload.message_id == 505374520522047506 :
        try:
            await member.edit(nick = '[SAM] '+user2)
        except:
            print("Permission denied")
    if payload.message_id == 505374624096190477 :
        try:
            await member.edit(nick = '[AF] '+user2)
        except:
            print("Permission denied")
    if payload.message_id == 505375014699139072 :
        try:
            await member.edit(nick = '[SAS] '+user2)
        except:
            print("Permission denied")
    if payload.message_id == 505375252692336650 :
        try:
            await member.edit(nick = '[NAS] '+user2)
        except:
            print("Permission denied")
    if payload.message_id == 505376389760024576 :
        try:
            await member.edit(nick = '[OC] '+user2)
        except:
            print("Permission denied")



@client.event
async def on_message(message):
    try:
        print(f"{message.channel}:{message.content}:{message.author}:{message.author.name}")
    except:
        print(f"{message.channel}:{message.content}")
        message.chanel.send("**Please dont use special characters in your username as it causes issues for this bot if you want a special name please change you nick name instead**")
    member_HandK = client.get_guild(315139594771234816)

    if message.content.lower() == '!logout' and message.author.id == 285494159203368960 :
        await client.close()

    
    elif "8N41AQBE9N52268" in message.content:
        user_message = str(message.content)
        user_message = user_message.split("-")

        if user_message[1].lower() == "test":
            await client.get_channel(487643571709542411).send("This is just a test please ignor.")
            await client.get_user(249213499279015936).send("This is a test please ignor.")
        else:
            await client.get_channel(487643571709542411).send(user_message[1])
            await client.get_user(249213499279015936).send(user_message[1])

    elif "info" == message.content.lower() and message.guild.name == "Harv & Kapps":
        await message.channel.send("""
VISIT OUR YOUTUBE AT:https://www.youtube.com/channel/UCEXTVmaQGltsa_1tPgdCq-g
AND OUR WEBSITE AT: https://hrvdmn.wixsite.com/harvandkapps
JOIN OUR PARTNER DISCORD SERVER AT: https://discord.gg/WmXuJfH
""")

    elif "info" == message.content.lower() and message.guild.name == "Zilas discord server":
        await message.channel.send("""
vi er en lille discord gruppe, med hoved dellen af medlemmerne værnede dansk.
invitations link: https://discord.gg/WmXuJfH
Vi er partnere med:  https://discord.gg/QBGAhpN
""")
    elif "member count" == message.content.lower() and message.guild.name == "Harv & Kapps":
        member_count = str(member_HandK.member_count)
        bot_message = f"There are  "+member_count+"  members on this discord server"
        bot_message = str(bot_message)
        bot_message = bot_message.strip("'")
        bot_message = bot_message.strip(")")
        bot_message = bot_message.strip("(")
        bot_message = bot_message.strip(",")

        await message.channel.send(bot_message)
    elif "help" == message.content.lower() and message.guild.name == "Harv & Kapps":
        await message.channel.send("""**HELLO THERE I SEE YOU ARE LOST DONT WORRY ILL TALK YOU THROUGH IT #general-beskeder IS THE GENERAL CHAT
THE RULES ARE IN #welcome-velkommen AND THE MEMES GO IN WHATEVER THE MEME CHANNEL IS CALLED MOST LIKELY #memez ANNOUNCEMENTS ARE IN #announcements AND
THE DOWNLOAD LINKS FOR STAGE 9 RE-UPLOAD ARE IN #stage-9-download-links-files IF YOU NEED FURTHER ASSISTANCE CONTACT A MODERATOR BY @ADMINS OR @OWNER.**""")
    
    elif "minecraft" in message.content.lower() or "roblox" in message.content.lower():
        if message.guild.name == "Harv & Kapps":
            await message.channel.send("""**PLEASE DONT USE FOBIDDEN LANGUAGE IN THIS DISCORD SERVER**""")

    elif "pls meme" == message.content.lower():
        memes = os.listdir('MEMES')
        upernum = len(memes)-1
        num = random.randint(0,upernum)
        file_name = ("memes/meme"+str(num)+".jpg")
        file = discord.File(file_name, filename = file_name)
        await message.channel.send("This is a meme", file = file)

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

    elif "!delete" in message.content and discord.utils.get(message.guild.roles, name= "Admins") in message.author.roles:
        messages_to_delete = int(message.content.split(" ")[1]) + 1
        messages = message.channel.history(limit= messages_to_delete)
        async for i in messages:
            message = i
            await message.delete()

client.run("NTAyMTg0OTA1NjA2OTU1MDA5.DrTsDg.gfd66dBd287Ofx8XSB70fptWrLM")