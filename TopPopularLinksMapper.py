#!/usr/bin/env python3
import sys

link_counts = []

for line in sys.stdin:
    line = line.strip()
    link, count = line.split('\t', 1)
    count = int(count)

    link_counts.append((link, count))

top_links = sorted(link_counts, key = lambda x: (-x[1],x[0]))[:10]

for link, count in top_links:
    print('%s\t%s' % (link, count))
