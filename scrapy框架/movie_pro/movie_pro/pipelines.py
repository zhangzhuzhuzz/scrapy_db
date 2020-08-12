# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class MovieProPipeline:
    f = None

    def open_spider(self, spider):
        self.f = open('./movie.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        print(type(item['title']))
        print(type(item['detail']))
        self.f.write(item['title']+'>>>'+item['detail']+'\n')
        return item

    def close_spider(self, spider):
        self.f.close()
