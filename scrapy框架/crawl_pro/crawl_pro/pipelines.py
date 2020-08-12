# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CrawlProPipeline:
    f = None

    def open_spider(self, spider):
        self.f = open('./daxuemeinv.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        try:
            self.f.write(item['name'] + '\n')
        except TypeError as e:
            print(e)
        return item

    def close_spider(self, spider):
        self.f.close()
