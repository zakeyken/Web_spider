# -*- coding: utf-8 -*-
import scrapy


class SaSpiderSpider(scrapy.Spider):
    name = 'sa_spider'
    allowed_domains = ['https://immigration.saskatchewan.ca']
    start_urls = ['http://https://immigration.saskatchewan.ca/']

    def parse(self, response):
        pass
