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
            'Rus Name',
            'Rus Description',
            'Image Url',
            'Rus Url',
            'Eng Url',
            'Eng Name',
            'Eng Description',
            'Race'
            ])

    def process_item(self, item, spider):
        line = [
            item['name'],
            item['full_description'],
            item['image_url'],
            item['rus_url'],
            item['eng_url'],
            item['eng_name'],
            item['eng_description'],
            item['race']
            ]

        # Add the data to xlsx as a line
        self.ws.append(line)

        # Save the XLSX file
        self.wb.save('./result-excel.xlsx')

        return item
