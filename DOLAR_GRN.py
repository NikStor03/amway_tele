from bs4 import BeautifulSoup
import requests


class Currensy_grn:
	#Ссылка на сам ссайт
	DOLAR_UA = 'https://www.google.com/search?sxsrf=ALeKk03fHfLO2ZLgvH2aCYHyylK169bp7Q%3A1584807405441&ei=7T12Xt69Gsyf6ASQjpvADw&q=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D0%B0+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_l=psy-ab.3..0i7i30j0i7i10i30l9.96278.96485..97742...0.2..0.99.195.2......0....1..gws-wiz.......0i71.ruuxORUhmxA&ved=0ahUKEwie6MDT-6voAhXMD5oKHRDHBvgQ4dUDCAs&uact=5'
	EURO_UA = 'https://www.google.com/search?sxsrf=ALeKk00nmSjKVbsph2SV1RR2nLWcgcV-KA%3A1585942862164&ei=TpGHXqjJCajIrgTtiJyQAg&q=%D1%8D%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=%D1%8D%D0%B2%D1%80%D0%BE+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoECAAQRzoICAAQBxAKEB46BggAEAcQHjoKCAAQBxAFEAoQHkoJCBcSBTEwLTkxSggIGBIEMTAtNFCSNliwPGCIP2gAcAF4AIABdogBrwOSAQMxLjOYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwioqLvHgc3oAhUopIsKHW0EByIQ4dUDCAw&uact=5'
	FUNT_UA = 'https://www.google.com/search?sxsrf=ALeKk03aNMecHdZdmkMNpa8hpgl7FfGowQ%3A1585943618111&ei=QpSHXqOwBumMrgSthJPAAQ&q=%D1%84%D1%83%D0%BD%D1%82+%D0%BA+%D0%B3%D1%80%D0%B8%D0%B2%D0%BD%D0%B5&oq=aeyn+r+uhbdyt&gs_lcp=CgZwc3ktYWIQA1AAWABgocwHaABwAHgAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwij2favhM3oAhVphosKHS3CBBgQ4dUDCAw&uact=5'
	#Для таго чтоб сайт понял что вы не бот
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
	}


	def get_currency_price_dollar(self):
		try:
			#делаем запрос на самом сайте
			full_page = requests.get(self.DOLAR_UA, headers=self.headers)
			
			#Делаю так чтоб мы парсели через библиотеку бютифулл суп
			soup = BeautifulSoup(full_page.content, 'html.parser')
			
			#Нахожу все нужные елементы 
			convert1 = soup.find('span', {'class': 'DFlfde', 
											'class': 'SwHCTb',
											'data-precision': 2}) 
			return convert1.text
		except AttributeError:
			return f'К сажелению меня не пустили на сайт.\nПоробуйте снова.'

	def get_currency_price_euro(self):
		try:
			#делаем запрос на самом сайте
			full_page = requests.get(self.EURO_UA, headers=self.headers)
			
			#Делаю так чтоб мы парсели через библиотеку бютифулл суп
			soup = BeautifulSoup(full_page.content, 'html.parser')
			
			#Нахожу все нужные елементы 
			convert2 = soup.find('span', {'class': 'DFlfde', 
											'class': 'SwHCTb',
											'data-precision': 2}) 
			return convert2.text
		except AttributeError:
			return f'К сажелению меня не пустили на сайт.\nПоробуйте снова.'

	def get_currency_price_funt(self):
		try:
			#делаем запрос на самом сайте
			full_page = requests.get(self.FUNT_UA, headers=self.headers)
			
			#Делаю так чтоб мы парсели через библиотеку бютифулл суп
			soup = BeautifulSoup(full_page.content, 'html.parser')
			
			#Нахожу все нужные елементы 
			convert3 = soup.find('span', {'class': 'DFlfde', 
											'class': 'SwHCTb',
											'data-precision': 2}) 
			return convert3.text
		except AttributeError:
			return f'К сажелению меня не пустили на сайт.\nПоробуйте снова.'
class Currensy_rub():
	#Ссылка на сам ссайт
	DOLAR_RUB = 'https://www.google.com/search?sxsrf=ALeKk00ccGasjaTNM6rnRts62iwmKaYsfw%3A1586006258048&ei=8oiIXqWvApLsrgTHnobABA&q=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQA1AAWABghIoCaABwAHgAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwil8Pzc7c7oAhUStosKHUePAUgQ4dUDCAw&uact=5'
	EURO_RUB = 'https://www.google.com/search?sxsrf=ALeKk0028uy6z9AF4bcG2si08XhxMT38_A%3A1586006340371&ei=RImIXuOMFumqrgTcvay4Cw&q=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=%D0%B5%D0%B2%D1%80%D0%BE+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQAzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQRzIECAAQR0oJCBcSBTEwLTExSggIGBIEMTAtMlAAWABgkYIDaABwAngAgAEAiAEAkgEAmAEAqgEHZ3dzLXdpeg&sclient=psy-ab&ved=0ahUKEwjjvp2E7s7oAhVplYsKHdweC7cQ4dUDCAw&uact=5'
	FUNT_RUB = 'https://www.google.com/search?sxsrf=ALeKk03OlYb4_oeZ2ZZR9_pt01g3-Gi03Q%3A1586006437273&ei=pYmIXpuUEKmFwPAPne64iAI&q=%D1%84%D1%83%D0%BD%D1%82+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=qeyn+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=CgZwc3ktYWIQA1AAWABguxJoAHAAeACAAQCIAQCSAQCYAQCqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwjb-rey7s7oAhWpAhAIHR03DiEQ4dUDCAw&uact=5'
	#Для таго чтоб сайт понял что вы не бот
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
	

	def get_currency_price_dollar_rub(self):
		try:	
			#делаем запрос на самом сайте
			full_page = requests.get(self.DOLAR_RUB, headers=self.headers)
			
			#Делаю так чтоб мы парсели через библиотеку бютифулл суп
			soup = BeautifulSoup(full_page.content, 'html.parser')
			
			#Нахожу все нужные елементы 
			convert1 = soup.find('span', {'class': 'DFlfde', 
											'class': 'SwHCTb',
											'data-precision': 2}) 
			return convert1.text
		except AttributeError:
			return f'К сажелению меня не пустили на сайт.\nПоробуйте снова.'	
	
	def get_currency_price_euro_rub(self):
		try:
			#делаем запрос на самом сайте
			full_page = requests.get(self.EURO_RUB, headers=self.headers)
			
			#Делаю так чтоб мы парсели через библиотеку бютифулл суп
			soup = BeautifulSoup(full_page.content, 'html.parser')
			
			#Нахожу все нужные елементы 
			convert2 = soup.find('span', {'class': 'DFlfde', 
											'class': 'SwHCTb',
											'data-precision': 2}) 
			return convert2.text
		except AttributeError:
			return f'К сажелению меня не пустили на сайт.\nПоробуйте снова.'	
	
	def get_currency_price_funt_rub(self):
		try:
			#делаем запрос на самом сайте
			full_page = requests.get(self.FUNT_RUB, headers=self.headers)
			
			#Делаю так чтоб мы парсели через библиотеку бютифулл суп
			soup = BeautifulSoup(full_page.content, 'html.parser')
			
			#Нахожу все нужные елементы 
			convert3 = soup.find('span', {'class': 'DFlfde', 
											'class': 'SwHCTb',
											'data-precision': 2}) 
			return convert3.text
		except AttributeError:
			return f'К сажелению меня не пустили на сайт.\nПоробуйте снова.'
		