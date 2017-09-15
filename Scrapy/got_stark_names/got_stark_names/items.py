# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GotItem(scrapy.Item):
    name = scrapy.Field()
    full_description = scrapy.Field()
    image_url = scrapy.Field()
    rus_url = scrapy.Field()
    eng_url = scrapy.Field()
