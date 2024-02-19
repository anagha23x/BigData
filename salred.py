#!/usr/bin/python3

import sys
u = {}
cnt=0
for line in sys.stdin:
	line = line.strip()
	unit,sal = line.split()
	if cnt==0:
		cnt+=1
	else:
		if unit not in u:
			u[unit] = list()
			u[unit].append(int(sal))
		else:
			u[unit].append(int(sal))
for x in u:
	print(x,sum(u[x]))
