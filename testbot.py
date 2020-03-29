import discord
import asyncio
from captcha.image import ImageCaptcha
import random
import re
import openpyxl
import datetime
import requests
import openpyxl
from json import loads
from discord.ext import tasks
import urllib
import urllib.request
import bs4
import os
from urllib.request import urlopen, Request
import json



game = discord.Game("test")


client = discord.Client()



@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    print('작동을 시작합니다')
    print(client.user.name)
    print(client.user.id)
    user =  len(client.users)
    server = len(client.guilds)
    
    messages = ["test","열공","생각","아무생각",f"{user}명의 사람들과 함께","%봇소개",f'{server}개의 서버와 함께']
    while True:
       await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=messages[0], type=discord.ActivityType.playing))
       messages.append(messages.pop(0))
       await asyncio.sleep(7)



queues={}
musiclist=[]






        
    


@client.event
async def on_message(message):
    
    if message.author.bot:
        return None
    
    
    if message.content.startswith("%잘가"):
        await message.channel.send("ㅃ2")

    if message.content.startswith("%같이"):
        await message.channel.send("저도요?")

    if message.content.startswith("%아니"):
        await message.channel.send("네.....")

    if message.content.startswith("%와"):
        await message.channel.send("샌즈")

    if message.content.startswith("%와"):
        await message.channel.send("샌즈")

    if message.content.startswith(";;"):
        await message.channel.send("아 그건 좀....")
    
    if message.content.startswith("쌋다"):
        await message.channel.send("저는 로봇이라 그런게 없네요")

    if message.content.startswith("%우린아"):
        await message.channel.send("제가 우린님 대신 말씀 드릴게요")
        await message.channel.send("보낼것 라고 말씀 후 말할 내용을 적어주세요")
    if message.content.startswith("보낼것"):
        send = message.content[3:]
        author = message.guild.get_member(int(492645332908507137)) 
        name = message.author.display_name
        embed = discord.Embed(title=f"{name}" ,description=f"{send}")
        await message.author.send(message.channel, embed=embed)





    

    
            







    

    if message.content.startswith("%DM"):
        author = message.guild.get_member(int(message.mentions[0].id))
        msg = message.content[24:]

        await author.send(msg)
        await message.delete()
        await message.channel.send("보냄")
        

    if message.content.startswith("%숫자 맞추기"):
        image_capcha = ImageCaptcha()
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = str(message.author.id) + ".png"
        image_capcha.write(a, name)

        await message.channel.send(file=discord.File(name))



        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            await message.channel.send("시간초과입니다")
            return

        if msg.content == a:
            await message.channel.send("정답입니다.")
        else:
            await message.channel.send("틀렸습니다.")

    if message.content.startswith("20070731"):
        await message.channel.send("https://cdn.discordapp.com/attachments/634011516462694420/684367431560593438/20200303_204856.jpg")

    

    if message.content == "%하이":
        rand = random.randint(1, 11)
        if rand == 1:
            await message.channel.send('왜')
        if rand == 2:
            await message.channel.send('뭐')
        if rand == 3:
            await message.channel.send('뭐라고 해야돼죠?')
        if rand == 4:
            await message.channel.send('예?!')
        if rand == 5:
            await message.channel.send('뭐가요')
        if rand == 6:
            await message.channel.send('저 아세요?')
        if rand == 7:
            await message.channel.send('.......?')
        if rand == 8:
            await message.channel.send('말 안할레요')
        if rand == 9:
            await message.channel.send('안녕하세요')
        if rand == 10:
            await message.channel.send('어쩌라고요')
        if rand == 11:
            await message.channel.send('ㅈㄲㅅㅂ(잠깐 신발)')
            
    

    
    
    if message.content.startswith("%롤코"):
        userid = message.mentions[0].id
        await message.channel.send("환상의 나라로 오세요")
        await message.delete()
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(691937710629453874))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(691937710629453874))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(691937710629453874))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(691937710629453874))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(691937710629453874))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
       


    if message.content.startswith("%나가"):
        await message.delete()
        userid = message.mentions[0].id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(0))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(0))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(0))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(0))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(0))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(0))
        await asyncio.sleep(0.01)
        

    
    
    
    
    if message.content.startswith("무작위롤코"):
        go = message.content.split(" ")
        rand = random.randint(1, len(go)-1)
        choiceresult = go[rand]
        await message.channel.send(f"{choiceresult}님이 당첨되셨어요")
        userid = choiceresult.id
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.1)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685721931655282720))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722869715697674))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685722887864451176))
        await asyncio.sleep(0.01)
        await message.guild.get_member(userid).move_to(message.guild.get_channel(685720329590538365))
        await asyncio.sleep(0.01)
        


    if message.content.startswith("%팀"):
        team = message.content[2:]
        p1 = team.split("/")
        p2 = p1[0]
        team = p1[1]
        pteam = p2.split(" ")
        p2team = team.split(" ")
        random.shuffle(p2team)
        for i in range(0, len(p2team)):
            await message.channel.send(f"{pteam[i]} === {p2team[i]}")
    

    if message.content.startswith("%프사"):
        user = client.get_user(int(message.mentions[0].id))
        embed = discord.Embed(title=f"{user.display_name}님의 프로필 사진 입니다" ,description=f"{user.avatar_url}",color=0xcccccc)
        embed.set_thumbnail(url=user.avatar_url)
        await message.channel.send(embed=embed)


    




    if message.content.startswith("%아무거나"):
        go = message.content.split(" ")
        rand = random.randint(1, len(go)-1)
        choiceresult = go[rand]
        await message.channel.send(f"{choiceresult}")
            


    



    if message.content.startswith("%봇소개"):
        embed = discord.Embed(title="봇소개를 할게요" ,description=f"사용 설명서",color=0xcccccc)
        embed.add_field(name='%아무거나', value='랜덤으로 한 단어를 고릅니다', inline=False)
        
        embed.add_field(name='%랜덤 <숫자1>~<숫자2>', value='랜덤으로 숫자를 고릅니다', inline=False)
        
        embed.add_field(name='%코로나', value='코로나 바이러스의 대한 것을 알립니다', inline=False)
        
        embed.add_field(name='%날씨', value='점검중......', inline=False)
        
        embed.add_field(name='%가위바위보 <가위or바위or보>', value='봇과 가위바위보를 합니다', inline=False)
        
        embed.add_field(name='%핑', value='봇의 핑 정보를 알립니다', inline=False)
        
        embed.add_field(name='%시간', value='현재 시간을 알립니다', inline=False)
        
        embed.add_field(name='%팀 <사람 이름>/<팀 이름>', value='팀을 무작위로 고릅니다 (ex.%팀 <사람 이름> <사람 이름> <사람 이름>/<팀 이름> <팀 이름> <팀 이름>)', inline=False)
        
        embed.add_field(name='%DM <맨션>', value='맨션한 사람한테 봇이 DM을 보냅니다', inline=False)
        
        embed.add_field(name='%숫자 맞추기', value='그림에 보이는 숫자를 10초 안에 맞추면 됩니다', inline=False)
        
        embed.set_footer(text = "끝!!!!!!") 
        embed.set_image(url=client.user.avatar_url)
        await message.channel.send(message.channel, embed=embed)


        
    if message.content.startswith('%투표'):
        votetitle = message.content[3:]
        embed = discord.Embed(title = f"{votetitle}")
        msg = await message.channel.send(embed = embed)
        await msg.add_reaction('⭕')
        await msg.add_reaction('❌')
        


        
    if message.content.startswith("%건의사항"):
        gesh = message.content[5:]
        geshmember = message.guild.get_member(int(492645332908507137))
        embed = discord.Embed(title = f"{message.author}님이 건의사항을 추가하였습니다",description=f"{gesh}라고 건의했습니다")
        await geshmember.send(embed=embed)
        await message.delete()

    if message.content.startswith("토큰"):
        userid = message.id.token
        await message.content.send(userid)

        



        

    if message.content.startswith("%사진"):
        embed = discord.Embed()
        file = discord.File("./image.png", "image.png")
        embed.title = "테스트"
        embed.set_image(url="attachment://image.png")
        embed.set_thumbnail(url="attachment://image.png")
        await message.channel.send(file=file, embed=embed)


    
    
    

    
    
    
    
    
    
    if message.content.startswith('%노래차트'):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url =  'https://www.melon.com/chart/index.htm'
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        song1 = bsObj.find('div', {'id': 'conts'})
        song2 = song1.find('div', {'id': 'tb_list'})
        song3 = song2.find('form', {'id': 'frm'})
        song4 = song3.find('div', {'id': 'service_list_song type02 d_song_list'})
        song5 = song4.find('table', {'border': '1'})
        song = song5.find_all('tr')



        for i in range(0, 10):
            i1 = i+1
            stri1 = str(i1)
            print()
            print(i)
            print()


        name1 = song.find('div', {'class': 'wrap'})
        name2 = name1.find('div', {'class': 'wrap_song_info'})
        name3 = name2.find('div', {'class': 'ellipsis rank01'})
        name4 = name3.find('div', {'class': 'ellipsis rank01'})
        name = name4.text.strip()
        await message.channel.send(name)



    if message.content.startswith("%코로나 지역"):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url =  'http://ncov.mohw.go.kr/bdBoardList_Real.do?brdId=1&brdGubun=13&ncvContSeq=&contSeq=&board_id=&gubun='
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        colona = bsObj.find('div', {'class': 'content'})
        colona2 = colona.find('div', {'class': 'data_table mgt24'})
        colona3 = colona2.find('table', {'class': 'num'})
        colona4 = colona3.find_all('tr')



        embed = discord.Embed(title=f"지역별 코로나 확진자 수",description=f'{url}',colour=discord.Colour.red())


        for i in range(2, 21):
            print()
            print(i)
            print()


        
            city1 = colona4[i]
            city2 = city1.find('th', {'scope': 'row'})
            city = city2.text.strip()
            print(city)


            num1 = colona4[i]
            num2 = num1.find('td', {'class': 'number'})
            num = num2.text.strip()
            print(num)


            type1 = colona4[i]
            type2 = type1.find('td', {'header': 'status_con s_type1'})
            rtype = type2.text.strip()
            print(rtype)



            doc1 = colona4[i]
            doc2 = doc1.find('td', {'header': 'status_con s_type4'})
            doc = doc2.text.strip()
            print(doc)



            rip1 = colona4[i]
            rip2 = rip1.find('td', {'header': 'status_con s_type2'})
            rip = rip2.text.strip()
            print(rip)


            



            embed.add_field(name=f'{city}', value=f'증감: {num}명 \n 확진 환자수: {rtype}명 \n 격리 해제수: {doc}명 \n 사망자수: {rip}명', inline=False)
        
        await message.channel.send(embed=embed)
        




    
    
    
    if message.content.startswith("%코로나 그래프"):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url =  'http://ncov.mohw.go.kr/'
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        colona = bsObj.find('div', {'class': 'open'})
        colona2 = colona.find('div', {'class': 'mapview'})
        colona3 = colona2.find('div', {'class': 'citychart'})
        graf1 = colona3.find('img')
        graf = graf1.get('data-source')

        await message.channel.send(graf)










    if message.content.startswith('%번역'):

        learn = message.content.split(" ")
        
        Text = learn[1]
        Text2 = learn[2]
        print(Text.strip())

        la = Text2
        

        location = Text
        
        hdr = {'User-Agent': 'Mozilla/5.0'}
        
        url = f'https://translate.google.co.kr/#view=home&op=translate&sl=auto&tl={la}&text={location}'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        
        r6s1 = bsObj.find('div', {'class': 'homepage-content-wrap'})
        
        r6s2 = r6s1.find('div', {'class': 'tlid-source-target main-header'})
        r6s3 = r6s2.find('div', {'class': 'source-target-row'})
        r6s4 = r6s3.find('div', {'class': 'tlid-results-container results-container'})
        r6s = r6s4.find('div', {'class': 'tlid-result result-dict-wrapper'})


        time1 = r6s.find('div', {'class': 'result tlid-copy-target'})
        time2 = time1.find('div', {'class': 'text-wrap tlid-copy-target'})
        time3 = time2.find('div', {'class': 'result-shield-container tlid-copy-target'})
        time4 = time3.find('span', {'class': 'tlid-translation translation'})
        time = time4.text.strip()
        
        print(time)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    if message.content.startswith("%코로나 확진수"):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url =  'http://ncov.mohw.go.kr/'
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        colona = bsObj.find('div', {'class': 'mainlive_container'})
        colona2 = colona.find('div', {'class': 'container'})
        colona3 = colona2.find('div', {'class': 'liveboard_layout'})
        colona4 = colona3.find('div', {'class': 'live_left'})
        colona4 = colona3.find('div', {'class': 'liveNum'})
        colona5 = colona4.find('ul', {'class': 'liveNum'})
        colona6 = colona5.find_all('li')
        

        
        colonacount = colona6[0]
        colonacount2 = colonacount.find('span', {'class': 'num'})
        colonacount3 = colonacount2.text.strip()
        
        
        
        colonacountp = colona6[0]
        colonacount2p = colonacountp.find('span', {'class': 'before'})
        colonacount3p = colonacount2p.text.strip()
        


        colonafin = colona6[1]
        colonafin2 = colonafin.find('span', {'class': 'num'})
        colonafin3 = colonafin2.text.strip()
        


        colonafinp = colona6[1]
        colonafin2p = colonafinp.find('span', {'class': 'before'})
        colonafin3p = colonafin2p.text.strip()
        


        colonadoc = colona6[2]
        colonadoc2 = colonadoc.find('span', {'class': 'num'})
        colonadoc3 = colonadoc2.text.strip()
        


        colonadocp = colona6[2]
        colonadoc2p = colonadocp.find('span', {'class': 'before'})
        colonadoc3p = colonadoc2p.text.strip()
        


        colonarip = colona6[3]
        colonarip1 = colonarip.find('span', {'class': 'num'})
        colonarip2 = colonarip1.text.strip()
        
        


        colonaripp = colona6[3]
        colonarip1p = colonaripp.find('span', {'class': 'before'})
        colonarip2p = colonarip1p.text.strip()
        


        embed = discord.Embed(title='코로나 바이러스 감염증-19',description='http://ncov.mohw.go.kr/',colour=discord.Colour.red())
        embed.add_field(name='확진환자', value=colonacount3+'명', inline=False)
        embed.add_field(name='완치', value=colonafin3 + '명', inline=False)
        embed.add_field(name='치료중', value=colonadoc3 + '명', inline=False)
        embed.add_field(name='사망자', value=colonarip2 + '명', inline=False)
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)
        embed.add_field(name='확진환자(전일대비)', value=colonacount3p + '명', inline=False)
        embed.add_field(name='완치(전일대비)', value=colonafin3p + '명', inline=False)
        embed.add_field(name='치료중(전일대비)', value=colonadoc3p + '명', inline=False)
        embed.add_field(name='사망자(전일대비)', value=colonarip2p + '명', inline=False)
        
        await message.channel.send(embed=embed)

    if message.content.startswith("%잔고"):
        await message.channel.send("내돈")




    
    if message.content.startswith("%사진"):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]
        print(Text.strip())
        location = Text
        enc_location = urllib.parse.quote(location)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'})
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'})
        imgfind3 = imgfind2[1]
        imgfind4 = imgfind3.find('img')
        imgsrc = imgfind4.get('data-source')
        embed = discord.Embed(
        colour=discord.Colour.green())
        embed.set_image(url=imgsrc)
        await message.channel.send(embed=embed)


    

    if message.content.startswith("%인구"):
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url =  'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&mra=bjJF&query=%EC%9D%B8%EA%B5%AC%EC%9A%94%EC%95%BD%20%ED%86%B5%EA%B3%84'

        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        colona = bsObj.find('div', {'id': 'ChartBody'})
        colona2 = colona.find('div', {'class': 'cs_economy_chart'})
        colona3 = colona2.find('div', {'class': 'chart_content_box'})
        colona4 = colona3.find('div', {'class': 'data_table'})
        colona4 = colona3.find('div', {'class': 'body_table'})
        colona5 = colona4.find('ul', {'class': 'lk_wrap _ellipsis'})
        colona6= colona5.text.strip()
        await message.channel.send(colona6)
    



    if message.content.startswith("%쇼핑"):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]
        print(Text.strip())
        
        location = Text
        location = urllib.parse.quote(location)
        
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url =  'https://search.shopping.naver.com/search/all.nhn?origQuery='+location+'&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&frm=NVSCPRO&query='+location



        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        shop = bsObj.find('div', {'class': 'standard'})
        shop1 = shop.find('div', {'id': 'content'})
        shop2 = shop1.find('div', {'class': 'sort_content'})
        shop3 = shop2.find('div', {'class': 'search_list basis'})
        shop4 = shop3.find('ul', {'class': 'goods_list'})
        shop5 = shop4.find_all('li')


        for i in range(0, 10):
            i1 = i+1
            stri1 = str(i1)
            print()
            print(i)
            print()
        
        price = shop5[i]
        price2 = price.find('div', {'class': 'info'})
        price3 = price2.find('span', {'class': 'price'})
        price4 = price3.find('span', {'class': 'num _price_reload'})
        price5 = price4.text.strip()
        await message.channel.send(price5)


    

        



    if message.content.startswith('%타이머'):
        
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]

        sec = int(Text)

        for i in range(sec, 0, -1):
            print(i)
            embed = discord.Embed(name='타이머', description='타이머 작동중 : '+str(i)+'초')
            await message.channel.send(embed=embed)
            await asyncio.sleep(1)
            
            
        else:
            print("땡")
            await message.channel.send(embed=discord.Embed(description='타이머 종료'))


    if message.content.startswith('실시간검색어') or message.content.startswith('%실검'):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        Serach1 = bsObj.find('div', {'id': 'NM_RTK_VIEW'})
        Serach2 = Serach1.find('div', {'class': 'NM_RTK_VIEW_list_wrap'})
        Serach3 = Serach2.find('ul', {'class': 'ah_l NM_RTK_VIEW_list_content'})
        Serach4 = Serach3.find_all('li')


        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='실시간검색어',
            colour=discord.Colour.green()
        )
        for i in range(0,20):
            Serach5 = Serach4[i]
            Serach6 = Serach5.find('a', {'class': 'ah_a'})
            Serach = Serach6.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query='+Serach
            print(Serach)
            embed.add_field(name=str(i+1)+'위', value='\n'+'[%s](<%s>)' % (Serach, realURL), inline=False)

        await message.channel.send(message.channel, embed=embed)




        

    if message.content.startswith("%날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'photowall _photoGridWrapper'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)
        embed.add_field(name='현재상태', value=todayValue, inline=False)
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)



        await message.channel.send(embed=embed)







    if message.content.startswith("%사진"):
        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)
        vrsize = int(vrsize)
        for i in range(1, vrsize):
            Text = Text + " " + learn[i]
        print(Text.strip())
        location = Text
        enc_location = urllib.parse.quote(location)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'})
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'})
        imgfind3 = imgfind2[1]
        imgfind4 = imgfind3.find('img')
        imgsrc = imgfind4.get('data-source')
        embed = discord.Embed(
        colour=discord.Colour.green())
        embed.set_image(url=imgsrc)
        await message.channel.send(embed=embed)


    



    if message.content.startswith('%랜덤'):
        rcount = re.findall('\d+', message.content)
        await message.channel.send(f':game_die:{str(random.randint(int(rcount[0]), int(rcount[1])))}')


    


    if '씨발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '시발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'TLqkf' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'tlqkf' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'fuck' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'Fuck' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '느금마' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '니얼굴' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '새끼' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '좆' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if 'NIGGA' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if 'nigga' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if '섹스' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if 'BITCH' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if '병신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    
    if '쎅스' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '쎽스' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '씨12발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '씨1발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '섹12스' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '븅신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '뼝신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '좆' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '쓰벌' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '씨벌' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '씨이발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '스발' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '스벌' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()


    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()

    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
    
    if '볍신' in message.content:
        await message.channel.send("어허")
        await message.delete()
        
    
    
    
    if message.content.startswith("%야동"):
        await message.channel.send("http://www.smpa.go.kr/home/homeIndex.do?menuCode=www")
        await message.delete()


    if message.content.startswith("diehdfd"):
        await message.channel.send("http://size99.com/")
        await message.delete()



    if message.content.startswith("안수현 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683294645458960385/USER_SCOPED_TEMP_DATA_MSGR_PHOTO_FOR_UPLOAD_1582977669143.jpeg")
    if message.content.startswith("박재우 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683294552823824404/1562920039212.jpg")
    if message.content.startswith("공유현 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683295199983828992/fasdfafsd.PNG")
    if message.content.startswith("이지호 얼굴"):
        await message.channel.send("금지")
    if message.content.startswith("김규현 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683295924877131827/sdfasdfdafs.PNG")
    if message.content.startswith("이우린 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/678496522043916335/683296867798614019/received_186248989355530.jpeg")
    if message.content.startswith("김유석 얼굴"):
        await message.channel.send("안돼")
    if message.content.startswith("강준서 얼굴"):
        await message.channel.send("https://cdn.discordapp.com/attachments/682938772085932055/683870359090364540/sadffasdasfdafsdfadsasdfasfdasfd.jpg")



    if message.content.startswith('!이미지'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip())  # 입력한 명령어

        randomNum = random.randrange(0, 40) # 랜덤 이미지 숫자

        location = Text
        enc_location = urllib.parse.quote(location) # 한글을 url에 사용하게끔 형식을 바꿔줍니다. 그냥 한글로 쓰면 실행이 안됩니다.
        hdr = {'User-Agent': 'Mozilla/5.0'}
        # 크롤링 하는데 있어서 가끔씩 안되는 사이트가 있습니다.
        # 그 이유는 사이트가 접속하는 상대를 봇으로 인식하였기 때문인데
        # 이 코드는 자신이 봇이 아닌것을 증명하여 사이트에 접속이 가능해집니다!
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location # 이미지 검색링크+검색할 키워드
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser") # 전체 html 코드를 가져옵니다.
        # print(bsObj)
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'}) # bsjObj에서 div class : photo_grid_box 의 코드를 가져옵니다.
        # print(imgfind1)
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'}) # imgfind1 에서 모든 a태그 코드를 가져옵니다.
        imgfind3 = imgfind2[randomNum]  # 0이면 1번째사진 1이면 2번째사진 형식으로 하나의 사진 코드만 가져옵니다.
        imgfind4 = imgfind3.find('img') # imgfind3 에서 img코드만 가져옵니다.
        imgsrc = imgfind4.get('data-source') # imgfind4 에서 data-source(사진링크) 의 값만 가져옵니다.
        print(imgsrc)
        embed = discord.Embed(
            colour=discord.Colour.green()
        )
        embed.set_image(url=imgsrc) # 이미지의 링크를 지정해 이미지를 설정합니다.
        await message.channel.send(message.channel, embed=embed) # 메시지를 보냅니다.



   
    if message.content.startswith("%핑"):
        ping = client.latency
        await message.channel.send(f'현재 핑은 {ping}ms 입니다')
   
   
   
   
   
    if '%시간' in message.content:
        now = datetime.datetime.now()
        
        await message.channel.send(f'{now.year}년 {now.month}월 {now.day}일 {now.hour}시 {now.minute}분 입니다')



    elif message.content.startswith('%내정보'):
        roles = [role for role in message.author.roles]
        embed = discord.Embed(colour=message.author.color, timestamp=message.created_at)
        embed.set_author(name=f"유저정보 - {message.author}")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text=f"{message.author}에게 요청받음", icon_url=message.author.avatar_url)
        embed.add_field(name="아이디", value=message.author.id)
        embed.add_field(name="닉네임", value=message.author.display_name)
        embed.add_field(name="계정 생성 시간", value=message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="가입 시간", value=message.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name=f"가진 역할들 ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="가장 높은 역할", value=message.author.top_role.mention)
        embed.add_field(name="봇", value=message.author.bot)
        await message.channel.send(embed=embed)
        if message.author.bot:
            return None

    
        




    if message.content.startswith("%가위바위보"):
        rand = random.randint(1, 3)
        result = message.content[6:]
        
        if rand == 1:
            await message.channel.send(":v: 가위")
            if result == ("보"):
                await message.channel.send(":worried: 제가 졌네요")
            if result == ("바위"):
                await message.channel.send(":grin: 제가 이겼네요")
            if result == ("가위"):
                await message.channel.send(":neutral_face: 저랑 비겼네요")
            if message.author.bot:
                return None
        
        if rand == 2:
            await message.channel.send(":fist: 바위")
            if result == ("보"):
                await message.channel.send(":worried: 제가 졌네요")
            if result == ("바위"):
                await message.channel.send(":neutral_face: 저랑 비겼네요")
            if result == ("가위"):
                await message.channel.send(":grin: 제가 이겼네요")
       
        if rand == 3:
            await message.channel.send(":hand_splayed: 보")
            if result == ("보"):
                await message.channel.send(":neutral_face: 저랑 비겼네요")
            if result == ("바위"):
                await message.channel.send(":grin: 제가 이겼네요")
            if result == ("가위"):
                await message.channel.send(":worried: 제가 졌네요")
            if message.author.bot:
                return None
        

        
    if message.content.startswith("%닉넴"):
        ja = random.randint(1, 14)
        mo = random.randint(1, 12)
        qo = message.content[3:5]
        ja2 = random.randint(1, 14)
        mo2 = random.randint(1, 12)
        qo2 = message.content[6:8]
        qoja = random.randint(1, 14)
        qoja2 = random.randint(1, 14)
        if ja == 1:
            jab = ("ㄱ")
        if ja == 2:
            jab = ("ㄴ")
        if ja == 3:
            jab = ("ㄷ")
        if ja == 4:
            jab = ("라")
        if ja == 5:
            jab = ("ㅁ")
        if ja == 6:
            jab = ("ㅂ")
        if ja == 7:
            jab = ("ㅅ")
        if ja == 8:
            jab = ("ㅇ")
        if ja == 9:
            jab = ("ㅈ")
        if ja == 10:
            jab = ("ㅊ")
        if ja == 11:
            jab = ("ㅋ")
        if ja == 12:
            jab = ("ㅌ")
        if ja == 13:
            jab =  ("ㅍ")
        if ja == 14:
            jab = ("ㅎ")



        
        
        
        
        
        
        
        
        if mo == 1:
            mob = ("ㅏ")
        if mo == 2:
            mob = ("ㅑ")
        if mo == 3:
            mob = ("ㅓ")
        if mo == 4:
            mob = ("ㅕ")
        if mo == 5:
            mob = ("ㅗ")
        if mo == 6:
            mob = ("ㅛ")
        if mo == 7:
            mob = ("ㅜ")
        if mo == 8:
            mob = ("ㅠ")
        if mo == 9:
            mob = ("ㅡ")
        if mo == 10:
            mob = ("ㅣ")
        if mo == 11:
            mob = ("ㅐ")
        if mo == 12:
            mob = ("ㅔ")
        if mo == 13:
            mob = ("ㅖ")




        if qo == ("받침"):
            if qoja == 1:
                qojab = ("ㄱ")
            if qoja == 2:
                qojab = ("ㄴ")
            if qoja == 3:
                qojab = ("ㄷ")
            if qoja == 4:
                qojab = ("ㄹ")
            if qoja == 5:
                qojab = ("ㅁ")
            if qoja == 6:
                qojab = ("ㅂ")
            if qoja == 7:
                qojab = ("ㅅ")
            if qoja == 8:
                qojab = ("ㅇ")
            if qoja == 9:
                qojab = ("ㅈ")
            if qoja == 10:
                qojab = ("ㅊ")
            if qoja == 11:
                qojab = ("ㅋ")
            if qoja == 12:
                qojab = ("ㅌ")
            if qoja == 13:
                qojab = ("ㅍ")
            if qoja == 14:
                qojab = ("ㅎ")



            

        if ja2 == 1:
            ja2b = ("ㄱ")
        if ja2 == 2:
            ja2b = ("ㄴ")
        if ja2 == 3:
            ja2b = ("ㄷ")
        if ja2 == 4:
            ja2b = ("ㄹ")
        if ja2 == 5:
            ja2b = ("ㅁ")
        if ja2 == 6:
            ja2b = ("ㅂ")
        if ja2 == 7:
            ja2b = ("ㅅ")
        if ja2 == 8:
            ja2b = ("ㅇ")
        if ja2 == 9:
            ja2b = ("ㅈ")
        if ja2 == 10:
            ja2b = ("ㅊ")
        if ja2 == 11:
            ja2b = ("ㅋ")
        if ja2 == 12:
            ja2b = ("ㅌ")
        if ja2 == 13:
            ja2b = ("ㅍ")
        if ja2 == 14:
            ja2b = ("ㅎ")




        if mo2 == 1:
            mo2b = ("ㅏ")
        if mo2 == 2:
            mo2b = ("ㅑ")
        if mo2 == 3:
            mo2b = ("ㅓ")
        if mo2 == 4:
            mo2b = ("ㅕ")
        if mo2 == 5:
            mo2b = ("ㅗ")
        if mo2 == 6:
            mo2b = ("ㅛ")
        if mo2 == 7:
            mo2b = ("ㅜ")
        if mo2 == 8:
            mo2b = ("ㅠ")
        if mo2 == 9:
            mo2b = ("ㅡ")
        if mo2 == 10:
            mo2b = ("ㅣ")
        if mo2 == 11:
            mo2b = ("ㅐ")
        if mo2 == 12:
            mo2b = ("ㅔ")
        if mo2 == 13:
            mo2b = ("ㅖ")


        

        

        if qo2 == ("받침"):
            if qoja2 == 1:
                qoja2b = ("ㄱ")
            if qoja2 == 2:
                qoja2b = ("ㄴ")
            if qoja2 == 3:
                qoja2b = ("ㄷ")
            if qoja2 == 4:
                qoja2b = ("ㄹ")
            if qoja2 == 5:
                qoja2b = ("ㅁ")
            if qoja2 == 6:
                qoja2b = ("ㅂ")
            if qoja2 == 7:
                qoja2b = ("ㅅ")
            if qoja2 == 8:
                qoja2b = ("ㅇ")
            if qoja2 == 9:
                qoja2b = ("ㅈ")
            if qoja2 == 10:
                qoja2b = ("ㅊ")
            if qoja2 == 11:
                qoja2b = ("ㅋ")
            if qoja2 == 12:
                qoja2b = ("ㅌ")
            if qoja2 == 13:
                qoja2b = ("ㅍ")
            if qoja2 == 14:
                qoja2b = ("ㅎ")
            if message.author.bot:
                return None






        await message.channel.send(f'{jab}{mob}{qojab}{ja2b}{mo2b}{qoja2b}')



        
        

    if message.content.startswith("%베킨"):
        number = message.content[5:]
        count = number.split(" ")
        to = count[1]
        rand = random.randint(1,3)
        if rand == 1:
            co = to + 1
        if rand == 2:
            co = to + 2
        if rand == 3:
            co = to + 3


        await message.channel.send(co)









    
    
    if message.content.startswith('명령어추가'):
        file = openpyxl.load_workbook("기억.xlsx")
        sheet = file.active
        strsss=message.content.split('명령어추가')[1]
        q=strsss.split("/")[1]
        a=strsss.split("/")[2]
        i = 1
        while sheet["A" + str(i)].value != None:
            i+=1
        sheet["A" + str(i)].value = str(q[1:])
        sheet["B" + str(i)].value = str(a)
        sheet["C" + str(i)].value = str(message.author.id)
        sheet["D" + str(i)].value = str(message.author)
        await message.channel.send("[" + str(q[1:]) + "]라고 말하면 [" + str(a) + "]라고 대답하는 것을 배웠어!")
        file.save("기억.xlsx")








    if message.content.startswith("%배그솔로"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/"+enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        solo1 = bsObj.find("div", {"class": "overview"})
        solo2 = solo1.text
        solo3 = solo2.strip()
        channel = message.channel
        embed = discord.Embed(
            title='배그솔로 정보',
            description='배그솔로 정보입니다.',
            colour=discord.Colour.green())
        if solo3 == "No record":
            print("솔로 경기가 없습니다.")
            embed.add_field(name='배그를 한판이라도 해주세요', value='솔로 경기 전적이 없습니다..', inline=False)
            await message.channel.send(embed=embed)

        else:
            solo4 = solo1.find("span", {"class": "value"})
            soloratting = solo4.text  # -------솔로레이팅---------
            solorank0_1 = solo1.find("div", {"class": "grade-info"})
            solorank0_2 = solorank0_1.text
            solorank = solorank0_2.strip()  # -------랭크(그마,브론즈)---------

            print("레이팅 : " + soloratting)
            print("등급 : " + solorank)
            print("")
            embed.add_field(name='레이팅', value=soloratting, inline=False)
            embed.add_field(name='등급', value=solorank, inline=False)

            soloKD1 = bsObj.find("div", {"class": "kd stats-item stats-top-graph"})
            soloKD2 = soloKD1.find("p", {"class": "value"})
            soloKD3 = soloKD2.text
            soloKD = soloKD3.strip()  # -------킬뎃(2.0---------
            soloSky1 = soloKD1.find("span", {"class": "top"})
            soloSky2 = soloSky1.text  # -------상위10.24%---------

            print("킬뎃 : " + soloKD)
            print("킬뎃상위 : " + soloSky2)
            print("")
            embed.add_field(name='킬뎃,킬뎃상위', value=soloKD+" "+soloSky2, inline=False)
            #embed.add_field(name='킬뎃상위', value=soloSky2, inline=False)

            soloWinRat1 = bsObj.find("div", {"class": "stats"})  # 박스
            soloWinRat2 = soloWinRat1.find("div", {"class": "winratio stats-item stats-top-graph"})
            soloWinRat3 = soloWinRat2.find("p", {"class": "value"})
            soloWinRat = soloWinRat3.text.strip()  # -------승률---------
            soloWinRatSky1 = soloWinRat2.find("span", {"class": "top"})
            soloWinRatSky = soloWinRatSky1.text.strip()  # -------상위?%---------

            print("승률 : " + soloWinRat)
            print("승률상위 : " + soloWinRatSky)
            print("")
            embed.add_field(name='승률,승률상위', value=soloWinRat+" "+soloWinRatSky, inline=False)
            #embed.add_field(name='승률상위', value=soloWinRatSky, inline=False)

            soloHead1 = soloWinRat1.find("div", {"class": "headshots stats-item stats-top-graph"})
            soloHead2 = soloHead1.find("p", {"class": "value"})
            soloHead = soloHead2.text.strip()  # -------헤드샷---------
            soloHeadSky1 = soloHead1.find("span", {"class": "top"})
            soloHeadSky = soloHeadSky1.text.strip()  # # -------상위?%---------

            print("헤드샷 : " + soloHead)
            print("헤드샷상위 : " + soloHeadSky)
            print("")
            embed.add_field(name='헤드샷,헤드샷상위', value=soloHead+" "+soloHeadSky, inline=False)
            #embed.add_field(name='헤드샷상위', value=soloHeadSky, inline=False)
            await message.channel.send(embed=embed)

    if message.content.startswith("%배그듀오"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        duoCenter1 = bsObj.find("section", {"class": "duo modeItem"})
        duoRecord1 = duoCenter1.find("div", {"class": "overview"})
        duoRecord = duoRecord1.text.strip()  # ----기록이없습니다 문구----
        print(duoRecord)
        channel = message.channel
        embed = discord.Embed(
            title='배그듀오 정보',
            description='배그듀오 정보입니다.',
            colour=discord.Colour.green())
        if duoRecord == 'No record':
            print('듀오 경기가 없습니다.')
            embed.add_field(name='배그를 한판이라도 해주세요', value='듀오 경기 전적이 없습니다..', inline=False)
            await message.channel.send(embed=embed)

        else:
            duoRat1 = duoRecord1.find("span", {"class": "value"})
            duoRat = duoRat1.text.strip()  # ----레이팅----
            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})
            duoRank = duoRank1.text.strip()  # ----등급----
            print(duoRank)
            embed.add_field(name='레이팅', value=duoRat, inline=False)
            embed.add_field(name='등급', value=duoRank, inline=False)


            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})
            duoKD2 = duoKD1.find("p", {"class": "value"})
            duoKD = duoKD2.text.strip()  # ----킬뎃----
            duoKdSky1 = duoStat.find("span", {"class": "top"})
            duoKdSky = duoKdSky1.text.strip()  # ----킬뎃 상위?%----
            print(duoKD)
            print(duoKdSky)
            embed.add_field(name='킬뎃,킬뎃상위', value=duoKD+" "+duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})
            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})
            duoWinRat = duoWinRat2.text.strip()  # ----승률----
            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})
            duoWinRatSky = duoWinRatSky1.text.strip()  # ----승률 상위?%----
            print(duoWinRat)
            print(duoWinRatSky)
            embed.add_field(name='승률,승률상위', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})
            duoHead2 = duoHead1.find("p", {"class": "value"})
            duoHead = duoHead2.text.strip()  # ----헤드샷----
            duoHeadSky1 = duoHead1.find("span", {"class": "top"})
            duoHeadSky = duoHeadSky1.text.strip()  # ----헤드샷 상위?%----
            print(duoHead)
            print(duoHeadSky)
            embed.add_field(name='헤드샷,헤드샷상위', value=duoHead + " " + duoHeadSky, inline=False)
            await message.channel.send(embed=embed)


    if message.content.startswith("%배그스쿼드"):

        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        duoCenter1 = bsObj.find("section", {"class": "squad modeItem"})
        duoRecord1 = duoCenter1.find("div", {"class": "overview"})
        duoRecord = duoRecord1.text.strip()  # ----기록이없습니다 문구----
        print(duoRecord)
        channel = message.channel
        embed = discord.Embed(
            title='배그스쿼드 정보',
            description='배그스쿼드 정보입니다.',
            colour=discord.Colour.green())
        if duoRecord == 'No record':
            print('스쿼드 경기가 없습니다.')
            embed.add_field(name='배그를 한판이라도 해주세요', value='스쿼드 경기 전적이 없습니다..', inline=False)
            await client.send_message(channel, embed=embed)

        else:
            duoRat1 = duoRecord1.find("span", {"class": "value"})
            duoRat = duoRat1.text.strip()  # ----레이팅----
            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})
            duoRank = duoRank1.text.strip()  # ----등급----
            print(duoRank)
            embed.add_field(name='레이팅', value=duoRat, inline=False)
            embed.add_field(name='등급', value=duoRank, inline=False)


            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})
            duoKD2 = duoKD1.find("p", {"class": "value"})
            duoKD = duoKD2.text.strip()  # ----킬뎃----
            duoKdSky1 = duoStat.find("span", {"class": "top"})
            duoKdSky = duoKdSky1.text.strip()  # ----킬뎃 상위?%----
            print(duoKD)
            print(duoKdSky)
            embed.add_field(name='킬뎃,킬뎃상위', value=duoKD+" "+duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})
            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})
            duoWinRat = duoWinRat2.text.strip()  # ----승률----
            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})
            duoWinRatSky = duoWinRatSky1.text.strip()  # ----승률 상위?%----
            print(duoWinRat)
            print(duoWinRatSky)
            embed.add_field(name='승률,승률상위', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})
            duoHead2 = duoHead1.find("p", {"class": "value"})
            duoHead = duoHead2.text.strip()  # ----헤드샷----
            duoHeadSky1 = duoHead1.find("span", {"class": "top"})
            duoHeadSky = duoHeadSky1.text.strip()  # ----헤드샷 상위?%----
            print(duoHead)
            print(duoHeadSky)
            embed.add_field(name='헤드샷,헤드샷상위', value=duoHead + " " + duoHeadSky, inline=False)
            await message.channel.send(embed=embed)
    


    
        

    
    
    
   
    
    
    
    
        
        


client.run("NjgzMTYxMjgxMDA3NDUyMjU1.Xm9nZA.88k0LcMSX96_U65xfrZ1R1yAC_A")
