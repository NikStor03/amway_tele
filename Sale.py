import requests
from bs4 import BeautifulSoup

results = []

class Sale:
	#Данный по ктороым он будет искать
	Sale = 'https://www.amway.ua/nashi-marky/holiday-promotions'
	haders = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
	}
	def parse(self):
		full_page = requests.get(self.Sale, headers=self.haders)
		soup = BeautifulSoup(full_page.content, 'html.parser')
		global results
		for comps in soup.findAll('div', class_='layout_element component_wrapper wrapped_amway_product_teaser'):
			if soup.a.get('href') is None:
				pass
			else:
				results.append({
					'Artical':  comps.find('div', class_='sku'),
					'Link': comps.find('div', class_='panel_title'),
					'Title': comps.find('div', class_='panel_title'),
					'Price': comps.find('td', class_='cell_2 data_column'),
					'Image': comps.find('img')
					})