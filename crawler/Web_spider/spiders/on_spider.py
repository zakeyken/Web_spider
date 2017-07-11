# -*- coding: utf-8 -*-
import scrapy


class OnSpiderSpider(scrapy.Spider):
    name = 'on_spider'
    allowed_domains = ['http://www.ontarioimmigration.ca/en/pnp/OI_PNPNEW.html']
    start_urls = ['http://http://www.ontarioimmigration.ca/en/pnp/OI_PNPNEW.html/']

    def parse(self, response):
        pass
