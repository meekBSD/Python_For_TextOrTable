#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from Bio import SeqIO
from glob import glob
import os
import subprocess
from collections import defaultdict
import linecache

def GC_number(seq):
    gc = sum(seq.count(x) for x in ['G', 'C', 'g', 'c', 'S', 's'])
    return gc


fa_file = glob("*.fasta")
d_stat = defaultdict(list)

for i in fa_file:
    #print(i)
    records = SeqIO.parse(i, "fasta")
    gc_n = 0
    genome = 0
    for rec in records:
        sequence = str(rec.seq)
        gc_n += GC_number(sequence)
        genome += len(sequence)
    d_stat[i].append(genome)
    #print("%d\n" % genome)
    #print("%.4f\n" % (gc_n*1.0/genome))
    d_stat[i].append(gc_n*1.0/genome)
    
    gff_file = os.popen("ls "+i.rstrip(".fasta")+"/temp*.txt").read()

    #print os.popen("awk '!/^#/{print $9}' "+ gff_file.rstrip() + " | wc -l").read()
    cds_number = 0
    with open("./"+gff_file.rstrip(),"r") as f:
        for cnt, line in enumerate(f.readlines()):
            if line.startswith("#"):
                continue
            cds_number += 1
    #print cds_number
    d_stat[i].append(cds_number)
    coding_region=os.popen("awk 'BEGIN{sum=0}!/^#/{a=$5-$4;sum+=a}END{print sum}' "+gff_file.rstrip()).read()
    #print("%.4f\n" % (float(coding_region.rstrip())/genome))
    d_stat[i].append(float(coding_region.rstrip())/genome)
    
    tRNA_stat=os.popen("ls " +i.rstrip(".fasta")+"/tRNA/*_stat").read()
    #print linecache.getline(tRNA_stat.rstrip(), 56).rstrip().split()[2]
    d_stat[i].append(linecache.getline(tRNA_stat.rstrip(), 56).rstrip().split()[2])

    rRNA_seq = os.listdir(i.rstrip(".fasta")+"/rRNA/out/")
    #print rRNA_seq
    r_seq = [t for t in rRNA_seq if t.endswith(".seq")]
    if r_seq != []:
        a = os.popen("grep -c '>' "+ i.rstrip(".fasta")+"/rRNA/out/"+r_seq[0]).read()
        #print ("rRNA number: "+a)
        d_stat[i].append(a.rstrip())
    else:
        d_stat[i].append("-") 
        

    hmmID = os.popen("ls "+ i.rstrip(".fasta") + "/assembly_*.hmm.id.txt").read()

    tot_ess = os.popen("wc -l " + hmmID.rstrip()).read()
    uniq_ess =os.popen("cut -d ' ' -f 2 "+ hmmID.rstrip() +" | sort -u | wc -l").read()
    #print tot_ess.rstrip().split()[0]
    d_stat[i].append(tot_ess.rstrip().split()[0])
    #print uniq_ess
    d_stat[i].append(uniq_ess.rstrip())

print ("species\tgenome\tgc_ratio\tCDS\tcoding density\ttRNA\trRNA\ttot.ess\tuniq_ess\n")
for item in d_stat.items():
    print ("{0}\t{1}\t{2:.4f}\t{3}\t{4:.4f}\t{5}\t{6}\t{7}\t{8}".format(item[0],
            item[1][0],item[1][1], item[1][2], item[1][3], item[1][4], item[1][5],item[1][6], item[1][7]))

print ("###############################################################################\n")

all_ks = d_stat.keys()
#k_num = len(all_ks)

print "species"+"\t"+"\t".join([k0.rstrip(".fasta") for k0 in all_ks])
print "genome\t"+"\t".join([str(d_stat.get(k1)[0]) for k1 in all_ks])
print "gc_ratio\t"+"\t".join([str("{0:.4f}".format(d_stat.get(k2)[1])) for k2 in all_ks])
print "CDS\t"+"\t".join([str(d_stat.get(k3)[2]) for k3 in all_ks])
print "coding density\t"+"\t".join([str("{0:.4f}".format(d_stat.get(k4)[3])) for k4 in all_ks])
print "tRNA\t"+"\t".join([str(d_stat.get(k5)[4]) for k5 in all_ks])
print "rRNA\t"+"\t".join([str(d_stat.get(k6)[5]) for k6 in all_ks])
print "tot.ess\t"+"\t".join([str(d_stat.get(k7)[6]) for k7 in all_ks])
print "uniq_ess\t"+"\t".join([str(d_stat.get(k8)[7]) for k8 in all_ks])


