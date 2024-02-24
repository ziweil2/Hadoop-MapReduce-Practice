#!/usr/bin/env python3
import sys


for line in sys.stdin:
    line = line.strip()
    page, links = line.split(':')
    page = page.strip()
    links = links.strip().split()
    
    for link in links:
        print('%s\t%s' % ( page, link ))
