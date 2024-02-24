#!/usr/bin/env python3

import sys
import string
import json

stopWordsPath = sys.argv[1]
delimitersPath = sys.argv[2]

stopWords = set()
with open(stopWordsPath) as f:
    for line in f:
        stopWords.add(line.strip().lower())

with open(delimitersPath) as f:
    delimiters = f.read().strip()

for line in sys.stdin:
    line = line.strip()
    review = json.loads(line)
    business_id  = review['business_id']
    stars = int(review['stars']) - 3
    reviewText = review['text']
    for d in delimiters:
        reviewText = reviewText.replace(d, ' ')

    reviewText_cleaned = [word for word in reviewText.lower().split() if word not in stopWords]
    length = len(reviewText_cleaned)

    print('%s\t%s' % ( business_id, stars * length ))
