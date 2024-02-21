#!/usr/bin/env python3
import sys

link_counts = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    link, count = line.split('\t', 1)
    link_counts.append((link, int(count)))

top_links = sorted(link_counts, key = lambda x: (x[1],x[0]))

for word, count in top_links:
    print('%s\t%s' % (link, count))
