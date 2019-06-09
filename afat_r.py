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
    print('使用者ID: ' + str(bot.user.id))
    print('使用者全名: ' + str(bot.user))
    print('MentionID: ' + bot.user.mention)
    print('顯示名稱: ' + bot.user.display_name)
    global own
    own = await bot.application_info()
    own = own.owner
    print('擁有者: ' + str(own))
    print('指令前輟: ' + command_prefix)
    print(spline)
    print('邀請碼: ')
    print('https://discordapp.com/oauth2/authorize?client_id=' + str(bot.user.id) + '&scope=bot&permissions=8')
    print(spline)


@bot.command(description='pong!')
async def ping(ctx):

    import datetime
    now = datetime.datetime.now()
    timezone = datetime.timedelta(hours=8)
    delay = now - ctx.message.created_at - timezone
    delay = delay.total_seconds()
    delay = "%.3f" % float(str(delay))
    await ctx.send(str(float(delay)) + ' pong!')


@bot.event
async def on_message_delete(msg):
    if not msg.author.bot and not msg.content.startswith(command_prefix):
        import datetime
        now = datetime.datetime.now()
        timezone = datetime.timedelta(hours=8)
        delay = now - msg.created_at - timezone
        delay = delay.total_seconds()
        delay = "%.3f" % float(str(delay))
        if float(delay) < 15:
            embed = discord.Embed(description=msg.content, color=0xEE4BB5)
            embed.set_author(name=msg.author.display_name, icon_url=msg.author.avatar_url)
            for i, l in enumerate(msg.attachments):
                i += 1
                embed.add_field(name="圖 " + str(i), value=l['proxy_url'])
            await msg.channel.send(content='自刪俠 **{0}** 在 **{1}** 秒內自刪ㄌ！'.format(msg.author.mention, delay),
                                       embed=embed)


def permission_check(member, channel):
    permission = channel.permissions_for(member)
    return permission.administrator
    # permission_check(ctx.message.author, ctx.message.channel)


with open('token', 'r') as t:
    token = t.readline()
bot.run(token)
