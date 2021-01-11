import discord
import asyncio
import commands
import moderation
import streamConstants
import time
import os

intents = discord.Intents.all()
client = discord.Client(intents=intents)

INSTALL_DIR = str(os.getcwd())

async def create_log_dirs():
    log_wd = INSTALL_DIR + '/logs/'
    print("Time to set up the localized files!")

    print("Creating directory in %s" % INSTALL_DIR)
    os.system("mkdir ./logs")

    print("Creating moderation_logs.txt in %s" % log_wd)
    os.system("touch ./logs/moderation_logs.txt")

    print("Creating init_logs.txt in %s" % log_wd)
    os.system("touch ./logs/init_logs.txt")
    return

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    
    if await moderation.blacklisted_word(message) == 1:
        return

    if(message.content.startswith('!', 0, 1)) or 'sesame' in message.content.lower():
        msg = await commands.read_msg(message) 
        if msg == message.content.lower():
            return
        await message.channel.send(msg)

    return
        
@client.event
async def on_ready():
    await create_log_dirs()
    os.chdir(INSTALL_DIR)

    with open("./logs/init_logs.txt", "w") as f:        
        f.write('Logged in as %s' % client.user.name)
        f.write('\n------------------------------')
    return

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

with open("/home/pi/bot_token.txt") as fd:
    print("Running token for testbed_sesame\n")
    token = fd.read()
    client.run(token)
