#-*- coding:utf-8 -*-
# 번역기봇 제작:권오준 http://www.kwon5jun.com


#----추가하기 중간에 일본어로 번역을 넣기

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
	print('너굴번역기 베타4 작동!!!') 
	print("="*20)

@client.event
async def on_message(message):
	await client.change_presence(game=discord.Game(name='!!help 번역기봇 베타4버전입니다.@ 오류문의는 꼬기빙수#5197 ')) # ~~~ playing
	if message.author != client.user: # 봇이 봇에게 명령하지 못합니다.
        
		if message.content.startswith('!!help'): # !commands
			print("도움말을 요청")
			await client.send_message(message.channel, """
모든 명령어 앞에는 항상 !!를 붙입니다. Bata V3
!!en2ko [...] English -> Korean
!!ko2en [...] Korean  -> English
!![...]2[...] [...] LANGUAGES -> LANGUAGES
ex) !!en2ko Hi 
LANGUAGES List: !!language '""") # bot's answer

		elif message.content.startswith('!!language'):
			await client.send_message(message.channel, """ 
LANGUAGES List:
'ko': 'korean'---- 'en':'english'---- 'ja':'japanese'   
'fy': 'frisian'--- 'uk': 'ukrainian'- 'ps': 'pashto'    
'hr': 'croatian'-- 'ar': 'arabic'---- 'so': 'somali'    
'vi': 'vietnamese' 'tr': 'turkish'--- 'ne': 'nepali'    
'bs': 'bosnian'--- 'es': 'spanish'--- 'mg': 'malagasy'  
'id': 'indonesian' 'ig': 'igbo'------ 'sk': 'slovak'    
'mi': 'maori'----- 'ro': 'romanian'-- 'iw': 'hebrew'    
'zu': 'zulu'------ 'st': 'sesotho'--- 'he': 'Hebrew'    
'si': 'sinhala'--- 'lv': 'latvian'--- 'fy': 'frisian'   
'km': 'khmer'----- 'no': 'norwegian'- 'su': 'sundanese' 
'sw': 'swahili'--- 'fr': 'french'---- 'ta': 'tamil'     
'fi': 'finnish'--- 'tl': 'filipino'-- 'hi': 'hindi'
'ny': 'chichewa'-- 'gu': 'gujarati'-- 'ru': 'russian'   
'pa': 'punjabi'--- 'sl': 'slovenian'- 'ha': 'hausa'      
'co': 'corsican'-- 'la': 'latin'----- 'sv': 'swedish'   
'it': 'italian'--- 'sr': 'serbian'--- 'uz': 'uzbek'      
'nl': 'dutch'----- 'ur': 'urdu'------ 'ht': 'haitian'    
'de': 'german'---- 'sq': 'albanian'-- 'te': 'telugu'    
'is': 'icelandic'- 'gl': 'galician'-- 'ml': 'malayalam'  
'pl': 'polish'---- 'lo': 'lao'------- 'ms': 'malay'     
'cs': 'czech'----- 'th': 'thai'------ 'be': 'belarusian'
'mn': 'mongolian'- 'bg': 'bulgarian'- 'sm': 'samoan'    
'eu': 'basque'---- 'ka': 'georgian'-- 'hy': 'armenian'  
'yo': 'yoruba'---- 'kn': 'kannada'--- 'lt': 'lithuanian'
'eo': 'esperanto'- 'et': 'estonian'-- 'kk': 'kazakh'     
'tg': 'tajik'----- 'mk': 'macedonian' 'jw': 'javanese'  
'mt': 'maltese'--- 'da': 'danish'---- 'fa': 'persian'   
'sn': 'shona'----- 'bn': 'bengali'--- 'am': 'amharic'   
'pt': 'portuguese' 'hu': 'hungarian'- 'mr': 'marathi'   
'lb': 'luxembourg' 'ky': 'kyrgyz'---- 'hmn': 'hmong'     
'cy': 'welsh'----- 'az': 'Azerbaijan' 'yi': 'yiddish'   
'ga': 'irish'----- 'sd': 'sindhi'---- 'af': 'afrikaans' 
'el': 'greek'----- 'ca': 'catalan'--- 'xh': 'xhosa' """)

#--언어>언어
		elif message.content.startswith('!!'):
			m = message.content
			if(len(m)>8):
				try:
					translator = Translator()
					txtname = message.author.display_name
					sourcetxt = m[2:4]
					targettxt = m[5:7]

					middle=translator.translate(m[7:], src=sourcetxt, dest='ja').text
					await client.send_message(message.channel,sourcetxt+"""->"""+targettxt+"""번역하였습니다. (translated it.)
["""+ txtname +"""] """+translator.translate(middle, src='ja', dest=targettxt).text)
				except:
					await client.send_message(message.channel,"""번역오류! (translation error!)""")
			elif(len(m)==2):
				await client.send_message(message.channel,"""번역할 언어를 입력하세요. (Please enter a language to translate.)""")
			else:
				await client.send_message(message.channel,"""번역할 문자를 입력하세요. (Please enter what you want to translate.)""")

	
access_token = os.environ["BOT_TOKEN"]
client.run('access_token') #디스코드 사이트 > 개발자 포털 > 내 봇 > Bot token