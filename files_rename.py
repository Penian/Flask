#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
import os
import re

if not(3 <= len(sys.argv) <= 4):
    print('Usage: ./files_rename.py from_regex to_regex [dir|.')
    sys.exit(1)

if len(sys.argv) == 4:
    dir = sys.argv[3]
    os.dir(dir)

count = 0
for oldFilename in os.listdir():
    if os.path.isfile(oldFilename):
        newFilename = re.sub(sys.argv[1], sys.argv[2], oldFilename)
        if oldFilename != newFilename:
            count += 1 
            os.rename(oldFilename, newFilename)
            print(oldFilename, '->', newFilename)

print("Number of files renamed:", count)

