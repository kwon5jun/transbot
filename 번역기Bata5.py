#-*- coding:utf-8 -*-
# 번역기봇 제작:권오준 http://www.kwon5jun.com

import discord
import asyncio
import os
import urllib.request
from googletrans import Translator

client = discord.Client()

@client.event
async def on_ready():
	print("="*20)
	print(client.user.name)
	print('너굴번역기 베타5 작동!!!') 
	print("="*20)

@client.event
async def on_message(message):
	await client.change_presence(game=discord.Game(name='!!help 번역기봇 베타5버전입니다.@ 오류문의는 꼬기빙수#5197 ')) # ~~~ playing
	if message.author != client.user: # 봇이 봇에게 명령하지 못합니다.
        
		if message.content.startswith('!!help'): # !commands
			print("도움말을 요청")
			await client.send_message(message.channel, """
너굴번역기 Bata5 텍스트입력시 자동번역
한글은 영어로 영어는 한글로 번역 """) # bot's answer

		elif(message.content.count(':')>0):
			print("이모티콘은 패스")

		else:
			m = message.content
			translator = Translator()
			txtname = message.author.display_name
			startenc=translator.detect(m).lang
			print(translator.detect(m).confidence,startenc,txtname)
			if(translator.detect(m).confidence > 0.4):
				if(startenc=='ko'):
					finalenc='en'
				elif(startenc=='en'):
					finalenc='ko'
				else:
					print("only ko,en")
					await client.send_message(message.channel,"""only Korean or English""")
				try:
					centertxt = translator.translate(m, src=startenc, dest='ja').text
					await client.send_message(message.channel,startenc+"""->"""+finalenc+"""번역하였습니다. (translated it.)
["""+ txtname +"""] """+translator.translate(centertxt, src='ja', dest=finalenc).text)
				except:
					print('번역에러')
					await client.send_message(message.channel,"""번역실패! (translation fail!)""")
			else:
				print('인식에러')
				await client.send_message(message.channel,"""인식 오류! (Recognition error!)""")
	
access_token = os.environ["BOT_TOKEN"]
client.run('access_token') #디스코드 사이트 > 개발자 포털 > 내 봇 > Bot token