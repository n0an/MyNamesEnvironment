#!/usr/bin/python3
# coding: utf-8

import os
import shutil

import struct
import imghdr


def get_image_size(fname):
    '''Determine the image type of fhandle and return its size.
    from draco'''
    with open(fname, 'rb') as fhandle:
        head = fhandle.read(24)
        if len(head) != 24:
            return
        if imghdr.what(fname) == 'png':

            check = struct.unpack('>i', head[4:8])[0]
            if check != 0x0d0a1a0a:
                return
            width, height = struct.unpack('>ii', head[16:24])
        elif imghdr.what(fname) == 'gif':

            width, height = struct.unpack('<HH', head[6:10])
        elif imghdr.what(fname) == 'jpeg':

            try:
                fhandle.seek(0) # Read 0xff next
                size = 2
                ftype = 0
                while not 0xc0 <= ftype <= 0xcf:
                    fhandle.seek(size, 1)
                    byte = fhandle.read(1)
                    while ord(byte) == 0xff:
                        byte = fhandle.read(1)
                    ftype = ord(byte)
                    size = struct.unpack('>H', fhandle.read(2))[0] - 2
                # We are at a SOFn block
                fhandle.seek(1, 1)  # Skip `precision' byte.
                height, width = struct.unpack('>HH', fhandle.read(4))
            except Exception: #IGNORE:W0703
                return
        else:
            return
        return width, height



# ================= SCRIPT STARTS HERE ===================

dirPath = 'Fiction/Dune/Masc/'
os.makedirs('BestImages')
targetPath = 'BestImages/'

dirs_list = os.listdir(dirPath)

# 1. Cleaning list from non neccessary dirs
for dirr in dirs_list:
	if dirr[:4] != 'Fiction':
		dirs_list.remove(dirr)


# 2. Entering in each dir, and cycling through images in it, finding the best in pixels
#	 And copy best image to targetPath

def cyclethroughdir(directory):
	files_list = os.listdir(dirPath + directory)
	# print(directory, files_list)
	images_qualities = []
	maxQuality = 0
	maxQualityFile = ''

	for file_name in files_list:
		full_fname = dirPath + directory + '/' + file_name
		t = get_image_size(full_fname)
		if t != None:
			# Don't take too wide or too high pics
			if t[0]/t[1] > 3:
				continue
			if t[1]/t[0] > 3:
				continue

			img_quality = t[0]*t[1]

			images_qualities.append(img_quality)

			if img_quality > maxQuality:

				maxQualityFile = file_name
				maxQuality = img_quality

	if len(images_qualities) == 0:
		return 'NoImagesInside'

	tpl = (maxQuality, maxQualityFile, max(images_qualities))
	return maxQualityFile



for dirr in dirs_list:
	result_file = cyclethroughdir(dirr)

	if result_file == 'NoImagesInside':
		continue

	file_extenstion = result_file[-4:]

	full_scr_name = dirPath + dirr + '/' + result_file

	full_new_name = targetPath + dirr + file_extenstion

	# print('full_scr_name =', full_scr_name)
	# print('full_new_name =', full_new_name)

	shutil.copy(full_scr_name, full_new_name) #copy with renaming
