import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawl_pro.items import CrawlProItem


class FirstSpider(CrawlSpider):
    name = 'first'
    # allowed_domains = ['www.aaa.com']
    start_urls = ['http://www.521609.com/daxuemeinv/']

    rules = (
        Rule(LinkExtractor(allow=r'list8\d+\.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        li_lis = response.xpath('/html/body/div[4]/div[2]/div[2]/ul/li')
        for li in li_lis:
            href = 'http://www.521609.com/'+li.xpath('./a/@href').extract_first()
            yield scrapy.Request(url=href, callback=self.parse_href)

    def parse_href(self, response):
        alt = response.xpath('//*[@id="bigimg"]/@alt').extract_first()
        item = CrawlProItem()
        item['name'] = alt
        yield item
