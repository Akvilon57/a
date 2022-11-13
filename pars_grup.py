import configparser
import json
import time,random,schedule

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
from telethon.tl.functions.channels import InviteToChannelRequest

# Считываем учетные данные

config = configparser.ConfigParser()
config.read("config.ini")
api_id   = config['Telegram']['api_id']
api_hash = config['Telegram']['api_hash']
username = config['Telegram']['username']
	

grups=['ReceptyKulinariya','zv_kulinariya','retseptyChat','varka01','keto_vkusno','chat_eda','Goa_Food_Cafe_chat']#'chatvkus''ReceptyKulinariya','zv_kulinariya','retseptyChat','varka01','keto_vkusno','chat_eda','Goa_Food_Cafe_chat'


	




#Юзеры в группе
def iduser():
	client = TelegramClient('bos', api_id, api_hash)
	client.start()
	for masiv in grups:
		spisk_list=[]
		try:
			participants = client.get_participants(masiv)
		except Exception as e:
			print(e)
		for participant in participants:
			
			#print(participant.to_dict()['username'],participant.to_dict()['phone'],participant.to_dict()['id'])
			if participant.to_dict()['username'] != None:
				if participant.to_dict()['bot'] == False:
					spisk_list.append(str(participant.to_dict()['username']))
					print(participant.to_dict()['username'])

	#	with open("rassilka.json", 'r+',encoding='utf-8') as fe:
	#		f=json.load(fe)
	#		if len(f)==0:
	#			f=[]
	#		for namb in spisk_list:
	#			if namb not in f:
	#				f.append(namb)
	#		fe.seek(0)
	#		fe.truncate(0)
	#		json.dump(f, fe)
	#		fe.close()
	#		print(len(f))

# 	Добавление юзеров в группу
def add_user():
	client = TelegramClient('bos', api_id, api_hash)
	client.start()
	with open("rassilka.json", 'r+',encoding='utf-8') as fe:
		f=json.load(fe)
		print(len(f))
		if len(f)==0:
			f=[]
			fe.seek(0)
			fe.truncate(0)
			json.dump(f, fe)
			fe.close()
			print('Spisok pust')

		else:
			print('start')
	
			try:
				us=random.randint(10,20)
				client(InviteToChannelRequest(channel='vkusno_poest_recepti', users = f[:us]))
				for i in f[:us]:	
					f.remove(i)
			except Exception as e:
				print(e)
			
			fe.seek(0)
			fe.truncate(0)
			json.dump(f, fe)
			fe.close()	
			print(len(f))

	



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
	

#Парсер сообщений группы Телеграм

def vkusno_poest():
	client = TelegramClient('bos', api_id, api_hash)
	client.start()
	t=0
	s=client.iter_messages('topretsept')#zagotovka_na100
	a=0
	k=0
	key=0
	vkusno=[]
	print(type(s))
	with open('vkusno.txt', 'r', encoding='utf-8') as file_object:
	    key=file_object.read()
	    key=int(key)
	    file_object.close()

	if len(vkusno)==0:
		for ii in s:
			vkusno.append(ii)
		print(len(vkusno))

	numb=len(vkusno)-1-key
	i=vkusno[numb]
	
	
	try:
		i.text=str(i.text).replace('🔝 https://t.me/topretsept 🔝','https://t.me/vkusno_poest_recepti').replace('🔝https://t.me/topretsept🔝','https://t.me/vkusno_poest_recepti')
		client.send_message('vkusno_poest_recepti', i)
		print(f'Tovar{numb}')
		
	except Exception as e:
		print(f'Error: {e}')
		key+=1
	
					
	with open('vkusno.txt', 'w', encoding='utf-8') as file:
		file.write(f'{key+1}')
		file.close()
				

	print('disconnect')
	client.disconnect()
	print('end')
	vkusno=[]
			#client.run_until_disconnected()

def anekdot():
	client = TelegramClient('bos', api_id, api_hash)
	client.start()

	spis=['AnekdotRu','AnekdotRu','AnekdotRu','AnekdotRu','anekdot18']
	number=random.randint(0,len(spis)-1)
	channnel = spis[number]
	print(channnel)

	k=0
	t=0
	s=client.iter_messages(channnel)
	a=0
	key=0
	with open(f'{channnel}.txt', 'r', encoding='utf-8') as file_object:
	    key=file_object.read()
	    key=int(key)
	    file_object.close()

	 
	vkusno=[]
	if len(vkusno)==0:
		for ii in s:
			vkusno.append(ii)
		print(len(vkusno))

	numb=len(vkusno)-1-key
	i=vkusno[numb]


	try:
		while True:
			a=str(i.text)
			if a.find('www')>=0:
				numb-=1
				key+=1
				i=vkusno[numb]
			else:
				i=str(i.text).replace('▶️','').replace(f'@{channnel}','https://t.me/anekdot_days')
				
		client.send_message('anekdot_days', i)
		print(f'Tovar{numb}')	
	except Exception as e:
		print(f'Error: {e}')
		key+=1
	
				
				


			

			
	with open(f'{channnel}.txt', 'w', encoding='utf-8') as file:
		file.write(f'{key+1}')
		file.close()
				
	#client.run_until_disconnected()
	print('disconnect')
	client.disconnect()
	print('end')
	vkusno=[]

				


			






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

def timer(vkusno1):
    
    
    #schedule.every(2).minutes.do(func)
    #schedule.every().hour.do(job)
    #schedule.every('2').day.do(func)
    #schedule.every().monday.do(func)
    #schedule.every().wednesday.at("13:15").do(job)
    #schedule.every().minute.at(":17").do(job)
    #schedule.every(4).days.at("02:00").do(func)
    #schedule.every().days.at("13:30:00").do(func)
	schedule.every().day.at("07:14").do(vkusno1)
	schedule.every().day.at("11:13").do(vkusno1)
	schedule.every().day.at("16:10").do(vkusno1)
	#schedule.every().day.at("07:17").do(anekdot2)
	#schedule.every().day.at("11:17").do(anekdot2)
	#schedule.every().day.at("16:15").do(anekdot2)


	while True:
		schedule.run_pending()
		print('ok')
		time.sleep(58)

def main():
	vkusno_poest()
	add_user()

if __name__ == '__main__': 
	
	while True:
		try:
			timer(main)
		except Exception as d:
			print(d)
		print('next')
		time.sleep(120)

	#anekdot()
	#vkusno_poest()
	#iduser()
	#add_user()
	

	

