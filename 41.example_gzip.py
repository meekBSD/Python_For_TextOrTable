#!/usr/bin/python
# -*- coding: UTF-8 -*-

import gzip
# import lzma
# with lzma.open("file.xz") as f:
#     file_content = f.read()     ##  https://docs.python.org/3/library/lzma.html

# from zipfile import ZipFile     ##  https://docs.python.org/3/library/zipfile.html
# with ZipFile('spam.zip', 'r') as myzip:
#    with myzip.open('eggs.txt') as myfile:
#        print(myfile.read())

# from shutil import make_archive
# from os import path
# root_dir, tail = path.split("/home/absolute_path/src_code.c")   # path.realpath("src_code.c")
# make_archive("test_compressed", 'zip', root_dir) 

with gzip.open("test.gz", "rb") as f:
    for n, line in enumerate(f):
        line_Splits = line.rstrip().split("\t")

            print (len(line_Splits))


