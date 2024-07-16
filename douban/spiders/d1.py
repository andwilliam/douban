import scrapy


class D1Spider(scrapy.Spider):
    name = "d1"
    allowed_domains = ["douban.com"]
    start_urls = ["https://douban.com"]

    def parse(self, response):
        pass
