#!/usr/bin/python3
# coding: utf-8

from selenium import webdriver

import os
import shutil
import openpyxl
import bs4
import requests


# Windows ver:
# driver = webdriver.Chrome("C:/chromedriver.exe")

# MacOS ver:
# driver = webdriver.Chrome("../chromedriver")

# === 1. Opening source workbook with names ===

workbook = openpyxl.load_workbook('sourcetable.xlsx')
sheet = workbook.get_sheet_by_name('sheet1')



for index in range(7,10):
    name_cell       = sheet['B'+str(index)]
    imagename_cell  = sheet['F'+str(index)]
    link_cell       = sheet['E'+str(index)]

    name = name_cell.value
    imagename = imagename_cell.value
    url = link_cell.value

    print(' ^^^^^^^^^^^^^^ Start processing name: ' + name)

    # driver.get(url)

    res = requests.get(url)
    soup = bs4.BeautifulSoup(res.text, "lxml")


    # thumbnails_list = driver.find_elements_by_css_selector('.image.image-thumbnail>img')

    thumbnails_list = soup.select('.image.image-thumbnail')

    selectedUrls = []

    for thumbnail in thumbnails_list:
        raw_src = str(thumbnail)

        print('Working with thumbnail: \n' + raw_src + '\n')

        widthStr_start_index = raw_src.finc('width=')
        width_rawStr = raw_src[widthStr_start_index+7:]
        widthStr_end_index = width_rawStr.find('"')
        widthStr = width_rawStr[:3]

        print('Width = ' + widthStr)

        src_index = raw_src.find('src="')

        clean_src = raw_src[src_index+5:]

        urlEndPosition = clean_src.find('/revision')

        clean_src = clean_src[:urlEndPosition]

        print('Cleaned url: \n' + clean_src)

        if (int(widthStr) > 150) and (raw_src.find("wikia.nocookie.net/lotr/images") != -1):
            print('--Size and url location passed')
            if src.find('.jpg') != -1 or src.find('.png') != 1:
                print('==== extension passed!')
                selectedUrls.append(clean_src)

    print('selectedThumbs for name ' + name + ': \n')

    imagesCounter = 1

    for selectedUrl in selectedUrls:


        print(selectedUrl)

        # urlEndPosition = imgSrc.find('/revision')
        # cleanedImgSrc = imgSrc[:urlEndPosition]
        # print('Link found: ' + cleanedImgSrc)
        # driver.get(cleanedImgSrc)
        #
        # # Windows ver:
        # # driver.get_screenshot_as_file('C:/Users/nag/Desktop/aragorn.png')
        #
        # # MacOS ver:
        # image_file_name = imagename + str(imagesCounter) + '.jpg'
        # imagesCounter += 1
        # driver.get_screenshot_as_file(image_file_name)
        # print('***** Image saved!!! *****')




#
#
# # driver.get('http://lotr.wikia.com/wiki/Aragorn_II_Elessar')
# driver.get('http://lotr.wikia.com/wiki/Melkor')
#
# # x = driver.find_element_by_xpath("//*[@id='mw-content-text']/div[3]/div[2]/div[1]/div/a/img")
#
# linksList = driver.find_elements_by_css_selector('.image.image-thumbnail>img')
# # x = driver.find_element_by_css_selector('.image.image-thumbnail>img')
#
#
# selectedLinks = []
#
# if len(linksList) > 1:
#     print('More than 1 link found:')
#     for link in linksList:
#         src = link.get_attribute('src')
#         print('Working with link: \n' + src + '\n')
#         if (int(link.get_attribute('width')) > 200) and (src.find("wikia.nocookie.net/lotr/images") != -1):
#             print('--Size and vignette passed')
#             if src.find('.jpg') != -1 or src.find('.png') != 1:
#                 print('==== extension passed!')
#                 selectedLinks.append(link)
#
# else:
#     print('Only 1 link found:')
#     print(linksList[0].get_attribute('src'))
#
# print('Selected links:')
#
# for link in selectedLinks:
#     imgSrc = link.get_attribute('src')
#
#     print(imgSrc)
#
#     linkEndPosition = imgSrc.find('/revision')
#     cleanedImgSrc = imgSrc[:linkEndPosition]
#     print('Link found: ' + cleanedImgSrc)
#     driver.get(cleanedImgSrc)
#
#     # Windows ver:
#     # driver.get_screenshot_as_file('C:/Users/nag/Desktop/aragorn.png')
#
#     # MacOS ver:
#     driver.get_screenshot_as_file('./aragorn.png')
