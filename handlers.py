import requests

from Brend import BREND_health, BREND_fasion, BREND_dom, BREND_enother_produkts
from DOLAR_GRN import Currensy_grn, Currensy_rub
from News import NEWS_AMWAY
from TelegramBotAmvay import bot, dp
from aiogram.types import Message
from config import admin_id
from keyboards import ListOfButtons
from aiogram.types.reply_keyboard import ReplyKeyboardRemove
from aiogram import types
from random import choice
from bs4 import BeautifulSoup
from aiogram.types import (ReplyKeyboardRemove,
	ReplyKeyboardMarkup, KeyboardButton,
	InlineKeyboardMarkup, InlineKeyboardButton)

class Sale:
	#Данный по ктороым он будет искать
	Sale = 'https://www.amway.ua/nashi-marky/holiday-promotions'
	haders = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}
	def parse(self):
		full_page = requests.get(self.Sale, headers=self.haders)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		global results
		results = []
		for comps in soup.findAll('div', class_='layout_element component_wrapper wrapped_amway_product_teaser'):
			if soup.a.get('href') is None:
				pass
			else:
				results.append({
					'Artical':  comps.find('div', class_='sku'),
					'Link': comps.find('div', class_='panel_title'),
					'Title': comps.find('div', class_='panel_title'),
					'Price': comps.find('td', class_='cell_2 data_column'),
					})

#бот подключился
async def handle_start(message):
	print('Bot connected')
	await bot.send_message(chat_id=admin_id, text='Bot connected')

words_hello = ['привет', 'здрасте', 'хелоу', 'пр', 'hello', 'hi', 'dratute', 'дратуте', 'хай', 'ky', 'ку']
answer_hello = ['Как жизнь?', 'Чего хотел?', 'Я готов служить',]

words_by = ['пока', 'бай', 'я пошел', 'бб', 'досведания', ]
answer_by = ['Давай', 'Буду ждать......', 'Удачи', 'Приходи еще']

#Курс валют
btn_for_currency = InlineKeyboardMarkup().add(
	InlineKeyboardButton('Узнать про рубль', callback_data='btn_for_currency_ua'),
	InlineKeyboardButton('Узнать про гривну', callback_data='btn_for_currency_rub'))
btn_for_mainmenu_currency = InlineKeyboardMarkup().add(
	InlineKeyboardButton('Вернутся на главное меню ⬅️', callback_data='btn_for_mainmenu_currency'))

#Amway
btn_for_amway = InlineKeyboardMarkup(row_width=1).add(
	InlineKeyboardButton('Товары 📦', callback_data='Towar'),
	InlineKeyboardButton('Новости 🎥', callback_data='News'),
	InlineKeyboardButton('Акции 🎁' , callback_data='Sale'))
btn_for_amway_mainmenu = InlineKeyboardButton(
	'Вернутся на главное меню 🗺', callback_data='btn_for_amway_mainmenu')
#Towar
btn_for_towar = InlineKeyboardMarkup(row_width=1).add(
	InlineKeyboardButton('Бренды 🏷', callback_data='btn_for_towar_br'),
	btn_for_amway_mainmenu)

@dp.callback_query_handler(lambda call:True)
async def btn_good(call):
	if call.data == 'btn_for_currency_ua':
		await bot.edit_message_text(chat_id=call.message.chat.id,
				message_id=call.message.message_id,
				text='Прошу, подождите........')
		currensy_rub = Currensy_rub()
		dollar_rub = currensy_rub.get_currency_price_dollar_rub()
		euro_rub = currensy_rub.get_currency_price_euro_rub()
		funt_rub = currensy_rub.get_currency_price_funt_rub()
		await bot.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id, 
			text='⬇️ ₽ На данный момент курс *рубля* ₽ ⬇️'
			f'\n________________\n'
			f'|1$💰 = {dollar_rub}₽|\n|1€💶 = {euro_rub}₽|\n|1£💷 = {funt_rub}₽|'
			'\n________________',
			parse_mode= "Markdown",
			reply_markup=btn_for_mainmenu_currency)
	elif call.data == 'btn_for_currency_rub':
		await bot.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text='Прошу, подождите........')
		currensy = Currensy_grn()
		dollar = currensy.get_currency_price_dollar()
		euro = currensy.get_currency_price_euro()
		funt = currensy.get_currency_price_funt()
		await bot.edit_message_text(chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text='⬇️ ₴ На данный момент курс *гривны* ₴ ⬇️'
			f'\n________________\n'
			f'|1$💰 = {dollar}₴|\n|1€💶 = {euro}₴|\n|1£💷 = {funt}₴|'
			'\n________________',
			parse_mode= "Markdown",
			reply_markup=btn_for_mainmenu_currency)
	elif call.data == 'btn_for_mainmenu_currency':
		await bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text='💰Хочешь увидеть курс валют снова?💰',
			reply_markup=btn_for_currency)



	#Главное менню
	if call.data == 'btn_for_amway_mainmenu':
		await bot.edit_message_text(
			chat_id=call.message.chat.id, 
			message_id=call.message.message_id,
			text='🔗 Вот все что я знаю на данный момент 🔰\n'
			'                       ⬇️ *Про Amway* ⬇️',
			parse_mode= "Markdown",
			reply_markup=btn_for_amway)
	#скидки
	if call.data == 'Sale':
		sale = Sale()
		sale.parse()
		for res in results:
			if res['Artical'] is None:
				pass
			else:
				await bot.send_message(call.message.chat.id, 
					f"🔰{res['Artical'].text.replace(' ', ': ')}\n"
					f"🔗Ссылка: https://www.amway.ua/{res['Link'].a.get('href')}\n"
					f"➡️Название: {res['Title'].text}\n"
					f"💸Цена: {res['Price'].text}\n")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.username} узнал все скидки')
	# Новости
	if call.data == 'News':
		nw = NEWS_AMWAY()
		nw.news()
		list_ = ''
		num = 1
		for res in nw.results:
			list_ += f"{num}) ➡️ <a href=\"{res['href']}\">{res['title']}\n</a>\n"# 🔗Ссылка: {res['href']}\n➡️Заголовк: {res['title']}\n*******************************\n
			num += 1
			if num >= 10:
				break

		await bot.send_message(call.message.chat.id, list_)
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.username} узнал новости')

	#Товар
	if call.data == 'Towar':
		await bot.edit_message_text(
			chat_id=call.message.chat.id, 
			message_id=call.message.message_id,
			text='⬇️ *Выбери то что хочешь найти* ⬇️',
			parse_mode= "Markdown",
			reply_markup=btn_for_towar)
	#Здоровье
	elif call.data == 'btn_for_towar_br' or call.data == 'last_1':
		#Вызываю клас и функцию
		brend = BREND_health()
		brend.br_health()
		#Кнопки для Здаровье
		btn_br1 = InlineKeyboardMarkup(row_width=1)		
		i = 1
		for url in brend.results_br:
			if i == 5:
				break
			else:
				#Из класса беру результат и вывожу все в кнопку 
				btn = InlineKeyboardButton(f"{url['title'].replace('+', ' ')}", 
					callback_data=f"{url['title'].replace('+', ' ')}")
				btn_br1.add(btn)#Добовляю все в ту кнопку которую создал ранее
				i +=1
		#Добовляю кнопку вперед и вернутся на главное менню
		btn_br1.add(
		InlineKeyboardButton('Следушея категория ➡️', callback_data='next_1'),
		btn_for_amway_mainmenu)
		await bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text='🔗Бренды*(Здоровье)*🔗',
			parse_mode= "Markdown",
			reply_markup=btn_br1)
	#Красота и уход
	elif call.data == 'next_1' or call.data == 'last_2'or call.data == 'last_3':
		#Вызываю клас и функцию
		brend_fasion = BREND_fasion()
		brend_fasion.br_fasion()
		#Кнопки для Здаровье
		btn_br2 = InlineKeyboardMarkup(row_width=2)		
		i = 0
		for firm in BREND_fasion.results_br_f:
			if i == 8:
				break
			else:
				#Из класса беру результат и вывожу все в кнопку 
				btn2 = InlineKeyboardButton(f"{firm['title'].replace('+', ' ')}", 
					callback_data=f"{firm['title'].replace('+', ' ')}")
				btn_br2.add(btn2)#Добовляю все в ту кнопку которую создал ранее
				i +=1
		#Добовляю кнопку вперед и вернутся на главное менню
		btn_br2.add(
		InlineKeyboardButton('Назад ⬅️', callback_data='last_1'),
		InlineKeyboardButton('Дальше ➡️', callback_data='next_2'),
		InlineKeyboardButton('След. категория ➡️', callback_data='next_categoria'))
		btn_br2.add(btn_for_amway_mainmenu)
		await bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text='🔗Бренды*(Красота и уход за телом)№1*🔗',
			parse_mode= "Markdown",
			reply_markup=btn_br2)
	elif call.data == 'next_2':
		#Вызываю клас и функцию
		brend_fasion = BREND_fasion()
		brend_fasion.br_fasion_2()
		#Кнопки для Здаровье
		btn_br_3 = InlineKeyboardMarkup(row_width=2)		
		i = 0
		for firm in brend_fasion.results_br_f2:
			if i == 6:
				break
			else:
				if firm['title'].replace('+', ' ') == 'ARTISTRY™ Коллекция средств дополнительного ухода':
					firm['title'] = "ARTISTRY™ Collection of medium care extras"
					#Из класса беру результат и вывожу все в кнопку 
					btn3 = InlineKeyboardButton(f"{firm['title'].replace('+', ' ')}", 
						callback_data=f"{firm['title'].replace('+', ' ')}")
					btn_br_3.add(btn3)#Добовляю все в ту кнопку которую создал ранее
				else:
					#Из класса беру результат и вывожу все в кнопку 
					btn3 = InlineKeyboardButton(f"{firm['title'].replace('+', ' ')}", 
						callback_data=f"{firm['title'].replace('+', ' ')}")
					btn_br_3.add(btn3)#Добовляю все в ту кнопку которую создал ранее
				i += 1
		#Добовляю кнопку вперед и вернутся на главное менню
		btn_br_3.add(
		InlineKeyboardButton('Назад ⬅️', callback_data='last_2'),
		InlineKeyboardButton('След. категория ➡️', callback_data='next_categoria'),
		btn_for_amway_mainmenu)
		await bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text='🔗Бренды*(Красота и уход за телом)№2*🔗',
			parse_mode= "Markdown",
			reply_markup=btn_br_3)
	#Дом
	elif call.data == 'next_categoria' or call.data == 'last_4':
		#Вызываю клас и функцию
		brend_dom = BREND_dom()
		brend_dom.br_dom()
		#Кнопки для Здаровье
		btn_br_4 = InlineKeyboardMarkup(row_width=2)		
		i = 0
		for firm in brend_dom.results_br:
			if i == 3:
				break
			else:
				#Из класса беру результат и вывожу все в кнопку 
				btn4 = InlineKeyboardButton(f"{firm['title'].replace('+', ' ')}", 
					callback_data=f"{firm['title'].replace('+', ' ')}")
				btn_br_4.add(btn4)#Добовляю все в ту кнопку которую создал ранее
				i += 1
		#Добовляю кнопку вперед и вернутся на главное менню
		btn_br_4.add(
		InlineKeyboardButton('Назад ⬅️', callback_data='last_3'),
		InlineKeyboardButton('След. категория ➡️', callback_data='next_categoria_2'),
		btn_for_amway_mainmenu)
		await bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text='🔗Бренды*(Дом)*🔗',
			parse_mode= "Markdown",
			reply_markup=btn_br_4)
	#Другие продукты
	elif call.data == 'next_categoria_2':
		#Вызываю клас и функцию
		brend_dom = BREND_enother_produkts()
		brend_dom.br_enother_produkts()
		#Кнопки для Здаровье
		btn_br_5 = InlineKeyboardMarkup(row_width=2)		
		i = 0
		for firm in brend_dom.results_br:
			if i == 5:
				break
			else:
				#Из класса беру результат и вывожу все в кнопку 
				btn5 = InlineKeyboardButton(f"{firm['title'].replace('+', ' ')}", 
					callback_data=f"{firm['title'].replace('+', ' ')}{i}")
				btn_br_5.add(btn5)#Добовляю все в ту кнопку которую создал ранее
				i += 1
		#Добовляю кнопку вперед и вернутся на главное менню
		btn_br_5.add(
		InlineKeyboardButton('Назад ⬅️', callback_data='last_4'))
		btn_br_5.add(btn_for_amway_mainmenu)
		await bot.edit_message_text(
			chat_id=call.message.chat.id,
			message_id=call.message.message_id,
			text='🔗Бренды*(Другие продукты)*🔗',
			parse_mode= "Markdown",
			reply_markup=btn_br_5)

	#Кнопки для Здаровья
	if call.data == 'NUTRILITE™':
		br = BREND_health()
		url = "NUTRILITE™"
		br.br_health()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал NUTRILITE™')
	elif call.data == 'Bodykey by NUTRILITE™':
		br = BREND_health()
		url = "Bodykey+by+NUTRILITE™"
		br.br_health()
		br.nutrila(url, br.title_hrefs2)
		for title_href in br.title_hrefs2:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Bodykey by NUTRILITE™')
	elif call.data == 'Truvivity by NUTRILITE™':
		br = BREND_health()
		url = "Truvivity+by+NUTRILITE™"
		br.br_health()
		br.nutrila(url, br.title_hrefs3)
		for title_href in br.title_hrefs3:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")		
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Truvivity by NUTRILITE™')
	elif call.data == 'XS™':
		br = BREND_health()
		url = "XS™"
		br.br_health()
		br.nutrila(url, br.title_hrefs4)
		for title_href in br.title_hrefs4:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал XS™')

	#кнопки для красота и уход
	if call.data == 'ARTISTRY YOUTH XTEND™':
		br = BREND_fasion()
		url = "ARTISTRY YOUTH XTEND™"
		br.br_fasion()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY YOUTH XTEND™')
	elif call.data == 'ARTISTRY HYDRA-V™':
		br = BREND_fasion()
		url = "ARTISTRY+HYDRA-V™"
		br.br_fasion()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY HYDRA-V™')
	elif call.data == 'essentials by ARTISTRY™':
		br = BREND_fasion()
		url = "essentials by ARTISTRY™"
		br.br_fasion()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал essentials by ARTISTRY™')
	elif call.data == 'ARTISTRY INTENSIVE SKINCARE™':
		br = BREND_fasion()
		url = "ARTISTRY INTENSIVE SKINCARE™"
		br.br_fasion()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY INTENSIVE SKINCARE™')
	elif call.data == 'ARTISTRY IDEAL RADIANCE™':
		br = BREND_fasion()
		url = "ARTISTRY IDEAL RADIANCE™"
		br.br_fasion()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY IDEAL RADIANCE™')
	elif call.data == 'Flora Chic™':
		br = BREND_fasion()
		url = "Flora Chic™"
		br.br_fasion()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Flora Chic™')
	elif call.data == 'G&H':
		br = BREND_fasion()
		url = "G%26H"
		br.br_fasion()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал G&H')
	elif call.data == 'Satinique™':
		br = BREND_fasion()
		url = "Satinique™"
		br.br_fasion()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Satinique™')
	elif call.data == 'HYMM™':
		br = BREND_fasion()
		url = "HYMM™"
		br.br_fasion_2()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал HYMM™')
	elif call.data == 'Glister™':
		br = BREND_fasion()
		url = "Glister™"
		br.br_fasion_2()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Glister™')
	elif call.data == 'ARTISTRY™ Color':
		br = BREND_fasion()
		url = "ARTISTRY™ Color"
		br.br_fasion_2()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY™ Color')
	elif call.data == 'ARTISTRY SUPREME LX™':
		br = BREND_fasion()
		url = "ARTISTRY SUPREME LX™"
		br.br_fasion_2()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY SUPREME LX™')
	elif call.data == 'ARTISTRY™ Collection of medium care extras':
		br = BREND_fasion()
		url = "ARTISTRY™+Коллекция+средств+дополнительного+ухода"
		br.br_fasion_2()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY™ Collection of medium care extras')
	elif call.data == 'ARTISTRY STUDIO™':
		br = BREND_fasion()
		url = "ARTISTRY STUDIO™"
		br.br_fasion_2()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY STUDIO™')
	elif call.data == 'Artistry Signature Select™':
		br = BREND_fasion()
		url = "Artistry Signature Select™"
		br.br_fasion_2()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Artistry Signature Select™')
	
	#кнопки для ДОМ
	if call.data == 'Amway Home™':
		br = BREND_dom()
		url = "Amway Home™"
		br.br_dom()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Amway Home™')
	elif call.data == 'eSpring™':
		br = BREND_dom()
		url = "eSpring™"
		br.br_dom()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал eSpring™')
	elif call.data == 'iCook™':
		br = BREND_dom()
		url = "iCook™"
		br.br_dom()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал iCook™')

	#Кнопки для Другие продукты
	if call.data == 'NUTRILITE™0':
		br = BREND_enother_produkts()
		url = "NUTRILITE™"
		br.br_enother_produkts()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал NUTRILITE™0')
	elif call.data == 'Truvivity by NUTRILITE™1':
		br = BREND_enother_produkts()
		url = "Truvivity by NUTRILITE™"
		br.br_enother_produkts()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Truvivity by NUTRILITE™1')
	elif call.data == 'XS™2':
		br = BREND_enother_produkts()
		url = "XS™"
		br.br_enother_produkts()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал XS™2')
	elif call.data == 'G&H3':
		br = BREND_enother_produkts()
		url = "G%26H"
		br.br_enother_produkts()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал G&H3')
	elif call.data == 'ARTISTRY STUDIO™4':
		br = BREND_enother_produkts()
		url = "ARTISTRY STUDIO™"
		br.br_enother_produkts()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал ARTISTRY STUDIO™4')
	elif call.data == 'Artistry Signature Select™5':
		br = BREND_enother_produkts()
		url = "Artistry Signature Select™"
		br.br_enother_produkts()
		title_hrefs1 = []
		br.nutrila(url, title_hrefs1)
		for title_href in title_hrefs1:
			await bot.send_message(call.message.chat.id,
				f"Ссылка: https://www.amway.ua{title_href['href']}\n"
				f"{title_href['artical']}\nЦена: {title_href['money']}")
		await bot.send_message(chat_id=admin_id, text=f'{call.from_user.first_name} узнал Artistry Signature Select™5')



#Все команды
@dp.message_handler(commands=['help', 'start'])
async def help(user: types.Message):
	kb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
	kb_menu.add(
		KeyboardButton('/Amway'),
		KeyboardButton('дай ссылку'))
	kb_menu.add(KeyboardButton('/currency'))
	await bot.send_message(user.chat.id, #user.from_user.id
		'🔥Команды🔥\n\n'
		'1) /Amway - узнать все скидки на данный моммент\n'
		'2) Дай ссылку - Ссылка на сайт\n'
		'2) /currency - Узнать курс валют (к гривне, к рублю)\n',
		reply_markup=kb_menu)
	await bot.send_message(chat_id=admin_id, text=f'{user.from_user.first_name} воспользевался командой Help')

@dp.message_handler(commands=['Amway'])
async def amway(message: types.Message):
	await bot.send_message(message.chat.id, '🔗 Вот все что я знаю на данный момент 🔰\n'
		'                       ⬇️ *Про Amway* ⬇️',
		parse_mode= "Markdown",
		reply_markup=btn_for_amway)
	await bot.send_message(chat_id=admin_id, text=f'{message.from_user.first_name} узнал Amway')	

#Курс волют
@dp.message_handler(commands=['currency'])
async def dollar(message: types.Message):
	await bot.send_message(message.chat.id, '💰Привет, хочешь увидеть курс волют?💶',
		reply_markup=btn_for_currency)
	await bot.send_message(chat_id=admin_id, text=f'{message.from_user.first_name} узнал курс валют')	

# команда по запуску этих все function
@dp.message_handler()
async def send_text(message: Message):
	if message.text.lower() == 'дай ссылку':
		btn = InlineKeyboardMarkup().add(InlineKeyboardButton('Amway', url="https://www.amway.ua/"))
		await bot.send_message(message.chat.id, '⬇️ Ссылка на сайт Amway ⬇️', reply_markup=btn)
		await bot.send_message(chat_id=admin_id, text=f'{message.from_user.username} узнал ссылку на сайт Amway')
