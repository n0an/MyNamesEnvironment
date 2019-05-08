# -*- coding: utf-8 -*-

import re
from scrapy import Spider
from scrapy.http import Request
from starwars.items import StarwarsItem

def cleanhtml(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext

class StarwarsSpiderSpider(Spider):
    name = 'starwars_spider'
    # allowed_domains = ['https://starwars.fandom.com']
    # start_urls = ['https://starwars.fandom.com/wiki/Category:Females']

    def __init__(self, category):
        self.start_urls = [category]

    def parse(self, response):
        characters_links = response.xpath('//a[@class="category-page__member-link"]')

        for charlink in characters_links:
            name_url = charlink.xpath('./@href').extract_first()
            absolute_name_url = response.urljoin(name_url)

            yield Request(absolute_name_url, callback=self.parse_name_page)

        next_page_url = response.xpath(
            '//a[@class="category-page__pagination-next wds-button wds-is-secondary"]/@href').extract_first()
        if next_page_url:
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

        eng_url = response.xpath('//*[@class="interwiki-en plainlinks"]//a/@href').extract_first()

        image_url = response.xpath('//*[@class="pi-image-thumbnail"]/@src').extract_first()


        rus_name_meta = {
                'name': name,
                'full_description': full_description.strip(),
                'image_url': image_url,
                'rus_url': rus_url,
                'eng_url': eng_url
            }

        if eng_url != None:
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


        race = response.xpath('//div[@data-source="species"]/div[@class="pi-data-value pi-font"]/a/text()').extract_first()

        item = StarwarsItem()

        item['name'] = response.meta['name']
        item['full_description'] = response.meta['full_description']

        item['rus_url'] = response.meta['rus_url']
        item['eng_url'] = response.meta['eng_url']

        item["eng_name"] = eng_name
        item['eng_description'] = full_eng_description.strip()

        item['race'] = race

        rus_image_url = response.meta['image_url']

        eng_image_url = response.xpath('//*[@class="pi-image-thumbnail"]/@src').extract_first()


        if eng_image_url:
            item['image_url'] = eng_image_url
        else:
            if rus_image_url:
                item['image_url'] = rus_image_url
            else:
                item['image_url'] = ''

        yield item



    