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


scrDir = 'toRename/'
targetDir = 'renamed/'

files_list = os.listdir(scrDir)
fileIndex = '01'
for file_name in files_list:
	
	file_extenstion = file_name[-4:].lower()
	if file_extenstion == 'jpeg':
		file_extenstion = '.jpg'

	file_name_stripped = file_name[:-4]
	full_scr_name = scrDir + file_name

	t = get_image_size(full_scr_name)
	if t != None:
		resolution = max(t)

		print('t[0] = ', t[0])
		print('t[1] = ', t[1])
		print('max = ', resolution)


	
	full_new_name = targetDir + 'diceBG' + fileIndex + '_' + str(resolution) + file_extenstion




	tmpIndex = int(fileIndex) + 1
	print('tmpIndex = ',tmpIndex)
	if tmpIndex < 10:
		fileIndex = '0'+str(tmpIndex)
	else:
		fileIndex = str(tmpIndex)
	print(fileIndex)

	shutil.copy(full_scr_name, full_new_name)
