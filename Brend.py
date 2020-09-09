from bs4 import BeautifulSoup
import requests



class BREND_health:
	URL = 'https://www.amway.ua/ru/Nutrition'
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}
	results_br = []
	def br_health(self):
		full_page = requests.get(self.URL, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		global results_br
		for comps in soup.find_all('span', class_='checkbox_text')[3:7]:
			self.results_br.append({
				'title': comps.text.replace(' ', '+')
				})

	def nutrila(self, url, name):
		url1 = f"https://www.amway.ua/ru/Nutrition?бренд={url}#.XosrIMgza3d"

		full_page1 = requests.get(url1, headers=self.headers)
		soup = BeautifulSoup(full_page1.content, 'html.parser')
		
		table = soup.find('tbody')#Нахожу Tbody
		#Тут я все перебераю и сохраняю в переменную 
		for row1 in table.find_all('div', class_='product_list_variant current'):
			try:
				#сохранняю все в список
				name.append({
					'href': row1.a.get('href'),
					'artical': row1.find('span', class_='sku').text,
					'money': row1.find('span', class_='money').text,
					})
			except AttributeError:
				#сохранняю все в список
				name.append({
					'href': row1.a.get('href'),
					'artical': row1.find('span', class_='sku').text,
					'money': row1.find('span', class_='money'),
					})



class BREND_fasion:
	URL = 'https://www.amway.ua/ru/krasota-i-ukhod-za-telom'
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}
	results_br_f = []
	results_br_f2 = []
	def br_fasion(self):
		full_page = requests.get(self.URL, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		global results_br_f
		for comps in soup.find_all('span', class_='checkbox_text')[2:10]:
			self.results_br_f.append({
				'title': comps.text.replace(' ', '+')
				})
	def br_fasion_2(self):
		full_page1 = requests.get(self.URL, headers=self.headers)
		soup1 = BeautifulSoup(full_page1.content, 'html.parser')
		global results_br_f2
		for comps1 in soup1.find_all('span', class_='checkbox_text')[10:16]:
			self.results_br_f2.append({
				'title': comps1.text.replace(' ', '+')
				})
	def nutrila(self, url, name):
		url1 = f"https://www.amway.ua/ru/krasota-i-ukhod-za-telom?бренд={url.replace(' ', '+')}#.XoxC88gza3c"

		full_page1 = requests.get(url1, headers=self.headers)
		soup = BeautifulSoup(full_page1.content, 'html.parser')
		
		table = soup.find('tbody')#Нахожу Tbody
		#Тут я все перебераю и сохраняю в переменную 
		for row1 in table.find_all('div', class_='product_list_variant current'):
			try:
				#сохранняю все в список
				name.append({
					'href': row1.a.get('href'),
					'artical': row1.find('span', class_='sku').text,
					'money': row1.find('span', class_='money').text,
					})
			except AttributeError:
				#сохранняю все в список
				name.append({
					'href': row1.a.get('href'),
					'artical': row1.find('span', class_='sku').text,
					'money': row1.find('span', class_='money'),
					})	


class BREND_dom:
	URL = 'https://www.amway.ua/ru/dom'
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}
	results_br = []
	def br_dom(self):
		full_page = requests.get(self.URL, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		global results_br
		for comps in soup.find_all('span', class_='checkbox_text')[1:4]:
			self.results_br.append({
				'title': comps.text.replace(' ', '+')
				})
	def nutrila(self, url, name):
		url1 = f"https://www.amway.ua/ru/dom?бренд={url.replace(' ', '+')}#.XoxC88gza3c"

		full_page1 = requests.get(url1, headers=self.headers)
		soup = BeautifulSoup(full_page1.content, 'html.parser')
		
		table = soup.find('tbody')#Нахожу Tbody
		#Тут я все перебераю и сохраняю в переменную 
		for row1 in table.find_all('div', class_='product_list_variant current'):
			try:
				#сохранняю все в список
				name.append({
					'href': row1.a.get('href'),
					'artical': row1.find('span', class_='sku').text,
					'money': row1.find('span', class_='money').text,
					})
			except AttributeError:
				#сохранняю все в список
				name.append({
					'href': row1.a.get('href'),
					'artical': row1.find('span', class_='sku').text,
					'money': row1.find('span', class_='money'),
					})	
class BREND_enother_produkts:
	URL = 'https://www.amway.ua/ru/drugie-produkty'
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}
	results_br = []
	def br_enother_produkts(self):
		full_page = requests.get(self.URL, headers=self.headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		global results_br
		for comps in soup.find_all('span', class_='checkbox_text')[0:6]:
			self.results_br.append({
				'title': comps.text.replace(' ', '+')
				})
	def nutrila(self, url, name):
		url1 = f"https://www.amway.ua/ru/drugie-produkty?бренд={url.replace(' ', '+')}#.Xoxg-Mgza3c"

		full_page1 = requests.get(url1, headers=self.headers)
		soup = BeautifulSoup(full_page1.content, 'html.parser')
		
		table = soup.find('tbody')#Нахожу Tbody
		#Тут я все перебераю и сохраняю в переменную 
		for row1 in table.find_all('div', class_='product_list_variant current'):
			try:
				#сохранняю все в список
				name.append({
					'href': row1.a.get('href'),
					'artical': row1.find('span', class_='sku').text,
					'money': row1.find('span', class_='money').text,
					})
			except AttributeError:
				#сохранняю все в список
				name.append({
					'href': row1.a.get('href'),
					'artical': row1.find('span', class_='sku').text,
					'money': row1.find('span', class_='money'),
					})