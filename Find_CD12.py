#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import with_statement
from collections import defaultdict
import StringIO
import csv
import argparse

USAGE = """ %prog -q phylogroup -o out_file, you shall provide the phyloname of query """

parser = argparse.ArgumentParser(description = USAGE)

parser.add_argument('-o', "--output", default = "test_result.txt")
parser.add_argument("-q", "--query", default = "CD12")

args = parser.parse_args()

L = []

with open("blast_result_tabdel.txt",'r') as f_handle:
    for line in f_handle.readlines():
        All_cols = line.rstrip().split("\t")
        if args.query in All_cols[-1]:                 # Here is the first argument.
            L.append(All_cols[0].split("_")[0])

d = defaultdict(list)

HPminus_file = open("HPminus.scaffold.coverage.csv", 'r')

Hpm = StringIO.StringIO(HPminus_file.read())
try:    
    reader_hm = csv.reader(Hpm)
    for num, i in enumerate(reader_hm):
        if i[0] in L:
            d[i[0]].append(i[2])
            d[i[0]].append(i[1])

except Exception, e:
    print str(e)

HPplus_file = open("HPplus.scaffold.coverage.csv", 'r')

Hpp = StringIO.StringIO(HPplus_file.read())
try:
    reader_hp = csv.reader(Hpp)
    for num, i in enumerate(reader_hp):
        if i[0] in L:
            d[i[0]].append(i[1])

except Exception, e:
    print str(e)

result_CD12 = open(args.output,'w')                # Here is the second argument, args.output
for k,v in d.iteritems():
    result_CD12.write("{0}\t{1}\n".format(k,"\t".join(v)))
result_CD12.close()

