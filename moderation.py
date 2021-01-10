import discord
import streamConstants
import datetime

async def blacklisted_word(message):

    msg = message.content.lower()
'''    
    with open("./resources/blacklist.txt") as fd:
        blacklist = fd.read().splitlines()
        length = len(blacklist)
        
        for i in range(length):
            if blacklist[i] in msg:
                with open("./logs/moderation_logs.log", "a") as f:
                    print("The following action was logged:", file=f)
                    print(message.author, file=f)
                    print(message.content, file=f)
                    '''print(datetime.now(), file=f)'''
                    print("Message was deleted, moderation action pending", file=f)
                    print("-----------------------------------------------------", file=f)
                    print('', file=f)
                    await message.delete()
                return 1
    return 0
'''
async def notif_toggle_on(message):
    server = message.guild

    if server.id != streamConstants.STREAM_GUILD:
        msg = "This command is for The Stream only. Exiting..."
        return msg
    
    await message.author.add_roles(server.get_role(streamConstants.SCREM_ROLE))
    msg = "Stream notifications enabled. Enjoy!~"
    return msg

async def notif_toggle_off(message):
    server = message.guild

    if server.id != streamConstants.STREAM_GUILD:
        msg = "This command is for The Stream only. Exiting..."
        return msg

    await message.author.remove_roles(server.get_role(streamConstants.SCREM_ROLE))
    msg = "Stream notifications disabled... Rude >:I"
    return msg
