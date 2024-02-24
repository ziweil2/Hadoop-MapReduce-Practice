#!/usr/bin/env python3
from operator import itemgetter
import sys

business_reviews = {}
review_counts = {}

# input comes from STDIN
for line in sys.stdin:
    business_id, weighted_star = line.strip().split('\t')
    
    if business_id in business_reviews:
        business_reviews[business_id] += int(weighted_star)
        review_counts[business_id] += 1
    else:
        business_reviews[business_id] = int(weighted_star)
        review_counts[business_id] = 1

for business_id in business_reviews:
    print('%s\t%s' % ( business_id , business_reviews[business_id] / review_counts[business_id] ))
