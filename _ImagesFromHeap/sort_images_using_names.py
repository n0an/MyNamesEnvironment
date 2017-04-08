#!/usr/bin/python3
# coding: utf-8

import os
import shutil

# +++++++++++++++ SCRIPT START +++++++++++++++

# *** SCRIPT CONFIGURATION:
input_file_name 	= '!fem_name_image_conc.txt'
dir_path 			= 'Fiction/Tolkien/Fem/'
images_source_dir 	= 'SRCImages/'

os.chdir('!WORKFLOW')

inputFile = open(input_file_name, 'r')

dir1 = {}

# Getting lines from inputFile
# 1. Setting keys of dictionary
for line in inputFile:
	trimmedLine = line.strip()
	components = trimmedLine.split(':')
	image_name = components[1]
	name = components[0]
	dir1[image_name] = []

# Go back to start of file
inputFile.seek(0)

# 2. Filling dictionary values with names
for line in inputFile:
	trimmedLine = line.strip()
	components = trimmedLine.split(':')
	image_name = components[1]
	name = components[0].lower()
	curr_names_for_img = dir1[image_name]
	curr_names_for_img.append(name)
	curr_names_for_img = list(set(curr_names_for_img))


# --- CHECKING ---
# for key in dir1.keys():
# 	print(key + ':')
# 	print(dir1[key])
# 	print()


# 2.5 Creating directories in dir_path
dirPath = dir_path

for image_name in dir1.keys():
	fullPath = dirPath+image_name
	os.makedirs(fullPath)

# 3. Cycling through dictionary's arrays.
#	 Making "traits", and searching files using them
#	 If file found - copy it to corresponding directory
srcImgDir = images_source_dir
files_list = os.listdir(srcImgDir)

full_total_files_copied = 0

for image_name in dir1.keys():
	fileIndex = '01'
	curr_names_for_img = dir1[image_name]

	print(curr_names_for_img)

	files_count = 0
	for name in curr_names_for_img:
		for file_name in files_list:
			l_file_name = file_name.lower()

			if len(name) > 4:
				trait = name[:4-len(name)]
			else:
				trait = name

			index = l_file_name.find(trait)
			if index != -1:
				print(index)
				print(file_name)

				statinfo = os.stat(srcImgDir + file_name)
				if statinfo.st_size < 30*1024:  # Don't copy files less that 25Kb size
					print('file too small')
					continue

				# We found file and now copy to corresponding dir
				full_dst_dir_path = dirPath + image_name

				file_extenstion = file_name[-4:].lower()

				if file_extenstion == 'jpeg':
					file_extenstion = '.jpg'

				full_new_name = full_dst_dir_path + '/' + image_name[13:].lower() + fileIndex + file_extenstion
				print('fileIndex = ',fileIndex)
				tmpIndex = int(fileIndex) + 1
				if tmpIndex < 10:
					fileIndex = '0'+str(tmpIndex)
				else:
					fileIndex = str(tmpIndex)

				# shutil.copy('testfolder/'+file_name, full_dst_dir_path) #copy withot renaming
				shutil.copy(srcImgDir+file_name, full_new_name) #copy with renaming
				files_count += 1
				# print(file_name + ' copied!!!')

	print('total ', files_count, 'copied\n')
	full_total_files_copied += files_count

print('TOTALLY ',full_total_files_copied,' FILES COPIED!!!')
