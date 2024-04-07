from scrapy.crawler import CrawlerProcess
from Atelier1.spiders.cnn_spider import CNNWorldSpider  # Chemin relatif au Spider

process = CrawlerProcess()
process.crawl(CNNWorldSpider)
process.start()
