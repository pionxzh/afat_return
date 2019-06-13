#!/usr/bin/python3.6
# coding=utf-8

import re
import discord
import datetime
from discord.ext import commands

# package import
from package.fake_quote import fakequote

command_prefix = 'r>'
description = '阿肥重返榮耀，阿肥Return！'
bot = commands.Bot(command_prefix=command_prefix, description=description)

global spline
spline = '-' * 80  # 分隔線


@bot.event  # 初始預備
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

@bot.command(description='假造文字截圖')
async def fake(ctx, member: discord.Member, *, content):
    # user = discord.utils.get(bot.get_all_members(), mention=member)  # 尋找該member

    # handle user-mention
    mentions = ctx.message.mentions
    for user in mentions:
        #USERS_PATTERN = re.compile(r'/<@!?(\d{17,19})>/g')
        USERS_PATTERN = re.compile(r'<@!?{0}>'.format(user.id))
        content = re.sub(USERS_PATTERN, r'$-${0}$-$'.format(user.nick), content)

    time = datetime.datetime.now().strftime('%I{0}%M{1}').format('點', '分').strip('0')
    if datetime.datetime.now().strftime('%p') == 'AM':
        noon = '今天上午'
    else:
        noon = '今天晚上'
    avatar_url = str(member.avatar_url).replace('webp?size=1024', 'png')
    color = member.colour
    if str(color) == '#000000':  # 如果無設定顏色，discord.colour返回值0
        color = '#dcddde'  # 預設白
    result = fakequote.fq(avatar_url, member.display_name, noon + time, content, color=color)
    await ctx.send(file=discord.File(result))


@bot.command(description='pong!')  # 查看延遲
async def ping(ctx):
    now = datetime.datetime.now()
    timezone = datetime.timedelta(hours=8)
    delay = now - ctx.message.created_at - timezone
    delay = delay.total_seconds()
    delay = '{:.0f}'.format(float(str((delay+1)*1000)))
    await ctx.send('`' + str(delay) + 'ms` Pong!')


prefix_whitelist = ('r>', '><', '>', '.', '!')  # str.startswith()接受tuple

@bot.event
async def on_message_delete(msg):
    if not msg.author.bot and not msg.content.startswith(prefix_whitelist):  # 排除以指令前輟開頭及機器人的訊息
        # 自刪俠
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


def permission_check(member, channel):   # 檢查權限
    permission = channel.permissions_for(member)
    return permission.administrator
    # permission_check(ctx.message.author, ctx.message.channel)


if __name__ == '__main__':  # 開啟bot
    with open('token', 'r') as t:
        token = t.readline()
    bot.run(token)
