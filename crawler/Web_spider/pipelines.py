# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import connect

from scrapy.log import logger
from Web_spider.items import WebSpiderItem, CommitItem

class WebSpiderPipeline(object):

    def __init__(self):
        self.conn = connect(
            host = 'rm-uf6vwd4k0y2o4b33bo.mysql.rds.aliyuncs.com',
            port = 3306,
            user = 'root',
            password ='Myzh1987',
            db = 'ca_immigration',
            charset = 'utf8'
        )
        self.cursor = self.conn.cursor()
        self.sql = "INSERT IGNORE INTO ns_data (`crawl_time`, `key_word`) VALUES (%s,%s)"

    def process_item(self, item, spider):
        try:
            self.cursor.execute(self.sql, (item['crawl_time'], item['key_word']))
            self.conn.commit()
        except Exception , e:
            logger.warning("execute sql fail.")
            logger.warning(str(e))
            logger.warning(item)
