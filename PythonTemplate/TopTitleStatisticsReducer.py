#!/usr/bin/env python3
import sys
import math

counts  = []

for line in sys.stdin:
    _, count = line.strip().split('\t', 1)
    counts.append(int(count))

_total = sum(counts)
_mean = total / len(counts)
_min = min(counts)
_max = max(counts)

variance = sum((x - mean) ** 2 for x in counts) / len(counts)

print('%s\t%s' % ( 'Mean' , _mean))
print('%s\t%s' % ( 'Sum' ,  _total))
print('%s\t%s' % ( 'Min' , _min))
print('%s\t%s' % ( 'Max' , _max))
print('%s\t%s' % ( 'Var' , variance))
