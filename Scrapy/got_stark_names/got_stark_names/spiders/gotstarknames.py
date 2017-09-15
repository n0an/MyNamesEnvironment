# -*- coding: utf-8 -*-
import re
from scrapy import Spider
from scrapy.http import Request
from got_stark_names.items import GotItem

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

class GotstarknamesSpider(Spider):
    name = 'gotstarknames'
    allowed_domains = ['ru.gameofthrones.wikia.com']
    # start_urls = ['http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%94%D0%BE%D0%BC_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2/']

    def __init__(self, category):
        self.start_urls = [category]

    def parse(self, response):
        pages = response.xpath('//*[@id="mw-pages"]')
        name_pages_urls = pages.xpath('div[@class="mw-content-ltr"]//a/@href').extract()
        # print "name_pages_urls =" + str(len(name_pages_urls))

        for name_page_url in name_pages_urls:
            absolute_url = response.urljoin(name_page_url)
            # print "Open page = " + absolute_url
            yield Request(absolute_url, callback=self.parse_name_page)

        # Process next page (for future)


    def parse_name_page(self, response):

        name = response.xpath('//*[@class="page-header__title"]/text()').extract_first()

        full_description = ""

        cleanr = re.compile('<.*?>')

        all_paragraphs = response.xpath('//*[@id="mw-content-text"]/p').extract()

        for par in all_paragraphs:
            clean_description = cleanhtml(par)
            if len(full_description) < 5000:
                full_description += clean_description
            else:
                break

        rus_url = response.request.url
        eng_url = response.xpath('//*[@data-tracking="interwiki-en"]/@href').extract_first()
        image_url = response.xpath('//*[@class="pi-image-thumbnail"]/@src').extract_first()

        item = GotItem()

        item['name'] = name
        item['full_description'] = full_description
        item['image_url'] = image_url
        item['rus_url'] = rus_url
        item['eng_url'] = eng_url

        yield item
