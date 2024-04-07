BOT_NAME = 'Atelier1'

SPIDER_MODULES = ['Atelier1.spiders']
NEWSPIDER_MODULE = 'Atelier1.spiders'

ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
DOWNLOAD_DELAY = 3

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'Atelier1.pipelines.MongoPipeline': 300,  # Adjust the priority as needed
}

MONGO_URI = 'mongodb://localhost:27017/'
MONGO_DATABASE = 'cnn'
