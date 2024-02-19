#!/usr/bin/env python3
import sys

word_counts = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    word_counts.append((word, int(count)))

top_words = sorted(word_counts, key = lambda x: (x[1],x[0]))

for word, count in top_words:
    print('%s\t%s' % (word, count))
