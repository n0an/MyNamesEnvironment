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
    allowed_domains = ['ru.gameofthrones.wikia.com', 'gameofthrones.wikia.com']
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

        # Process next page
        next_page_url = response.xpath('//*[@class="paginator-next button secondary"]/@href').extract_first()
        if next_page_url != None:
            yield Request(next_page_url)

    def parse_name_page(self, response):

        name = response.xpath('//*[@class="page-header__title"]/text()').extract_first()

        full_description = ""

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


        rus_name_meta = {
                'name': name,
                'full_description': full_description.strip(),
                'image_url': image_url,
                'rus_url': rus_url,
                'eng_url': eng_url
        }

        yield Request(eng_url, callback=self.parse_eng_name_page, meta=rus_name_meta)

    def parse_eng_name_page(self, response):
        eng_name = response.xpath('//*[@class="page-header__title"]/text()').extract_first()

        full_eng_description = ""

        all_paragraphs = response.xpath('//*[@id="mw-content-text"]/p').extract()

        for par in all_paragraphs:
            clean_description = cleanhtml(par)
            if len(full_eng_description) < 5000:
                full_eng_description += clean_description
            else:
                break

        house = response.xpath('//h3[text()="Allegiance"]/following-sibling::div/a/text()').extract_first()

        item = GotItem()

        item['name'] = response.meta['name']
        item['full_description'] = response.meta['full_description']
        item['image_url'] = response.meta['image_url']
        item['rus_url'] = response.meta['rus_url']
        item['eng_url'] = response.meta['eng_url']

        eng_image_url = response.xpath('//*[@class="pi-image-thumbnail"]/@src').extract_first()
        item["eng_name"] = eng_name
        item['eng_description'] = full_eng_description.strip()
        item['eng_image_url'] = eng_image_url
        item['house'] = house

        yield item
