#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from __future__ import with_statement

lp = []
lq = []

## awk -F "\t" '{if($5~/phylum/){print;}}' > phylum_1_name.txt  --- This command could create a file contain phylums

##phyd = open("phyname.txt",'r')

##for i in phyd.readlines():
##	a = i.rstrip().split("\t")[1]
##	lp.append(a)

with open("nodes.dmp",'r') as n:
	for i in n.readlines():
		ThirdColumn = i.rstrip().split("\t")[4]
		if ThirdColumn.find("phylum") != -1:
			lq.append(i.rstrip().split("\t")[0])

with open("taxonomy_name.txt", 'r') as t:
	for i in t.readlines():
		if i.rstrip().split("\t")[0] in lq:
			lp.append(i.rstrip().split("\t")[2])

outfile = open("result_taname_2.txt",'w')

all_ta = open("all_taxonomy.txt", 'r')

for i in all_ta.readlines():
	tax_id = i.rstrip().split("\t")[0]
	name = i.rstrip().split("\t")[1]
	Notfound = True
	for i in lp:
		if name.find(i) != -1:
			outfile.write(tax_id + "\t" + i + "\t" + name + "\n")
			Notfound = False
			break
	if Notfound:
		if name.find("virus") != -1 or name.find("Virus") != -1:
			outfile.write(tax_id + "\t" + "Virus" + "\t" + name +"\n")
		elif name.find("Eukaryota") != -1:
			outfile.write(tax_id + "\t" + "Eukaryota" +"\t" + name +"\n")
		elif name.find("division WS6") != -1:
			outfile.write(tax_id + "\t" + "WS6" +"\t"+ name +"\n")
		elif name.find("Parcubacteria group") != -1:
			outfile.write(tax_id + "\t" + "Parcubacteria" + "\t" + name +"\n")
		elif name.find("division Kazan-3B-28") != -1:
			outfile.write(tax_id + "\t" + "Kazan" +"\t" + name +"\n")
		elif name.find("Bacteria (miscellaneous)") != -1:
			outfile.write(tax_id + "\t" + "miscellaneous unclassified" +"\t" + name +"\n")
		elif name.find("Candidatus Dependentiae")!= -1:
			outfile.write(tax_id + "\t" + "Dependentiae" + "\t" + name +"\n")
		elif name.find("division BRC1") != -1:
			outfile.write(tax_id + "\t" + "BRC1" + "\t" + name + "\n")
		elif name.find("Microgenomates group") != -1:
			outfile.write(tax_id + "\t" + "Microgenomates" + "\t" + name + "\n")
		elif name.find("Haloplasmatales") != -1:
			outfile.write(tax_id + "\t" + "Haloplasmatales" + "\t" + name + "\n")
		elif name.find("division TA06") != -1:
			outfile.write(tax_id + "\t" + "TA06" + "\t" + name + "\n")
		elif name.find("division WOR-1") != -1:
			outfile.write(tax_id + "\t" + "WOR-1" + "\t" + name + "\n")
		elif name.find("division SR1") != -1:
			outfile.write(tax_id + "\t" + "SR1" + "\t" + name + "\n")
		elif name.find("Thermobaculum") != -1:
			outfile.write(tax_id + "\t" + "Thermobaculum" + "\t" + name + "\n")
		elif name.find("samples;Bacteria") != -1 or name.find("Bacteria;cellular") != -1:
			outfile.write(tax_id + "\t" + "unclassified Bacteria" + "\t" + name +"\n")	
		elif name.find("prokaryotic environmental") != -1:
			outfile.write(tax_id + "\t" + "Prokaryotic" + "\t" + name +"\n")	
		elif name.find("Archaea") != -1:
			outfile.write(tax_id + "\t" + "Archaea" + "\t" + name +"\n")	
		else:
			outfile.write(tax_id + "\tNoClassifi" + "\t" + name + "\n")

all_ta.close()
outfile.close()
