# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

# class ImgProPipeline:
#     def process_item(self, item, spider):
#         return item


from scrapy.pipelines.images import ImagesPipeline
import scrapy


class ImgPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(url=item['src'], meta={'item': item})

    def file_path(self, request, response=None, info=None):
        item = request.meta['item']
        file_path = item['name']
        return file_path

    def item_completed(self, results, item, info):
        return item
