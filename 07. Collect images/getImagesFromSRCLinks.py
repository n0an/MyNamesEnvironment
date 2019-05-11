#!/usr/bin/python3
# coding: utf-8

import os
import shutil
import openpyxl
import urllib.request

# Helper methods
def create_dir_for_names_images(category_path):
    dir_path = category_path
    os.makedirs(dir_path)
    return dir_path

def is_element_contains_extension(str, extension):
    return str.lower().find(extension) != -1

def get_image_extension(url):
    if is_element_contains_extension(url, ".jpg"):
        return '.jpg'
    elif is_element_contains_extension(url, ".png"):
        return '.png'
    elif is_element_contains_extension(url, ".jpeg"):
        return '.jpeg'
    else:
        return '.file'

def retr_image_for_url(url):
    cleanedImgSrc = url

    print('Downloading image with url: ' + cleanedImgSrc)

    image_file_name = imagename

    image_file_name = imagename + get_image_extension(url)

    urllib.request.urlretrieve(cleanedImgSrc, dir_path + image_file_name)
    print('***** Image saved!!! *****')



# ********* SCRIPT CONFIGURATION: ************
cell_start_number   = 2
cell_end_number     = 100
dir_path = create_dir_for_names_images('Fiction/Starwars/')

# +++++++++++++++ SCRIPT START +++++++++++++++

# *** SCRIPT START:
# os.chdir('../!WORKFLOW')

# === 1. Opening source workbook with names ===
workbook = openpyxl.load_workbook('FictionStarwarsFemHuman.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')

# === 2. Iterating throught cells
for index in range(cell_start_number ,cell_end_number + 1):
    name_cell       = sheet['B'+str(index)]
    image_url_cell  = sheet['F'+str(index)]
    imagename_cell  = sheet['G'+str(index)]
    name            = name_cell.value
    imagename       = imagename_cell.value
    image_url       = image_url_cell.value


    print('\n' + str(index-1) + '. ^^^^^^^^^^^^^^ Start processing name: ' + name)

    # *** Saving image for name
    print('==== Saving process for name: ' + name + ':')
    if (image_url !="") and (image_url != None):
        print('--- Saving image ---')
        retr_image_for_url(image_url)
    
