#!/usr/bin/python3

import sys

for line in sys.stdin:
	line = line.strip()
	year,temp = line.split()
	print(year,'\t',temp)
