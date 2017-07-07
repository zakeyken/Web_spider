# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymysql import connections

from Web_spider.items import WebSpiderItem, CommitItem

class WebSpiderPipeline(object):

    def __init__(self):
        self.conn = connections

    def process_item(self, item, spider):
        return item
