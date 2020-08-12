# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql


# 存储到本地的管道
class DuanziProPipeline:
    fp = None

    def open_spider(self, spider):
        self.fp = open('duanzi.txt', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write(item['head'] + ':' + item['content'] + '\n')
        return item

    def close_spider(self, spider):
        self.fp.close()


# 存储到mysql数据库的管道
class MysqlPipeline:
    conn = None
    cursor = None

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='1004',
            database='scrapy_db',
            charset='utf8'
        )
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        sql = 'insert into duanzi (head,content) values (%s, %s)'
        try:
            self.cursor.execute(sql, (item['head'], item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.conn.close()
