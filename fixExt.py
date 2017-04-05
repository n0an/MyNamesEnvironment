#!/usr/bin/python3
# coding: utf-8

import os
import shutil

scrDir = '!ReadyImages/'
targetDir = '!CorrectedImages/'

files_list = os.listdir(scrDir)

for file_name in files_list:
	file_extenstion = file_name[-4:].lower()
	file_name_stripped = file_name[:-4]

	full_scr_name = scrDir + file_name
	full_new_name = targetDir + file_name_stripped + file_extenstion

	shutil.copy(full_scr_name, full_new_name)





