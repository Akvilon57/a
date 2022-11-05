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
config = configparser.ConfigParser()
config.read("config.ini")

# Присваиваем значения внутренним переменным
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
print()

mas=['brawlstars333333']#'odezhdAotYanaSaxova','DO_Tvortsov_v_Tvortse_Chat'
client = TelegramClient('bos', api_id, api_hash)
spisk=['me']
client.start()
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
print('ok')

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
t=0
s=client.iter_messages('topretsept')#zagotovka_na100
a=0
for i in s:
	a+=1
	if a==193:
		i.text=str(i.text).replace('🔝 https://t.me/topretsept 🔝','https://t.me/vkusno_poest_recepti')
		client.send_message('vkusno_poest_recepti', i)
		print(f'Tovar{a}')
			






#for dialog in client.iter_dialogs():
#	try:
#		print(dialog, "\n-----")
#	except UnicodeEncodeError as e:
#		print(e)


#dialogs = client.get_dialogs()
#for d in dialogs:
#	print(d.name)


@client.on(events.NewMessage(chats = ['MihaAnarchyst','guraanton']))
async def main(event):
	await client.send_message('dasspi', event.message)
	try:
		print(event.message)
	except UnicodeEncodeError:
		pass
	try:
		print(event.message.from_id.user_id)
	except AttributeError as e:
		print(e)



client.run_until_disconnected()



