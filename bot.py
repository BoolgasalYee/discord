import asyncio
import discord
import sys
import io
import random
import youtube_dl
import os
from discord.utils import get
from discord.ext import commands

client = discord.Client()

# 생성된 토큰을 입력해준다.
token = "NzQwNTY5NDE4MTU2ODY3Njk0.Xyq7BA.cUqe2Co7P4lry-kVsQyyHLprjOE"

bot = commands.Bot(command_prefix='_')

# 봇이 구동되었을 때 보여지는 코드
@client.event
async def on_ready():
    print("다음으로 로그인합니다")
    print(client.user.name)
    print(client.user.id)
    print("================")

# 봇이 특정 메세지를 받고 인식하는 코드
@client.event
async def on_message(message):
    # 메세지를 보낸 사람이 봇일 경우 무시한다
    if message.author.bot:
        return None

    if message.content.startswith('!엄'):
        channel = message.channel 
        await channel.send('준')

    if message.content.startswith('!준'):
        channel = message.channel
        await channel.send('식')

    if message.content.startswith('!식'):
        channel = message.channel
        await channel.send('엄')

    if message.content.startswith('#~@@'):
        channel = message.channel
        await channel.send('~')
    
    if message.content.startswith('!대답'):
        channel = message.channel
        await channel.send('어딜 주인한테 대답해라 마라야')

    if message.content.startswith('!꼴받네'):
        channel = message.channel
        await channel.send('꼴받는다고요? 어쩌라구여~^^')

    if message.content.startswith('야 나두!'):
        embed = discord.Embed(title="야!", description="너두 할 수 있어", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://newsimg.sedaily.com/2020/06/04/1Z3WAC8B84_1.jpg")
        embed.set_footer(text="-J.S Jo-") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('!야'):
        embed = discord.Embed(title="꿀벌!", description="왜 울고있는거야", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://mblogthumb-phinf.pstatic.net/MjAxODA1MTdfMjg5/MDAxNTI2NTQ3NTYzMDIz.awWFb8WW9qSk85krQsWf7GXGOShPNS5ilZyVOFyrbIUg.07pMLGfgYvN_IQPPn9JLBRRvVE8yMY_xiN4LzuIfElEg.PNG.heekyun93/4c7a1d3932a211fa.png?type=w800")
        embed.set_footer(text="-そうなんだ~-") # 하단에 들어가는 조그마한 설명을 잡아줍니다
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.

    if message.content.startswith('삼성전자'):
        embed = discord.Embed(title="삼성전자 주가", description="떨어져라", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        
    if message.content.startswith('!승페'):
        embed = discord.Embed(title="지건", description="따악대!", color=0x62c1cc) # Embed의 기본 틀(색상, 메인 제목, 설명)을 잡아줍니다
        embed.set_image(url="https://cdn.discordapp.com/attachments/677020634437648418/819532485411078154/-3.gif")
        await message.channel.send(embed=embed) # embed를 포함 한 채로 메시지를 전송합니다.


    if message.content.startswith("!팀"):
        team = message.content[3:]
        peopleteam = team.split("/")
        people = peopleteam[0]
        team = peopleteam[1]
        person = people.split(" ")
        teamname = team.split(" ")
        random.shuffle(teamname)
        for i in range(0, len(person)):
            await message.channel.send(person[i] + "   ==   " + teamname[i])

client.run(token)