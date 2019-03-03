# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class StarwarsItem(scrapy.Item):
    name = scrapy.Field()
    full_description = scrapy.Field()
    image_url = scrapy.Field()
    eng_url = scrapy.Field()
    rus_url = scrapy.Field()

    rus_name = scrapy.Field()
    rus_description = scrapy.Field()
    rus_image_url = scrapy.Field()
    race = scrapy.Field()
