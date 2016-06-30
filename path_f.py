#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import csv
import StringIO


## recreate the basic data of metagenome binning in R ##


print os.getcwd()

D = os.sep.join(["D:","R_bin_newBacArc","archaea"])

f = os.walk(D)

#print f
#sys.exit()

bac_PFM = [i.rstrip() for i in open("bacteria.pf.tx", 'r').readlines()]
arc_PFM = [i.rstrip() for i in open("archaea_pf.tx", 'r').readlines()]

only_bacteria = set(bac_PFM) - set(arc_PFM)

orfs_hmm_id = open("assembly.orfs.hmm.id.txt", 'r')

# define an empty dict which will store the scaffolds' name
scaffs = {}
scaffs["contig"] = None
scaffs["Contig"] = None
scaffs["scaffold"] = None

# define a set storing the ID of scaffolds only related bacteria
bac_ID=set()

for i in orfs_hmm_id.readlines():
    
    cols_3 = i.rstrip().split()[2]
    if cols_3 in only_bacteria:
        bac_ID.add(i.rstrip().split()[0])    # add elements to bac_ID
orfs_hmm_id.close()

gc_with_ID = open("assembly.gc.tab","r")
line_num = 0
for line in gc_with_ID.readlines():
    line_num += 1
    if line.rstrip().split("\t")[0] in bac_ID:
        continue 
    k = line.rstrip().split()[0]
    scaffs[k] = line_num                   # add keys to the scaffs

gc_with_ID.close()
print len(scaffs)
print line_num

for i in f:
    for t in i[2]:
        if t.startswith("assembly.kmer") and not t.startswith("new"):       # check the file name
            print t
            with open(t, 'r') as file_handle, open("new_"+t, "w") as out_handle:
                line = file_handle.readline()
                while line:
                    a= line.rstrip().split("\t")[0]
                    #a = line.rstrip().split(",")[0].srtip('"')
                    if a in scaffs:
                        #print line
                        out_handle.write(line.encode("utf-8"))
                    line = file_handle.readline()

        elif (t.endswith("txt") or t.endswith("tab")) and not t.startswith("new"):    # check the file name
            print t
            with open(t ,"r") as f_2, open("new_"+t, "w") as f_w:
                for line in f_2.readlines():
                    if line.rstrip().split()[0] in scaffs or line.rstrip().split("\t")[0] in scaffs:
                        f_w.write(line.encode("utf-8"))
                        
        elif t.endswith("csv") and not t.startswith("new"):                           # check the file name if it ends with "csv" and then use csv reader module
            with open(t, "r") as f_handle, open("new_" +t, "w") as f_o:
                data = StringIO.StringIO(f_handle.read())
                reader = csv.reader(data)
                for num, i in enumerate(reader):
                    if i[0] == "Name" or i[0] in scaffs:
                        f_o.write(("\t".join(i)+"\n").encode("utf-8"))
                        
