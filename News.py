from bs4 import BeautifulSoup
import requests



class NEWS_AMWAY:
    URL = 'https://news-ua.amway.ua/category/%d0%bd%d0%be%d0%b2%d0%be%d1%81%d1%82%d0%b8/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
    }
    results = []
    def news(self):
        full_page = requests.get(self.URL, headers=self.headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        table = soup.find("div", class_="row")
        for column in table.findAll("h2"):
            self.results.append({
                "href": column.a.get("href"),
                "title": column.a.get("title")
            })
