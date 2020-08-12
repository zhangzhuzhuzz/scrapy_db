import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.aaa.com']
    start_urls = ['https://www.baidu.com/', 'https://www.taobao.com/']

    def parse(self, response):
        print(response)
