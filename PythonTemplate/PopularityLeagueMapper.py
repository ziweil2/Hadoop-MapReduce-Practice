#!/usr/bin/env python3
import sys

leaguePath = sys.argv[1]
leaguePages = set()

with open(leaguePath) as f:
    for line in f:
        page = line.strip()
        leaguePages.add(page)

for line in sys.stdin:
    line = line.strip()
    page, count = line.split('\t', 1)

    if page in leaguePages:
        print('%s\t%s' % ( page, count ))
