#################################################################
#                             _`				                #
#                          _ooOoo_				                #
#                         o8888888o				                #
#                         88" . "88				                #
#                         (| -_- |)				                #
#                         O\  =  /O				                #
#                      ____/`---'\____				            #
#                    .'  \\|     |//  `.			            #
#                   /  \\|||  :  |||//  \			            #
#                  /  _||||| -:- |||||_  \			            #
#                  |   | \\\  -  /'| |   |			            #
#                  | \_|  `\`---'//  |_/ |			            #
#                  \  .-\__ `-. -'__/-.  /			            #
#                ___`. .'  /--.--\  `. .'___			        #
#             ."" '<  `.___\_<|>_/___.' _> \"".			        #
#            | | :  `- \`. ;`. _/; .'/ /  .' ; |		        #
#            \  \ `-.   \_\_`. _.'_/_/  -' _.' /		        #
#=============`-.`___`-.__\ \___  /__.-'_.'_.-'=================#
#                           `=--=-'                          


import discord
from discord.utils import sleep_until
import requests
import asyncio
import random
import sys
from discord import channel
from discord.ext import commands
from friday_image import friday_image
response = requests.get('https://api.apify.com/v2/key-value-stores/ZsOpZgeg7dFS1rgfM/records/LATEST?utm_source=j2team&utm_medium=url_shortener')
data = response.json()
Bot = commands.Bot(command_prefix = '/')
Bot.add_cog(friday_image(Bot))


@Bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(Bot))

@Bot.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == Bot.user:
        return
    
    if message.channel.name == 'zoo' or message.channel.name == 'code' or message.channel.name == 'math' or message.channel.name == 'test-bot':
        if 'hello' in user_message.lower():
            await message.channel.send(f'Hello {username}!')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif 'dcm' in user_message.lower():
            await message.channel.send(f'djtmemay {username}!')
            return
        elif user_message.lower() == 'vjp':
            await message.channel.send(f'```{username}pr0vjp```')
            return
        elif user_message.lower() == '!hcm':
            tpHCM = f'```Detail: {data["detail"][0]["name"]} \nDeath: {data["detail"][0]["death"]} \nCases: {data["detail"][0]["cases"]} \nCases Today: {data["detail"][0]["casesToday"]}```'
            await message.channel.send(tpHCM)
            return
        elif '!vp' in  user_message.lower():
            vinhphuc = f'```Detail: {data["detail"][46]["name"]} \nDeath: {data["detail"][46]["death"]} \nCases: {data["detail"][46]["cases"]} \nCases Today: {data["detail"][46]["casesToday"]}```'
            await message.channel.send(vinhphuc)
            return
        elif user_message.lower() == '!hanoi':
            hanoi = f'`Detail: {data["detail"][13]["name"]} \nDeath: {data["detail"][13]["death"]} \nCases: {data["detail"][13]["cases"]} \nCases Today: {data["detail"][13]["casesToday"]}`'
            await message.channel.send(hanoi)
            return
        elif user_message.lower() == 'exit@':
            exit = "```Goodbye sir! \nBot is offline```"
            await message.channel.send(exit)
            sys.exit()
        elif user_message.lower() == '!fe':
            fe = f'```PRF192      06/11/2021      12h50-14h20      PE      \nCSI104      17/11/2021      07h30-09h00      FE      \nPRF192      18/11/2021      16h10-17h40      FE      \nMAE101      19/11/2021      07h30-09h00      FE      \nCEA201      20/11/2021      09h10-10h40      FE      ```'
            await message.channel.send(fe)
            return
        elif user_message.lower() == '!random':
            response = f'`This is your random number: {random.randrange(4)}`'
            await message.channel.send(response)
            return

@Bot.command()
async def rep(ctx, *args):
    m_args = " ".join(args)
    await ctx.send(m_args)

# @Bot.command(aliases=['paly', 'queue', 'que'])
# async def play(ctx):
#     guild = ctx.guild
#     voice_client: discord.VoiceClient = discord.utils.get(Bot.voice_clients, guild=guild)
#     audio_source = discord.FFmpegPCMAudio('Buc-Tranh-Tu-Nuoc-Mat-Mr-Siro.mp3')
#     if not voice_client.is_playing():
#         voice_client.play(audio_source, after=None)

# @Bot.command(name="play")
# async def play(ctx):
#     # Gets voice channel of message author
#     voice_channel = ctx.author.channel
#     channel = None
#     if voice_channel != None:
#         channel = voice_channel.name
#         vc = await voice_channel.connect()
#         vc.play(discord.FFmpegPCMAudio(executable="C:/Users/leduc/Documents/Coding/LearnPython/BOT/ffmpeg/bin/ffmpeg.exe", source=r"C:/Users/leduc/Music"))
#         # Sleep while audio is playing.
#         while vc.is_playing():
#             sleep_until(.1)
#         await vc.disconnect()
#     else:
#         await ctx.send(str(ctx.author.name) + "is not in a channel.")
#     # Delete command after the audio is done playing.
#     await ctx.message.delete()




token = ""
with open("token.txt") as file:
    token = file.read()
Bot.run(token)

