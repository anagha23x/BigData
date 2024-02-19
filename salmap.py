#!/usr/bin/python3
import sys

for line in sys.stdin:
	line = line.strip()
	eno,ename,unit,desig,sal = line.split()
	print(unit,'\t',sal);
