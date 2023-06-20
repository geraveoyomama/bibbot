#!/usr/bin/env python
# main.py

import discord
from discord.ext import commands
from wakeonlan import send_magic_packet
import urllib
from urllib import parse, request

bot = commands.Bot(command_prefix='>', description="This is a bot to wake sleeping silicon.", intents=discord.Intents.all(), case_insensitive=True)

@bot.command()
async def clients(ctx):
    await ctx.send('client BIB online')

@bot.command()
async def start(ctx):
    #starts SE:Dedicated server using wakeonlan
    if isinstance(ctx.channel, discord.DMChannel) and ctx.author.id != OWNER_ID:
        return
    else:
        send_magic_packet(MAC_WAKE)
        print("Magic packets sent.")
    await ctx.send('Magic packets sent.')

@bot.command()
async def startPriv(ctx):
    if ctx.author.id != OWNER_ID:
        return
    else:
        send_magic_packet(MAC_WAKE)
    return

@bot.command()
async def ip(ctx):
    if isinstance(ctx.channel, discord.DMChannel) and ctx.author.id != OWNER_ID:
        return
    else:
        uf = urllib.request.urlopen('https://api.ipify.org/').read().decode('utf-8')
    await ctx.send(uf+":27016")

MAC_WAKE='A0.B1.C3.D4.E5.F6'
MAC_WAKE_PRIV='A0.B1.C3.D4.E5.F6'
OWNER_ID=
bot.run('TOKEN')
