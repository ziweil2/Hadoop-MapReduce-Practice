#!/usr/bin/env python3

import sys
import string

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stopWords = set()

with open(stopWordsPath) as f:
    for line in f:
	stopWords.add(line.strip().lower())

with open(delimitersPath) as f:
    delimiters =  f.read().strip()

for line in sys.stdin:
    line = line.strip()
    
    for d in delimiters:
	line = line.replace(d, ' ')

    words = line.split()

    for word in words:
	if word is not null and word.lower() not in stopWords:
	    print('%s\t%s' % (word.lower() , 1))


