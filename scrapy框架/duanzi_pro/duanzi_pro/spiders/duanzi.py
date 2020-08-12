import scrapy
from duanzi_pro.items import DuanziProItem


class DuanziSpider(scrapy.Spider):
    name = 'duanzi'
    # allowed_domains = []

    start_urls = ['https://duanziwang.com/category/一句话段子/1/']

    # # 基于终端指令的持久化存储
    # def parse(self, response):
    #     data_lis = []
    #     article_lis = response.xpath('/html/body/section/div/div/main/article')
    #     for article in article_lis:
    #         head = article.xpath('./div[1]/h1/a/text()').extract_first()
    #         content = article.xpath('./div[2]/p/text()').extract_first()
    #         dic = {'head': head, 'content': content}
    #         data_lis.append(dic)
    #     return data_lis

    url = 'https://duanziwang.com/category/一句话段子/%d/'
    page_num = 1

    # def start_requests(self):
    #     for url in self.start_urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # 基于管道的持久化存储
    def parse(self, response):
        article_lis = response.xpath('/html/body/section/div/div/main/article')
        for article in article_lis:
            head = article.xpath('./div[1]/h1/a/text()').extract_first()
            content = article.xpath('./div[2]/p/text()').extract_first()
            item = DuanziProItem()
            item['head'] = head
            item['content'] = content
            yield item
        if self.page_num <= 5:
            self.page_num += 1
            new_url = format(self.url % self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)
