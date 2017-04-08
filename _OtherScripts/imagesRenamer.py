#!/usr/bin/python3
# coding: utf-8

import os
import shutil
from unidecode import unidecode

# HELPER METHODS
def plain_rename(files_list, crop_from_index, new_prefix):
    for file_name in files_list:
        cropped = file_name[crop_from_index:]
        #TODO: Configure new name here
        new_name = new_prefix + cropped

        full_src_name = src_dir + file_name
        full_new_name = target_dir + new_name

        shutil.copy(full_src_name, full_new_name)


def remove_diacritic_spaces_and_dashes(files_list):
    for file_name in files_list:

        new_name = unidecode(file_name)
        new_name = new_name.replace(" ", "")
        new_name = new_name.replace("-", "")

        full_src_name = src_dir + file_name
        full_new_name = target_dir + new_name

        shutil.copy(full_src_name, full_new_name)


# +++++++++++++++ SCRIPT START +++++++++++++++
# *** SCRIPT CONFIGURATION:
src_dir = 'toRename/'
target_dir = 'renamed/'
crop_from_index = 18
new_prefix = 'FictionTolkienElvesMasc'
# ***

os.chdir('!WORKFLOW')

files_list = os.listdir(src_dir)

remove_diacritic_spaces_and_dashes(files_list, crop_from_index, new_prefix)
