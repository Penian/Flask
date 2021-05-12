#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys

if len(sys.argv) != 3:
    print('Usage: ./htmlescape.py infile outfile')
    sys.exit(1)

with open(sys.argv[1]) as infile, open(sys.argv[2], 'w') as outfile:
    for line in infile:
        line = line.rstrip()

        line = line.replace('&', '&amp;')  # Need to do first as the rest uses it
        line = line.replace('<', '&lt;')
        line = line.replace('>', '&gt;')
        line = line.replace('"', '&quot;')
        outfile.write('%s\n' % line)  # write() does not output newline

