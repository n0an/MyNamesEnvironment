#!/usr/bin/python3
# coding: utf-8

from selenium import webdriver

import os
import shutil
import openpyxl

# Helper methods
# ** Checking found CSS element
def is_element_width_ok(element):
    element_width = int(element.get_attribute('width'))
    return element_width > 190

def is_element_src_ok(element):
    element_scr_contains_lotr_traits = element.get_attribute('src').find("wikia.nocookie.net/lotr/images") != -1
    return element_scr_contains_lotr_traits

def is_element_extension_ok(element):
    element_src = element.get_attribute('src')
    return element_src.find('.jpg') != -1 or element_src.find('.png') != 1

def is_element_ok(element):
    is_width_ok     = is_element_width_ok(element)
    is_src_ok       = is_element_src_ok(element)
    is_extension_ok = is_element_extension_ok(element)
    return is_width_ok and is_src_ok and is_extension_ok

def save_image_for_url(url, imagesCounter = -1):
    urlEndPosition = url.find('/revision')
    cleanedImgSrc = url[:urlEndPosition]
    print('Link found: ' + cleanedImgSrc)
    driver.get(cleanedImgSrc)

    image_file_name = imagename

    if imagesCounter == -1:
        image_file_name = imagename + '.jpg'
    else:
         image_file_name = imagename + str(imagesCounter) + '.jpg'

    driver.get_screenshot_as_file(image_file_name)
    print('***** Image saved!!! *****')

def save_images_for_urlsList(urls_list):
    imagesCounter = 1
    for url in urls_list:
        save_image_for_url(url, imagesCounter)
        imagesCounter += 1

def save_first_image_for_urlsList(urls_list):
    save_image_for_url(urls_list[0])


# +++++++++++++++ SCRIPT START +++++++++++++++
# Windows ver:
driver = webdriver.Chrome("C:/chromedriver.exe")

# MacOS ver:
# driver = webdriver.Chrome("../chromedriver")

# === 1. Opening source workbook with names ===
workbook = openpyxl.load_workbook('sourcetable.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')

# === 2. Iterating throught cells
for index in range(7,15):
    name_cell       = sheet['B'+str(index)]
    link_cell       = sheet['E'+str(index)]
    gender_cell     = sheet['C'+str(index)]

    name        = name_cell.value
    imagename   = 'FictionTolkien' + gender_cell.value + name
    url         = link_cell.value

    print('\n ^^^^^^^^^^^^^^ Start processing name: ' + name)
    driver.get(url)

    thumbnails_list = driver.find_elements_by_css_selector('.image.image-thumbnail>img')

    selected_urls = []

    # *** Checking thumbnails for size, url_src, extension
    for thumbnail in thumbnails_list:
        if is_element_ok(thumbnail):
            src = thumbnail.get_attribute('src')
            selected_urls.append(src)

    # *** Printing selected URLs for name
    print('selectedUrls for name ' + name + ':')
    for selected_url in selected_urls:
        print(selected_url)

    # *** Saving image for name
    if len(selected_urls) > 0:
        print('==== Saving process for name: ' + name + ':')
        save_first_image_for_urlsList(selected_urls)
    else:
        print('No images found for name')
        continue



