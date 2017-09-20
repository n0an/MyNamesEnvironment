#!/usr/bin/python3
# coding: utf-8

import os
import shutil
import openpyxl
import webbrowser
import bs4
import requests

os.chdir('!WORKFLOW')

workbook = openpyxl.load_workbook('resulttableStage1.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')
sourceSheet = workbook.get_sheet_by_name('sourcesheet')

# +++++++++++++++ SCRIPT START +++++++++++++++
# *** SCRIPT CONFIGURATION:
cell_start_number   = 2
cell_end_number     = 8

cell_source_start_number = 2
cell_source_end_number = 4

counter = 0

for index in range(cell_start_number, cell_end_number + 1):
    initcounter = counter
    name_cell = sheet['A'+str(index)]
    ruslink_cell = sheet['E'+str(index)]

    rusUrl = ruslink_cell.value

    for indexInSource in range(cell_source_start_number, cell_source_end_number + 1):

        nameSource_cell = sourceSheet['A'+str(indexInSource)]

        sourceRusLink_cell = sourceSheet['C'+str(indexInSource)]
        sourceRusUrl = sourceRusLink_cell.value

        if rusUrl == sourceRusUrl:
            print('Proceeding: '+name_cell.value)
            sheet['F'+str(index)] = sourceSheet['A'+str(indexInSource)].value
            sheet['G'+str(index)] = sourceSheet['B'+str(indexInSource)].value
            sourceSheet['D'+str(indexInSource)] = "USED"
            counter += 1

    if counter == initcounter:
        print('Not found url for name: ' + str(name_cell.value))


print('Total equal found: ' + str(counter))
workbook.save('resulttableStage2.xlsx')
