#!/usr/bin/python3.6
# coding=utf-8

import discord
from discord.ext import commands
import random

command_prefix = 'r>'
description = '阿肥重返榮耀，**阿肥Return**'
bot = commands.Bot(command_prefix=command_prefix, description=description)

global spline
spline = '-' * 80


@bot.event
async def on_ready():
    print('已登入Discord為: ')
    print('使用者名稱: ' + bot.user.name)
    print('使用者ID: ' + bot.user.id)
    print('使用者全名: ' + str(bot.user))
    print('MentionID: ' + bot.user.mention)
    print('顯示名稱: ' + bot.user.display_name)
    global own
    own = await disbot.application_info()
    own = own.owner
    print('擁有者: ' + str(own))
    print(spline)
    print('邀請碼: ')
    print('https://discordapp.com/oauth2/authorize?client_id=' + disbot.user.id + '&scope=bot&permissions=8')
    print(spline)
    print('指令: ' + command_prefix)


@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

@bot.command(description='pong!')
async def ping(ctx):
    """Chooses between multiple choices."""
    await ctx.send('pong!')

bot.run('token')