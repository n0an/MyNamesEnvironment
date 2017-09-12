# -*- coding: utf-8 -*-
import scrapy


class GotspiderSpider(scrapy.Spider):
    name = 'gotspider'
    allowed_domains = ['http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%94%D0%BE%D0%BC_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2']
    start_urls = ['http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%94%D0%BE%D0%BC_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2']

    def parse(self, response):

        table = response.xpath('//*[@class="mw-content-ltr"]')[1]

        links = table.xpath('.//a/@href').extract()

        urls = []

        for link in links:
            url = 'http://ru.gameofthrones.wikia.com' + link
            urls.append(url)
            print('url = ',url)
            yield {'Url': url}
