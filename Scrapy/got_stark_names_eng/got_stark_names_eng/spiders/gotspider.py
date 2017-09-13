# -*- coding: utf-8 -*-
import scrapy
import re

class GotspiderSpider(scrapy.Spider):
    name = 'gotspider'
    allowed_domains = ['gameofthrones.wikia.com']
    # start_urls = ['http://gameofthrones.wikia.com/']
    start_urls = [u'http://gameofthrones.wikia.com/wiki/Brandon_Stark_(the_Breaker)', u'http://gameofthrones.wikia.com/wiki/Brandon_Stark_(son_of_Rickard)', u'http://gameofthrones.wikia.com/wiki/Benjen_Stark', u'http://gameofthrones.wikia.com/wiki/Varly', u'http://gameofthrones.wikia.com/wiki/Arya_Stark', u'http://gameofthrones.wikia.com/wiki/Bran_Stark', u'http://gameofthrones.wikia.com/wiki/Brandon_Stark_(the_Builder)', u'http://gameofthrones.wikia.com/wiki/Winterfell', u'http://gameofthrones.wikia.com/wiki/Jeyne_Poole', u'http://gameofthrones.wikia.com/wiki/Jory_Cassel', u'http://gameofthrones.wikia.com/wiki/Dorren_Stark', u'http://gameofthrones.wikia.com/wiki/Needle', u'http://gameofthrones.wikia.com/wiki/Jon_Snow', u'http://gameofthrones.wikia.com/wiki/Catelyn_Stark', u'http://gameofthrones.wikia.com/wiki/Karlon_Stark', u'http://gameofthrones.wikia.com/wiki/King_in_the_North', u'http://gameofthrones.wikia.com/wiki/Cregan_Stark', u'http://gameofthrones.wikia.com/wiki/Ice', u'http://gameofthrones.wikia.com/wiki/Lyanna_Stark', u'http://gameofthrones.wikia.com/wiki/Northern_Lord', u'http://gameofthrones.wikia.com/wiki/Luwin', u'http://gameofthrones.wikia.com/wiki/Mikken', u'http://gameofthrones.wikia.com/wiki/Mordane', u'http://gameofthrones.wikia.com/wiki/Old_Nan', u'http://gameofthrones.wikia.com/wiki/Osric_Stark', u'http://gameofthrones.wikia.com/wiki/Stark_guard_(A_Man_Without_Honor)', u'http://gameofthrones.wikia.com/wiki/Osha', u'http://gameofthrones.wikia.com/wiki/Palla', u'http://gameofthrones.wikia.com/wiki/Winterfell_shepherd', u'http://gameofthrones.wikia.com/wiki/Portan', u'http://gameofthrones.wikia.com/wiki/Theon%27s_master_of_hounds', u'http://gameofthrones.wikia.com/wiki/Stark_messenger', u'http://gameofthrones.wikia.com/wiki/Rickard_Stark_(King)', u'http://gameofthrones.wikia.com/wiki/Rickard_Stark', u'http://gameofthrones.wikia.com/wiki/Rickon_Stark', u'http://gameofthrones.wikia.com/wiki/Rodrik_Cassel', u'http://gameofthrones.wikia.com/wiki/Rodrik_Stark', u'http://gameofthrones.wikia.com/wiki/Robb_Stark', u'http://gameofthrones.wikia.com/wiki/Sansa_Stark', u'http://gameofthrones.wikia.com/wiki/Stark_guard_(The_Pointy_End)', u'http://gameofthrones.wikia.com/wiki/Jacks', u'http://gameofthrones.wikia.com/wiki/Tom', u'http://gameofthrones.wikia.com/wiki/Stark_soldier_(Valar_Morghulis)', u'http://gameofthrones.wikia.com/wiki/House_Stark', u'http://gameofthrones.wikia.com/wiki/Stark_guard_(Fire_and_Blood)', u'http://gameofthrones.wikia.com/wiki/Theon_Stark', u'http://gameofthrones.wikia.com/wiki/Talisa_Stark', u'http://gameofthrones.wikia.com/wiki/Tomard', u'http://gameofthrones.wikia.com/wiki/Tommy', u'http://gameofthrones.wikia.com/wiki/Farlen', u'http://gameofthrones.wikia.com/wiki/Torrhen_Stark', u'http://gameofthrones.wikia.com/wiki/Wolkan', u'http://gameofthrones.wikia.com/wiki/Hodor', u'http://gameofthrones.wikia.com/wiki/Eddard_Stark']


    def parse(self, response):
        name = response.xpath('//*[@class="page-header__title"]/text()').extract()



        full_description = ""

        cleanr = re.compile('<.*?>')

        all_paragraphs = response.xpath('//*[@id="mw-content-text"]/p').extract()


        for par in all_paragraphs:
            clean_description = re.sub(cleanr, '', par)
            if len(full_description) < 5000:
                full_description += clean_description
            else:
                break


        engurl = response.xpath('//*[@data-tracking="interwiki-en"]/@href').extract()

        print('Eng Name = ', name)
        if full_description != "":
            print('Description +++')

        yield {
                'Eng Name':         name,
                'Eng Description':  full_description,
                'Eng Url':          response.url
                }
