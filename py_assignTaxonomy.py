#!/usr/bin/env python
# -*- coding: UTF-8 -*-

#######################################################################
##      Two Input Files : result_taname_1.txt                       ##
##                        PF_test.txt                               ##
##      Three Output Files: test_tmp.txt                            ##
##                          test_blast_tab.txt                      ##
##                          assembly.tax.consensus_"+ num + ".txt   ##
##                                                                    ##
#######################################################################

from __future__ import with_statement
from collections import defaultdict
from collections import Counter
import os

d_tax = {}

d=defaultdict(list)

with open("result_taname_1.txt", 'r') as tan:
    for i in tan.readlines():
        allcol = i.rstrip().split("\t")
        d_tax[allcol[0]] = allcol[1]

with open("PF_Test.txt", 'r') as preT:
    for i in preT.readlines():
	line = i.rstrip().split("\t")
	taxonomy = line[-1]
	for a in line[0].split(";"):
            if taxonomy == "NOCLassi":
		#print ("{0}\t{1}".format(a,d_tax.get(line[2],"-")))
                d[a].append(d_tax.get(line[2], "-"))
            else:
                #print ("{0}\t{1}".format(a,taxonomy))
                d[a].append(taxonomy)

out_tmp = open("test_tmp.txt",'w')
for k,v in d.iteritems():
    kk =k.split("_")
    cnt = Counter(v).most_common(2)
    if len(cnt) == 2 and cnt[1][0] == "TA06":
        out_tmp.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(kk[0], kk[1], cnt[1][0],cnt[1][1], cnt[0][0], cnt[0][1]))
    elif len(cnt) == 2:
        out_tmp.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(kk[0], kk[1], cnt[0][0],cnt[0][1], cnt[1][0], cnt[1][1]))
        #print("{0}\t{1}\t{2}\t{3}\t{4}".format(k, cnt[0][0],cnt[0][1], cnt[1][0], cnt[1][1]))
    else:
        out_tmp.write("{0}\t{1}\t{2}\t{3}\t{4}\t{5}\n".format(kk[0], kk[1], cnt[0][0],cnt[0][1], "-", "-"))
        #print("{0}\t{1}\t{2}\t{3}\t{4}".format(k, cnt[0][0],cnt[0][1], "-", "-"))

out_tmp.close()

blast_tab = open("test_blast_tab.txt",'w')
d_cons = defaultdict(list)

with open("test_tmp.txt",'r') as tre:
    for i in tre.readlines():
        line = i.rstrip().split("\t")
        scaffold = line[0]
        orf_order = line[1]
        d_cons[scaffold].append(line[2])
        blast_tab.write("{0}\t{1}\t{2}\n".format(scaffold, orf_order, line[2]))

tax_color = {'Firmicutes': 1 ,
             'Euryarchaeota': 2 , 
             'Proteobacteria': 3 ,
             'delta/epsilon subdivisions': 4 ,
             'Chloroflexi': 5 , 
             'Bacteroidetes': 6 , 
             'Planctomycetes': 7 , 
             'Actinobacteria': 8 , 
             'Spirochaetes': 9 , 
             'Thaumarchaeota': 10 , 
             'Parcubacteria': 11 , 
             'Crenarchaeota': 12 , 
             'Cyanobacteria': 13 , 
             'Archaea': 14 ,
             'Ascomycota': 15 ,
             'TA06': 16,
             'unclassified Bacteria': 17
             }
#num = 0

assmbly_results = [i for i in os.listdir(".") if i.startswith("assembly.tax.consensus")]

outfile = "assembly.tax.consensus_"+str(len(assmbly_results)+1) + ".txt"
out_consensus = open(outfile, 'w')

out_consensus.write("scaffold\tphylum\ttaxcolor\tall.assignments\n")
most_tax = []
for k,v in d_cons.iteritems():
    #num += 1
    cnt = Counter(v)
    mostcnt = cnt.most_common(1)
    phylum = mostcnt[0][0]
    most_tax.append(mostcnt[0][0])
    each_phylum = ";".join([i[0] for i in cnt.items()])
    out_consensus.write("{0}\t{1}\t{2}\t{3}\n".format(k, phylum, tax_color.get(phylum, "18"), each_phylum))
    #print("{0}\t{1}\t{2}\t{3}".format(k, tax_color.get(phylum, "17"), phylum, each_phylum))
    #if num == 10:
    #    break
out_consensus.close()
#print num

tax_assign = Counter(most_tax)
print tax_assign.most_common(20)
