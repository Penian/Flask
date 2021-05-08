#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import sys
if len(sys.argv) != 2:
    print('Usage: ./wc.py filename')
    sys.exit(1)

num_words = num_lines = num_chars = 0

with open(sys.argv[1]) as infile:
    for line in infile:
        num_lines += 1
        num_chars += len(line)
        line = line.strip()
        words = line.split()
        num_words += len(words)

print('Number of Lines is', num_lines)
print('Number of Words is: {0:5d}'.format(num_words))
print('Number of Characters is: %8.0f' % num_chars)


'''
from subprocess import call
call(['wc', sys.argv[1]])

import os
os.system('wc ' + sys.argv[1])

'''