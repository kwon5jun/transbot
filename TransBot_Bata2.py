#-*- coding:utf-8 -*-
# 번역기봇 제작:권오준 http://www.kwon5jun.com

import discord
import asyncio
import os
import urllib.request

if not discord.opus.is_loaded():
	discord.opus.load_opus('opus')

client = discord.Client()


client_id = os.environ["Naver_API_ID"]
client_secret = os.environ["Naver_API_Secrdt"]


@client.event
async def on_ready():
	print("="*20)
	print(client.user.name)
	print('너굴너굴 번역기 봇 작동!!!') 
	print("="*20)

@client.event
async def on_message(message):
	await client.change_presence(game=discord.Game(name='!!help 번역기봇 베타버전입니다.@@ 오류문의는 꼬기빙수#5197 ')) # ~~~ playing
	if message.author != client.user: # 봇이 봇에게 명령하지 못합니다.
        
		if message.content.startswith('!!help'): # !commands
			print("도움말을 요청")
			msg = await client.send_message(message.channel, """
모든 명령어 앞에는 항상 !!를 붙입니다. Bata V2.2
!!en2ko [...] English -> Korean
!!ko2en [...] Korean  -> English
!!ja2ko [...] Japanese-> Korean
!!ko2ja [...] Korean  -> Japanese 
ex) !!en2ko Hi """) # bot's answer

#--영어>한글
		elif message.content.startswith('!!en2ko'):
			m = message.content
			if(len(m)>8):
				txtname = message.author.display_name
				print("'영어>한글 번역")
				sourcetxt = 'en'
				targettxt = 'ko'
				await client.send_message(message.channel,trans(sourcetxt,targettxt,m,txtname))
			else:
				await client.send_message(message.channel,"""번역할 문자를 입력하세요. (Please enter what you want to translate.)""")


#--한글>영어
		elif message.content.startswith('!!ko2en'):
			m = message.content
			if(len(m)>8):
				txtname = message.author.display_name
				print("'한글>영어 번역")
				sourcetxt = 'ko'
				targettxt = 'en'
				await client.send_message(message.channel,trans(sourcetxt,targettxt,m,txtname))
			else:
				await client.send_message(message.channel,"""번역할 문자를 입력하세요. (Please enter what you want to translate.)""")
		
#--일어>한글
		elif message.content.startswith('!!ja2ko'):
			m = message.content
			if(len(m)>8):
				txtname = message.author.display_name
				print("'일어>한글 번역")
				sourcetxt = 'ja'
				targettxt = 'ko'
				await client.send_message(message.channel,trans(sourcetxt,targettxt,m,txtname))
			else:
				await client.send_message(message.channel,"""번역할 문자를 입력하세요. (Please enter what you want to translate.)""")

#--한글>일어
		elif message.content.startswith('!!ko2ja'):
			m = message.content
			if(len(m)>8):
				txtname = message.author.display_name
				print("'한글>일어' 번역")
				sourcetxt = 'ko'
				targettxt = 'ja'
				await client.send_message(message.channel,trans(sourcetxt,targettxt,m,txtname))
			else:
				await client.send_message(message.channel,"""번역할 문자를 입력하세요. (Please enter what you want to translate.)""")

#--영어>일어
		elif message.content.startswith('!!en2ja'):
			m = message.content
			if(len(m)>8):
				txtname = message.author.display_name
				print("'영어>일어' 번역")
				sourcetxt = 'en'
				targettxt = 'ja'
				await client.send_message(message.channel,trans(sourcetxt,targettxt,m,txtname))
			else:
				await client.send_message(message.channel,"""번역할 문자를 입력하세요. (Please enter what you want to translate.)""")

#--일어>영어
		elif message.content.startswith('!!ja2en'):
			m = message.content
			if(len(m)>8):
				txtname = message.author.display_name
				print("'일어>영어' 번역")
				sourcetxt = 'en'
				targettxt = 'ja'
				await client.send_message(message.channel,trans(sourcetxt,targettxt,m,txtname))
			else:
				await client.send_message(message.channel,"""번역할 문자를 입력하세요. (Please enter what you want to translate.)""")


def trans(sourcetxt,targettxt,m,txtname):
	print(txtname+"님이 번역요청")
	encText = urllib.parse.quote(m[7:])
	data = "source="+sourcetxt+"&target="+targettxt+"&text=" + encText
	url = "https://openapi.naver.com/v1/papago/n2mt"
	request = urllib.request.Request(url)
	request.add_header("X-Naver-Client-Id",client_id)
	request.add_header("X-Naver-Client-Secret",client_secret)
	response = urllib.request.urlopen(request, data=data.encode("utf-8"))
	rescode = response.getcode()
	if(rescode==200):
		response_body = response.read()
		msg = sourcetxt+"""->"""+targettxt+"""번역하였습니다. (translated it.)
["""+ txtname +"""] """+response_body.decode('utf-8')[152:-4]
	elif(rescode==400):
		msg = """HTTP 400 오류."""
	elif(rescode==429):
		msg = """한도초과입니다 내일 이용해주세요..."""
	elif(rescode==500):
		msg = """HTTP 500 오류."""
	else:
		msg = """알수없는 오류"""
	return msg

access_token = os.environ["BOT_TOKEN"]
client.run('access_token') #디스코드 사이트 > 개발자 포털 > 내 봇 > Bot token
