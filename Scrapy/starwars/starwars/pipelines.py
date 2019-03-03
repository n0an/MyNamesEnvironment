# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from openpyxl import Workbook

class StarwarsPipeline(object):
    wb = Workbook()
    ws = wb.active

    # Excel File Headers
    ws.append([
            'Name',
            'Description',
            'Eng Image Url',
            'Eng Url',
            'Rus Url',
            'Rus Name',
            'Rus Description',
            'Rus Image Url',
            'Race'
            ])

    def process_item(self, item, spider):
        line = [
            item['name'],
            item['full_description'],
            item['image_url'],
            item['eng_url'],
            item['rus_url'],
            item['rus_name'],
            item['rus_description'],
            item['rus_image_url'],
            item['race']
            ]




        # Add the data to xlsx as a line
        self.ws.append(line)

        # Save the XLSX file
        self.wb.save('./result-excel.xlsx')

        return item
