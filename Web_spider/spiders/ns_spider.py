# -*- coding: utf-8 -*-
import scrapy, datetime
from Web_spider.items import WebSpiderItem



class NsSpiderSpider(scrapy.Spider):
    name = 'ns_spider'
    allowed_domains = ['http://novascotiaimmigration.com/move-here/nova-scotia-demand-express-entry/']
    start_urls = ['http://http://novascotiaimmigration.com/move-here/nova-scotia-demand-express-entry//']

    def parse(self, response):

        target_string = response.xpath("//article[@role='main']/div[@class='note']")[0].extract()
        item = WebSpiderItem()
        item['crawl_time'] = datetime.datetime.now()
        item['key_word'] = target_string

        yield item
