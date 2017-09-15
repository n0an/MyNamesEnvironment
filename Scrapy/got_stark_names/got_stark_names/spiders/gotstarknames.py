# -*- coding: utf-8 -*-
import re
from scrapy import Spider
from scrapy.http import Request

class GotstarknamesSpider(scrapy.Spider):
    name = 'gotstarknames'
    allowed_domains = ['ru.gameofthrones.wikia.com']
    # start_urls = ['http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%94%D0%BE%D0%BC_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2/']

 #    start_urls = [u'http://ru.gameofthrones.wikia.com/wiki/%D0%90%D1%80%D1%8C%D1%8F_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%91%D0%B5%D0%BD%D0%B4%D0%B6%D0%B5%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%91%D1%80%D0%B0%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%91%D1%80%D0%B0%D0%BD%D0%B4%D0%BE%D0%BD_%D0%9A%D1%80%D1%83%D1%88%D0%B8%D1%82%D0%B5%D0%BB%D1%8C',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%91%D1%80%D0%B0%D0%BD%D0%B4%D0%BE%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA_(%D1%81%D1%8B%D0%BD_%D0%A0%D0%B8%D0%BA%D0%B0%D1%80%D0%B4%D0%B0)',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%91%D1%80%D0%B0%D0%BD%D0%B4%D0%BE%D0%BD_%D0%A1%D1%82%D1%80%D0%BE%D0%B8%D1%82%D0%B5%D0%BB%D1%8C',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%92%D0%B0%D1%80%D0%BB%D0%B8',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%92%D0%B5%D0%B9%D0%BE%D0%BD_%D0%9F%D1%83%D0%BB%D1%8C',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%92%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%BB%D0%BB',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%94%D0%B6%D0%B5%D0%B9%D0%BD%D0%B8_%D0%9F%D1%83%D0%BB%D1%8C',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%94%D0%B6%D0%BE%D0%BD_%D0%A1%D0%BD%D0%BE%D1%83',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%94%D0%B6%D0%BE%D1%80%D0%B8_%D0%9A%D0%B0%D1%81%D1%81%D0%B5%D0%BB%D1%8C',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%94%D0%BE%D1%80%D1%80%D0%B5%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%98%D0%B3%D0%BB%D0%B0',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B0%D1%80%D0%BB%D0%BE%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%B5%D0%B9%D1%82%D0%B8%D0%BB%D0%B8%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D0%BE%D1%80%D0%BE%D0%BB%D1%8C_%D0%A1%D0%B5%D0%B2%D0%B5%D1%80%D0%B0',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9A%D1%80%D0%B8%D0%B3%D0%B0%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9B%D1%91%D0%B4',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9B%D0%B8%D0%B0%D0%BD%D0%BD%D0%B0_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9B%D0%BE%D1%80%D0%B4_%D1%81_%D0%A1%D0%B5%D0%B2%D0%B5%D1%80%D0%B0',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9B%D1%8E%D0%B2%D0%B8%D0%BD',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9C%D0%B8%D0%BA%D0%BA%D0%B5%D0%BD',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9C%D0%BE%D1%80%D0%B4%D0%B5%D0%B9%D0%BD',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9D%D1%8D%D0%BD',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9E%D0%B7%D1%80%D0%B8%D0%BA_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9E%D1%85%D1%80%D0%B0%D0%BD%D0%BD%D0%B8%D0%BA_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2_(%D0%A7%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA_%D0%B1%D0%B5%D0%B7_%D1%87%D0%B5%D1%81%D1%82%D0%B8)',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9E%D1%88%D0%B0',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9F%D0%B0%D0%BB%D0%BB%D0%B0',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9F%D0%B0%D1%81%D1%82%D1%83%D1%85_%D0%B8%D0%B7_%D0%92%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%BB%D0%BB%D0%B0',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9F%D0%BE%D1%80%D1%82%D0%B0%D0%BD',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9F%D0%BE%D1%81%D1%8B%D0%BB%D1%8C%D0%BD%D1%8B%D0%B9_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%9F%D1%81%D0%B0%D1%80%D1%8C_%D0%92%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D1%84%D0%B5%D0%BB%D0%BB%D0%B0',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A0%D0%B8%D0%BA%D0%B0%D1%80%D0%B4_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A0%D0%B8%D0%BA%D0%B0%D1%80%D0%B4_%D0%A1%D1%82%D0%B0%D1%80%D0%BA_(%D0%BA%D0%BE%D1%80%D0%BE%D0%BB%D1%8C)',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A0%D0%B8%D0%BA%D0%BE%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A0%D0%BE%D0%B1%D0%B1_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A0%D0%BE%D0%B4%D1%80%D0%B8%D0%BA_%D0%9A%D0%B0%D1%81%D1%81%D0%B5%D0%BB%D1%8C',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A0%D0%BE%D0%B4%D1%80%D0%B8%D0%BA_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A1%D0%B0%D0%BD%D1%81%D0%B0_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A1%D0%BE%D0%BB%D0%B4%D0%B0%D1%82_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A1%D0%BE%D0%BB%D0%B4%D0%B0%D1%82_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2_(%D0%A7%D0%B5%D0%BB%D0%BE%D0%B2%D0%B5%D0%BA_%D0%B1%D0%B5%D0%B7_%D1%87%D0%B5%D1%81%D1%82%D0%B8)',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A1%D0%BE%D0%BB%D0%B4%D0%B0%D1%82_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2_1_(%D0%92%D0%B0%D0%BB%D0%B0%D1%80_%D0%BC%D0%BE%D1%80%D0%B3%D1%83%D0%BB%D0%B8%D1%81)',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A1%D0%BE%D0%BB%D0%B4%D0%B0%D1%82_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2_2_(%D0%92%D0%B0%D0%BB%D0%B0%D1%80_%D0%BC%D0%BE%D1%80%D0%B3%D1%83%D0%BB%D0%B8%D1%81)',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%B8',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A1%D1%82%D1%80%D0%B0%D0%B6%D0%BD%D0%B8%D0%BA_%D0%A1%D1%82%D0%B0%D1%80%D0%BA%D0%BE%D0%B2_(%D0%9F%D0%BB%D0%B0%D0%BC%D1%8F_%D0%B8_%D0%BA%D1%80%D0%BE%D0%B2%D1%8C)',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A2%D0%B0%D0%BB%D0%B8%D1%81%D0%B0_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A2%D0%B5%D0%BE%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A2%D0%BE%D0%BC%D0%B0%D1%80%D0%B4',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A2%D0%BE%D0%BC%D0%BC%D0%B8',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A2%D0%BE%D1%80%D1%80%D1%85%D0%B5%D0%BD_%D0%A1%D1%82%D0%B0%D1%80%D0%BA',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A3%D0%BE%D0%BB%D0%BA%D0%B0%D0%BD',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A4%D0%B0%D1%80%D0%BB%D0%B5%D0%BD',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%A5%D0%BE%D0%B4%D0%BE%D1%80',
 # u'http://ru.gameofthrones.wikia.com/wiki/%D0%AD%D0%B4%D0%B4%D0%B0%D1%80%D0%B4_%D0%A1%D1%82%D0%B0%D1%80%D0%BA']

    def __init__(self, category):
        self.start_urls = [category]

    # Method doesn't work as supposed. Copy paste of re.sub... into parse() method used.
    def cleanhtml(self, raw_html):
        cleanr = re.compile('<.*?>')
        cleantext = re.sub(cleanr, '', raw_html)
        return cleantext

    def parse(self, response):
        pages = response.xpath('//*[@id="mw-pages"]')
        name_pages_urls = pages.xpath('div[@class="mw-content-ltr"]//a/@href').extract()

        for name_page_url in name_pages_urls:
            absolute_url = response.urljoin(name_page_url)
            yield Request(absolute_url, callback=self.parse_name_page)

        # Process next page (for future)


    def parse_name_page(self, response):

        name = response.xpath('//*[@class="page-header__title"]/text()').extract_first

        full_description = ""

        # cleanr = re.compile('<.*?>')

        all_paragraphs = response.xpath('//*[@id="mw-content-text"]/p').extract()


        for par in all_paragraphs:
            # clean_description = re.sub(cleanr, '', par)
            clean_description = cleanhtml(par)
            if len(full_description) < 5000:
                full_description += clean_description
            else:
                break


        # full_description = ""
        #
        # description1 = response.xpath('//*[@id="mw-content-text"]/p[1]').extract_first()
        # description2 = response.xpath('//*[@id="mw-content-text"]/p[2]').extract_first()
        # # description1ByCss = response.css('#mw-content-text > p:nth-child(2)').extract()
        #
        # # description1_text = cleanhtml(description1)
        # # description2_text = cleanhtml(description2)
        #
        # cleanr = re.compile('<.*?>')
        # description1_text = re.sub(cleanr, '', description1)
        # description2_text = re.sub(cleanr, '', description2)
        #
        # full_description = description1_text + description2_text

        engurl = response.xpath('//*[@data-tracking="interwiki-en"]/@href').extract()

        # print('Name = ', name)
        # if full_description != "":
        #     print('Description +++')

        image_url = response.xpath('//*[@class="pi-image-thumbnail"]/@src').extract_first()

        yield {
                'Rus Name':         name,
                'Rus Description':  full_description,
                'Rus Url':          response.request.url,
                'Eng Url':          engurl
                }
