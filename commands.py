import discord
import asyncio
import moderation
import streamConstants

from random import randint

cmd_list = ['!hewwo', '!owner', '!roll', '!voreme', '!commands', '!updates', '!screm', '!noscrem', '!dadjoke']

async def read_msg(message):
    msg = message.content.lower()
    call_check = msg[:9]
    if 'sesame' in msg:
        msg = await mention_msg(message)
        return msg

    if '!iamagoodboye' in msg:
        msg = await allow_access(message)
        return msg

    for elem in func_map:
        if elem in call_check:
            msg = await func_map[elem](message)

    return msg

async def allow_access(message):
    if message.guild.id != streamConstants.STREAM_GUILD:
        msg = "I'm sorry, but this command can only be used in 'The Stream' server!"
        return msg
    
    role = message.guild.get_role(streamConstants.SWIM_ROLE)
    await message.delete()
    msg = f"{message.author.mention} has agreed to follow the rules and regulations of The Stream. Enjoy your swim~!"
    await message.author.add_roles(role)
    role = message.guild.get_role(streamConstants.SCREM_ROLE)
    await message.author.add_roles(role)

    return msg

async def roll(message):
    msg = message.content
    side = msg[6:] 

    if side.isnumeric():
        side = int(side)
        result = randint(1, side)
        msg = "BBTBTBBTBTBTBT (That's the sound a die makes)!!! You rolled a " + str(result) + "!"
    else:
        msg = "Seems you've overcooked your command! Try using '!roll [number]' to roll a die of [number] sides!"
    
    return msg

async def mention_msg(message):

    with open("./resources/quotes.txt", "r") as f:
        quote_list = f.readlines()
        num_lines = len(quote_list)

        resp_index = randint(0, num_lines - 1)  
    return quote_list[resp_index]

async def dadjokes_msg(message):

    with open("./resources/dadjokes.txt", "r") as f:
        quote_list = f.readlines()
        num_lines = len(quote_list)

        resp_index = randint(0, num_lines - 1)
    return quote_list[resp_index]

async def cmd_msg(message):
    msg = 'My commands are: '

    for x in cmd_list:
        msg = msg + ' ' + x

    return msg

async def hewwo_msg(message):
    msg = """\n
    rawr x3 nuzzles pounces on u uwu u so warm.
    couldn't help but ur bulge from across the floor,
    nuzzlez yo' necky~ murr~ hehe
    unzips yo baggy ass pants,
    oof baby u so musky
   
    take me home, pet me, N' make me yours
    & dont forget to stuff me!
    see me wag my widdle baby tail,
    all for your bolgy-wolgy!
    
    kisses n lickies yo neck,
    i hope daddy likeies
    nuzzles n wuzzles yo chest,
    i be gettin thirsty
    """
    
    return msg

async def vore_msg(message):
    msg = "I put {0.author.mention} between my greasy, well toasted buns and chomp down hard uwu~".format(message)
    return msg

async def own_msg(message):
    msg = "Labraderpy is my chef owo~ Find him at https://twitter.com/labraderpy"
    return msg

async def patch_msg(message):
    msg = """
    Follow the development at https://t.me/sesameburgal

    Sesame is Version 0.4

    Patch Notes:
    - Optimization in handling roles for "The Stream" guild
    - Optimization for command usages
    - func_map implementation cleaned up

    Upcoming Features:
    - Automatic role assignment for Subscribers (The Stream only)
    - Moderation log split based on server (Currently just one thicc log)
    """

    return msg

func_map = {"sesame": mention_msg,
            "!hewwo": hewwo_msg,
            "!voreme": vore_msg,
            "!commands": cmd_msg,
            "!owner": own_msg,
            "!roll": roll,
            "!updates": patch_msg,
            "!dadjoke": dadjokes_msg,
            "!screm": moderation.notif_toggle_on,
            "!noscrem": moderation.notif_toggle_off}
