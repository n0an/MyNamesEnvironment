#!/usr/bin/python3
# coding: utf-8

import os
import shutil
import openpyxl
import webbrowser
import bs4
import requests

workbook = openpyxl.load_workbook('sourcetableStage1.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')

counter = 0

for index in range(2, 235):
    name_cell = sheet['A'+str(index)]
    link_cell = sheet['D'+str(index)]

    engUrl = link_cell.value
    # webbrowser.open(engUrl)

    res = requests.get(engUrl)
    soup = bs4.BeautifulSoup(res.text, "lxml")

    linksList = soup.select('#WikiaMainContentContainer > nav.WikiaArticleInterlang > ul > li')

    for link in linksList:
        linkStr = str(link)
        if linkStr[32:34] == 'ru':
            print(name_cell.value)
            print('Found link: '+linkStr[42:-19])
            counter += 1

            sheet['E'+str(index)] = linkStr[42:-19]



print('Total rus urls found: ' + str(counter))
workbook.save('resulttableStage1.xlsx')
