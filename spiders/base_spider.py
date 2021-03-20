import scrapy

class BaseSpider(scrapy.Spider):
    name = None
    start_urls = []