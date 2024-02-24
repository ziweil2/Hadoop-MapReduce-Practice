#!/usr/bin/env python3
import sys

review_star = []

for line in sys.stdin:
    line = line.strip()
    bid, star = line.split('\t', 1)
    star = float(star)
    review_star.append((bid, star))

top_business = sorted(review_star, key=lambda x: (-x[1],x[0]))[:10]

for business, star in top_business:
    print('%s\t%s' % ( business, star ))
