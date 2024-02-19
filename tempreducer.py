#!/usr/bin/python3

import sys
dic={}
for line in sys.stdin:
	line = line.strip()
	year,temp = line.split('\t')
	if year not in  dic:
		dic[year] = list()
		dic[year].append(int(temp))
	else:
		dic[year].append(int(temp))
ans={}
print("year\tmin\tmax\tavg")
for x in dic:
	print(x,'\t',min(dic[x]),'\t',max(dic[x]),'\t',sum(dic[x])/len(dic[x]))
