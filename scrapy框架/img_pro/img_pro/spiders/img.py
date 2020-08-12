import scrapy
from img_pro.items import ImgProItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.aaa.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/']

    def parse(self, response):
        li_lis = response.xpath('/html/body/div[4]/div[2]/div[2]/ul/li')
        for li in li_lis:
            img_src = 'http://www.521609.com/'+li.xpath('./a/img/@src').extract_first()
            img_name = li.xpath('./a/img/@alt').extract_first()+'.jpg'
            item = ImgProItem()
            item['src'] = img_src
            item['name'] = img_name
            yield item
