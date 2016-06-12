#!/usr/bin/env python
# -*- coding:utf-8 -*-

from __future__ import with_statement
import os
import sys
import datetime
from collections import defaultdict

USAGE="python DeReplicateLines.py file1 file2 file3... "
cwd = os.getcwd()

# print current working directory
print cwd

# make directory for the result file
if not os.path.exists(cwd+r"/DeRep_Result"):
	os.makedirs(cwd+r"/DeRep_Result")
else:
	pass

# get the time when this script running
jobTime = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")


resultD = {}
for i in sys.argv[1:]:
	with open(i,'r') as source_file:
		for x in source_file.readlines():
			# if line starts with # skip this loop
			if x.startswith("#"):
				continue
			# else get cols 0 and col 3 to compare the value of col4
			else:
				cols = x.rstrip().split()
				#print cols[0] + ":"+ cols[3]
				IDAsKeys = cols[0]+":"+cols[3]
				if resultD.get(IDAsKeys, None) == None or (resultD.get(IDAsKeys,None) != None and \
					float(resultD.get(IDAsKeys,None)) > float(cols[4])):
					resultD[IDAsKeys] = cols[4]

# change directory to result dir
os.chdir(cwd + r"/DeRep_Result/")

# create result file
filename = "file"+"_"+jobTime
# open result file for writing

result_file = open(filename, "w")
#for i in resultD.iteritems():
#	result_file.write(i[0]+"\t"+i[1]+"\n")

for i in sorted(resultD.iteritems(), key = lambda x:int(x[0].split("_")[0]), reverse=False):
	result_file.write(i[0]+"\t"+i[1]+"\n")

result_file.close()

filename2 = "file"+"_"+jobTime+"_2"

d_2 = defaultdict(list)

for k,v in resultD.iteritems():
        k2 = k.split(":")[0]
        v2 = k.split(":")[1] + "\t"+v
        if d_2[k2] == []:
                d_2[k2].append(v2)
        elif v < float(d_2[k2][0].split("\t")[1]):
                d_2[k2][0] = v2

fresult = open(filename2, "w")
for k,v in d_2.iteritems():
        fresult.write("\t".join(k.split("_"))+"\t"+v[0]+"\n")

fresult.close()

	
