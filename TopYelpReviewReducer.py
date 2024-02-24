#!/usr/bin/env python3
import sys

bus_review = []

# input comes from STDIN
for line in sys.stdin:
     line = line.strip()
     bus, star = line.split('\t', 1)
     bus_review.append((bus, float(star)))
     
top_business = sorted(bus_review, key=lambda x: (-x[1],x[0]))

for bus, star in bus_review:
    print('%s\t%s' % ( bus, star ))
