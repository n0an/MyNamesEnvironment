#!/usr/bin/python3
# coding: utf-8

import os
import shutil
import openpyxl
import webbrowser
import bs4
import requests
from unidecode import unidecode

workbook = openpyxl.load_workbook('sourcetable.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')

for index in range(2, 69):
    name_cell       = sheet['B'+str(index)]
    gender_cell     = sheet['C'+str(index)]

    name        = name_cell.value
    imagename   = 'FictionTolkien' + gender_cell.value + name

    imagename = unidecode(imagename)
    imagename = imagename.replace(" ", "")
    imagename = imagename.replace("-", "")

    sheet['F'+str(index)] = imagename

workbook.save('editedTable.xlsx')
