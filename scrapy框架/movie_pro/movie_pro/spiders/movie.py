import scrapy
from movie_pro.items import MovieProItem


class MovieSpider(scrapy.Spider):
    name = 'movie'
    # allowed_domains = ['www.aaa.com']
    start_urls = ['https://www.4567kan.com/index.php/vod/show/id/5/page/1.html']

    url = 'https://www.4567kan.com/index.php/vod/show/id/5/page/%d.html'
    page_num = 1

    def parse(self, response):
        li_lis = response.xpath('/html/body/div[1]/div/div/div/div[2]/ul/li')
        for li in li_lis:
            title = li.xpath('./div/a/@title').extract_first()
            href = 'https://www.4567kan.com/'+li.xpath('./div/a/@href').extract_first()
            item = MovieProItem()
            item['title'] = title
            yield scrapy.Request(url=href, callback=self.parse_detail, meta={'item': item})

        if self.page_num <= 5:
            self.page_num += 1
            new_url = format(self.url % self.page_num)
            yield scrapy.Request(url=new_url, callback=self.parse)

    def parse_detail(self, response):
        detail = response.xpath('/html/body/div[1]/div/div/div/div[2]/p[5]/span[2]/text()').extract_first()
        item = response.meta['item']
        item['detail'] = detail
        yield item
