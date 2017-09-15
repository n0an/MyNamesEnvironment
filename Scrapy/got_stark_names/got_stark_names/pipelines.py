# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


from openpyxl import Workbook

class GotPipeline(object):
    wb = Workbook()
    ws = wb.active

    # Excel File Headers
    ws.append([
            'Rus Name',
            'Rus Description',
            'Image Url',
            'Rus Url',
            'Eng Url'
            ])

    def process_item(self, item, spider):
        line = [
            item['name'],
            item['full_description'],
            item['image_url'],
            item['rus_url'],
            item['eng_url']
            ]


        # Add the data to xlsx as a line
        self.ws.append(line)

        # Save the XLSX file
        self.wb.save('./result-excel.xlsx')

        return item
