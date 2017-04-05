#!/usr/bin/python3
# coding: utf-8

import os
import shutil

inputFile = open('FictionDuneFemUnique.txt', 'r')

# Stripping whitespaces around line
linesList = []

for line in inputFile:
	trimmedLine = line.strip()
	resLine = trimmedLine
	linesList.append(resLine)

# print(linesList)

cleanedNames = sorted(list(set(linesList)))

print(len(cleanedNames))

dirPath = 'Fiction/Dune/Fem/'
for name in cleanedNames:
	fullPath = dirPath+name
	os.makedirs(fullPath)
