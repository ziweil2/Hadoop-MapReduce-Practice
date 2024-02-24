#!/usr/bin/env python3
import sys

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    print('%s\t%s' % ( None, count ))
