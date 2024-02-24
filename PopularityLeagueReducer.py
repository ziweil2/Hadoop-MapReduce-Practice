#!/usr/bin/env python3
import sys

pageCounts = []

# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    page, count = line.split('\t', 1)
    pageCounts.append((int(page), int(count)))

pageCounts.sort(key=lambda x: x[1], reverse=False)

currentRank = 0
currentCount = 0
counter = 0
pageRanks = []

for page, count in pageCounts:
    if count > currentCount and counter > 0:
        currentRank = counter
        pageRanks.append((page, currentRank))
    else:
        pageRanks.append((page, currentRank))

    currentCount = count
    counter += 1

pageRanks.sort(key=lambda x: x[0], reverse = True)

for page, rank in pageRanks:
    print('%s\t%s' % ( page, rank ))
