# sniper.py
import discord
from discord.ext import commands
import random
import asyncio
import os
import subprocess
import logging

command_prefix='+'
bot = commands.Bot(command_prefix)
description = 'sniper.py, coded by unpredictable'
 
@bot.event
async def on_message(message):
    if message.content.startswith('+snipeadd'):
            embed = discord.Embed(title="Let's walk you through the process of queueing a snipe.", description="DM the bot with 'beginqueue' to queue your snipe.", colour=0x1a94f0)
            embed.set_author(name="Thanks for choosing sniper.py!", icon_url="")
            embed.add_field(name="Enjoy your new name!", value="-trinity and iliyan")
            embed.set_footer(text="sniper.py™ © coded by unpredictable")
            await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('+help'):
        embed=discord.Embed(title="+snipeadd: queues a snipe", description="+invite: Prints an invite link for the bot.", color=0x1a94f0)
        embed.set_author(name='Commands', icon_url="")
        embed.add_field(name="+help: Brings up list of commands", value="+info: Prints info about the bot.", inline=True)
        embed.set_footer(text='coded by unpredictable')
        await bot.send_message(message.channel, embed=embed)

    if message.content.startswith('+invite'):
        await bot.send_message(message.channel, "**Here's the invite for the bot:** INVITE")
        print('Bot has been added to new server')

    if message.content.startswith('?tag twitter'):
        await bot.send_message(message.channel, "https://twitter.com/PaintToolApp")

async def status_task():
    while True:
        await bot.change_presence(game=discord.Game(name="with og names"))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="+help | coded by ili"))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="with my sniper"))
        await asyncio.sleep(10)
        await bot.change_presence(game=discord.Game(name="with a fidget spinner"))
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print('sniper.py coded by unpredictable')
    print('------')
    print('INFO')
    print('------')
    print('Logged in as: ' + bot.user.name + ', ' + bot.user.id)
    print('------')

client.run(os.getenv('TOKEN'))
