#!/usr/bin/python3
# coding: utf-8

import os
import shutil
from unidecode import unidecode

# HELPER METHODS
def plain_rename(files_list):
    for file_name in files_list:
        cropped = file_name[18:]
        new_name = 'FictionTolkienMenMasc' + cropped

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


# ================= SCRIPT STARTS HERE ===================

src_dir = 'toRename/'
target_dir = 'renamed/'

files_list = os.listdir(src_dir)

remove_diacritic_spaces_and_dashes(files_list)
