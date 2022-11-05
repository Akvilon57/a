import configparser
import json
import time

from telethon.sync import TelegramClient
from telethon import connection,events

# для корректного переноса времени сообщений в json
from datetime import date, datetime

# классы для работы с каналами
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
# класс для работы с сообщениями
from telethon.tl.functions.messages import GetHistoryRequest
from telethon import functions, types

# Считываем учетные данные



	
	




#Юзеры в группе
def iduser(client):
    for masiv in mas:
        participants = client.get_participants(masiv)
        for participant in participants:
            print(participant.to_dict()['username'],participant.to_dict()['phone'],participant.to_dict()['id'])
            if participant.to_dict()['username'] != None:
            	spisk.append(str(participant.to_dict()['username']))

#iduser(client)
#client.send_message('me', 'hi')
#print(client.get_me())


def dump_all_participants(channel):
	offset_user = 0
	limit_user = 100
	all_participants = []
	filter_user = ChannelParticipantsSearch('')
	while True:
		participants = client(GetParticipantsRequest(channel,filter_user, offset_user, limit_user, hash=0))
		
		#if not participants.users:
		#	break
		all_participants.extend(participants.users)
		offset_user += len(participants.users)
		for p in participants.users:
			print(p.id)
	
import time,random
#Парсер сообщений группы Телеграм

def vkusno_poest(client):
	t=0
	s=client.iter_messages('topretsept')#zagotovka_na100
	a=0
	key=0
	with open('vkusno.txt', 'r', encoding='utf-8') as file_object:
	    key=file_object.read()
	    key=int(key)
	    file_object.close()


	for i in s:
		a+=1
		if a==key:
			i.text=str(i.text).replace('🔝 https://t.me/topretsept 🔝','https://t.me/vkusno_poest_recepti')
			client.send_message('vkusno_poest_recepti', i)
			print(f'Tovar{a}')

			
			with open('vkusno.txt', 'w', encoding='utf-8') as file:
				file.write(f'{key+1}')
				file.close()
			client.run_until_disconnected()	



			






#for dialog in client.iter_dialogs():
#	try:
#		print(dialog, "\n-----")
#	except UnicodeEncodeError as e:
#		print(e)


#dialogs = client.get_dialogs()
#for d in dialogs:
#	print(d.name)


#@client.on(events.NewMessage(chats = ['MihaAnarchyst','guraanton']))
#async def main(event):
#	await client.send_message('dasspi', event.message)
#	try:
#		print(event.message)
#	except UnicodeEncodeError:
#		pass
#	try:
#		print(event.message.from_id.user_id)
#	except AttributeError as e:
#		print(e)


#telethon_on(vkusno_poest())
import schedule
import time
def timer(func):
    
    
    #schedule.every(2).minutes.do(func)
    #schedule.every().hour.do(job)
    #schedule.every('2').day.do(func)
    #schedule.every().monday.do(func)
    #schedule.every().wednesday.at("13:15").do(job)
    #schedule.every().minute.at(":17").do(job)
    #schedule.every(4).days.at("02:00").do(func)
    #schedule.every().days.at("13:30:00").do(func)
    schedule.every().day.at("10:00").do(func)
    schedule.every().day.at("18:01").do(func)

    while True:
        schedule.run_pending()
    
        time.sleep(1)



if __name__ == '__main__': 
	config = configparser.ConfigParser()
	config.read("config.ini")
	api_id   = config['Telegram']['api_id']
	api_hash = config['Telegram']['api_hash']
	username = config['Telegram']['username']
	client = TelegramClient('bos', api_id, api_hash)
	client.start()
	def main():
		vkusno_poest(client)
	
	timer(main)

