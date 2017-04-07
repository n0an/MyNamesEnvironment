#!/usr/bin/python3
# coding: utf-8

import os
import shutil
import openpyxl
import webbrowser
import bs4
import requests
from unidecode import unidecode

# +++++++++++++++ SCRIPT START +++++++++++++++

# *** SCRIPT CONFIGURATION:
cell_start_number   = 2
cell_end_number     = 6

workbook = openpyxl.load_workbook('sourceTableStage2.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')

for index in range(cell_start_number, cell_end_number + 1):
    name_cell       = sheet['B'+str(index)]
    gender_cell     = sheet['C'+str(index)]

    name        = name_cell.value
    imagename   = 'FictionTolkien' + gender_cell.value + name

    imagename = unidecode(imagename)
    imagename = imagename.replace(" ", "")
    imagename = imagename.replace("-", "")

    sheet['F'+str(index)] = imagename

workbook.save('DoneTable.xlsx')
