##Configuration
token = ''

minecraft_rcon_host = ''
minecraft_rcon_port = ''
minecraft_rcon_password = ''

import os
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import requests
import json
import time
from rcon.source import rcon

intents = discord.Intents.all()

client = commands.Bot(command_prefix='#',intents=intents)

@client.event
async def on_ready():
    print('Connected to Discord')

## Music commands

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def stop(ctx):
    voice = get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send("OK")

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')

    else:
        await ctx.send("Bot is aleready playing")

## Emote commands

@client.command()
async def emote(ctx, cat, usr):

    aut = ctx.message.author.mention

    match (cat):
        case 'help':
            await ctx.send('bully, cuddle, cry, hug, kiss, lick, pat, bonk, yeet, blush, smile, wave, handhold, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe')
        case 'bully':
            response = requests.get('https://api.waifu.pics/sfw/bully')
            json = response.json()
            await ctx.send(f'{aut} is bullying {usr}')
            await ctx.send(json["url"])

        case 'cuddle':
            response = requests.get('https://api.waifu.pics/sfw/cuddle')
            json = response.json()
            await ctx.send(f'{aut} is hugging {usr}')
            await ctx.send(json["url"])

        case 'cry':
            response = requests.get('https://api.waifu.pics/sfw/cry')
            json = response.json()
            await ctx.send(f'{aut} is crying')
            await ctx.send(json["url"])

        case 'hug':
            response = requests.get('https://api.waifu.pics/sfw/hug')
            json = response.json()
            await ctx.send(f'{aut} is hugging {usr}')
            await ctx.send(json["url"])

        case 'kiss':
            response = requests.get('https://api.waifu.pics/sfw/kiss')
            json = response.json()
            await ctx.send(f'{aut} kissed {usr}')
            await ctx.send(json["url"])

        case 'lick':
            response = requests.get('https://api.waifu.pics/sfw/lick')
            json = response.json()
            await ctx.send(f'{aut} licked {usr}')
            await ctx.send(json["url"])

        case 'pat':
            response = requests.get('https://api.waifu.pics/sfw/pat')
            json = response.json()
            await ctx.send(f'{aut} patted {usr}')
            await ctx.send(json["url"])

        case 'bonk':
            response = requests.get('https://api.waifu.pics/sfw/bonk')
            json = response.json()
            await ctx.send(f'{aut} have hitted {usr}')
            await ctx.send(json["url"])

        case 'yeet':
            response = requests.get('https://api.waifu.pics/sfw/yeet')
            json = response.json()
            await ctx.send(f'{aut} have threw {usr}')
            await ctx.send(json["url"])

        case 'blush':
            response = requests.get('https://api.waifu.pics/sfw/blush')
            json = response.json()
            await ctx.send(f'{aut} has blushed')
            await ctx.send(json["url"])

        case 'smile':
            response = requests.get('https://api.waifu.pics/sfw/smile')
            json = response.json()
            await ctx.send(f'{aut} is smiling')
            await ctx.send(json["url"])
        
        case 'wave':
            response = requests.get('https://api.waifu.pics/sfw/wave')
            json = response.json()
            await ctx.send(f'{aut} is waving to {usr}')
            await ctx.send(json["url"])

        case 'highfive':
            response = requests.get('https://api.waifu.pics/sfw/highfive')
            json = response.json()
            await ctx.send(f'{aut} gave {usr} a high five')
            await ctx.send(json["url"])

        case 'handhold':
            response = requests.get('https://api.waifu.pics/sfw/handhold')
            json = response.json()
            await ctx.send(f'{aut} is hand holding {usr}')
            await ctx.send(json["url"])

        case 'nom':
            response = requests.get('https://api.waifu.pics/sfw/nom')
            json = response.json()
            await ctx.send(json["url"])

        case 'bite':
            response = requests.get('https://api.waifu.pics/sfw/bite')
            json = response.json()
            await ctx.send(f'{aut} is bitting {usr}')
            await ctx.send(json["url"])

        case 'glomp':
            response = requests.get('https://api.waifu.pics/sfw/glomp')
            json = response.json()
            await ctx.send(f'{aut} is hugging {usr} very hard')
            await ctx.send(json["url"])

        case 'slap':
            response = requests.get('https://api.waifu.pics/sfw/slap')
            json = response.json()
            await ctx.send(f'{aut} slapped {usr}')
            await ctx.send(json["url"])

        case 'kill':    
            response = requests.get('https://api.waifu.pics/sfw/kill')
            json = response.json()
            await ctx.send(f'{aut} have killed {usr}')
            await ctx.send(json["url"])

        case 'kick':    
            response = requests.get('https://api.waifu.pics/sfw/kick')
            json = response.json()
            await ctx.send(f'{aut} have kicked {usr}')
            await ctx.send(json["url"])

        case 'happy':
            response = requests.get('https://api.waifu.pics/sfw/happy')
            json = response.json()
            await ctx.send(f'{aut} have is happy')
            await ctx.send(json["url"])

        case 'wink':
            response = requests.get('https://api.waifu.pics/sfw/wink')
            json = response.json()
            await ctx.send(f'{aut} is winking to {usr}')
            await ctx.send(json["url"])

        case 'poke':
            response = requests.get('https://api.waifu.pics/sfw/poke')
            json = response.json()
            await ctx.send(f'{aut} is poking {usr}')
            await ctx.send(json["url"])

        case 'dance':
            response = requests.get('https://api.waifu.pics/sfw/dance')
            json = response.json()
            await ctx.send(f'{aut} is dancing with {usr}')
            await ctx.send(json["url"])

        case 'cringe':
            response = requests.get('https://api.waifu.pics/sfw/cringe')
            json = response.json()
            await ctx.send(f'{aut} is embarassed with {usr}')
            await ctx.send(json["url"])

@client.command()
async def waifu(ctx, cat):

    

    match (cat):
        case 'help':
            await ctx.send('waifu, awoo, neko, shinobu, megumin, awoo')

        case 'waifu':
            response = requests.get('https://api.waifu.pics/sfw/waifu')
            json = response.json()
            await ctx.send(json["url"])

        case 'neko':
            response = requests.get('https://api.waifu.pics/sfw/neko')
            json = response.json()
            await ctx.send(json["url"])

        case 'shinobu':
            response = requests.get('https://api.waifu.pics/sfw/shinobu')
            json = response.json()
            await ctx.send(json["url"])

        case 'megumin':
            response = requests.get('https://api.waifu.pics/sfw/megumin')
            json = response.json()
            await ctx.send(json["url"])

        case 'awoo':
            response = requests.get('https://api.waifu.pics/sfw/awoo')
            json = response.json()
            await ctx.send(json["url"])
        
@client.command()
async def nswaifu(ctx, cat):

    json = requests.json()

    match (cat):
        case 'help':
            await ctx.send('waifu, neko, trap, blowjob')

        case 'waifu':
            response = requests.get('https://api.waifu.pics/nsfw/waifu')
            json = response.json()
            await ctx.send(json["url"])

        case 'neko':
            response = requests.get('https://api.waifu.pics/nsfw/neko')
            json = response.json()
            await ctx.send(json["url"])

        case 'trap':
            response = requests.get('https://api.waifu.pics/nsfw/trap')
            json = response.json()
            await ctx.send(json["url"])

        case 'blowjob':
            response = requests.get('https://api.waifu.pics/nsfw/trap')
            json = response.json()
            await ctx.send(json["url"])

##Minecraft RCON commands

@client.command()
async def mc(ctx, com):
    
    match(com):
        case 'players':
            response = await rcon(
                'list',
                host=minecraft_rcon_host, port=minecraft_rcon_port, passwd=minecraft_rcon_password
            )
            await ctx.send(response)
        
        case 'tps':
            response = await rcon(
                'debug', 'start',
                host=minecraft_rcon_host, port=minecraft_rcon_port, passwd=minecraft_rcon_password
            )
            await ctx.send(response)
            await ctx.send('Please wait for 10 seconds')
            time.sleep(10)
            response = await rcon(
                'debug', 'stop',
                host=minecraft_rcon_host, port=minecraft_rcon_port, passwd=minecraft_rcon_password
            )
            await ctx.send(response)
            

client.run(bot_token)
