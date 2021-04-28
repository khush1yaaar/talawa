#!/usr/bin/env python
import os
import glob
import sys

#get current working dir
path = os.getcwd()

#parses through files and saves to a dict
names={}
pathName = path + '/**/*.dart'
for fn in glob.glob(pathname = pathName, recursive = True):
    with open(fn) as f:
        names[fn]=sum(1 for line in f if line.strip() and not line.startswith('#'))    

#if the line rule is voilated then value is changed to 1 
isLineRuleVoilated = 0
fileCount = 0
for key, value in names.items():
    if value > 1000:
        isLineRuleVoilated = 1
        fileCount += 1 
        print("{}: {}".format(key, value))

"""Error
If the number of coded lines is more than 300 in a File
Than the error message will be displayed

Empty lines are not counted as part of the file size
"""
if isLineRuleVoilated != 0:
    msg = "Below " + str(fileCount) + " files have more than 300 lines"
    print(msg)
    sys.exit(1)
else:
    sys.exit(0)
