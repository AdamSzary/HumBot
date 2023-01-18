import os
import discord
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
import requests
import json

intents = discord.Intents.all()

client = commands.Bot(command_prefix='.',intents=intents)

@client.event
async def on_ready():
    print('Podłączono do Discorda')

@client.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()

@client.command()
async def play(ctx, url):
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True'}
    FFMPEG_OPTIONS = {
        'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    voice = get(client.voice_clients, guild=ctx.guild)

    #Playing
    if not voice.is_playing():
        with YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['url']
        voice.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice.is_playing()
        await ctx.send('Bot is playing')


    else:
        await ctx.send("Bot is aleready playing")

@client.command()
async def emote(ctx, cat, usr):

    if cat in ['help']:
        await ctx.send('bully, cuddle, cry, hug, kiss, lick, pat, bonk, yeet, blush, smile, wave, handhold, handhold, nom, bite, glomp, slap, kill, kick, happy, wink, poke, dance, cringe')

    if cat in ['bully']:
        response = requests.get('https://api.waifu.pics/sfw/bully')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is bullying {usr}')
        await ctx.send(json["url"])

    if cat in ['cuddle']:
        response = requests.get('https://api.waifu.pics/sfw/cuddle')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is hugging {usr}')
        await ctx.send(json["url"])

    if cat in ['cry']:
        response = requests.get('https://api.waifu.pics/sfw/cry')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is crying')
        await ctx.send(json["url"])

    if cat in ['hug']:
        response = requests.get('https://api.waifu.pics/sfw/hug')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is hugging {usr}')
        await ctx.send(json["url"])

    if cat in ['kiss']:
        response = requests.get('https://api.waifu.pics/sfw/kiss')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} kissed {usr}')
        await ctx.send(json["url"])

    if cat in ['lick']:
        response = requests.get('https://api.waifu.pics/sfw/lick')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} licked {usr}')
        await ctx.send(json["url"])

    if cat in ['pat']:
        response = requests.get('https://api.waifu.pics/sfw/pat')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} patted {usr}')
        await ctx.send(json["url"])

    if cat in ['bonk']:
        response = requests.get('https://api.waifu.pics/sfw/bonk')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} have hitted {usr}')
        await ctx.send(json["url"])

    if cat in ['yeet']:
        response = requests.get('https://api.waifu.pics/sfw/yeet')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} have threw {usr}')
        await ctx.send(json["url"])

    if cat in ['blush']:
        response = requests.get('https://api.waifu.pics/sfw/blush')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} has blushed')
        await ctx.send(json["url"])

    if cat in ['smile']:
        response = requests.get('https://api.waifu.pics/sfw/smile')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is smiling')
        await ctx.send(json["url"])

    if cat in ['wave']:
        response = requests.get('https://api.waifu.pics/sfw/wave')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is waving to {usr}')
        await ctx.send(json["url"])

    if cat in ['highfive']:
        response = requests.get('https://api.waifu.pics/sfw/highfive')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} gave {usr} a high five')
        await ctx.send(json["url"])

    if cat in ['handhold']:
        response = requests.get('https://api.waifu.pics/sfw/handhold')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is hand holding {usr}')
        await ctx.send(json["url"])

    if cat in ['nom']:
        response = requests.get('https://api.waifu.pics/sfw/nom')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['bite']:
        response = requests.get('https://api.waifu.pics/sfw/bite')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is bitting {usr}')
        await ctx.send(json["url"])

    if cat in ['glomp']:
        response = requests.get('https://api.waifu.pics/sfw/glomp')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is hugging {usr} very hard')
        await ctx.send(json["url"])

    if cat in ['slap']:
        response = requests.get('https://api.waifu.pics/sfw/slap')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} slapped {usr}')
        await ctx.send(json["url"])

    if cat in ['kill']:
        response = requests.get('https://api.waifu.pics/sfw/kill')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} have killed {usr}')
        await ctx.send(json["url"])

    if cat in ['kick']:
        response = requests.get('https://api.waifu.pics/sfw/kick')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} have kicked {usr}')
        await ctx.send(json["url"])

    if cat in ['happy']:
        response = requests.get('https://api.waifu.pics/sfw/happy')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} have is happy')
        await ctx.send(json["url"])

    if cat in ['wink']:
        response = requests.get('https://api.waifu.pics/sfw/wink')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is winking to {usr}')
        await ctx.send(json["url"])

    if cat in ['poke']:
        response = requests.get('https://api.waifu.pics/sfw/poke')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is poking {usr}')
        await ctx.send(json["url"])

    if cat in ['dance']:
        response = requests.get('https://api.waifu.pics/sfw/dance')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is dancing with {usr}')
        await ctx.send(json["url"])

    if cat in ['cringe']:
        response = requests.get('https://api.waifu.pics/sfw/cringe')
        json = response.json()
        aut = ctx.message.author.mention
        await ctx.send(f'{aut} is embarassed with {usr}')
        await ctx.send(json["url"])


@client.command()
async def waifu(ctx, cat):

    if cat in ['waifu']:
        response = requests.get('https://api.waifu.pics/sfw/waifu')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['neko']:
        response = requests.get('https://api.waifu.pics/sfw/neko')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['shinobu']:
        response = requests.get('https://api.waifu.pics/sfw/shinobu')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['megumin']:
        response = requests.get('https://api.waifu.pics/sfw/megumin')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['awoo']:
        response = requests.get('https://api.waifu.pics/sfw/awoo')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['help']:
        await ctx.send('waifu, awoo, neko, shinobu, megumin, awoo')

@client.command()
async def nswaifu(ctx, cat):
    if cat in ['waifu']:
        response = requests.get('https://api.waifu.pics/nsfw/waifu')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['neko']:
        response = requests.get('https://api.waifu.pics/nsfw/neko')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['trap']:
        response = requests.get('https://api.waifu.pics/nsfw/trap')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['blowjob']:
        response = requests.get('https://api.waifu.pics/nsfw/trap')
        json = response.json()
        await ctx.send(json["url"])

    if cat in ['help']:
        await ctx.send('waifu, neko, trap, blowjob')

@client.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()

client.run('Token Here')
