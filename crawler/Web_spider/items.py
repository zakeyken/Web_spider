# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class WebSpiderItem(scrapy.Item):
    """关键字存Item"""
    crawl_time = scrapy.Field()
    key_word = scrapy.Field()


class CommitItem(scrapy.Item):
    pass
