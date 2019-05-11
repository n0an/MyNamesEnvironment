#!/usr/bin/python3
# coding: utf-8

import os
import shutil
import openpyxl
from unidecode import unidecode


# ********* SCRIPT CONFIGURATION: ************
cell_start_number   = 2
cell_end_number     = 4
prefix = 'FictionStarwars'

# +++++++++++++++ SCRIPT START +++++++++++++++

workbook = openpyxl.load_workbook('TemplateTable.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')

for index in range(cell_start_number, cell_end_number + 1):
    name_cell   = sheet['B'+str(index)]
    gender_cell = sheet['C'+str(index)]

    name        = name_cell.value
    imagename   = prefix + gender_cell.value + name

    imagename = unidecode(imagename)
    imagename = imagename.replace(" ", "")
    imagename = imagename.replace("-", "")

    sheet['G'+str(index)] = imagename

    eng_description = sheet['D'+str(index)].value
    rus_description = sheet['K'+str(index)].value

    sheet['D'+str(index)] = eng_description.strip()
    sheet['K'+str(index)] = rus_description.strip()



workbook.save('DoneTable.xlsx')
