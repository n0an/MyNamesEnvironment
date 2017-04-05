#!/usr/bin/python3
# coding: utf-8

import os
import shutil
import openpyxl
import webbrowser
import bs4
import requests

workbook = openpyxl.load_workbook('editex.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')
sourceSheet = workbook.get_sheet_by_name('sourcesheet')

counter = 0

for index in range(2, 235):
    initcounter = counter
    name_cell = sheet['A'+str(index)]
    ruslink_cell = sheet['E'+str(index)]

    rusUrl = ruslink_cell.value

    # if index == 62:
    #     print('Main name: ' + str(name_cell.value))


    for indexInSource in range(2, 35):

        nameSource_cell = sourceSheet['A'+str(indexInSource)]

        # if index == 62:
        #     print('-- Equal to ? : ' + str(nameSource_cell.value))


        sourceRusLink_cell = sourceSheet['C'+str(indexInSource)]
        sourceRusUrl = sourceRusLink_cell.value

        if rusUrl == sourceRusUrl:
            print('Proceeding: '+name_cell.value)
            sheet['G'+str(index)] = sourceSheet['A'+str(indexInSource)].value
            sheet['H'+str(index)] = sourceSheet['B'+str(indexInSource)].value
            sourceSheet['D'+str(indexInSource)] = "USED"
            counter += 1

    if counter == initcounter:
        print('Not found url for name: ' + str(name_cell.value))



print('Total equal found: ' + str(counter))
workbook.save('editexDone.xlsx')
