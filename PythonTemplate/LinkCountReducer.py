#!/usr/bin/env python3
import sys

link_counts = {}

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    page, link = line.split('\t', 1)

    if page not in link_counts:
        link_counts[page] = 0

    if link not in link_counts:
        link_counts[link] = 1
    else: 
        link_counts[link] += 1

for link, count in link_counts:
    print('%s\t%s' % ( link, count ))
