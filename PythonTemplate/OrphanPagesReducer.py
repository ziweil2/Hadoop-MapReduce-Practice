#!/usr/bin/env python3
import sys

pages = set()
referenced = set()

for line in sys.stdin:
  line = line.strip()
  page, link = line.strip().split('\t', 1)

  pages.add(int(page))
  referenced.add(int(link))

orphans = pages - referenced

for page in sorted(orphans):
    print(page)
