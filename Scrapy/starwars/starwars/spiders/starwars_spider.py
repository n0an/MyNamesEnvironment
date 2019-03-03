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
            # name = charlink.xpath('./text()').extract_first()
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

        eng_url = response.request.url

        rus_url = response.xpath('//*[@class="interwiki-ru plainlinks"]/a/@href').extract_first()

        image_url = response.xpath('//*[@class="pi-image-thumbnail"]/@src').extract_first()

        race = response.xpath('//div[@data-source="species"]/div[@class="pi-data-value pi-font"]/a/text()').extract_first()

        if rus_url == None:

            item = StarwarsItem()

            item['name'] = name
            item['full_description'] = full_description.strip()
            item['image_url'] = image_url
            item['eng_url'] = eng_url

            item['rus_url'] = eng_url
            item["rus_name"] = name
            item['rus_description'] = full_description.strip()
            item['rus_image_url'] = image_url

            item['race'] = race

            yield item

        else:
            print('================ FOUND RUS NAME ======================')
            if rus_url[:2] == '//':
                rus_url = 'https:'+rus_url

            print(rus_url)
            eng_name_meta = {
                'name': name,
                'full_description': full_description.strip(),
                'image_url': image_url,
                'rus_url': rus_url,
                'eng_url': eng_url,
                'race': race
            }

            yield Request(rus_url, callback=self.parse_rus_name_page, meta=eng_name_meta)


    def parse_rus_name_page(self, response):

        rus_name = response.xpath('//*[@class="page-header__title"]/text()').extract_first()

        full_rus_description = ""

        all_paragraphs = response.xpath('//*[@id="mw-content-text"]/p').extract()

        for par in all_paragraphs:
            clean_description = cleanhtml(par)
            if len(full_rus_description) < 5000:
                full_rus_description += clean_description
            else:
                break

        item = StarwarsItem()

        item['name'] = response.meta['name']
        item['full_description'] = response.meta['full_description']
        item['eng_url'] = response.meta['eng_url']

        item['rus_url'] = response.meta['rus_url']
        item["rus_name"] = rus_name
        item['rus_description'] = full_rus_description.strip()

        item['race'] = response.meta['race']

        rus_image_url = response.xpath('//*[@class="pi-image-thumbnail"]/@src').extract_first()

        eng_image_url = response.meta['image_url']

        if rus_image_url:
            item['rus_image_url'] = rus_image_url
        else:
            if eng_image_url:
                item['rus_image_url'] = eng_image_url
            else:
                item['rus_image_url'] = ''


        if eng_image_url:
            item['image_url'] = eng_image_url
        else:
            if rus_image_url:
                item['image_url'] = rus_image_url
            else:
                item['image_url'] = ''

        yield item