#!/usr/bin/python3
# coding: utf-8

import os
import shutil

# inputFile = open('MythGreekMascUnique.txt', 'r')
inputFile = open('FictionDuneFemUnique.txt', 'r')

outputFile = open('UniqueFemNames.txt', 'w')

# Stripping whitespaces around line
linesList = []

for line in inputFile:
	trimmedLine = line.strip()
	resLine = trimmedLine[13:]
	linesList.append(resLine)

# print(linesList)

cleanedNames = sorted(list(set(linesList)))

print(len(cleanedNames))


for line in cleanedNames:
	wl = line+'\n'
	outputFile.write(wl)

# dirPath = 'Myth/Greek/Fem/'
# for name in cleanedNames:
# 	fullPath = dirPath+name
# 	os.makedirs(fullPath)
