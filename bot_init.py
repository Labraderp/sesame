import discord
import asyncio
import commands
import moderation
import streamConstants
import time

from importlib import reload

TOKEN = 'MjUzNzI5OTc1MTU1Mjk0MjA4.WD-edA.InrA0Xo_Q-6MMC_ML0rLeIf4J_4'
intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if await moderation.blacklisted_word(message) == 1:
        return
    
    if(message.content.startswith('!', 0, 1)) or 'sesame' in message.content.lower():
        reload(commands)
        msg = await commands.read_msg(message) 
        if msg == message.content.lower():
            return
        
        await message.channel.send(msg)
        with open("./logs/init_logs.log", "a") as f:
            print(message.author, file=f)
            print(message.content, file=f)
            print(message.channel, file=f)
            print('------------------------------', file=f)
            print('',file=f)
        return

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------------------------------')
    print()

@client.event
async def on_member_join(member):
    if member.guild.id != streamConstants.STREAM_GUILD:
        return

    chnl = member.guild.get_channel(streamConstants.KP_CHANNEL)
    rules = member.guild.get_channel(streamConstants.RULES_CHANNEL)

    msg = f"Welcome, {member.mention}! Please take a moment to read {rules.mention}. Use the command found inside to gain access to the rest of the server. Thanks for joining The Stream and I hope that you have a fantastic swim~"
    
    time.sleep(3)

    await chnl.send(msg)
    return

@client.event
async def on_member_update(member_old, member_new):
    if member_old.guild.id != streamConstants.STREAM_GUILD or member_old.guild.id != streamConstants.TEST_GUILD:
        return

    if 'Twitch Subscriber' in member_new.roles:
        await member_new.add_roles(server.get_role(streamConstants.SUB_ROLE))
    elif 'Twitch Subscriber' not in member_new.roles and 'Doggy Paddler' in member_new.roles:
        await member_new.remove_roles(server.get_role(streamConstants.SUB_ROLE))
    return

with open("/home/labraderp/bot_token.txt") as fd:
    token = fd.read()
    client.run(token)
