#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# - - - - - - - - - - - - - - - - - - - - - - - - -
out_file = open('other_data.txt', 'w')
out_file.write('hello world!\n')
out_file.close()

# - - - - - - - - - - - - - - - - - - - - - - - - -
Count = {}
file_object = 'species.txt'
infile = open( file_object , 'r')
for line in infile:
    name = line.strip().split('\t')[0]
    if name in Count:
        Count[name] = Count[name] + 1
    else:
        Count[name] = 1

infile.close()
keys = list(Count.keys())
keys.sort()

for b in keys:
    if b != 'Taxa':
        print(b, Count[b])
# - - - - - - - - - - - - - - - - - - - - - - - - -

import string
file_object = 'species.txt'
infile = open( file_object , 'r')
for line in infile:
    lr = line.rstrip()
    for i in lr:
        if i not in string.printable:
            print(lr)
            break
infile.close()

# - - - - - - - - - - - - - - - - - - - - - - - - -

import linecache

fourth_line = linecache.getline(r'species.txt', 5)
print(fourth_line)

# - - - - - - - - - - - - - - - - - - - - - - - - -

from collections import Counter

MyList = []
infile = open( file_object , 'r')
infile.readline()
for line in infile:
    name = line.strip().split('\t')[0]
    MyList.append(name)
infile.close()

Animal_Count = Counter(MyList)
print(Animal_Count)

for e in Animal_Count.items():
    print('Item: ', e[0], 'Appears', e[1], 'times.')

# - - - - - - - - - - - - - - - - - - - - - - - - -

import pandas as pd

data=pd.read_csv(file_object, sep='\t', header=0)
print(data.iloc[1:5,:])

