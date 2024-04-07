import scrapy
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['scrapy_db']
collection = db['articles']

class CNNWorldSpider(scrapy.Spider):
    name = 'cnn_world'
    start_urls = ['https://arabic.cnn.com/world']

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        for link in links:
            href = link.get('href')
            if href and not href.startswith('#') and not href.startswith('javascript:'):
                full_url = urljoin(response.url, href)
                yield scrapy.Request(full_url, callback=self.parse_article)

    def parse_article(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.find('h1')
        text_elements = soup.find_all('p')

        article_text = ''
        for element in text_elements:
            if element.text.strip():
                article_text += element.text.strip() + ' '

        # Stockage des données dans MongoDB
        collection.insert_one({
            'title': title.text.strip() if title else None,
            'text': article_text.strip(),
            'url': response.url
        })

        yield {
            'title': title.text.strip() if title else None,
            'text': article_text.strip(),
            'url': response.url
        }