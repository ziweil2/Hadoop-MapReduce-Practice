#!/usr/bin/env python3
import sys

word_counts = []

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    count = int(count)

    word_counts.append((word, count))

top_words = sorted(word_counts, key = lambda x: (-x[1],x[0]))[:10]

for word, count in top_words:
    print('%s\t%s' % (word, count))
