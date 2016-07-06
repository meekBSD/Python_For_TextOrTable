#!/usr/bin/env python
# -*- coding: UTF-8 -*-


import sys
import re

nodesFile = open("nodes.dmp","r")
nodescon = nodesFile.readlines()
nodesFile.close()

d_tree = {}

for i in nodescon:
    columns = i.split("\t")
    d_tree[columns[0]] = columns[2]


phylist = []
pattern = re.compile(r"\t(.*)phylum\t")
for i in nodescon:
    if pattern.search(i):
        phylist.append(i.split("\t")[0])

d_pp = {}
d_pq = {}
d_pr = {}
d_ps = {}
d_pt = {}

d_pv = {}

m = set()

######################################
 
#output1 = open("phy1.txt",'w')
for k1,v1 in d_tree.iteritems():
    
    if v1 in phylist:
        m.add(v1)
        #output1.write(k1+"\t"+v1+"\n")
        d_pp[k1] = v1

for i in phylist:
    if i not in m:
        d_pv[i]="NoClassifi\t" * 5

#output1.close()

print len(m)
######################################

for k1, v1 in d_tree.iteritems():
    if v1 in d_pp:
        m.add(v1)
        d_pq[k1] = v1+"\t"+d_pp.get(v1)

for i in d_pp:
    if i not in m:
        a = i+"\t"+d_pp.get(i)
        d_pv[a]="NoClassifi\t" *4

print len(m)

#######################################

for k1, v1 in d_tree.iteritems():
    if v1 in d_pq:
        m.add(v1)
        d_pr[k1] = v1+"\t"+d_pq.get(v1)

for i in d_pq:
    if i not in m:
        a = i + "\t" +d_pq.get(i)
        d_pv[a] = "NoClassifi\t" *3

print len(m)

########################################

for k1, v1 in d_tree.iteritems():
    if v1 in d_pr:
        m.add(v1)
        d_ps[k1] = v1 + "\t" + d_pr.get(v1)

for i in d_pr:
    if i not in m:
        a = i + "\t" +d_pr.get(i)
        d_pv[a] = "NoClassifi\t" * 2

print len(m)

########################################

for k1, v1 in d_tree.iteritems():
    if v1 in d_ps:
        m.add(v1)
        d_pt[k1] = v1 + "\t" + d_ps.get(v1)

for i in d_ps:
    if i not in m:
        a = i + "\t" +d_ps.get(i)
        d_pv[a] = "NoClassifi\t"

print len(m)
########################################

output2 = open("phy3.txt","w")
for k1, v1 in d_pt.iteritems():

    output2.write(k1+"\t"+v1+"\n")

i = 0
for k2, v2 in d_pv.iteritems():
    i += 1
    output2.write(v2+k2+"\n")

output2.close()

print "values in d_pv: %d" % i

a = set()
for i in set(d_pq.values()):
    n = i.split("\t")[1]
    a.add(n)

print len(a)
