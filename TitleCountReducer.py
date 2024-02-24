#!/usr/bin/env python3
from operator import itemgetter
import sys

word_counts = {}

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    if word in word_counts:
        word_counts[word] += count
    else:
        word_counts[word] = count

for word, count in word_counts.items():
    print('%s\t%s' % (word, count))
