#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# Lesson 33 - - - - - - - - - - - - - - - - - - - - - - - - -

from io import StringIO
import csv

data = StringIO("bread\t4\t1.6\tfood\nnewspapers\t1\t2.0\tstationery\napples\t10\t8.5\tfood\npears\t6\t5.0\tfood\n")

##  test_file = open("test.txt", 'r')
##  data2 = StringIO(test_file.read())
##  test_file.close()

c_reader = csv.reader(data, delimiter="\t")

out_file = open('food.txt', 'w')
out_writer = csv.writer(out_file, delimiter='\t',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

for num,r in enumerate(c_reader):
    if r[3] == 'food':
        out_writer.writerow(r)

out_file.close()
