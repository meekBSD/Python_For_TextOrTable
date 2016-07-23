#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import re
import StringIO
import csv

testFile = open("result6.txt","r")
testcon = testFile.readlines()
testFile.close()

dict_a = {}

for i in testcon:
    columns = i.rstrip().split("\t")
    #dict_a[columns[2]] = "\t".join(columns[0:-1])
    dict_a[i.rstrip()] = columns[2]


phy_dict = {}

file2 = open("phy3.txt","r")

for i in file2.readlines():
    all_col = i.rstrip()
    fir_col = all_col.lstrip("NoClassifi\t").split("\t")[0]
    phy_dict[all_col]= fir_col
file2.close()


outFile = open("result_phy2.txt",'w')
for k1,v1 in dict_a.iteritems():
    flag = True
    #pattern_nc = re.compile(r"^[a-zA-Z\s]+"+v1)
    #pattern = re.compile(v1)
    #print k1
    for k,v in phy_dict.iteritems():
        #if pattern.match(k) or pattern_nc.match(k):
        if v1 == v:
            outFile.write(k1+"\t"+k+"\n")
            flag = False
            break
    if flag:
        outFile.write(k1+"\t"+"NoClassifi\t"*5 + "NoClassifi\n")
outFile.close()

## read in csvFile and get length of each contig
sca_lenFile = open("taxonomy_name.txt",'r')

data = StringIO.StringIO(sca_lenFile.read())

sca_lenFile.close()
d_len = {}
try:
    reader = csv.reader(data, delimiter="\t")
    for num,i in enumerate(reader):
        if i[0] == 'Name':
            continue
        else:
            d_len[i[0]] = i[2]
        
        #print i
        #if num == 5:
        #    break
except Exception, e:
    print str(e)
    
id_File2 = open("result_phy2.txt", 'r')
data2 = StringIO.StringIO(id_File2.read())
id_File2.close()

test_PFresult = open("PFList.txt",'w')
try:
    reader2 = csv.reader(data2, delimiter="\t")
    for num , j in enumerate(reader2):
    	test_PFresult.write("\t".join(j[0:3])+"\t")
        for i in j[3:]:
            test_PFresult.write(d_len.get(i,"NOCLassi")+"\t")
        test_PFresult.write("\n")
        #print j
        #if num == 10:
        #    break
except Exception, e:
    print str(e)
    
test_PFresult.close()
