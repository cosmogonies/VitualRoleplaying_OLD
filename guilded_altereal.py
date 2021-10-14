import guilded
from guilded.ext import commands
import random

import os, sys
import pprint

import guilded.channel

# Several snippets developed to manage a larp massive server on guilded.
# API under MIT Licence by shayypy:
# https://github.com/shayypy/guilded.py/blob/master/guilded/client.py

description = '''An example bot to showcase the guilded.ext.commands extension
module, as well as to furthermore demonstrate the similarities between
guilded.py and discord.py.'''

bot = commands.Bot(command_prefix='?', description=description)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


#======================================================================================

@bot.command()
async def test(ctx, poolSize: int, difficulty=6):
    """Lancer de dés pour déterminer action à issu incertaine."""
    success = 0
    detailsFormated = "("
    result = ""

    pool = []
    for i in range(poolSize):
        pool.append(random.randint(1, 10)) # both included
    pool = sorted(pool)
    for diceRoll in pool:
        if diceRoll == 1:
            success = success - 1
            #detailsFormated +=  " 1 "
            detailsFormated +=  " :1fumble: "
        elif diceRoll >= difficulty:
            success = success + 1
            detailsFormated +=  " **"+str(diceRoll)+"** "
        else:
            detailsFormated+= str(diceRoll)
        detailsFormated+=","
    detailsFormated =detailsFormated[:-1] #removing last ","
    detailsFormated+=")"

    if(success==0):
        result = "Résultat: échec... "+detailsFormated
    elif(success<0):
        result = "Résultat: **ECHEC CRITIQUE** !!! "+detailsFormated
    else:
        result = "Résultat: "+str(success)+ " succès ! "+detailsFormated

    await ctx.send(result)


#gon's own command
@bot.command()
async def backupChannel(ctx, channelName='Charte'):
    """Backup a channel."""
    import guilded.team
    import guilded.client
    #pprint.pprint(guilded.team.Team)
    #pprint.pprint(dir(guilded.team.Team))

    pprint.pprint(dir(guilded.team.Team.channels))

    #pprint.pprint("len(guilded.team.Team.channels)=")
    #pprint.pprint(len(guilded.team.Team.channels))

    #pprint.pprint("help(guilded.team.Team.channels('Charte')=")
    #pprint.pprint(help(guilded.team.Team.channels('Charte')))

    #myChannel = guilded.team.Team.channels
    #pprint.pprint(myChannel)


    text_channel_list = []
    for server in guilded.client.Client.teams:
        for channel in server.channels:
            if str(channel.type) == 'text':
                text_channel_list.append(channel)
    print("found "+str(len(text_channel_list) +" lists."))


    #guilded.team.Team.create_chat_channel(name="Michel")
    #newChannel = guilded.channel.ChatChannel(state=guilded.channel.ChannelType.forum ,name="Suivi", message="placeHolder")
    await ctx.send("channels created (name="+str(channelName)+")")



@bot.command()
async def createForum(ctx, forumName='forumName'):
    """Create all forum/topics required for a newly character."""
    import guilded.team
    #pprint.pprint(guilded.team.Team)
    #pprint.pprint(dir(guilded.team.Team))

    #pprint.pprint(dir(guilded.team.Team.channels))
    #guilded.team.Team().create_forum_channel(name="forumName")
    #toto = guilded.team.Team()
    #guilded.team.Team().create_forum_channel(name="forumName")
    guilded.team.Team.create_forum_channel(name="forumName")

    #guilded.team.Team.create_chat_channel(name="Michel")
    #newChannel = guilded.channel.ChatChannel(state=guilded.channel.ChannelType.forum ,name="Suivi", message="placeHolder")
    await ctx.send("channels created (name="+str(forumName)+")")





bot.run('email', 'password')
